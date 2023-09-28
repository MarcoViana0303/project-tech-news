from tech_news.database import db


# Requisito 7
def search_by_title(title):
    # Realiza a busca no banco de dados por título (case insensitive)
    results = db.news.find({"title": {"$regex": title, "$options": "i"}})

    # Transforma os resultados em uma lista de tuplas (título, URL)
    news_list = [(result["title"], result["url"]) for result in results]

    return news_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
