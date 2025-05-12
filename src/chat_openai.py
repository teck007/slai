import os
from dotenv import load_dotenv
from openai import OpenAI

# Carga las variables del archivo .env
load_dotenv()
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)
def chat(mensaje_usuario: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-nano", 
        messages=[
            {"role": "user", "content": mensaje_usuario}
        ]
    )
    # 3. Extrae y devuelve el texto
    return response.choices[0].message.content

def shorten(url: str, descripcion: str,) -> str:
    prompt = (
        f"tengo esta url " + url +" y esta descripcion " + descripcion + " quiero transformar la url " +
            "y descripciona un texto corto representativo y en el menor cantidad de caracteres posibles y" + 
            "solo con minusculas, debes solo entregarme una sola opcion de nombre corto y nada mas, ideal " +
            "solo desde 4 a 10 caracteres basandose principalmente en la descripcion")
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-nano", 
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print(e)
