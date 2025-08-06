import subprocess

def run_gemma(prompt: str) -> str:
    """
    Sends prompt to locally running Ollama instance with Gemma model.
    """
    command = ["ollama", "run", "gemma3n:e4b", prompt]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()
