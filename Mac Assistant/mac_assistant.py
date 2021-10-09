"""
Mac Assistant
- Automates simple tasks using voice commands for a Macbook.

Author : Aditya Singh [https://github.com/aditya172926]
Date   : 9/10/21
"""

import os
import speech_recognition as sr
import webbrowser
from datetime import datetime
from googlesearch import search

print('=============================================================\n\n')
print('\t\tRules to follow while giving commands')
print('\n1) To open application say:- "Open Application <application name>')
print('\n2) To perform a google search say:- "Search web for <anything>"')
print('\n3) To perform google search for images say:- "Search web for images of <anything>"')
print('\n4) To quit say:- "Stop"')
print('\n\nThere is no time limit, speak when you are prompted.')
print('Use headphone for better results')
print('=============================================================\n\n')

# Function to launch an Application
def application(name):
    if len(name)>1:
        name = ' '.join(name)
    else:
        name = str(name[0])
    command = 'open -a "{}"'.format(str(name))
    os.system(command)

# Function to search the web for Images as well
def search_web(searchtype, query):
    if searchtype != 'image':
        search_results = 'https://www.google.com/search?q='+query+'&rlz=1C5CHFA_enUS860US860&oq=washing&aqs=chrome.0.0j69i57j46j0j69i60j69i65j69i60l2.2604j0j7&sourceid=chrome&ie=UTF-8'
        webbrowser.open(search_results)
    else:
        image_search = 'https://www.google.com/search?q='+query+'&rlz=1C5CHFA_enUS860US860&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjqg__ehr3qAhUZyjgGHbcJDrgQ_AUoAXoECAwQAw&biw=1440&bih=788'
        webbrowser.open(image_search)

# Function to open websites on default browser
def open_websites(query):
    print('called')
    print(query)
    for j in search(query[0], tld='com', num=2, stop=1, pause=2):
        print(j)
        webbrowser.open(j)

# specific words necessary in the voice commands.
keywords = ['application', 'folder', 'desktop', 'open']
web_search = ['search', 'web']

print('Be very consize and strictly say what you want to do')
print('To open application say "open application WhatsApp"')    
#This is fixed voice template to open an application. Do not change it

r = sr.Recognizer()

audio_spoken = ''
with sr.Microphone() as source:
    while audio_spoken != 'stop':
        print("Say Something")
        os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("Title", "Say Something"))
        audio = r.listen(source)
        print('Time over')
        os.system("""osascript -e 'display notification "{}" with title "{}"'""".format("Title", "Time Over, Say when Prompted"))

        try:
            audio_spoken = r.recognize_google(audio)
            # keeps a record/log of your voice commands in a file
            f = open('history.txt', 'a')
            f.write('\n\n')
            f.write(str(datetime.now()))
            f.write('\n')
            f.write(audio_spoken)
            f.close()

            spoken_keyword1 = set(audio_spoken.split()) & set(keywords)
            spoken_keyword2 = set(audio_spoken.split()) & set(web_search)

            if 'application' in spoken_keyword1:
                spoken_words = audio_spoken.split()
                application(spoken_words[2:])
                
            if 'search' in spoken_keyword2 and 'web' in spoken_keyword2:
                spoken_words = audio_spoken.split()
                #search web for images of ----
                if 'image' in spoken_words or 'images' in spoken_words:
                    searchtype = 'image'
                    to_search = spoken_words[4:]
                    query = '+'.join(to_search)
                    print(query)
                    search_web(searchtype, query)
                #To search websites say: Search website linkedin.com
                elif 'website' in spoken_words:
                    searchtype = 'website'
                    to_search = spoken_words[-1:]
                    print('Website to visit: ', to_search)
                    open_websites(to_search)
                else:
                    searchtype = 'link'
                    to_search = spoken_words[4:]
                    query = '+'.join(to_search)
                    print(query)
                    search_web(searchtype, query)
        except:
            pass