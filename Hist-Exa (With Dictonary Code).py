#Libraries
import speech_recognition as speech
import pyttsx3 as spch
import pygame
from KeysDict import history

#Intilization
engine = spch.init()
voice = engine.getProperty("voices")

engine.setProperty("rate",150)
engine.setProperty("voice",voice[1].id)

pygame.init()

#Background Screen
width = 1200
height = 650
screen=pygame.display.set_mode( ( width, height) )

pygame.display.set_caption("Hist-Exa")

bg=pygame.image.load("Images/bg1.png")
image1=pygame.transform.scale(bg, (1200,650))
screen.blit(image1,(0,0))
pygame.display.update()

engine.say("Welcome to Hist-Exa")
engine.runAndWait()


activate="none"
exitstatus="no"

while True:
    try:
        bgh=pygame.image.load("Images/bg1.png")
        image078=pygame.transform.scale(bgh, (1200,650))
        screen.blit(image078,(0,0))
        pygame.display.update()
        for event in pygame.event.get():
            #Event to Quit Pygame Window
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            
            #To Read whether 's' key is pressed
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_s:
                    activate = "s"
                    print("S pressed")
                    
                    
         # if "s" key is pressed
        if activate=="s":
            #Change the background image to Listening Image
            listenImg2=pygame.image.load("Images/bg1.png")
            image14=pygame.transform.scale(listenImg2, (1200,650))
            screen.blit(image14,(0,0))
            pygame.display.update()
            
            #Start Listening the User Voice Input
            r=speech.Recognizer()
            
            with speech.Microphone() as source:
                    listenImg=pygame.image.load("Images/bg2.png")
                    image761=pygame.transform.scale(listenImg, (1200,650))
                    screen.blit(image761,(0,0))
                    pygame.display.update()
                    engine.say("Starting to Take Voice Command")
                    engine.runAndWait()
                    r.adjust_for_ambient_noise(source)
                    print("Speak:")
                    audio=r.listen(source)
                #Convert Voice Commands to Text
            command=r.recognize_google(audio).lower()
                
            print("You said: "+command)
            
            #Search each keyword in the dictionary one-by-one
            for keyword in history:
                
                #if one of the keyword in the dictionary is in 
                #User Input
                if keyword in command:
                    
                    #Check the response type for that keyword
                    
                    #Image & Speech Response type
                    if history[keyword][0]=="SpchImg":
                        #Showing Image
                        images=pygame.image.load("Images/"+ history[keyword][2])
                        image21=pygame.transform.scale(images, (1000,450))
                        screen.blit(image21,(95,135))
                        pygame.display.update()
                        
                        #Saying Text
                        engine.say(history[keyword][1])
                        engine.runAndWait()
                        
                        
                    if  history[keyword][0]=="exit":
                        engine.say(history[keyword][1])
                        engine.runAndWait()
                        exitstatus="yes"
                        break
            #if 'exit' in command then break from while loop        
            if exitstatus=="yes":
                    pygame.quit()
                    break
                
            #Reset the UI to get further inputs    
            activate="none" 
            bg=pygame.image.load("Images/bg1.png")
            image0=pygame.transform.scale(bg, (1200,650))
            screen.blit(image0,(0,0))
        
    #Stop Taking Voice Commands
    except speech.UnknownValueError:
        print ("Could not understand audio")
        engine.say("Could not understand audio")
        engine.runAndWait
    except speech.RequestError as e:
        print ("Could not request results; {0}".format(e))
        engine.say("Could not request results; {0}".format(e))
        engine.runAndWait
    except KeyboardInterrupt:
        break