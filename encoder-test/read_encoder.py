# Meant for circuitpython
import time
import board
import busio

i2c = busio.I2C(board.GP1, board.GP0)

AS5600_ADDR = 0x36
AS5600_REG_ANGLE_MSB = 0x0E
AS5600_REG_ANGLE_LSB = 0x0F

while not i2c.try_lock():
    pass

if not AS5600_ADDR in i2c.scan():
    print("couldnt find as5600")

while True:
    i2c.writeto(AS5600_ADDR, bytes([AS5600_REG_ANGLE_MSB])) # LSB is this reg + 1 so we'll rely on autoincrement
    result = bytearray(2) # read 2 bytes, MSB then LSB
    i2c.readfrom_into(AS5600_ADDR, result)
    angle = (int(result[0]) << 8) + int(result[1])
    print(angle)
    time.sleep(0.05)
