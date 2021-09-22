import json
from tkinter import *
from tkinter.messagebox import askyesno
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkhtmlview import HTMLLabel
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkdocviewer import *
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

dizi = []  # Bu dizi JSON dosyadaki "Basılan tuş" veri bilgisinin alınabilmesi içindir
basilantus = []  # # Bu ikinci diziyi basılan tuşlardan tekrarlı olanlarını bir kere tutmak için kullandım.
basilantus1 = []  # Basilan tus ifadesini silip sadece tuşun kalması için atanan dizi
sayilar = []  # Bu dizi "Tuşun basılma sayısı" verisini tutar.
basilmasayisi = []  # Birkaç kez basılan tuşların basılma sayısı da sayilar[] dizisinde birkaç kez tutuluyor. Bu verileri tekrarsız bir şekilde tutmak için olan dizi.
explode = [0, 0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

root = tk.Tk()  # Yeni bir pencere oluşturmaya yarar
root.title("JSON Log Viewer")  # Sayfaya isim verme
tabControl = ttk.Notebook(root)  # Üst sekmelere tıklayarak bağlantılı alt bölümlerin açılması için alan sağlanmış oldu

tab1 = ttk.Frame(tabControl)  # Grafikler için ayrı ayrı Frameler oluşturuldu.
tab2 = ttk.Frame(tabControl)
tab3=ttk.Frame(tabControl)

tabControl.add(tab1, text="Tab 1")  # Sekmelere ad verildi
tabControl.add(tab2, text="Tab 2")
tabControl.add(tab3, text="Tab 3")
tabControl.pack(expand=1, fill="both")  # Sekmeleri buton şeklinde yerleştirebilmek için pack() kullanıldı

root.geometry("700x350")  # Pencerenin boyutu

p = PhotoImage(file="root.png")  # Eklenecek olan resim

root.iconphoto(False, p)  # Resmin ikon olarak gözükmesi


def howToUse():  # "How To Use" sekmesine tıklayınca yapılacak işlemler için bir fonksiyon
    pencere1 = Toplevel()  # Yeni pencere açılması
    pencere1.geometry("700x350")  # Pencere boyutlandırılması
    pencere1.title("How To Use")  # Pencere başlığı
    p1 = PhotoImage(file="root.png")  # Penceredeki ikona konulaak resim
    pencere1.iconphoto(False, p1)

    # Pencerede HTML formatında yazılan yazı
    howtouselabel = HTMLLabel(pencere1, html="""

    <h1>NEED HELP?</h1>

    <h4>JSON LOG VİEWER NE İŞE YARAR?</h4>  
    <h5>Bu uygulamanın amacı JSON dosyalarını diğer dosyalardan ayıklamak, daha sonra bunları dönüştürmek ve seçilen JSON dosyasını grafiğe dönüştürmektir.</h5>


    <h4>JSON LOG VİEWER NASIL KULLANILIR?</h4>
    <h5>"File" menüsünden "Open" başlığına tıkladığınızda sizi bilgisayarınızın "Bu Bilgisayar" kısmına götürür. İstediğiniz bölümden JSON dosyası seçerseniz bunu "Tab1" de dairesel,  "Tab2" de çizgisel bir grafiğe dönüştürüp ekrana döker.</h5>

    <p><a href='https://kerteriz.net/python-json-okuma-yazma-donusturme-islemleri/'> PYTHON'DA JSON </a></p>
    <h5>JSON'ın tanımı, hangi amaçla kullanılabileceği ve dönüşümlerini içeren link yukarıda verilmiştir.</h5>

    <p><a href='https://medium.com/datarunner/matplotlibkutuphanesi-1-99087692102b/'> PYTHON'DA GRAFİK GÖRSELLEŞTİRME </a></p>
    <h5>Pythonda grafiğin nasıl çizilebileceği yukarıda verilmiştir. İlgileniyorsanız linke tıklayınız.</h5>

    <p><a href='https://medium.com/datarunner/piecharts-8b2b776f3018/'> PYTHON'DA PİECHART ÇİZİMİ </a></p>
    <h5>Python'da PieChart grafiğinin nasıl çizilebileceği ve bununla ilgili özellikler verilmiştir. Bilmiyorsanız ya da daha fazla bilgi istiyorsanız yukarıdaki linke tıklayabilirsiniz.</h5>


        """)

    howtouselabel.pack(fill="both", expand=True)


def about():  # howToUse fonksiyonundaki kullanımla aynıdır.
    pencere2 = Toplevel()
    pencere2.geometry("700x350")
    pencere2.title("About")
    p2 = PhotoImage(file="root.png")
    pencere2.iconphoto(False, p2)

    aboutlabel = HTMLLabel(pencere2, html="""

    <p><h3> Berre Yeşilyurt  </h3></p>


    <p><a href='https://github.com/BerreYesilyurt/'>Berre Github Hesabı</a></p>
    """)

    aboutlabel.pack(fill="both", expand=True)


def donothing():  # Tuşların basılabilmesi için fonksiyon
    filewin = Toplevel(root)
    dugme = Button(filewin, text=" ")
    dugme.pack()

def sorukutusu(name): # Raporlar için çıkan soru kutusunun fonksiyonu
    answer=askyesno(title="Confirmation",message="Raporu görüntülemek ister misiniz?") # Çıkan kutudaki başlık ve yazıyı askyesno ile aldık

    if answer: # Evete tıklanması durumunda
        rapor=Toplevel() # Yeni bir pencere açtık
        rapor.geometry("700x350") # Pencerenin ebatı
        rapor.title("Reports") # Pencerenin başlığı
        r = PhotoImage(file="root.png")
        rapor.iconphoto(False, r)

        v=DocViewer(rapor)  # Bir widget oluşturmak için kullanılıyor
        v.pack(side="top",expand=1,fill="both")
        v.display_file(name) # Belgeyi göstermek için display kullandık





rows = []  # Verileri ekemek için satırlar
rows1 = []
rows2 = []

def buttonClick():  # Dosyanın açılabilmesi için oluşturulan fonksiyon
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                               filetypes=(("json files", "*.json"), ("all files", "*.*")))

    with open(root.filename) as f:  # Dosyaya root.filename ismini veriyoruz. Yani JSON dosyasını
        veri = json.load(f)  # JSON dosyası dönüştürülür

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
            basilantus.append(dizi[i])  # O olduğu zaman veriyi basilantus[] dizisine ekle
            basilmasayisi.append(sayilar[
                                     i])  # Aynı zamanda basılan tuşun kaç kere basıldığına karşılık gelen ve yine aynı indekste bulunan basılma sayısını basilmasayisi[] dizisine ekle

    for i in range(0, 29):  # basilantus[] dizisinin uzunluğu adeddince döndürdüm
        basilantus1.append((basilantus[i][13:23]))  # Sadece harflerin eklenmesi için yazdım

    figure = Figure(figsize=(16, 7), dpi=100)  # Pencerede oluşturulan tuvalin boyutu
    plt = figure.add_subplot(1, 1, 1)


    plt.pie(basilmasayisi, labels=basilantus1, explode=explode, wedgeprops={'edgecolor': 'black'}, radius=1.0,
            textprops={'fontsize': 8, 'color': "#065535"}, rotatelabels=45,
            autopct='%1.1f%%')  # Dairesel grafiğin çizilmesi


    canvas = FigureCanvasTkAgg(figure, tab1)  # Tablonun sayfası belirlenir
    toolbar = NavigationToolbar2Tk(canvas, root)
    canvas.get_tk_widget().pack()  # Pack ile ekranda görünmesi sağlanır

    toplam = 0  # Yüzdeyi bulabilmek için toplam değişkeni atadım

    for i in range(29): # Basilmasayisini büyükten küçüğe doğru sıralamak için döngü kullandım

        for j in range(29):

            if (basilmasayisi[i] >= basilmasayisi[j]):

                temp = basilmasayisi[i] # Küçük ise yer değiştirdim
                basilmasayisi[i] = basilmasayisi[j]
                basilmasayisi[j] = temp

                temp1 = basilantus1[i] # Basilan tus ve basilma sayısı diilerinin indeksleri karşılıklı geldiği için basilantus dizisinde de aynı değşimi yaptım
                basilantus1[i] = basilantus1[j]
                basilantus1[j] = temp1

    """rows=[] # Verileri ekemek için satırlar
    rows1=[]
    rows2=[]
    toplam=0 # Yüzdeyi bulabilmek için toplam değişkeni atadım"""


    for i in range(3): # Sütunlarda döngü
        cols=[] # 3 tane sütun dizisi
        cols1 = []
        cols2=[]
        if(i==0): # Eğer birinci sütundaysa basilantus dizisinde işlem yapılır çünkü ilk sütun Key Name sütunu
            for j in range(29):
                e = Entry(tab3, text="", width=70)
                e.grid(row=j, column=i)
                e.insert(INSERT, basilantus1[j])
                cols.append(e) # Sütun dizisine değerler eklenşr
            rows.append(cols) # Bu değerler sonra satıra eklenir

        elif(i==1): # Aynı işlemler basilmasayisi için de yapılır
            for k in range(29):
                e = Entry(tab3, text="", width=70)
                e.grid(row=k, column=i)
                e.insert(INSERT, basilmasayisi[k])
                cols1.append(e)
                toplam=toplam+basilmasayisi[k]
            rows1.append(cols)

        else: # Yüzde bulma
            oran=0
            for l in range(29):
                e = Entry(tab3, text="", width=70)
                e.grid(row=l, column=i)
                oran=(basilmasayisi[l]/toplam)*100 # Yüzdeyi bulmak için count'u toplama bölüp 100 ile çarptık
                e.insert(INSERT, oran)
                cols2.append(e)
            rows2.append(cols)

    label=tk.Label(tab3,text="Key Name",bg="green",font="bold").place(x=330,y=0) # Key Name başlığı
    label1 = tk.Label(tab3, text="Count",bg="green",font="bold").place(x=795, y=0) # Count başlığı
    label2 = tk.Label(tab3, text="Percent",bg="green",font="bold").place(x=1205, y=0) # Percent başlığı

    x_ekseni = list()
    y1_ekseni = list()
    y2_ekseni = list()

    for i in range(0, 94):
        x_ekseni.append(i)  # Zamanın listeye aktarımı için yazdım.
        y1_ekseni.append(veri[i]["totallines"])  # Satırları bir listeye ekledim.
        y2_ekseni.append(veri[i]["totalchars"])  # Karakterleri listeye ekledim.

    figure = Figure(figsize=(5, 5), dpi=100)  # Ortaya çıkacak tablonun boyutu ve inç (dpi) değerlerini girdim.
    plt = figure.add_subplot(1, 1, 1)  # Tablonun konacağı yerin noktaları

    plt.plot(x_ekseni, y1_ekseni, label="Toplam Satır")
    plt.plot(x_ekseni, y2_ekseni, label="Toplam karakter")
    plt.set_title("Zamana Göre Toplam Karakter ve Satır Sayısı")
    plt.set_xlabel("Zaman")
    plt.set_ylabel("Toplam Karakter ve Toplam Satır")
    plt.legend()  # Grafik çubuklarının isimlerinin ekranda çıkması için yazdım.
    plt.grid(True)  # Arka taraftaki çizgilerin belirgin olması için True değeri verdim.

    canvas = FigureCanvasTkAgg(figure, tab2)  # Belirlenen tablonun nerede gösterileceğini belirttim.
    toolbar = NavigationToolbar2Tk(canvas, root)  # Normal matplotlib tablosunun altında yer alan toolbar için ekledim.
    canvas.get_tk_widget().pack()

