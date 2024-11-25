import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def get_openai_response(user_prompt):
    """Get a response from OpenAI's text generation API"""
    system_prompt = "You are a very helpful assitant for learning Python."

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ],
    )
    response = completion.choices[0].message.content
    return response


def text_to_speech(text):
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )
    with open("data/speech.mp3", "wb") as file:
        for chunk in response.iter_bytes():
            file.write(chunk)


def speech_to_text(file_path):
    with open(file_path, "rb") as file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=file,
            response_format="text",
        )
    return transcript


def main():
    # user_prompt = input("What is your question? \n")
    # response = get_openai_response(user_prompt)
    # print(response)
    # text = input("Enter the text you want to convert to speech: \n")
    # text_to_speech(text)
    text = speech_to_text("data/speech.mp3")
    print(text)


main()
