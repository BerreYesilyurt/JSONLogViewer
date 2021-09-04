# encoding:utf-8
import matplotlib.pyplot as plt
import json
import  seaborn as sns

with open("ebadestek.json",encoding="cp437", errors='ignore') as a:
    donusum=json.load(a)

sayi=list()
ilce=list()

for i in range(0,200):
    sayi.append(donusum[i]["Bilgisayar Sayisi"])
    ilce.append(donusum[i]["Ilce Toplami"])


axes=sns.regplot(x=sayi,y=ilce)
sns.set(style="darkgrid")

#sns.set_palette(['green'])


axes.set_title("Bilgisayar Sayılarının İlçe Toplamına Oranı")
axes.set_ylabel("Bilgisayar Sayısı")
axes.set_xlabel("İlçe Toplamı")

plt.plot(sayi,ilce,"ro")
#plt.figure(figsize=(9,5))
sns.set_palette(['green'])
plt.show()

