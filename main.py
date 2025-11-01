import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    # Loads my enviorment from my .env file using dotenv and reads my API key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Creates my client object
    client = genai.Client(api_key=api_key)

    # Checks all system args for verbose flag, if found verbose is set to True else args are appended to list 
    args = sys.argv[1:]
    verbose = False
    prompt_parts = []

    for a in args:
        if a == "--verbose":
            verbose = True
        else:
            prompt_parts.append(a)
    
    user_prompt = " ".join(prompt_parts)

    # Checks for sys.argv, if none provided raises error and exits
    if len(user_prompt) <= 0: 
        print("Missing argmunet... \n")
        print("Expected: uv run main.py 'your prompt here'")
        print("Example: uv run main.py 'What is the meaning of life?'")
        sys.exit(1)

    # Sets user prompt as the only message 
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Creates my response object in the client/response modle setup
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents = messages,
    )

    # Checks for verbose flag and outputs if found
    if verbose == True:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    # Prints response 
    print("AI Resposne: \n")
    print(response.text)






if __name__ == "__main__":
    main()