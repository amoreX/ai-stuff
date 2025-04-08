# Local Agent with Ollama Integration

This Python program acts as a local agent that integrates with the Ollama API to generate shell commands based on user instructions. It allows users to execute commands in a specified directory with the help of AI-generated suggestions.

## Features

- Interacts with the Ollama API to generate shell commands.
- Allows users to specify a working directory for command execution.
- Provides an option to review and confirm commands before execution.
- Maintains a **chat history** of user instructions and AI responses for context-aware suggestions.
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

## Chat History

The program maintains a chat history of all user instructions and AI responses. This history is used to provide context-aware suggestions. The chat history is saved to a `history.json` file in the project directory and is loaded automatically when the program starts.

### Chat History Functions

- **`save_chat(role, content)`**: Saves a message to the chat history with the specified role (`user` or `assistant`) and content.
- **`get_chat()`**: Retrieves the current chat history.

## Helper Functions

- **`construct_prompt(cwd, user_instruction, chat_history)`**: Constructs a context-aware prompt for the AI using the current working directory, user instruction, and chat history.
- **`run_shell_command(cmd, cwd)`**: Executes a shell command in the specified working directory.
- **`ask_ollama(prompt)`**: Sends a prompt to the Ollama API and retrieves the AI's response.

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
- The chat history is stored persistently in `history.json` and can be reviewed or cleared as needed.

## License

This project is licensed under the MIT License.