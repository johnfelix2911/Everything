import serial

# Replace with the actual COM port your Arduino is connected to
port = 'COM3'  # Windows example
# port = '/dev/ttyUSB0'  # Linux/macOS example (adjust as needed)

# Set the baud rate to match your Arduino sketch (common values are 9600, 115200)
baudrate = 9600

try:
    # Open the serial port
    ser = serial.Serial(port, baudrate)

    while True:
        # Read data from the serial port (up to the newline character)
        data = ser.readline().decode('utf-8').strip()

        # Print the received data
        if data:
            print(data)

except serial.SerialException as e:
    print(f"Error opening serial port: {e}")

finally:
    # Close the serial port to avoid resource leaks
    if ser:
        ser.close()
        print("Serial port closed")