def piechartreport(): # piechart'ı pdfe dönüştürmek için çizimleri aldım ve daha sonra pdf'e dönüştürmeyi amaçladım

    basilantus=[]# Tüm dizilere tekrar değer atanması için bış diziye atadım
    basilantus1=[]
    sayilar=[]
    basilmasayisi=[]

    with open('pynar_log.json') as f:  # Dosyaya root.filename ismini veriyoruz. Yani JSON dosyasını
        veri = json.load(f)  # JSON dosyası dönüştürülür

    for i in range(0, 94):  # JSON dosyasındaki dizide 94 adet eleman olduğu için 94 kere döndürdüm.
        dizi.append(veri[i]["action"])  # Basılan tuşu bulabilmek için sözlükten bu bilgiyi çektim ve dizi[]'ye ekledim

    for i in range(0, 94):
        b = 0  # a değişkeni o tuşun kaç kere basıldığını tutmak için var. Her döngüde farklı bir tuşa geçileceği için her seferinde 0'ladım.
        b = dizi.count(veri[i]["action"])  # count metodu ile dönüştürülen dosyadaki basılan tuşların kaç defa basıldığına dair bilgiyi a değişkenine aktardık.
        sayilar.append(b)  # Bu bilgiyi sayilar[] dizisine ekledim

    for i in range(0, 94):
        if (dizi[i] not in basilantus):  # Burada amaç tekrarsız bir dizi oluşturmaktır. Bu yüzden if koşulunu kullandım. Eğer basilantus[] dizisinde bu eleman yoksa:
            basilantus.append(dizi[i])  # O olduğu zaman veriyi basilantus[] dizisine ekle
            basilmasayisi.append(sayilar[i])  # Aynı zamanda basılan tuşun kaç kere basıldığına karşılık gelen ve yine aynı indekste bulunan basılma sayısını basilmasayisi[] dizisine ekle

    for i in range(0, 29):  # basilantus[] dizisinin uzunluğu adeddince döndürdüm
        basilantus1.append((basilantus[i][13:23])) # Sadece harflerin eklenmesi için yazdım

    figure1 = Figure(figsize=(16, 7), dpi=100)  # Pencerede oluşturulan tuvalin boyutu
    plt = figure1.add_subplot(1, 1, 1)

    plt.pie(basilmasayisi, labels=basilantus1, explode=explode, wedgeprops={'edgecolor': 'black'}, radius=1.0, rotatelabels=45,
            autopct='%1.1f%%')  # Dairesel grafiğin çizilmesi


    figure1.savefig("piechart.pdf") # Dosyayı pdf olarak kaydetmek için kullandım
    sorukutusu("piechart.pdf") # Yukarıda bulunan soru kutucuğu adlı fonksiyonu çağırdım




