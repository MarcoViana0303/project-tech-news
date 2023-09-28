import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    # Define o header user-agent
    headers = {"user-agent": "Fake user-agent"}

    try:
        # Faz a requisição HTTP com um timeout de 3 segundos
        response = requests.get(url, headers=headers, timeout=3)

        # Verifica se o status code é 200 (OK)
        if response.status_code == 200:
            # Retorna o conteúdo HTML da resposta
            return response.text
        else:
            # Em caso de status code diferente de 200, retorna None
            return None
    except requests.exceptions.Timeout:
        # Caso ocorra um timeout, retorna None
        return None
    except requests.exceptions.RequestException:
        # Caso ocorra outra exceção durante a requisição, retorna None
        return None
    finally:
        # Aguarda 1 segundo antes de fazer a próxima requisição
        time.sleep(1)


# Requisito 2
def scrape_updates(html_content):
    try:
        selector = (
            Selector(text=html_content)
            .css(".entry-title a::attr(href)").getall()
        )
        return selector
    except Exception:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
