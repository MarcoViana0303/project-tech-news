import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    # Cria um seletor Parsel a partir do conteúdo HTML
    try:
        selector = (
            Selector(text=html_content)
            .css(".entry-title a::attr(href)").getall()
        )
        return selector
    except Exception:
        # Em caso de erro, retorna uma lista vazia
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    try:
        # Criando um seletor Parsel a partir do conteúdo HTML
        selector = Selector(text=html_content)

        # Usando o seletor XPath para extrair a URL da próxima página
        next_page_link = (
            selector
            .xpath('//a[contains(@class, "next")]/@href')
            .extract_first()
        )

        # Retornando a URL obtida ou None se não encontrar
        return next_page_link
    except Exception:
        # Em caso de erro, retorna None
        return None


# Requisito 4
def scrape_news(html_content):
    try:
        # Criando um seletor Parsel a partir do conteúdo HTML
        selector = Selector(text=html_content)

        # Extrair informações da notícia
        url = (
            selector.css('link[rel=canonical]::attr(href)').get()
            )
        title = (
            selector.css('h1.entry-title::text')
            .get().strip()
        )
        timestamp = (
            selector.css('li.meta-date::text')
            .get()
        )
        writer = (
            selector.css('span.author a::text')
            .get()
        )
        reading_time = (
            int(selector.css('.meta-reading-time::text')
                .re_first(r'\d+'))
        )
        summary = (
            ''.join(selector.css('.entry-content > p:first-of-type *::text')
                    .getall()).strip()
        )
        category = (
            selector.css('.category-style span.label::text')
            .get()
        )

        # Criando o dicionário com as informações
        news_data = {
            "url": url,
            "title": title,
            "timestamp": timestamp,
            "writer": writer,
            "reading_time": reading_time,
            "summary": summary,
            "category": category,
        }

        return news_data
    except Exception as e:
        # Em caso de erro, imprima a exceção para depuração
        print(f"Error: {e}")
        return None


# Requisito 5
def get_tech_news(amount):
    base_url = 'https://blog.betrybe.com'
    news_links = []
    news_list = []

    while len(news_links) < amount:
        html = fetch(base_url)
        news_links.extend(scrape_updates(html))
        base_url = scrape_next_page_link(html)

    for link in news_links[:amount]:
        html = fetch(link)
        scraped_news = scrape_news(html)
        news_list.append(scraped_news)

    create_news(news_list)

    return news_list
