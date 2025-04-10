from helpers.ollama import ask_ollama
from helpers.shell import run_shell_command
from prompt_utils import construct_prompt
from helpers.chat_history import get_chat, save_chat
from testing import record_and_transcribe  # Import the new function
import os

def main():
    print("👋 Welcome to Modded Ollama ")
    cwd = input("📁 Enter folder to run commands in (default is current): ").strip() or os.getcwd()
    print(cwd)
    while True:
        chat_history = get_chat()
        
        input_mode = input("🗣️ Type 'v' for voice input or press ENTER for text input: ").strip().lower()
        if input_mode == 'v':
            print("🎤 Using voice input...")
            user_instruction = record_and_transcribe()
            print(f"🗣️ You said: {user_instruction}")
        else:
            user_instruction = input("🧠 What do you want the AI to do? ")
        
        if user_instruction == "/bye":
            break
        
        full_prompt = construct_prompt(cwd, user_instruction, chat_history)
        shell_cmd = ask_ollama(full_prompt).strip()
        
        save_chat(role="user", content=user_instruction)  # Store user input
        save_chat(role="assistant", content=shell_cmd)  # Store AI response
        
        print("\n📝 Ollama suggests:\n" + shell_cmd)
        run = input("\n⚠️ Run this command? (y/n): ").strip().lower()
        if run == 'y':
            print("\n🚀 Running the command...\n")
            run_shell_command(shell_cmd, cwd)
        else:
            print("❌ Command not run.")

if __name__ == "__main__":
    main()
