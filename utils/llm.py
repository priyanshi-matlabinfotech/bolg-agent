from crewai import LLM

def get_ollama():
    return LLM(
        model="ollama/deepseek-r1:32b",
        temperature=1,
        base_url="https://9ae8-2405-201-202e-b821-536b-183e-471f-a292.ngrok-free.app"

    )
