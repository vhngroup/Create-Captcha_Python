from captcha.image import ImageCaptcha
from PIL import Image
import string
import random

def generate_Catpcha_Text(length):
    letter = ''.join(random.choices(string.ascii_letters+string.digits, k=length))
    return letter

def generate_Captcha(len_captcha, save_path='Captcha.png'):
    image = ImageCaptcha(width=500, height=100)
    captcha_text = generate_Catpcha_Text(len_captcha)
    data = image.generate(captcha_text)
    image.write(captcha_text, save_path)
    return captcha_text


if __name__ == "__main__":
    while True:
        try:
            len_captcha = int(input("ingrese el numero de caracteres del la captcha "))
            captcha_text = generate_Captcha(len_captcha)
            print("Captcha Generada: ", captcha_text)
            Image.open('Captcha.png')
        except:
            print("No ingresaste un numero valido")
            break