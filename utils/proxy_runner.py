# utils/proxy_runner.py
import subprocess

def run_proxy_prompt(prompt: str) -> str:
    try:
        result = subprocess.run(
            ["python", "proxy.py", prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd="../proxy-lite"  # adjust path if needed
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error running proxy: {e}"
