from dotenv import load_dotenv
from pathlib import Path
import os

logo_bot = """
________________________________________________________________________________________________________

 ▄██████▄   ▄█        ▄█   ▄█    █▄     ▄████████    ▄████████      ▀█████████▄   ▄██████▄      ███     
███    ███ ███       ███  ███    ███   ███    ███   ███    ███        ███    ███ ███    ███ ▀█████████▄ 
███    ███ ███       ███▌ ███    ███   ███    █▀    ███    ███        ███    ███ ███    ███    ▀███▀▀██ 
███    ███ ███       ███▌ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀       ▄███▄▄▄██▀  ███    ███     ███   ▀ 
███    ███ ███       ███▌ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀        ▀▀███▀▀▀██▄  ███    ███     ███     
███    ███ ███       ███  ███    ███   ███    █▄  ▀███████████        ███    ██▄ ███    ███     ███     
███    ███ ███▌    ▄ ███  ███    ███   ███    ███   ███    ███        ███    ███ ███    ███     ███     
 ▀██████▀  █████▄▄██ █▀    ▀██████▀    ██████████   ███    ███      ▄█████████▀   ▀██████▀     ▄████▀   
           ▀                                        ███    ███                                          
________________________________________________________________________________________________________        
        Developed by: WHIAGO https://github.com/WictorHiago
        Bot Version: 1.0 | Python 3.10 | openai 1.3.5
"""


load_dotenv()
openai_key = os.getenv("OPENAI_KEY")
from openai import OpenAI

client = OpenAI(api_key=openai_key)

def chat_completion(message:str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=300,
        temperature=0.3,
        top_p=1,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ]
    )

    return response.choices[0].message.content

# ---RUN TEST chat_completion---
# gpt_response = chat_completion("how to lean python fast?")
# print(gpt_response)
# ----------------------------------------------

def create_speech():
    speech_file_path = Path(__file__).parent / "new-audio.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        input="Ahhh a.. Zeeh da Manhgha",
        voice="onyx",
        response_format="mp3",
        speed=1.0
    )

    print("Successfully created speech!")

    response.stream_to_file(speech_file_path)

# ---RUN TEST create_speech---
create_speech()
# ----------------------------------------------

# TRANSCRIBE AUDIO TO LANGUAGES ru|en|fr|es|de|it ...
def create_transcript():
    audio_file = open("audio.mp3", "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    language="fr",
    response_format="text",
    )

    return transcript

# ---RUN TEST create_transcript---
# audio_transcript = create_transcript()
# print(audio_transcript)
# ----------------------------------------------

# TRANSLATE AUDIO TO ENGLISH
def whisper():
    audio_file = open("audio.mp3", "rb")
    transcript = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file,
    response_format="text",
    )

    return transcript
    

# ---RUN TEST whisper---
# whisper_response = whisper()
# print(whisper_response)
# ----------------------------------------------

if __name__ == "__main__":
    print(logo_bot)
    print("""
Oliver say: Hello! How can I help you?

1. Transcribe audio to text
2. Translate audio to another language
3. Create audio from text
4. Translate text
5. Exit

Enter the number of the desired option and press Enter:

""")
    pass