def linechartreport(): # linechart çizimini kullandım ve pdf olarak kaydetmeyi amaçladım

    with open("pynar_log.json") as f:  # Dosyaya root.filename ismini veriyoruz. Yani JSON dosyasını
        veri = json.load(f)  # JSON dosyası dönüştürülür

    x_ekseni = list()
    y1_ekseni = list()
    y2_ekseni = list()

    for i in range(0, 94):
        x_ekseni.append(i)  # Zamanın listeye aktarımı için yazdım.
        y1_ekseni.append(veri[i]["totallines"])  # Satırları bir listeye ekledim.
        y2_ekseni.append(veri[i]["totalchars"])  # Karakterleri listeye ekledim.

    figure2 = Figure(figsize=(5, 5), dpi=100)  # Ortaya çıkacak tablonun boyutu ve inç (dpi) değerlerini girdim.
    plt = figure2.add_subplot(1, 1, 1)  # Tablonun konacağı yerin noktaları

    plt.plot(x_ekseni, y1_ekseni, label="Toplam Satır")
    plt.plot(x_ekseni, y2_ekseni, label="Toplam karakter")
    plt.set_title("Zamana Göre Toplam Karakter ve Satır Sayısı")
    plt.set_xlabel("Zaman")
    plt.set_ylabel("Toplam Karakter ve Toplam Satır")
    plt.legend()  # Grafik çubuklarının isimlerinin ekranda çıkması için yazdım.
    plt.grid(True)  # Arka taraftaki çizgilerin belirgin olması için True değeri verdim

    figure2.savefig("linechart.pdf") # pdf olarak kaydetmek
    sorukutusu("linechart.pdf")

