import requests
from django.shortcuts import render


def dogs_view(request):
    # Получаем список всех пород
    breeds_res = requests.get("https://dog.ceo/api/breeds/list/all")
    breeds = (
        list(breeds_res.json().get("message", {}).keys())
        if breeds_res.status_code == 200
        else []
    )

    # Обрабатываем строку поиска из формы
    query = request.GET.get("breeds", "")
    images = []

    if query:
        # Разбиваем введенную строку на отдельные породы, убираем пробелы
        breed_names = [b.strip().lower() for b in query.split(",") if b.strip()]
        for b in breed_names:
            img_res = requests.get(f"https://dog.ceo/api/breed/{b}/images/random")
            if img_res.status_code == 200:
                images.append({"name": b, "url": img_res.json().get("message")})

    # Передаем переменные в контекст шаблона
    return render(
        request, "dogs.html", {"breeds": breeds, "images": images, "query": query}
    )
