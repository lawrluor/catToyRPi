from flask import Flask, request
import RPi.GPIO as GPIO
import threading
import time
import random

app = Flask(__name__)

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

# Keep track of the last angle
last_angle = 90  # Initialize to a neutral position

def set_servo_angle(angle):
    global last_angle
    duty_cycle = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(WAIT_TIME)  # Allow time for the servo to move
    pwm.ChangeDutyCycle(0)  # Stop the PWM signal to prevent jitter
    last_angle = angle  # Update the last angle

def calculate_next_angle():
    global last_angle
    # Determine direction randomly: 1 for positive, -1 for negative
    direction = random.choice([1, -1])
    # Calculate new angle, ensuring it moves at least 45 degrees
    next_angle = last_angle + direction * random.randint(45, 135)

    # Adjust angle to stay within 0 to 180 degrees
    if next_angle > 180:
        next_angle = 180
    elif next_angle < 0:
        next_angle = 0
    return next_angle

def rotate_servo():
    while thread_running.is_set():
        next_angle = calculate_next_angle()
        set_servo_angle(next_angle)
        time.sleep(WAIT_TIME)

@app.route('/start', methods=['GET'])
def start_servo():
    global servo_thread
    with lock:
        if not thread_running.is_set():
            thread_running.set()
            servo_thread = threading.Thread(target=rotate_servo)
            servo_thread.start()
            return "Servo rotation started!", 200
        else:
            return "Servo is already rotating!", 200

@app.route('/stop', methods=['GET'])
def stop_servo():
    global servo_thread
    with lock:
        if thread_running.is_set():
            thread_running.clear()
            servo_thread.join()
            return "Servo rotation stopped!", 200
        else:
            return "Servo is already stopped!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)