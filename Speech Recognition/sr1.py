import speech_recognition as sr
import webbrowser

def google_search_song(song_name):
    url = f"https://www.google.com/search?q={song_name.replace(' ', '+')}+song"
    webbrowser.open(url)

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please say the name of the song:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Sorry, unable to access the Google Speech Recognition service.")
    return None

def main():
    song_name = speech_to_text()
    if song_name:
        google_search_song(song_name)

if __name__ == "__main__":
    main()