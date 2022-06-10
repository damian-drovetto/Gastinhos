import json

with open('./gastos/test.json', 'r') as file:
    data = json.load(file)

for category in data:
    total = 0
    for gasto in data[category]["gastos"]:
        total = gasto + total

    data[category]["total"] = total
    data[category]["valor_restante"] = data[category]["valor_especulado"] - total

    print(f"Você gastou R${total} na categoria {category}. Você ainda pode gastar R${data[category]['valor_restante']}.")

with open('./gastos/test.json', 'w') as file:
    json.dump(data, file)

print("Sucesso.")