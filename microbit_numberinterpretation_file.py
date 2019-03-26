from microbit import *
ledOff = 0 #Interpret as bit off
ledOn = 9 #Interpret as bit on

LongPress = 500 #No magic numbers!
ShortPress = 100

INPUTTING = 3 #Needed for switching between screens
CONVERTING = 4

screen = INPUTTING
leds = ["0" for i in range(32)] #Initialize 32 bit array to ascii 0s
bit = 0 #leds array index 0..31 - bit order: MSB:31..LSB:0 i.e. index=0 === bit 31 and index=31 === bit 0


while True:
    if screen == INPUTTING: #Do all the stuff in this INPUTTING body
        # x === column, y === row where x=0,y=0 is upper left led and x=4,y=4 is bottom right led
        x = 0
        y = 0

        page2 = True #For breaking to the CONVERSION screen from any point while on the INPUTTING screen

        while( y < 5 ): #Working with bits in range x: 0-->4 and y: 0-->4
            while( not( button_b.was_pressed())): #While b is not being pressed, flash a pixel
                display.set_pixel(x,y,ledOn)
                sleep(ShortPress)
                display.set_pixel(x,y,ledOff)
                sleep(ShortPress)
                if button_a.was_pressed():
                    display.set_pixel(x,y,ledOn)
                    break

            sleep(LongPress)
            if button_b.is_pressed(): #If b was held longer than .5 second, display CONVERTING screen
                page2 = False
                screen = CONVERTING
                break
            leds[bit] =  "0" if (0 == display.get_pixel(x,y)) else "1" #Appeneding to the leds list
            x = x+1 #Walking through the columns
            if x > 4: #If the next column is greater than 4:
                x = 0 #return to column 0
                y = y+1 #and drop down 1 row

            bit += 1 #Walk the bits by 1 from 31-->0





        if( page2 ):
            display.clear()
            # x === column, y === row where x=0,y=0 is upper left led
            x = 0
            y = 0
            while( y < 2 ): #Working with bits in range x: 0-->4 and y: 0-->1
                while( not( button_b.was_pressed())):
                    display.set_pixel(x,y,ledOn)
                    sleep(ShortPress)
                    display.set_pixel(x,y,ledOff)
                    sleep(ShortPress)
                    if button_a.was_pressed():
                        display.set_pixel(x,y,ledOn)
                        break

                sleep(LongPress)
                if button_b.is_pressed():
                    screen = CONVERTING
                    break

                leds[bit] =  "0" if (0 == display.get_pixel(x,y)) else "1"
                x = x+1 #Walking through the columns
                if x > 4: #If the next column is greater than 4:
                    x = 0 #return to column 0
                    y = y+1 #and drop down 1 row


                if( (1 == y) and (2 == x)): #Limiting the second screen to 7 bits
                    break

                bit += 1 #Walk the bits by 1 from 31-->0

    if screen == CONVERTING:
        display.clear()
        value = int("".join(leds),2) #Combine all the bit values and convert to an integer

        menu = [ "hex?", "uint?", "signed int?", "float?", "ascii?"]#Hex was included for a way to view the data

        menuIndex = 0
        CONVERTING = True



        while( CONVERTING ): #Do all the stuff in this CONVERTING body
            display.clear()
            while( not( button_b.was_pressed())):
                display.scroll(menu[menuIndex])
                if(button_a.was_pressed()):
                    while( not( button_a.was_pressed())):
                        if(0 == menuIndex):
                            #Hex logic
                            display.scroll("0x{:08x}".format(value),250)

                        elif(1 == menuIndex):
                            #Unsigned int logic
                            display.scroll(value)

                        elif(2 == menuIndex):
                            #Signed int logic
                            display.scroll("signed conversion")

                        elif(3 == menuIndex):
                            #Float logic
                            display.scroll("float conversion")


                        elif(4 == menuIndex):
                            #Ascii logic
                            asciiValue = value&0xff
                            asciiValue += ((value>>8)&0xff)
                            asciiValue += ((value>>16)&0xff)
                            asciiValue += ((value>>24)&0xff)
                            display.scroll(asciiValue)

            sleep(LongPress)
            if button_b.is_pressed(): #If true, break out of CONVERTING loop and go to INPUTTING screen
                screen = INPUTTING
                break

            menuIndex = (menuIndex + 1) % len(menu) #Walking through the menu options
