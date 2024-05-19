from flask import Flask
import RPi.GPIO as GPIO
import threading
import time

app = Flask(__name__)

# GPIO setup
servo_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set up PWM
pwm = GPIO.PWM(servo_pin, 50)  # 50 Hz
pwm.start(0)

# Thread control
servo_thread = None
thread_running = False

def set_servo_angle(angle):
    duty_cycle = 2 + (angle / 18)
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Give the servo time to move
    pwm.ChangeDutyCycle(0)  # Stop sending pulse to keep the servo from jittering

def rotate_servo():
    global thread_running
    while thread_running:
        set_servo_angle(0)   # Move to 0 degrees
        time.sleep(1)        # Wait for 1 second
        set_servo_angle(180) # Move to 180 degrees
        time.sleep(1)        # Wait for 1 second

@app.route('/start', methods=['GET'])
def start_servo():
    global servo_thread, thread_running
    if not thread_running:  # Only start the thread if it is not already running
        thread_running = True
        servo_thread = threading.Thread(target=rotate_servo)
        servo_thread.start()
        return "Servo rotation started!", 200
    else:
        return "Servo is already rotating!", 200

@app.route('/stop', methods=['GET'])
def stop_servo():
    global thread_running
    thread_running = False
    if servo_thread:
        servo_thread.join()  # Wait for the thread to finish
    pwm.ChangeDutyCycle(0)
    GPIO.cleanup()  # Clean up GPIO assignments
    return "Servo rotation stopped!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)