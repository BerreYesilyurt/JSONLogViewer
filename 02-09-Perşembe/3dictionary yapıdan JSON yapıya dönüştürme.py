import json

bilgi_dictionary={"Isim":"Berre", "Soyisim":"Yesilyurt", "Bolum":"Bilgisayar Muhendisligi"}

jsondonusumu=json.dumps(bilgi_dictionary)

print(jsondonusumu)

print((type(jsondonusumu)))
