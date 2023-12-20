import speech_recognition as sr


def speech_to_text(audio_file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(audio_file_path) as source:
        recognizer.adjust_for_ambient_noise(source, duration=21)
        audio = recognizer.record(source)

    try:
        # Use the Google Web Speech API for recognition
        text = recognizer.recognize_bing()
        print("Transcription: {}".format(text))
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand the audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Web Speech API; {0}".format(e))


speech_to_text('daddy_chill.wav')
