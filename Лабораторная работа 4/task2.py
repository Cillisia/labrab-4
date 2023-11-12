# TODO решите задачу
import json
file_path = 'input.json'
def task() -> float:
    with open(file_path, 'r') as file:
        data = json.load(file)

    product_sum = 0
    for item in data:
        score = item.get('score', 0)
        weight = item.get('weight', 0)
        product = score * weight
        product_sum += product

    return round(product_sum, 3)


print(task())
