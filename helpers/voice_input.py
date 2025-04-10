import whisper
import subprocess

# model = whisper.load_model("base")
model = whisper.load_model("small")

def record_and_transcribe():
    """
    Records audio from the microphone and transcribes it using Whisper.
    
    Returns:
        str: The transcribed text.
    """
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
    return result["text"]

if __name__ == "__main__":
    while True:
        text = record_and_transcribe()
        print("🗣️ You said:", text)
        print("-" * 40)
