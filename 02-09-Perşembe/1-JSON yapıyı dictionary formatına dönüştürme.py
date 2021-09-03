import json

bilgi_string='{"Isim":"Berre", "Soyisim":"Yesilyurt", "Bolum":"Bilgisayar Muhendisligi"}'

dictionarydonusumu= json.loads(bilgi_string)

print(dictionarydonusumu)

print((type(dictionarydonusumu)))