def tablereport(): # tablonun raporunu hazırlayıp pdf'e dönüştürebilmek için fonksiyon

    percent=[] # yüzde değerlerini atabilmek için bir dizi kullandım


    with open("pynar_log.json") as f:  # Dosyaya root.filename ismini veriyoruz. Yani JSON dosyasını
        veri = json.load(f)  # JSON dosyası dönüştürülür

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
            basilantus.append(dizi[i])  # O olduğu zaman veriyi basilantus[] dizisine ekle
            basilmasayisi.append(sayilar[
                                     i])  # Aynı zamanda basılan tuşun kaç kere basıldığına karşılık gelen ve yine aynı indekste bulunan basılma sayısını basilmasayisi[] dizisine ekle

    for i in range(0, 29):  # basilantus[] dizisinin uzunluğu adeddince döndürdüm
        basilantus1.append((basilantus[i][13:23]))  # Sadece harflerin eklenmesi için yazdım

    columns=3
    rows=29
    total=0

    data=[[0 for x in range(columns)] for y in range(rows)] # Tablo oluşturmak i.in iki boyutlu bir dizi kullandım


    for i in range(29): # Basilan tus dizisindeki elemanları ilk sütuna attım
        data[i][0] = basilantus1[i]

    for j in range(29): # Basilma sayısını ikinci sütuna attım
        data[j][1] = basilmasayisi[j]
        total=total+basilmasayisi[j]

    for k in range(29):
        yuzde= (basilmasayisi[k]/total)*100
        percent.append(yuzde) # percent dizisine append methodu ile eekleme yaptım

    for l in range(29):
        data[l][2]= percent[l] # percent dizisine eklenen verileri üçüncü sütuna ekledim

    items=[]

    doc=SimpleDocTemplate("tablo.pdf",pagesize=A4)

    table = Table(data, 3 * [inch], len(data) * [inch]) # Tablonun satır ve sütunlarını belirlemek
    table.setStyle(TableStyle([ # tablonun görseli ile alakalı ögeler
        ('FONT', (0, 0), (-1, -1), 'Helvetica'),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.blue),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.red),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    items.append(table) # satır ve sütunları items dizisine aktardık. Elemanları ekledik.
    doc.build([table]) # otomatik bir pdf dosyası oluşturmak için kullanılır
    sorukutusu("tablo.pdf")


menubar = Menu(root)  # Menü oluşturma
filemenu = Menu(menubar, tearoff=0)  # Sayfada kenarda açılan menünün ismi
filemenu.add_command(label="New", command=donothing)  # Menünün altındaki alt kısımlar eklenir
filemenu.add_command(label="Open", command=buttonClick)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()  # Ayırıcı bir çizgi çekmeye yarar
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

reportsmenu=Menu(menubar,tearoff=0)
reportsmenu.add_command(label="Piechart Report",command=piechartreport)
reportsmenu.add_command(label="Linechart Report",command=linechartreport)
reportsmenu.add_command(label="Table Report",command=tablereport)
menubar.add_cascade(label="Reports", menu=reportsmenu)

helpmenu = Menu(menubar, tearoff=0)  # Sayfada kenarında açılan help kısmının ismi
helpmenu.add_command(label="How To Use", command=howToUse)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)



root.config(menu=menubar)
root.mainloop()  # Döngünün devam etmesi için

