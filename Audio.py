from ast import Import
from email.mime import audio
import speech_recognition as sr
import subprocess
import webbrowser

recognizer = sr.Recognizer()


def capture_voice_input():
    with sr.Microphone() as sourse:
        print('Слухаю...')
        audio = recognizer.listen(sourse)    
        
    return audio

recognizer = sr.Recognizer()


def capture_voice_input():
    with sr.Microphone() as sourse:
        print('Listening...')
        audio = recognizer.listen(sourse)    
        
    return audio


def convert_voice_to_text(audio):
    try:
        text = recognizer.recognize_google(audio, language = 'uk-UK')
        print('You said:  '+ text)
    except sr.UnknownValueError:
        text = ''
        print('-_-')
    except sr.RequestError as e:
        text = ""
        print("Error; {0}".format(e))
    return text

def process_voice_command(text):
    if "привіт" in text.lower():
        print("Привіт! Як я можу Вам допомогти?")
    elif "прощавай" in text.lower():
        print("До побачення! Гарного дня!")
    elif "як справи" in text.lower():
        print("Супер, а у вас?")
        return True
    elif "калькулятор" in text.lower():
	    subprocess.call(['calc'])

    
def main():
    end_program = False
    while not end_program:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        end_program = process_voice_command(text)

if __name__ == '__main__':
    main()

def process_voice_command(text):
    if "привіт" in text.lower():
        print("Привіт! Як я можу Вам допомогти?")
    elif "прощавай" in text.lower():
        print("До побачення! Гарного дня!")
        return True
    else:
        print("Я вас не розумію. Повторіть ваш запит")
    return False
