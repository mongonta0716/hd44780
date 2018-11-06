#!/usr/bin/python3
# -*- coding:utf-8 -*-

import HD44780 as LCD
import time

lcd = LCD.HD44780('lcdsample.conf')
lcd.init()

while True:
    #            0123456789012345678901234567890123456789
    lcd.message('https://raspberrypi.mongonta.com', 1)
    lcd.message('Shift Demo012345678901234567890123456789', 2)
    time.sleep(1)
