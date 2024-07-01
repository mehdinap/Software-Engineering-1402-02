import speech_recognition as sr
from pydub import AudioSegment

def convert_audio_to_text(audio_file_path):
    # Convert audio file to WAV format if necessary
    if not audio_file_path.endswith('.wav'):
        audio = AudioSegment.from_file(audio_file_path)
        audio_file_path = "temp_audio.wav"
        audio.export(audio_file_path, format="wav")
    
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # Record the audio data from the source
        try:
            text = recognizer.recognize_google(audio_data)
            print("Transcription: ", text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    audio_file_path = "./voice2.mp3"  # Use raw string by prefixing with 'r'
    convert_audio_to_text(audio_file_path)
