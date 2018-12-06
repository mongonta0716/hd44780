# I2C communication module of HD44780 compatible LCD for Raspberry Pi

It is a module that controls the LCD equipped with HD44780 compatible controller such as LCD1602A, LCD2004A via I2C.

## Requirements

- Python3
※Changing the configparser part will work with Python2 as well.

- mojimoji==0.0.8

## Before install
This module use mojimoji to display japanese kana characters.
```pip3 install mojimoji```

# Setting config file
Create a config file and place it under the conf folder.Refer to conf/lcdsample.conf.
## Settings
- i2c_address  
The default I2C address is 0x27 of PCF9574T.
For PCF9574AT, the default I2C address is 0x3f.
- width  
Number of display digits on LCD
- lines  
Number of display rows on LCD
- backlight  
Backlight control flag
Normally set to 'On'.

- shiftmode  
Mode to shift when the number of display digits is exceeded
	- 0  
Not shift
	- 1  
One byte left shift
	- 2  
One byte right shift
	- 3  
Shift left and right alternately
- kanamode  
Set 'On' to use japanese kana characters.

# How to use
Refer to demo.py,demo_shift.py and incorporate it.

# About shift
With 1602A, up to 40 bytes of characters can be shifted per line.
In 2004A, 40 bytes of characters are all displayed, so it will not be useful.If shiftmode is 1 or 2, 40 bytes of characters including the blank are shifted.
