import whisper
import os
import subprocess

# model = whisper.load_model("base")
model = whisper.load_model("small")

while True:
    print("🎤 Recording... Press ENTER to stop.")
    
    # Start arecord as a background process
    process = subprocess.Popen([
        "arecord", "-f", "cd", "-t", "wav", "-r", "16000", "voice.wav"
    ])
    input()  # Wait for user to press Enter
    process.terminate()  # Stop recording
    process.wait()

    print("🧠 Transcribing...")
    result = model.transcribe("voice.wav")

    print("🗣️ You said:", result["text"])
    print("-" * 40)
