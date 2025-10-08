import os
from dotenv import load_dotenv
from clients.gemini_client import GeminiClient

def main():
    # Load environment variables from the .env file
    load_dotenv()

    # Get the API key from the environment variables
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY is not set in the environment.")
        return

    # Create an instance of the Gemini client
    client = GeminiClient(api_key=api_key)

    # Prompt the user for input
    print("Welcome to the content generator with Gemini.")
    prompt = input("Please enter the prompt: ")

    # Generate content using the client
    try:
        response = client.generate(prompt)
        print("\nGenerated content:")
        print(response)
    except RuntimeError as e:
        print(f"Error generating content: {e}")

if __name__ == "__main__":
    main()