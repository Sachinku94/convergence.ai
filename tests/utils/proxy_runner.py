# utils/proxy_runner.py
# import subprocess

# def run_proxy_prompt(prompt: str) -> str:
#     try:
#         result = subprocess.run(
#             ["python", "proxy.py", prompt],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             text=True,
#             cwd="convergence_tests\proxy-lite"  # adjust path if needed
#         )
#         return result.stdout.strip()
#     except Exception as e:
#         return f"Error running proxy: {e}"
from proxy__lite.src.proxy_lite import runner, RunnerConfig

def create_runner():
    config = RunnerConfig.from_dict(
        {
            "environment": {
                "name": "webbrowser",
                "homepage": "https://www.google.com",
                "headless": False,  # Set to True for headless mode
            },
            "solver": {
                "name": "simple",
                "agent": {
                    "name": "proxy_lite",
                    "client": {
                        "name": "convergence",
                        "model_id": "convergence-ai/proxy-lite-3b",
                        "api_base": "https://convergence-ai-demo-api.hf.space/v1",
                    },
                },
            },
            "max_steps": 50,
            "action_timeout": 1800,
            "environment_timeout": 1800,
            "task_timeout": 18000,
            "logger_level": "DEBUG",
        }
    )
    return runner(config=config)

