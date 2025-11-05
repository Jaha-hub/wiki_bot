# Cristiano Ronaldo лучше чем Лионель Месси
import requests
def get_wikipedia_results(query: str, lang:str = "ru"):
    url = f"https://{lang}.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
    }
    response = requests.get(url, params=params, headers=headers)
    data = response.json().get("query").get("search")
    return data
print(get_wikipedia_results("Роналду"))