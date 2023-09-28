from tech_news.database import db
from datetime import datetime


# Requisito 7
def search_by_title(title):
    # Realiza a busca no banco de dados por título (case insensitive)
    results = db.news.find({"title": {"$regex": title, "$options": "i"}})

    # Transforma os resultados em uma lista de tuplas (título, URL)
    news_list = [(result["title"], result["url"]) for result in results]

    return news_list


# Requisito 8
def search_by_date(date):
    try:
        # Converte a data para o formato dd/mm/AAAA
        formatted_date = (
            datetime.strptime(date, "%Y-%m-%d")
            .strftime("%d/%m/%Y")
        )
    except ValueError:
        raise ValueError("Data inválida")

    # Realiza a busca no banco de dados por data
    results = db.news.find({"timestamp": formatted_date})

    # Transforma os resultados em uma lista de tuplas (título, URL)
    news_list = [(result["title"], result["url"]) for result in results]

    return news_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
