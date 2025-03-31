sales = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
    {"item": "peach", "category": "fruit", "price": 0.7, "quantity": 8},
    {"item": "grapes", "category": "fruit", "price": 2.0, "quantity": 1},
    {"item": "eggs", "category": "dairy", "price": 1.3, "quantity": 4}
]


def total_revenue(purchases):
    res = 0
    for purchase in range(len(purchases)):
        res += purchases[purchase]['price'] * purchases[purchase]['quantity']

    return f'Общая выручка: {round(res, 1)}'


def items_by_category(purchases):
    dict_res = dict()
    for purchase in range(len(purchases)):
        if purchases[purchase]['category'] not in dict_res.keys():
            dict_res[purchases[purchase]['category']] = [purchases[purchase]['item']]
        else:
            dict_res[purchases[purchase]['category']].append(purchases[purchase]['item'])

    return f'Товары по категориям: {dict_res}'


def expensive_purchases(purchases):
    dict_res = list()
    min_price = min([purchase['price'] for purchase in purchases])
    for purchase in range(len(purchases)):
        if purchases[purchase]['price'] >= min_price:
            dict_res.append(purchases[purchase])

    return f'Покупки дороже {min_price}: {dict_res}'


def average_price_by_category(purchases):
    dict_res = dict()
    for purchase in range(len(purchases)):
        if purchases[purchase]['category'] not in dict_res.keys():
            dict_res[purchases[purchase]['category']] = [purchases[purchase]['price'], 1]
        else:
            dict_res[purchases[purchase]['category']] = [
                dict_res[purchases[purchase]['category']][0] + purchases[purchase]['price'],
                dict_res[purchases[purchase]['category']][1] + 1]

    return f'Средняя цена по категориям: {[{k: v[0]/v[1]} for k, v in dict_res.items()]}'


def most_frequent_category(purchases):
    dict_res = dict()
    for purchase in range(len(purchases)):
        if purchases[purchase]['category'] not in dict_res.keys():
            dict_res[purchases[purchase]['category']] = purchases[purchase]['quantity']
        else:
            dict_res[purchases[purchase]['category']] += purchases[purchase]['quantity']

    return f'Категория с наибольшим количеством проданных товаров: {"".join([k for k, v in dict_res.items() if v == max(dict_res.values())])}'


print(total_revenue(sales))

print(items_by_category(sales))

print(expensive_purchases(sales))

print(average_price_by_category(sales))

print(most_frequent_category(sales))
