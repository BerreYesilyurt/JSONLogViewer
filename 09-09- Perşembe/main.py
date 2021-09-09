import json
from tkinter import *
from tkinter import  filedialog
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

dizi=[] # Bu dizi JSON dosyadaki "Basılan tuş" veri bilgisinin alınabilmesi içindir
basilantus=[]# # Bu ikinci diziyi basılan tuşlardan tekrarlı olanlarını bir kere tutmak için kullandım.
basilantus1=[] # Basilan tus ifadesini silip sadece tuşun kalması için atanan dizi
sayilar=[] # Bu dizi "Tuşun basılma sayısı" verisini tutar.
basilmasayisi=[] # Birkaç kez basılan tuşların basılma sayısı da sayilar[] dizisinde birkaç kez tutuluyor. Bu verileri tekrarsız bir şekilde tutmak için olan dizi.
explode=[0,0,0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

root=Tk() # Yeni bir pencere oluşturmaya yarar

root.geometry("700x350") # Pencerenin boyutu



def donothing(): # Tuşların basılabilmesi için fonksiyon
    filewin=Toplevel(root)
    dugme=Button(filewin,text=" ")
    dugme.pack()

def buttonClick(): # Dosyanın açılabilmesi için oluşturulan fonksiyon
     root.filename=filedialog.askopenfilename(initialdir="/", title="Select File",
                                               filetypes=(("json files", "*.json"), ("all files", "*.*")))

     with open(root.filename) as f: # Dosyaya root.filename ismini veriyoruz. Yani JSON dosyasını
         veri = json.load(f) # JSON dosyası dönüştürülür

     for i in range(0, 94):  # JSON dosyasındaki dizide 94 adet eleman olduğu için 94 kere döndürdüm.
         dizi.append(veri[i]["action"])  # Basılan tuşu bulabilmek için sözlükten bu bilgiyi çektim ve dizi[]'ye ekledim

     for i in range(0, 94):
         a = 0  # a değişkeni o tuşun kaç kere basıldığını tutmak için var. Her döngüde farklı bir tuşa geçileceği için her seferinde 0'ladım.
         a = dizi.count(veri[i][
                            "action"])  # count metodu ile dönüştürülen dosyadaki basılan tuşların kaç defa basıldığına dair bilgiyi a değişkenine aktardık.
         sayilar.append(a)  # Bu bilgiyi sayilar[] dizisine ekledim

     for i in range(0, 94):
         if (dizi[
             i] not in basilantus):  # Burada amaç tekrarsız bir dizi oluşturmaktır. Bu yüzden if koşulunu kullandım. Eğer basilantus[] dizisinde bu eleman yoksa:
             basilantus.append(dizi[i])  # O zaman veryi basilantus[] dizisine ekle
             basilmasayisi.append(sayilar[
                                      i])  # Aynı zamanda basılan tuşun kaç kere basıldığına karşılık gelen ve yine aynı indekste bulunan basılma sayısını basilmasayisi[] dizisine ekle

     for i in range(0, 29):  # basilantus[] dizisinin uzunluğu adeddince döndürdüm
         basilantus1.append((basilantus[i][13:23]))  # Sadece harflerin eklenmesi için yazdım


     figure = Figure(figsize=(16, 7), dpi=100) # Pencerede oluşturulan tuvalin boyutu
     plt=figure.add_subplot(1,1,1)


     plt.pie(basilmasayisi, labels=basilantus1, explode=explode, wedgeprops={'edgecolor': 'black'}, radius=1.0,
                  textprops={'fontsize': 8, 'color': "#065535"}, rotatelabels=45, autopct='%1.1f%%') # Dairesel grafiğin çizilmesi

     canvas = FigureCanvasTkAgg(figure, root) # Tablonun sayfası belirlenir
     toolbar = NavigationToolbar2Tk(canvas, root)
     canvas.get_tk_widget().pack() # Pack ile ekranda görünmesi sağlanır


menubar=Menu(root) # Menü oluşturma
filemenu=Menu(menubar,tearoff=0) # Sayfada kenarda açılan menünün ismi
filemenu.add_command(label="New",command=donothing) # Menünün altındaki alt kısımlar eklenir
filemenu.add_command(label="Open",command=buttonClick)
filemenu.add_command(label="Save",command=donothing)
filemenu.add_separator() # Ayırıcı bir çizgi çekmeye yarar
filemenu.add_command(label="Exit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)


helpmenu=Menu(menubar,tearoff=0) # Sayfada kenarında açılan help kısmının ismi
helpmenu.add_command(label="Help Index",command=donothing)
helpmenu.add_command(label="About...",command=donothing)
menubar.add_cascade(label="Help",menu=helpmenu)



root.config(menu=menubar)
root.mainloop() # Döngünün devam etmesi için



