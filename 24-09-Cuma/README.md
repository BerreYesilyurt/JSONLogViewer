### DÜZENLEMELER
* Dosya raporlarıı açmadan önce ekrana bir soru kutucuğu geliyor. Evet denildiği takdirde grgafik raporu görüntülenebiliyor.

![Soru](https://user-images.githubusercontent.com/77548130/134783794-af0d8206-4e43-4287-b250-d002df527394.JPG)

* Raporlar kısmına scroolbar eklemesi yaptım. Böylece dosyayı görüntülemek için ekranı büyütmek zorunda kalınmadı.

![Scrollbar](https://user-images.githubusercontent.com/77548130/134783758-8dbf1a1a-b270-4398-aa98-f8e3c8f37c1e.JPG)

* Aşağıdaki kod bloğu ile bir dosya açılmış ve grafiği ekranda gözükürken başka bir dosya seçip üzerine yen seçilen dosyanın grafiğini çizdirebiliyoruz.

```
     for i in tabControl.winfo_children():
     
       i.destroy()    
```



