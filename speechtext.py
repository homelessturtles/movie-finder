from google.cloud import speech
from google.oauth2 import service_account

client_file = 'movie-finder-key.json'
credentials = service_account.Credentials.from_service_account_file(
    client_file)
client = speech.SpeechClient(credentials=credentials)

def speech_to_text(audio_file_path):
    transcriptions = []
    with open(audio_file_path, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    # Configure the speech recognition request
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        sample_rate_hertz=44000,
        audio_channel_count=2
    )

    response = client.recognize(audio=audio, config=config)

    # Print the transcriptions
    for result in response.results:
        transcriptions.append(result.alternatives[0].transcript)
    
    return ' '.join(transcriptions)

