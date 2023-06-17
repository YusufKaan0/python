def ortalama_hesapla(dersler,notlar):
    toplam = 0
    for not_ in notlar:
        toplam += not_
    ortalama = toplam / len(notlar)
    return ortalama