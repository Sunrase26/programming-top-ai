class Product:
    def __init__(self, name, price, count, category):
        self.name = name
        self.price = price
        self.count = count
        self.category = category


class Order:
    def __init__(self, tovary_v_zakaze, sale=0, nalog=0):
        self.tovary_v_zakaze = tovary_v_zakaze
        chistaya_cena = 0

        for tovar, kolichestvo in tovary_v_zakaze.items():
            chistaya_cena += tovar.price * kolichestvo

        self.total_price = chistaya_cena - sale + nalog


class ShoppingCart:
    def __init__(self):
        self.items = {}  # Словарь вида: {продукт: количество}

    def add_item(self, product, quantity=1):
        """Добавляет товар в корзину"""
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product):
        """Удаляет товар из корзины"""
        if product in self.items:
            del self.items[product]

    def update_quantity(self, product, quantity):
        """Обновляет колво товара"""
        if quantity <= 0:
            self.remove_item(product)
        else:
            self.items[product] = quantity


class Customer:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.shopping_cart = ShoppingCart()
        self.order_history = []

    def checkout(self, sale=0, nalog=0):
        """Оформляет заказ: берет товары из корзины и сохраняет в историю"""
        new_order = Order(self.shopping_cart.items, sale, nalog)
        self.order_history.append(new_order)
        print(f"Заказ оформлен! Итоговая стоимость: {new_order.total_price} руб.")
        self.shopping_cart = ShoppingCart()
        return new_order


# Проверка работы кода
phone = Product("Смартфон", 50000, 10, "Электроника")
case = Product("Чехол", 1000, 20, "Аксессуары")

buyer = Customer("Иван", "ivan@mail.ru")
buyer.shopping_cart.add_item(phone, 1)
buyer.shopping_cart.add_item(case, 5)
buyer.shopping_cart.update_quantity(case, 2)

my_order = buyer.checkout(sale=2000, nalog=0)
