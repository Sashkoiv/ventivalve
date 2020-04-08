
def encoder_routine():
    import time
    from rotary_irq_esp import RotaryIRQ

    r = RotaryIRQ(pin_num_clk=18,
                pin_num_dt=19,
                min_val=0,
                max_val=5,
                reverse=False,
                range_mode=RotaryIRQ.RANGE_WRAP)

    val_old = r.value()
    while True:
        val_new = r.value()

        if val_old != val_new:
            val_old = val_new
            print('result =', val_new)

        time.sleep_ms(50)

def bme_routine():
    from bme280 import BME280
    from machine import Pin, I2C

    b = BME280(I2C(scl=Pin(22), sda=Pin(21)))

    return b.get()

def lcd_routine():
    from machine import Pin, I2C
    import ssd1306
    from time import sleep

    # ESP32 Pin assignment
    i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

    oled.text('Hello, World 1!', 0, 0)
    oled.text('Hello, World 2!', 0, 10)
    oled.text('Hello, World 3!', 0, 20)

    oled.show()

def servo_routine():
    import machine
    import time
    p4 = machine.Pin(16)
    servo = machine.PWM(p4,freq=50)
    servo.duty(14)
    time.sleep_ms(1000)
    servo.duty(134)

def test():
    import time
    import machine
    from rotary_irq_esp import RotaryIRQ
    from machine import Pin, I2C
    import ssd1306
    from time import sleep
    from bme280 import BME280
    from machine import Pin, I2C

    p4 = machine.Pin(16)
    servo = machine.PWM(p4,freq=50)
    servo.duty(14)

    r = RotaryIRQ(pin_num_clk=18,
                pin_num_dt=19,
                min_val=14,
                max_val=134,
                reverse=False,
                range_mode=RotaryIRQ.RANGE_BOUNDED)

    i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
    b = BME280(i2c, 0x76)

    oled_width = 128
    oled_height = 64
    oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

    val_old = r.value()

    while True:
        val_new = r.value()

        if val_old != val_new:
            val_old = val_new
            servo.duty(val_new)
            print('result =', val_new)

            bme = b.get()

            oled.fill(0)
            oled.text('Temp  is {}'.format(bme[0]), 0, 0)
            oled.text('Press is {}'.format(bme[1]), 0, 10)
            oled.text('Humi  is {}'.format(bme[2]), 0, 20)
            oled.text('Encoder is {}'.format(val_new), 0, 30)
            oled.show()
        time.sleep_ms(50)


if __name__ == "__main__":
    test()