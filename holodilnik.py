import datetime
from decimal import Decimal

DATE_FORMAT = "%Y-%m-%d"
goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ]
}

def add(items, title, amount, expiration_date=None):
    """Добавляет продукт в словарь items."""
    if expiration_date is not None:
        exp_date = datetime.datetime.strptime(expiration_date, DATE_FORMAT).date()
    else:
        exp_date = None

    if title not in items:
        items[title] = []
        
    items[title].append({
        'amount': amount,
        'expiration_date': exp_date
    })

def add_by_note(items, note):
    """Преобразует текстовую строку и добавляет продукт в словарь items."""
    parts = note.split()

    if '-' in parts[-1]:
        expiration_date = parts[-1]
        amount = parts[-2]
        # Объединяем оставшиеся части в название продукта
        title = ' '.join(parts[:-2])
    else:
        expiration_date = None
        amount = parts[-1]
        title = ' '.join(parts[:-1])
        
    amount = Decimal(amount)
    add(items, title, amount, expiration_date)

def find(items, needle):
    """Ищет продукты в холодильнике."""
    found_items = []
    for title in items.keys():
        if needle.lower() in title.lower():
            found_items.append(title)
            
    return found_items

def amount(items, needle):
    """Возвращает общее колво запрошенного продукта."""
    found_products = find(items, needle)
    total = Decimal('0')
    
    for title in found_products:
        for partiya in items[title]:
            total += partiya['amount']
            
    return total
