import hesap
import ogrenci_bilgi

def main():
    ogrenci_bilgi.ogrenciler = []
    dersler = []
    notlar = []
    ders_sayisi = int(input("Kaç tane ders alıyosanız giriniz: "))
    
    for i in range(ders_sayisi):
        ders = input(f"{i+1}. dersin adını giriniz: ")
        dersler.append(ders)

        not_ = float(input(f"{ders} dersin ortalamasını giriniz: "))
        notlar.append(not_)
    
    ortalama = hesap.ortalama_hesapla(dersler,notlar)
    print("Not ortalamanız :",ortalama)
    
    if ortalama >= 50:
        print("Dönemi başarıyla tamamladınız.")
    else:
        print("Kaldınız.")
        
      

if __name__ == "__main__":
    main()        
    
