import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=20")
if response.status_code == 200:
    for p in response.json()["results"]:
        print(f"- {p['name']}")

name = input("\nИмя покемона: ").strip().lower()
res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")

if res.status_code == 200:
    data = res.json()
    types = [t["type"]["name"] for t in data["types"]]
    abilities = [a["ability"]["name"] for a in data["abilities"]]

    print(f"\nИмя: {data['name'].capitalize()}")
    print(f"Тип: {', '.join(types)}")
    print(f"Вес: {data['weight']}")
    print(f"Рост: {data['height']}")
    print(f"Способности: {', '.join(abilities)}")
else:
    print("Покемон не найден.")
