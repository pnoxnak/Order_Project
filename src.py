import csv


# Bu blok, pizza adında bir sınıf oluşturuyor. Bu sınıfın, bir pizza tanımı ve ücretini saklamak için kullanılabilecek 
# description ve cost adında iki özelliği var. Bunlar, sınıfın yapıcı (constructor) yöntemi olan __init__ içinde belirtiliyor. 
# get_description ve get_cost adında iki yöntem de, sınıfın tanım ve ücret özelliklerine erişmek için kullanılıyor.
class pizza:
    # Yapıcı olarak description ve cost değerleri tanıtılıyor
    def __init__(self,description,cost) -> None:
        self.description = description
        self.cost=cost

# get_description ve get_cost fonksiyonları tanımlanıyor
    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

# şimdi ise "pizza" sınıfının özelliklerini miras alan subclass'lar oluşturuluyor
class Margherita(pizza):
    def __init__(self)  -> None:
        super().__init__("Margherita Pizza", 50) # Her birinde pizza sınıfına ait olan yapıcı kullanılarak tanım ve ücret özellikleri atanıyor

class Classic(pizza):
    def __init__(self) -> None:
        super().__init__("Classic Pizza", 35)
        
class TurkPizza(pizza):
    def __init__(self) -> None:
        super().__init__("Turk Pizza", 45)

class PlainPizza(pizza):
    def __init__(self) -> None:
        super().__init__("Plain Pizza", 55)


# Decorator adında bir sınıf tanımlıyorum. Bu sınıf, pizza sınıfından türetiliyor ve 
# bir başka pizza türünü (component) dekoratif malzeme olarak kullanıyor. get_cost yöntemi, birinci pizza türünün 
# maliyetini (self.component.get_cost()) ikinci pizza türünün maliyetiyle (pizza.get_cost(self)) topluyor. 
# get_description yöntemi, birinci pizza türünün açıklamasını (self.component.get_description()) ve ikinci pizza türünün 
# açıklamasını (pizza.get_description(self)) birleştiriyor.

class Decorator(pizza):
    def __init__(self, component) -> None:
        self.component = component

    def get_cost(self):
       return self.component.get_cost() + \
         pizza.get_cost(self)

    def get_description(self):
       return self.component.get_description() + \
         ' with ' + pizza.get_description(self)

# Burdan sonra ise Decorator sınıfının özelliklerini alacak malzemeler tanımlanıyor.
# Her birine "Decorator" sınıfından miras aldığı description ve cost değerleri atanıyor.

class Olives(Decorator):
    def __init__(self, pizza) -> None:
        super().__init__(pizza)
        self.description = "Olives"
        self.cost = 12

class Mushrooms(Decorator):
    def __init__(self, pizza) -> None:
        super().__init__(pizza)
        self.description = "Mushrooms"
        self.cost = 16

class GoatCheese(Decorator):
    def __init__(self, pizza) -> None:
        super().__init__(pizza)
        self.description = "GoatCheese"
        self.cost = 20

class Meat(Decorator):
    def __init__(self, pizza) -> None:
        super().__init__(pizza)
        self.description = "Meat"
        self.cost = 27

class Onions(Decorator):
    def __init__(self, pizza) -> None:
        super().__init__(pizza)
        self.description = "Onions"
        self.cost = 15

class Corn(Decorator):
    def __init__(self, pizza) -> None:
        super().__init__(pizza)
        self.description = "Corn"
        self.cost = 14


# Bu fonksiyon main.py de kullanılacak ve kullanıcının pizza seçmesi için kullanıcı girdisi sunacak.
# Ardından kullanıcının seçtiği pizzayı döndürecek. Yanlış seçim durumunda ise uyarı verip program sonlandırılacak.
# Benzer durum Select_Sauce() fonksiyonu için de geçerli.
def Select_pizza():
    selected = int(input("Your pizza choice: "))
    if selected == 1:
        my_pizza = Classic()
    elif selected == 2:
        my_pizza = Margherita()
    elif selected == 3:
        my_pizza  = TurkPizza()
    elif selected == 4:
        my_pizza = PlainPizza()
    else:
        print("Wrong choice!")
        exit()
    
    return my_pizza

def Select_Sauce(x):
    selected = int(input("Your sauce choice: "))
    if selected == 11:
        my_pizza = Olives(x)
    elif selected == 12:
        my_pizza = Mushrooms(x)
    elif selected == 13:
        my_pizza  = GoatCheese(x)
    elif selected == 14:
        my_pizza = Meat(x)
    elif selected == 15:
        my_pizza = Onions(x)
    elif selected == 16:
        my_pizza = Corn(x)
    else:
        print("Wrong choice!")
        exit()
    
    return my_pizza

# Bu fonksiyon kendisine verilen parametreleri kullanarak bir .csv dosyasına fatura bilgisi ekleyecek.

def invoice(name,id_number,cc_number,description,time):
    with open('Orders_Database.csv', mode='a') as csv_file:
        fields = ['Name', 'ID Number', 'Credit Card Number', 'Description', 'Time Order']
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writerow({'Name': name, 'ID Number': id_number, 'Credit Card Number': cc_number,
                         'Description': description, 'Time Order': time})
    



