import json
import requests
from googletrans import Translator 
from PIL import Image
import pytesseract
import speech_recognition as sr
import os
# googletrans es utilizado para traducir el texto al idioma deseado
# speech_recognition para trnascribir el audio
# PIL para las imagenes

def translate_text():
    print("Ingrese el texto y el idioma objetivo en formato JSON (por ejemplo: {'text': 'Hello', 'language': 'es'}):")
    input_data = input()
    try:
        data = json.loads(input_data)
        text = data['text']
        target_language = data['language']
        translator = Translator()
        translated = translator.translate(text, dest=target_language)
        print(f"Texto traducido: {translated.text}")
    except Exception as e:
        print(f"Error al traducir el texto: {e}")

def download_image():
    print("Ingrese la URL de la imagen que desea descargar:")
    url = input()
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            filename = url.split("/")[-1]
            with open(filename, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Imagen descargada y guardada como {filename}")
        else:
            print("Error al descargar la imagen: URL no válida o inaccesible.")
    except Exception as e:
        print(f"Error al descargar la imagen: {e}")

def solve_problem_from_image():
    print("Ingrese la ruta del archivo PNG que contiene el problema:")
    image_path = input()
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        print(f"Texto extraído de la imagen: {text}")
    except Exception as e:
        print(f"Error al procesar la imagen: {e}")

def transcribe_audio():
    print("Ingrese la ruta del archivo de audio que desea transcribir:")
    audio_path = input()
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language="es-ES")  # Cambia el idioma según necesidad
            print(f"Transcripción del audio: {text}")
    except Exception as e:
        print(f"Error al transcribir el audio: {e}")

def main_menu():
    while True:
        print("\nAsistente interactivo: Seleccione una opción")
        print("1. Traducción de texto")
        print("2. Descargar imagen desde una URL")
        print("3. Resolver problemas desde una imagen")
        print("4. Transcribir audio")
        print("5. Salir")
        choice = input("Ingrese el número de su elección: ")

        if choice == '1':
            translate_text()
        elif choice == '2':
            download_image()
        elif choice == '3':
            solve_problem_from_image()
        elif choice == '4':
            transcribe_audio()
        elif choice == '5':
            print("Saliendo del asistente. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main_menu()