import os
from dotenv import load_dotenv
from google import genai

def main():
    # Loads my enviorment from my .env file using dotenv and reads my API key
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Creates my client object
    client = genai.Client(api_key=api_key)

    # Creates my response object in the client/response modle setup
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("**********************************************************************")
    print("AI Resposne: \n")
    print(response.text)









if __name__ == "__main__":
    main()