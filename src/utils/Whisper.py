import whisper
from io import BytesIO
from werkzeug.utils import secure_filename
import os


class WhisperProcess():
    @classmethod
    def convert_audio(self, audioRecord):
        try:
            audio_data = audioRecord.read()

            upload_folder = 'src/uploads'

            os.makedirs(upload_folder, exist_ok=True)

            filename = secure_filename(audioRecord.filename)

            audio_path = os.path.join(upload_folder, filename)
            with open(audio_path, 'wb') as audio_file:
                audio_file.write(audio_data)

            # tiny - base - medium
            model = whisper.load_model("tiny")
            result = model.transcribe(audio_path)
            print(result["text"])

            audio = whisper.load_audio(audio_path)
            audio = whisper.pad_or_trim(audio)

            mel = whisper.log_mel_spectrogram(audio).to(model.device)

            _, probs = model.detect_language(mel)
            print(f"Detected language: {max(probs, key=probs.get)}")

            response = {
                "text": result["text"],
                "language": max(probs, key=probs.get)
            }

            return response
        except Exception as ex:
            return str(ex)
