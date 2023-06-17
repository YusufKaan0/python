class Ogrenci:
    def __init__(self,name,surname,number):
        self.name = name
        self.surname = surname
        self.number = number

ogrenciler = []

while True:
    name = input("Adınızı giriniz: ")
    if name.lower() == "q":
        break

    surname = input("Soyadınızı giriniz: ")
    number = input("Numaranızı giriniz: ")
    
    ogrenci = Ogrenci(name,surname,number)
    ogrenciler.append(ogrenci)
    break

    
    
