from itertools import product


class Product:

    def __init__(self, name, weight, category):
        if weight < 0:
            print("\nError in specifying the weight\n")
        elif name == "":
            print("\nName error\n")
        elif category == "":
            print("\nError in the category\n")
        else:
            self.name = name
            self.weight = weight
            self.category = category

    def __str__(self):
        return (f"{self.name}, {self.weight}, {self.category}")

class Shop:
    __file_name = "products.txt"

    def get_products(self):
        db_shop = open(self.__file_name, "r")
        spisok = db_shop.read()
        db_shop.close()
        return spisok

    def add(self, *products):
        db_check = open(self.__file_name, "r")
        check_list = db_check.readlines()
        db_check.close()
        db_shop = open(self.__file_name, "a")
        for i in products:
            file = f"{i.name}, {i.weight}, {i.category} \n"
            if file not in check_list:
                db_shop.write(file)
            else:
                print(f"Продукт {i.name} уже есть в магазине")

        db_shop.close()



s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')



print(p2) # __str__



s1.add(p1, p2, p3)


print(s1.get_products())

