import json

class Gastinhos:
    def __init__(self, file_name):
        with open('./gastos/' + file_name, 'r') as file:
            self.data = json.load(file)
        
        self.file_name = file_name

    def gastos(self):
        for category in self.data:
            total = 0
            for gasto in self.data[category]["gastos"]:
                total = gasto + total

            self.data[category]["total"] = total
            self.data[category]["valor_restante"] = self.data[category]["valor_especulado"] - total

            print(f"Você gastou R${total} na categoria {category}. Você ainda pode gastar R${self.data[category]['valor_restante']}.")

        with open('./gastos/' + self.file_name, 'w') as file:
            json.dump(self.data, file)

    print("Sucesso.")