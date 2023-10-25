import whisper

model = whisper.load_model("medium")
result = model.transcribe("src/audio.mp3")
print(result["text"])

audio = whisper.load_audio("src/audio.mp3")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")