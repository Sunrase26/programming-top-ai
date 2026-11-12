import requests
import random


class PokemonManager:
    def __init__(self):
        self.team = {}

    def _get_api(self, name):
        res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
        return res.json() if res.status_code == 200 else None

    def add(self, name):
        name = name.lower()
        if name not in self.team:
            data = self._get_api(name)
            if data:
                self.team[name] = {
                    "name": data["name"].capitalize(),
                    "weight": data["weight"],
                    "height": data["height"],
                    "exp": data["base_experience"],
                }

    def remove(self, name):
        self.team.pop(name.lower(), None)

    def view(self):
        for data in self.team.values():
            print(
                f"{data['name']} | Рост: {data['height']} | Вес: {data['weight']} | Опыт: {data['exp']}"
            )

    def search(self, name):
        data = self._get_api(name)
        if data:
            print(
                f"Найден: {data['name'].capitalize()} (Опыт: {data['base_experience']})"
            )
        else:
            print("Не найден.")

    def battle(self, name1, name2):
        p1 = self.team.get(name1.lower()) or self._get_api(name1)
        p2 = self.team.get(name2.lower()) or self._get_api(name2)

        if p1 and p2:
            exp1 = p1.get("exp", p1.get("base_experience", 0)) + random.randint(1, 50)
            exp2 = p2.get("exp", p2.get("base_experience", 0)) + random.randint(1, 50)

            n1, n2 = p1["name"].capitalize(), p2["name"].capitalize()
            if exp1 > exp2:
                print(f"Победил {n1}")
            elif exp2 > exp1:
                print(f"Победил {n2}")
            else:
                print("Ничья")


if __name__ == "__main__":
    pm = PokemonManager()
    pm.add("pikachu")
    pm.add("bulbasaur")
    pm.view()
    pm.search("snorlax")
    pm.battle("pikachu", "bulbasaur")
    pm.remove("bulbasaur")
