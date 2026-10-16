class SpaceShip:
    def __init__(self, toplivo, korpus, speed):
        self.toplivo = toplivo
        self.korpus = korpus
        self.speed = speed

    def show_status(self):
        print(f"--- СТАТУС КОРАБЛЯ ---")
        print(
            f"Топливо: {self.toplivo}%, Корпус: {self.korpus}%, Скорость: {self.speed} км/ч"
        )


class CrewMember:
    def __init__(self, name, health, skills, role):
        self.name = name
        self.health = health
        self.skills = skills
        self.role = role


class Mission:
    def __init__(self, target, resources):
        self.target = target
        self.resources = resources

    def event(self, ship, event_type):
        """Возможные события во время миссии"""
        print(f"\n Внимание! Событие на пути к цели '{self.target}': {event_type}!")

        if event_type == "авария":
            ship.korpus -= 30
            ship.speed = 0
            print("Корпус сильно поврежден! Скорость упала до 0.")

        elif event_type == "встреча с астероидами":
            ship.toplivo -= 20
            print(
                "Корабль успешно маневрировал между астероидами, но потратил топливо."
            )


# Проверка работы кода
moy_korabl = SpaceShip(toplivo=100, korpus=100, speed=10000)

pilot = CrewMember(name="Алексей", health=100, skills=["маневрирование"], role="пилот")
injener = CrewMember(
    name="Елена", health=100, skills=["ремонт реактора"], role="инженер"
)

moya_missiya = Mission(
    target="Полет на Марс", resources=["кислород", "воода", "аптечки"]
)

moy_korabl.show_status()

moya_missiya.event(moy_korabl, "авария")

moy_korabl.show_status()
