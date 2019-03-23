from microbit import *
screen = 0
for screen = 0:
ledOff = 0
ledOn = 9

leds+ []

x = 0
y = 0
while( y < 5 ):
    while( not( button_b.was_pressed())):
        display.set_pixel(x,y,ledOn)
        sleep(100)
        display.set_pixel(x,y,ledOff)
        sleep(100)
        if button_a.was_pressed():
            display.set_pixel(x,y,ledOn)
            break

    leds.append( 0 if ("0" == display.get_pixel(x,y)) else 1)
    x = x+1
    if x > 4:
        x = 0
        y = y+1

display.clear()
x = 0
y = 0
while( y < 2 ):
    while( not( button_b.was_pressed())):
        display.set_pixel(x,y,ledOn)
        sleep(100)
        display.set_pixel(x,y,ledOff)
        sleep(100)
        if button_a.was_pressed():
            display.set_pixel(x,y,ledOn)
            break
    leds.append( 0 if ("0" == display.get_pixel(x,y)) else 1)
    x = x+1
    if x > 4:
        x = 0
        y = y+1

    if( (1 == y) and (2 == x)):
       break


leds.reverse()
exponent = 0
value = 0
for led in leds:
    value = value + (2**exponent)
    exponent += 1




