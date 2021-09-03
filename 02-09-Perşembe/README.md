* ### 1 - JSON yapıyı dictionary formatına dönüştürme
---

``` import json ```-> Bu modülün içerisindeki methodları kullanıyoruz.

``` dictionarydonusumu= json.loads(bilgi_string) ``` -> Burada "loads()" methodu ile json yapısından dictionary yapısına dönüşüm yapılır.

* ### 2 - JSON dosyasından dictionary formata dönüştürme
---

``` with open("kisi.json") as f: ``` -> "kisi.json" dosyasından okuma yapılır.

``` veri=json.load((f)) ``` -> "json.load()" methodu ile dosya içerisindeki JSON yapısı dictionary yapısına  dönüşür. 

* ### 3 - dictionary yapıdan JSON yapıya dönüştürme
---

```jsondonusumu=json.dumps(bilgi_dictionary) ``` -> "json.dumps()" methodu ile dictionary yapısı JSON yapısına dönüşür.

* ### 4 - dictionary yapısını JSON dosyasına yazma
---

``` with open("kisi.json","w") as f: ``` -> "kisi.json" dosyasına yazma yapılır.

```json.dump(yazi,f) ``` -> "json.dump()" ile içine verilen değişkendeki dictionary yapısı JSON yapısına dönüşür.
