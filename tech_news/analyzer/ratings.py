from tech_news.database import db


# Requisito 10
def top_5_categories():
    # Obtém a coleção de notícias do banco de dados
    news_collection = db.get_collection("news")

    # Define uma sequência de operações de agregação
    # para calcular as categorias mais populares
    pipeline = [
        # Separa cada categoria em documentos individuais
        {"$unwind": "$category"},
        # Agrupa as categorias e conta o número de ocorrências
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        # Ordena as categorias por contagem decrescente e,
        # em caso de empate, por ordem alfabética
        {"$sort": {"count": -1, "_id": 1}},
        # Limita o resultado às cinco categorias mais populares
        {"$limit": 5},
    ]

    # Executa as operações de agregação e armazena os resultados em uma lista
    results = list(news_collection.aggregate(pipeline))

    # Extrai apenas os nomes das categorias dos resultados
    top_categories = [result["_id"] for result in results]

    # Retorna as cinco categorias mais populares
    return top_categories
