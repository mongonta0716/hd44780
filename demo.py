#!/usr/bin/python3
# -*- coding:utf-8 -*-

import HD44780 as LCD

lcd = LCD.HD44780('lcdsample.conf')
lcd.init()

#            0123456789012345
lcd.message('https://raspberr', 1)
lcd.message('ypi.mongonta.com', 2)
