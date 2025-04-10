# Local Agent with Ollama Integration

This Python program acts as a local agent that integrates with the Ollama API to generate shell commands based on user instructions. It allows users to execute commands in a specified directory with the help of AI-generated suggestions.

## Features

- **Text Input**: Users can type their instructions directly.
- **Voice Input**: Users can now use voice commands to interact with the AI. The tool records and transcribes the user's voice input using the Whisper model.
- **Chat History**: Maintains a record of user instructions and AI responses for context-aware suggestions.
- **Command Execution**: Suggests shell commands and allows users to execute them directly.
- **Context-Aware Prompts**: Constructs prompts using the current working directory and chat history for better AI responses.

## Requirements

- Python 3.7 or higher
- Required Python libraries:
  - `requests`
  - `whisper`
- A running instance of the Ollama API at `http://localhost:11434`
- `arecord` utility for voice recording (Linux systems)

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required Python dependencies:
   ```bash
   pip install requests whisper
   ```

3. Ensure `arecord` is installed on your system for voice recording:
   ```bash
   sudo apt install alsa-utils
   ```

## Usage

1. Run the program:
   ```bash
   python local-agent.py
   ```

2. Enter the folder where you want to execute commands (leave blank to use the current directory).

3. Choose the input mode:
   - Press `ENTER` for text input.
   - Type `v` and press `ENTER` for voice input.

4. Provide instructions for the AI to generate shell commands.

5. Review the suggested command and choose whether to execute it.

6. Exit the program by typing `/bye`.

## Voice Input

The voice input functionality uses the `record_and_transcribe` method from the `helpers.voice_input` module. It records audio using the `arecord` utility and transcribes it using the Whisper model. Ensure your microphone is set up and accessible for this feature.

### Example Workflow with Voice Input

```plaintext
👋 Welcome to Modded Ollama 
📁 Enter folder to run commands in (default is current): /home/user/projects
/home/user/projects
🗣️ Type 'v' for voice input or press ENTER for text input: v
🎤 Using voice input...
🎤 Recording... Press ENTER to stop.
🧠 You said: List all files in this directory
📝 Ollama suggests:
cd "/home/user/projects" && ls -la

⚠️ Run this command? (y/n): y

🚀 Running the command...
```

## Chat History

The program maintains a chat history of all user instructions and AI responses. This history is used to provide context-aware suggestions. The chat history is saved to a `history.json` file in the project directory and is loaded automatically when the program starts.

### Chat History Functions

- **`save_chat(role, content)`**: Saves a message to the chat history with the specified role (`user` or `assistant`) and content.
- **`get_chat()`**: Retrieves the current chat history.

## Helper Modules

### `helpers/voice_input.py`
- **`record_and_transcribe()`**: Records audio from the microphone and transcribes it using the Whisper model.

### `helpers/ollama.py`
- **`ask_ollama(prompt)`**: Sends a prompt to the Ollama API and retrieves the AI's response.

### `helpers/shell.py`
- **`run_shell_command(cmd, cwd)`**: Executes a shell command in the specified working directory.

### `helpers/chat_history.py`
- **`save_chat(role, content)`**: Saves a message to the chat history.
- **`get_chat()`**: Retrieves the current chat history.

### `helpers/sessions.py`
- **`save_history(chat_history, file)`**: Saves the chat history to a JSON file.
- **`load_history(file)`**: Loads the chat history from a JSON file.

### `prompt_utils.py`
- **`construct_prompt(cwd, user_instruction, chat_history)`**: Constructs a context-aware prompt for the AI using the current working directory, user instruction, and chat history.

## Notes

- Ensure the Ollama API is running and accessible at the specified URL.
- The program only executes commands in the context of the specified directory.
- The chat history is stored persistently in `history.json` and can be reviewed or cleared as needed.
