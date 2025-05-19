import requests
from bs4 import BeautifulSoup
import openai

def url_content(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        texto = soup.get_text().replace("\n", "")
        return texto[:500]
    except Exception as e:
        return f"Error al acceder a la URL: {str(e)}"