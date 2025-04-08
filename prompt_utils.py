def construct_prompt(cwd, user_instruction,chat_history):
    """
    Constructs the system prompt for the AI assistant.
    
    Args:
        cwd (str): The current working directory.
        user_instruction (str): The user's instruction.

    Returns:
        str: The constructed prompt.
    """
    
    history_str = ""
    for message in chat_history:
        role = message["role"]
        content = message["content"]
        history_str += f"{role.upper()}: {content}\n"
    
    messages =  f"""
                You are a professional software engineer assistant.
                The user is currently working in the directory: '{cwd}'.
                You MUST begin all shell commands with 'cd "{cwd}" &&' to ensure correct context.
                If your task creates a subdirectory (e.g. with create-next-app), make sure to 'cd' into it after creation.
                Below is the previous chat history. Use it to understand what has already been done:
                {history_str}
                ONLY respond with valid shell commands to accomplish this task given by the user.
                '{user_instruction}'
                DO NOT include explanations, comments, may reply with text outside of commands only if task asked by user involves no commands , else ony reply with commands
    """
    return messages