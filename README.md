# Local Agent with Ollama Integration

This Python program acts as a local agent that integrates with the Ollama API to generate shell commands based on user instructions. It allows users to execute commands in a specified directory with the help of AI-generated suggestions.

## Features

- Interacts with the Ollama API to generate shell commands.
- Allows users to specify a working directory for command execution.
- Provides an option to review and confirm commands before execution.
- Supports exiting the program gracefully with `/bye`.

## Requirements

- Python 3.7 or higher
- `requests` library
- A running instance of the Ollama API at `http://localhost:11434`

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required Python dependencies:
   ```bash
   pip install requests
   ```

## Usage

1. Run the program:
   ```bash
   python local-agent.py
   ```

2. Enter the folder where you want to execute commands (leave blank to use the current directory).

3. Provide instructions for the AI to generate shell commands.

4. Review the suggested command and choose whether to execute it.

5. Exit the program by typing `/bye`.

## Example

```plaintext
👋 Welcome to Modded Ollama 
📁 Enter folder to run commands in (default is current): /home/user/projects
/home/user/projects
🧠 What do you want the AI to do? Create a new Python virtual environment
📝 Ollama suggests:
cd "/home/user/projects" && python3 -m venv env

⚠️ Run this command? (y/n): y

🚀 Running the command...
```

## Notes

- Ensure the Ollama API is running and accessible at the specified URL.
- The program only executes commands in the context of the specified directory.

## License

This project is licensed under the MIT License.