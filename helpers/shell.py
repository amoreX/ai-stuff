import subprocess

def run_shell_command(cmd, cwd):
    subprocess.run(cmd, shell=True, cwd=cwd)
