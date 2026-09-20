import os
from dotenv import load_dotenv
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
from google import genai

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
Client = genai.Client(api_key=GEMINI_API_KEY)

recognizer = sr.Recognizer()
engine = pyttsx3.init()





def speak(text):
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
     if "open google" in c.lower():
          webbrowser.open("https://google.com")
     elif "open youtube" in c.lower():
          webbrowser.open("https://youtube.com")
     elif c.lower().startswith("play"):
          parts = c.lower().split(" ")
          if len(parts) > 1:
               song = parts[1]
               link =musicLibrary.music.get(song)
               if link:
                    webbrowser.open(link)
               else:
                    print(f"song '{song}' not found in musiclibrary")
                    speak(f"song{song} not found in library")
          

     elif "patel" in c.lower()or "ai" in c.lower():
          response = Client.models.generate_content(model="gemini-3.6-flash",contents=c)
          print(response.text)
          speak(response.text)

     
     

if __name__ == "__main__":
    speak("Initializing patel....")
    while True:
        r = sr.Recognizer()
        

        print("recognizing...")
        try:
           with sr.Microphone() as source:
                       print("Listening...")
                       audio = r.listen(source,timeout=2,phrase_time_limit=1)
                                        
           
           word = r.recognize_google(audio)
           if(word.lower() == "patel"):
                speak("ya")
                with sr.Microphone() as source:
                     print("patel active...")
                     audio = r.listen(source)
                     command = r.recognize_google(audio)

                     processCommand(command)

        
        except Exception as e:
            print("Error; {0}".format(e))
        except Exception as e:
             pass
            
        