<h2>OLIVER BOT</h2>

Oliver é um bot em Python desenvolvido com api da openai

<p align="center">
<img src="https://github.com/WictorHiago/oliver-bot-python/blob/main/assets/avatar-bot-oliverx.png" width="50%" rigth="">
</p>
<br>
<p align="center">
<img src="https://github.com/WictorHiago/oliver-bot-python/blob/main/assets/text-logo-oliver-bot.png" width="70%">
</p>

<h2>API_KEY OPENAI</h2>
<h3>Necessário ter Créditos ou Assinatura</h3>
<p>Você precisa ter uma chave de api da OpenAI
visitando o site oficial <a href="https://openai.com/" target="blank">openai</a>
você facilmente obtem tem acesso a documentação caso queira saber mais sobre a API</p>

```
# crie um arquivo .env na raiz do projeto
OPENAI_KEY=COLOQUE_SUA_API_KEY_AQUI

```

<h2>Documentação oficial OpenAI</h2>
<a href="https://platform.openai.com/docs/introduction" target="blank">documentação</a>

<h2>Install</h2>

```
# update linux
sudo apt update

# create local enviroment
python3 -m venv .venv
source .venv/bin/activate

pip install openai
pip install python-dotenv

# verify functions for test
## example: create audio in format mp3 from input text
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

# run in root folder

python src/main.py

```

<span>More functions in development</span>
