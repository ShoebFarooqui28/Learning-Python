from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    timeElapsed = 0
    print(CLEAR)
    while timeElapsed < seconds:
        time.sleep(1)
        timeElapsed += 1
                
        timeLeft = seconds - timeElapsed
        minutesLeft = timeLeft // 60
        secondsLeft = timeLeft % 60
        
        print(f"{CLEAR_AND_RETURN}Alarm in : {minutesLeft:02d}:{secondsLeft:02d}")
        
    playsound("Mini Projects\\Alarm\\alarm.wav")
    
minutes = int(input("Minutes : "))
seconds = int(input("Seconds : "))

totalSeconds = minutes * 60 + seconds
alarm(totalSeconds)





        

