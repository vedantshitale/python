#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
import pyaudio
import webbrowser


print("Initializing Ganya")
engine=pyttsx3.init('sapi5')#name of the driver
voices = engine.getProperty('voices')#getting the voice propert
engine.setProperty('voice',voices[1].id)#id of voice
a="vedant"
def Bol(Shabda):
    engine.say(Shabda)#speaks the value in variable
    engine.runAndWait()
Bol("Thumcheyae swagat ahe ")
def wishme():
    hour=datetime.datetime.now().hour
    #the code (print(hour)) print time
    if hour>=0 and hour <12:
        Bol("good morning"+a)
    elif hour>=12 and hour<18:
        Bol("Śubha dupāra"+a)
    else:
        Bol("Śubha Rātrī"+a)
    Bol("me gunya... Me Thumchi kayy madat karu ")
#This func will speak or rather will wish       
wishme()
#takes command from microphone
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Aikat ahe...")
        audio = r.listen(source)
        try:
            print("Olakhuale...")
            query = r.recognize_google(audio, language='en-in')
   
            print(f"user said:{query}\n")
        except Exception as e:
            print("Punha bola")
            query=None
        return query

            
query = takecommand()
#Logic for executing basic task (taking task on basis of quary)
if 'wikipedia' in query.lower():
    Bol('wikipedia che Shodh ghet ahe ')
    query = query.replace("wikipedia","")
    results= wikipedia.summary(query,sentences=4)
    Bol(results)
    print(results)
elif 'youtube Ughaḍa'or 'youtube' in query.lower():
    Bol('youtube che Shodh ghet ahe ')
    chrome="C:\Program Files\Google\Chrome\Application\chrome.exe %s"
    webbrowser.open("youtube.com")
    

     

