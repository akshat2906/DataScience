import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please speak something...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    audio = recognizer.listen(source)  # Listen to the audio

# Recognize speech using Google Speech Recognition
try:
    print("Recognizing...")
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Sorry, could not understand the audio.")
except sr.RequestError:
    print("Sorry, unable to access the Google Speech Recognition service.")