from helpers.ollama import ask_ollama
from helpers.shell import run_shell_command
from prompt_utils import construct_prompt  # Import the new 
from helpers.chat_history import get_chat
from helpers.chat_history import save_chat
import os

def main():
    print("👋 Welcome to Modded Ollama ")
    cwd = input("📁 Enter folder to run commands in (default is current): ").strip() or os.getcwd()
    print(cwd)
    while True:
        chat_history=get_chat()
        
        user_instruction = input("🧠 What do you want the AI to do? ")
        
        if user_instruction == "/bye":
            break
        
        
        # Use the refactored function to construct the prompt
        full_prompt = construct_prompt(cwd, user_instruction,chat_history)
        
        shell_cmd = ask_ollama(full_prompt).strip()
        
        save_chat(role="user",content=user_instruction) #store user side content
        save_chat(role="assisstant",content=shell_cmd) #store ai ka answer
        
        print("\n📝 Ollama suggests:\n" + shell_cmd)
        run = input("\n⚠️ Run this command? (y/n): ").strip().lower()
        if run == 'y':
            print("\n🚀 Running the command...\n")
            run_shell_command(shell_cmd, cwd)
        else:
            print("❌ Command not run.")

if __name__ == "__main__":
    main()
