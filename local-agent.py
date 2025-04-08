from helpers.ollama import ask_ollama
from helpers.shell import run_shell_command
from prompt_utils import construct_prompt  # Import the new function
import os

def main():
    print("👋 Welcome to Modded Ollama ")
    cwd = input("📁 Enter folder to run commands in (default is current): ").strip() or os.getcwd()
    print(cwd)
    while True:
        user_instruction = input("🧠 What do you want the AI to do? ")
        if user_instruction == "/bye":
            break

        # Use the refactored function to construct the prompt
        full_prompt = construct_prompt(cwd, user_instruction)
        
        shell_cmd = ask_ollama(full_prompt).strip()
        print("\n📝 Ollama suggests:\n" + shell_cmd)

        run = input("\n⚠️ Run this command? (y/n): ").strip().lower()
        if run == 'y':
            print("\n🚀 Running the command...\n")
            run_shell_command(shell_cmd, cwd)
        else:
            print("❌ Command not run.")

if __name__ == "__main__":
    main()
