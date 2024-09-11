import openai
from instabot import Bot
from PIL import Image, ImageDraw, ImageFont
import random
import os
from themes import themes

# Configurações da API OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

# Função para gerar frase motivacional
def generate_motivational_quote(theme):
    print(f"Gerando frase motivacional para o tema: {theme}")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Crie uma frase motivacional sobre {theme}.",
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Função para criar imagem com a frase
def create_image_with_quote(quote, theme):
    print(f"Criando imagem com a frase: {quote}")
    img = Image.new('RGB', (800, 400), color=(73, 109, 137))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((10, 10), quote, fill=(255, 255, 0), font=font)
    image_path = f"images/{theme.replace(' ', '_')}.png"
    img.save(image_path)
    return image_path

# Função para postar no Instagram
def post_to_instagram(image_path, caption):
    print(f"Postando no Instagram: {image_path}")
    bot = Bot()
    bot.login(username=os.getenv('INSTAGRAM_USERNAME'), password=os.getenv('INSTAGRAM_PASSWORD'))
    bot.upload_photo(image_path, caption=caption)

# Função principal
def main():
    theme = random.choice(themes)
    print(f"Tema escolhido: {theme}")
    quote = generate_motivational_quote(theme)
    image_path = create_image_with_quote(quote, theme)
    post_to_instagram(image_path, quote)

if __name__ == "__main__":
    main()
