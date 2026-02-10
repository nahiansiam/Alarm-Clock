#⏰ Alarm Clock

import time
import winsound

def alarm_clock():
    target = input("Set alarm time (HH:MM:SS) : ")
    print("Alarm fixed at ->", target)

    while True:
        now = time.strftime("%H:%M:%S")

        # show running clock
        print("Time:", now, end="\r")

        # check alarm match
        if now == target:
            print("\nWake up! Time reached.")
            
            # ring sound few times
            count = 0
            while count < 5:
                winsound.Beep(1200, 800)
                count += 1
            break

        time.sleep(1)


# start program
alarm_clock()
