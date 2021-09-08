### PİECHART NEDİR?
---

Piechart matplotlib yardımı ile çizilebilen grafik türlerinden birisidir. Dairesel bir grafiktir. Çeşitli özellikleri vardır. Bu dosyada kullandığım bazı Piechart özellikleri şöyledir:

| Özellik      | Görevi                                                                 |
| -------      |  ----                                                                  |
| explode      | Dairesel grafiğin bir diliminin daha belirgin ve çıkık olmasını sağlar.|
| radius       | Dairesel grafiğin çapını ve böylece çevresini belirler.                |
| textprops    | Labelların büyüklüğü, rengi buradan belirlenebilir.                    |
| rotatelabels | İsteğe göre labelların yönü değiştirilip, döndürülebilir.              |
| autopct      | Dairesel grafiğin içerisine oranları yazmaya yarar.                    |


Kod parçasının çıktısı şu şekildedir:

![Resim](https://user-images.githubusercontent.com/77548130/132470611-44c6632d-ff77-440e-ad92-0e5f23739a13.JPG)



### ARGÜMAN NEDİR? NE İŞE YARAR?
---
Argümanlar programa dışarıdan veri girişi sağlamanın yollarından bir tanesidir. Argüman kullanırken "sys" adlı kütüphaneyi import etmeliyiz.

### PARAMETRE VE ARGÜMANIN FARKI NEDİR?
Parametre tanımlanan değişkenin kendisidir. Argüman ise kullanıcının verdiği değerdir. Örneğin:

``` int KokAl(int sayi, int karekok) ```          Bu koddaki "int sayi" ve "int karekok" değerleri bizim için birer parametredir.

``` KokAl(9,2) ```                                Bu kodda kullanıcı tarafından verilen değerler ise bir argümandır.



