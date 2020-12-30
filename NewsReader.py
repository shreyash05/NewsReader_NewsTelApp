from pygame import mixer
import requests
import json
import time

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()


if __name__ == '__main__':
    musiconloop('NewsMusic.mp3', '5')
    time.sleep(2)
    ch = 0
    while(True):


        speak("News for today.. Lets begin")
        print("Enetr Your Choice:")
        speak("Enetr Your Choice")
        print("1.Buisness")
        speak("1 Buisness")
        print("2.Entertainment")
        speak("2 Entertainment")
        print("3.Health")
        speak("3 Health")
        print("4.Science")
        speak("4 Science")
        print("5.Sport")
        speak("5 Sport")
        print("6.Technology")
        speak("6 Technology")
        print("7.Exit\n")
        speak("7 For Exit")
        ch = int(input())
        if ch==1 :
            i=1
            url = "http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=662d2940ba354cefa1cd36b657c331c6"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            musiconloop('newsrecording.mp3', '10')
            for article in arts:

                time.sleep(1)
                print(i)

                print("--------------------------------------------------------------------------------------------------------------------------")
                print(article['title'])
                print(article['description'])
                print("--------------------------------------------------------------------------------------------------------------------------")
                speak(article['title'])
                speak(article['description'])
                speak("Next news")
                i=i+1

            speak("Thanks for listening...")

        if ch == 2:
            i=1
            url = "http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=662d2940ba354cefa1cd36b657c331c6"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            musiconloop('newsrecording.mp3', '10')
            for article in arts:
                time.sleep(1)
                print(i)
                print("--------------------------------------------------------------------------------------------------------------------------")
                print(article['title'])
                print(article['description'])
                print("--------------------------------------------------------------------------------------------------------------------------")
                speak(article['title'])
                speak(article['description'])
                speak("Next news")
                i = i + 1
            speak("Thanks for listening...")

        if ch == 3:
            i=1
            url = "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=662d2940ba354cefa1cd36b657c331c6"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            musiconloop('newsrecording.mp3', '10')
            for article in arts:
                time.sleep(1)
                print(i)

                print("--------------------------------------------------------------------------------------------------------------------------")
                print(article['title'])
                print(article['description'])
                print("--------------------------------------------------------------------------------------------------------------------------")
                speak(article['title'])
                speak(article['description'])
                speak("Next news")
                i = i + 1
            speak("Thanks for listening...")

        if ch == 4:
            i=1
            url = "http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=662d2940ba354cefa1cd36b657c331c6"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            musiconloop('newsrecording.mp3', '10')
            for article in arts:
                time.sleep(1)
                print(i)

                print("--------------------------------------------------------------------------------------------------------------------------")
                print(article['title'])
                print(article['description'])
                print("--------------------------------------------------------------------------------------------------------------------------")
                speak(article['title'])
                speak(article['description'])
                speak("Next news")
                i = i + 1
            speak("Thanks for listening...")

        if ch == 5:
            i=1
            url = "http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=662d2940ba354cefa1cd36b657c331c6"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            musiconloop('newsrecording.mp3', '10')
            for article in arts:
                time.sleep(1)
                print(i)

                print("--------------------------------------------------------------------------------------------------------------------------")
                print(article['title'])
                print(article['description'])
                print("--------------------------------------------------------------------------------------------------------------------------")
                speak(article['title'])
                speak(article['description'])
                speak("Next news")
                i = i + 1
            speak("Thanks for listening...")

        if ch == 6:
            i=1
            url = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=662d2940ba354cefa1cd36b657c331c6"
            news = requests.get(url).text
            news_dict = json.loads(news)
            arts = news_dict['articles']
            musiconloop('newsrecording.mp3', '10')
            for article in arts:
                time.sleep(1)
                print(i)

                print("--------------------------------------------------------------------------------------------------------------------------")
                print(article['title'])
                print(article['description'])
                print("--------------------------------------------------------------------------------------------------------------------------")
                speak(article['title'])
                speak(article['description'])
                speak("Next news")
                i = i + 1
            speak("Thanks for listening...")

        if ch == 7 :
            print("Thank You for using Newstel app!")
            speak("Thank You for using Newstel app!")
            break;

        else:
            speak("Enetr valide choice")
            print("Enetr valide choice!")


