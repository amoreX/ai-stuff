def construct_prompt(cwd, user_instruction):
    """
    Constructs the system prompt for the AI assistant.
    
    Args:
        cwd (str): The current working directory.
        user_instruction (str): The user's instruction.

    Returns:
        str: The constructed prompt.
    """
    return (f"""
        You are a professional software engineer assistant.

        The user is currently working in the directory: '{cwd}'.
        You MUST begin all shell commands with 'cd "{cwd}" &&' to ensure correct context.
        If your task creates a subdirectory (e.g. with create-next-app), make sure to 'cd' into it after creation.

        ONLY respond with valid shell commands to accomplish the task:
        '{user_instruction}'

        DO NOT include explanations, comments, or non-command text.
        """)
