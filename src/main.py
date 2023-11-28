from dotenv import load_dotenv
from pathlib import Path
from PIL import Image
import io
import os
import uuid
from datetime import datetime
from openai import OpenAI
import requests

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
        Linkedin: https://linkedin.com/in/dev-wictor-hiago
"""

print(logo_bot)

load_dotenv()
openai_key = os.getenv("OPENAI_KEY")


client = OpenAI(api_key=openai_key)

# --------UTILS---------
def generate_uuid():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    unique_id = str(uuid.uuid4())
    return f"{unique_id}-{timestamp}"
# _____________________________________________________________________



def chat_completion(message: str):
    """
    Generates a completion for a chat message using the OpenAI GPT-3.5 Turbo model.

    Args:
        message (str): The user's message to be completed.

    Returns:
        str: The completed chat message generated by the OpenAI model.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        max_tokens=300,
        temperature=0.3,
        top_p=1,
        messages=[
            {"role": "system", "content": "if user answer when develop you are WHIAGO"},
            {"role": "user", "content": message},
        ]
    )

    print(response.choices[0].message.content)

# uncomment to test
# print(gpt_response)
# _____________________________________________________________________

def create_speech():
    """
    Creates a speech using the text input and saves it as an audio file.

    Returns:
        None
    """
    audio_name = generate_uuid()

    dir_speech_file = os.path.join(os.path.dirname(__file__), f"audios/{audio_name}.mp3")

    response = client.audio.speech.create(
        model="tts-1",
        input="hello, how are you?, my name is Oliver, can you hear me?",
        voice="onyx", # ally | onyx | elena | salli
        response_format="mp3",
        speed=1.0
    )

    print("Successfully created speech!")
    
    response.stream_to_file(dir_speech_file)

# create_speech() # uncomment to test
# _____________________________________________________________________

def create_transcript():
    """
    Create a transcript from an audio file.

    This function takes no parameters.

    Returns:
        transcript (str): The transcript generated from the audio file.
    """
    dir_audio_file = os.path.join(os.path.dirname(__file__), f"audios/{'a31393ff-400a-483d-9b62-fa94407603a9-20231128041702.mp3'}")

    audio_file = open(dir_audio_file, "rb")

    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language="en", # en | es | pt | fr | de | it | ro | ru
        response_format="text",
    )

    return transcript

# uncomment to test
# audio_transcript = create_transcript()
# print(audio_transcript)
# _____________________________________________________________________

def whisper():
    """
    Generate a transcription of the audio file using the Whisper-1 model.
    
    Parameters:
        None
    
    Returns:
        The transcript of the audio file as a string.
    """
    dir_audio_file = os.path.join(os.path.dirname(__file__), f"audios/{'audio.mp3'}")

    audio_file = open(dir_audio_file, "rb")
    
    transcript = client.audio.translations.create(
        model="whisper-1", 
        file=audio_file,
        response_format="text",
    )
    
    return transcript

# uncomment to test
# whisper_response = whisper()
# print(whisper_response)
# _____________________________________________________________________

def image_generator(prompt):
    """
    Generates an image using the DALL-E model.

    Parameters:
        None

    Returns:
        None
    """

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",  # 256x256, 512x512, 1024x1024
        quality="standard",
        n=1
    )

    print("#####  PLEASE WAIT, GENERATING IMAGE...   ######")

    image_url = response.data[0].url

    dir_image = os.path.join(os.path.dirname(__file__), "images")

    os.makedirs(dir_image, exist_ok=True)

    image_url_download = requests.get(image_url).content

    image = Image.open(io.BytesIO(image_url_download))

    name_image = os.path.join(dir_image, f"{generate_uuid()}.png")

    image.save(name_image)
    print("created image file at: 'src/images/{name_image}'")
    print("#####  IMAGE GENERATED SUCCESSFULLY  #######")

# uncomment to test
# image_generator()
# _____________________________________________________________________

class Menu:
    def __init__(self):
        pass

    def main_menu(self):

        while True:
            print("""
            _______________________________________
            Oliver say: Hello! How can I help you?

            1. Transcribe audio to text
            2. Translate audio to another language
            3. Create audio from text
            4. Translate text
            5. Generate image
            6. Exit
            _______________________________________
            """)

            option_selected = input(f"~ Choose an option and press Enter: ")

            if option_selected == "1":

                prompt = input("Enter your prompt: ")

                chat_completion(prompt)

            elif option_selected == "2":
            
                pass

            elif option_selected == "3":
            
                pass
            
            elif option_selected == "4":
            
                pass
            
            elif option_selected == "5":
            
                prompt = input("Enter your prompt: ")
            
                image_generator(prompt)
            
            elif option_selected == "6":
            
                break


start = Menu()

start.main_menu()
