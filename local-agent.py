import requests
import subprocess
import os

MODEL_NAME="llama3.2"
OLLAMA_URL="http://localhost:11434/api/generate"

def ask_ollama(prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })
    result=response.json()
    return(result['response'])

def run_shell_command(cmd, cwd):
    subprocess.run(cmd, shell=True, cwd=cwd)

def main():
    print("👋 Welcome to Modded Ollama ")
    cwd = input("📁 Enter folder to run commands in (default is current): ").strip() or os.getcwd()
    print(cwd)
    while True:
        
        user_instruction = input("🧠 What do you want the AI to do? ")
        if user_instruction=="/bye":
            break
        
    # Craft system prompt
        full_prompt = f"""
            You are a professional software engineer assistant.

            The user is currently working in the directory: '{cwd}'.
            You MUST begin all shell commands with 'cd "{cwd}" &&' to ensure correct context.
            If your task creates a subdirectory (e.g. with create-next-app), make sure to 'cd' into it after creation.

            ONLY respond with valid shell commands to accomplish the task:
            '{user_instruction}'

            DO NOT include explanations, comments, or non-command text.
            """
        

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
