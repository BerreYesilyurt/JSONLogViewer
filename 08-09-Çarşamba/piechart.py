
#import argparse
import sys
import json
import matplotlib.pyplot as plt


with open("pynar_log.json") as f: #JSON dosyası açılır
    veri=json.load(f) #JSON veriler string verilere dönüştürülür.


dizi=[] # Bu dizi JSON dosyadaki "Basılan tuş" veri bilgisinin alınabilmesi içindir
basilantus=[]# # Bu ikinci diziyi basılan tuşlardan tekrarlı olanlarını bir kere tutmak için kullandım.
sayilar=[] # Bu dizi "Tuşun basılma sayısı" verisini tutar.
basilmasayisi=[] # Birkaç kez basılan tuşların basılma sayısı da sayilar[] dizisinde birkaç kez tutuluyor. Bu verileri tekrarsız bir şekilde tutmak için olan dizi.
explode=[0,0,0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] # Dairesel grafikte belirli dilimin daha belirgin durması için


for i in range(0,94): # JSON dosyasındaki dizide 94 adet eleman olduğu için 94 kere döndürdüm.
    dizi.append(veri[i]["action"]) # Basılan tuşu bulabilmek için sözlükten bu bilgiyi çektim ve dizi[]'ye ekledim


for i in range(0,94):
    a=0 # a değişkeni o tuşun kaç kere basıldığını tutmak için var. Her döngüde farklı bir tuşa geçileceği için her seferinde 0'ladım.
    a=dizi.count(veri[i]["action"]) # count metodu ile dönüştürülen dosyadaki basılan tuşların kaç defa basıldığına dair bilgiyi a değişkenine aktardık.
    sayilar.append(a) # Bu bilgiyi sayilar[] dizisine ekledim

for i in range(0,94):
    if(dizi[i] not in basilantus): # Burada amaç tekrarsız bir dizi oluşturmaktır. Bu yüzden if koşulunu kullandım. Eğer basilantus[] dizisinde bu eleman yoksa:
        basilantus.append(dizi[i]) # O zaman veryi basilantus[] dizisine ekle
        basilmasayisi.append(sayilar[i]) # Aynı zamanda basılan tuşun kaç kere basıldığına karşılık gelen ve yine aynı indekste bulunan basılma sayısını basilmasayisi[] dizisine ekle


plt.pie(basilmasayisi,labels=basilantus,explode=explode,wedgeprops={'edgecolor':'black'},radius=1.0,textprops={'fontsize':8,'color':"#065535"},rotatelabels=45, autopct='%1.1f%%')
 # Burada dairesel grafik çizimi ve ona dair özellikler var
plt.title("Tuş Basma Dağılımı",color='#274E13',size=17) # Başlık yazısı, rengi ve büyüklüğü
#plt.tight_layout()
plt.show() # Grafiğin gösterimi






