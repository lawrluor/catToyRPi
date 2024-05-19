from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import threading
import time
import random

app = Flask(__name__)
app.config['DEBUG'] = True  # Enable debug mode

WAIT_TIME = 0.5  # Time to wait between moves

# GPIO setup
servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Initialize PWM
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz
pwm.start(0)

# Thread control and locking mechanism
servo_thread = None
thread_running = threading.Event()
lock = threading.Lock()

# Keep track of the last angle and direction state
last_angle = 90  # Initialize to a neutral position
move_direction = 1  # 1 for moving towards 180, -1 for moving towards 0

def set_servo_angle(angle):
    global last_angle
    duty_cycle = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(WAIT_TIME)  # Allow time for the servo to move
    pwm.ChangeDutyCycle(0)  # Stop the PWM signal to prevent jitter
    last_angle = angle  # Update the last angle

def calculate_next_angle():
    global last_angle, move_direction
    # Toggle the direction each move
    move_direction *= -1

    # Calculate next angle based on current direction
    if move_direction == 1:
        # Move towards 180, but ensure at least a 45-degree change
        min_angle = min(180, last_angle + 45)
        next_angle = random.randint(min_angle, 180)
    else:
        # Move towards 0, but ensure at least a 45-degree change
        max_angle = max(0, last_angle - 45)
        next_angle = random.randint(0, max_angle)

    return next_angle

def rotate_servo():
    while thread_running.is_set():
        next_angle = calculate_next_angle()
        set_servo_angle(next_angle)
        time.sleep(WAIT_TIME)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_servo():
    global servo_thread
    with lock:
        if not thread_running.is_set():
            thread_running.set()
            servo_thread = threading.Thread(target=rotate_servo)
            servo_thread.start()
            return "Started!", 200
        else:
            return "Toy is already started!", 200

@app.route('/stop', methods=['POST'])
def stop_servo():
    global servo_thread
    with lock:
        if thread_running.is_set():
            thread_running.clear()
            servo_thread.join()
            return "Toy stopped.", 200
        else:
            return "Toy is already stopped.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)