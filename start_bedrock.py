import RPi.GPIO as GPIO
import subprocess
import threading
import time

# Pin-Einstellung (Physischer Pin 11)
LED_PIN = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

running = True

def blink_led():
    while running:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)

# Blinken im Hintergrund starten
led_thread = threading.Thread(target=blink_led)
led_thread.start()

try:
    print("Starte BedrockConnect...")
    # Startet Java und reicht Ein-/Ausgaben an die Konsole weiter
    process = subprocess.Popen(["java", "-jar", "BedrockConnect.jar"])
    process.wait()  # Wartet, solange der Server läuft
except KeyboardInterrupt:
    pass
finally:
    print("\nServer gestoppt. Schalte LED aus...")
    running = False
    led_thread.join()
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
    print("Beendet.")
