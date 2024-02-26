import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)
tabControl.pack(pady=10, expand=True)

w=1000
h=1000
root.geometry('%dx%d' % (w, h))
currentpage=0
d_num=0
p_num=0
t_num=0
x_num=0
def nextpage():
    global currentpage
    currentpage+=1
    tabControl.select(currentpage)
def setpage(*args):
    global currentpage
    global d_num
    global t_num
    global p_num
    global x_num
    currentpage=tabControl.index('current')
    if currentpage==5:
        d_num=(d_num/5)*100
        p_num = (p_num / 5) * 100
        t_num = (t_num / 5) * 100
        x_num = (x_num / 5) * 100
        str = "%{} Deuteranopia \n%{} Protanopia \n%{} Tritanopia \n%{} Sağlıklı".format(d_num,p_num,t_num,x_num)
        my_label5.config(text=str)

def d():
    nextpage()
    global d_num
    d_num+=1

def p():
    nextpage()
    global p_num
    p_num+=1

def t():
    nextpage()
    global t_num
    t_num += 1

def x():
    nextpage()
    global x_num
    x_num += 1

def cikis():
    root.destroy()
    global d_num
    global t_num
    global p_num
    global x_num
    if (d_num>=t_num and d_num>=p_num and d_num>=x_num) or (p_num>d_num and p_num>t_num and p_num>x_num):
        #1.RESİM
        image = Image.open("45.jpg")
        image.show()
        pixels = image.load()
        redToplam = 0
        greenToplam = 0
        blueToplam = 0
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                redToplam += pixels[i, j][0]
                greenToplam += pixels[i, j][1]
                blueToplam += pixels[i, j][2]
        redToplam //= image.size[0] * image.size[1]
        greenToplam //= image.size[0] * image.size[1]
        blueToplam //= image.size[0] * image.size[1]
        toplam = redToplam + greenToplam + blueToplam
        toplam //= 3
        if toplam < 10:
            toplam = 10
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                if pixels[i, j][0] > (pixels[i, j][1] + pixels[i, j][2]) / (toplam / 160) and pixels[i, j][0] > 45:
                    pixels[i, j] = (180, 0, 0)

        image.show()
        #2.RESİM   turuncu(255,127,0)
        image = Image.open("test.jpg")
        image.show()
        pixels = image.load()
        redToplam = 0
        greenToplam = 0
        blueToplam = 0
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                redToplam += pixels[i, j][0]
                greenToplam += pixels[i, j][1]
                blueToplam += pixels[i, j][2]
        redToplam //= image.size[0] * image.size[1]
        greenToplam //= image.size[0] * image.size[1]
        blueToplam //= image.size[0] * image.size[1]
        toplam = redToplam + greenToplam + blueToplam
        toplam //= 3
        if toplam < 10:
            toplam = 10
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                if pixels[i, j][0] > (pixels[i, j][1] + pixels[i, j][2]) / (toplam / 177) and pixels[i, j][0] > 45:
                    pixels[i, j] = (255, 0, 0)
        image.show()
        #3.RESİM
        image = Image.open("ev.jpg")
        image.show()
        pixels = image.load()
        redToplam = 0
        greenToplam = 0
        blueToplam = 0
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                redToplam += pixels[i, j][0]
                greenToplam += pixels[i, j][1]
                blueToplam += pixels[i, j][2]
        redToplam //= image.size[0] * image.size[1]
        greenToplam //= image.size[0] * image.size[1]
        blueToplam //= image.size[0] * image.size[1]
        toplam = redToplam + greenToplam + blueToplam
        toplam //= 3
        if toplam < 10:
            toplam = 10
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                if pixels[i, j][0] > (pixels[i, j][1] + pixels[i, j][2]) / (toplam / 190) and pixels[i, j][0] > 80:
                    pixels[i, j] = (180, 0, 0)
                if pixels[i, j][1] > (pixels[i, j][0] + pixels[i, j][2]) / (toplam / 110) and pixels[i, j][1] > 30:
                    pixels[i, j] = (0, 150, 0)
        image.show()
        #4.RESİM
        image = Image.open("74.png")
        image.show()
        pixels = image.load()
        redToplam = 0
        greenToplam = 0
        blueToplam = 0
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                redToplam += pixels[i, j][0]
                greenToplam += pixels[i, j][1]
                blueToplam += pixels[i, j][2]
        redToplam //= image.size[0] * image.size[1]
        greenToplam //= image.size[0] * image.size[1]
        blueToplam //= image.size[0] * image.size[1]
        toplam = redToplam + greenToplam + blueToplam
        toplam //= 3
        if toplam < 10:
            toplam = 10
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                if pixels[i, j][1] > (pixels[i, j][0] + pixels[i, j][2]) / (toplam / 108) and pixels[i, j][1] > 40:
                    pixels[i, j] = (0, 255, 0)

        image.show()
        #5.RESİM
        image = Image.open("balon.jpg")
        image.show()
        pixels = image.load()
        redToplam = 0
        greenToplam = 0
        blueToplam = 0
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                redToplam += pixels[i, j][0]
                greenToplam += pixels[i, j][1]
                blueToplam += pixels[i, j][2]
        redToplam //= image.size[0] * image.size[1]
        greenToplam //= image.size[0] * image.size[1]
        blueToplam //= image.size[0] * image.size[1]
        toplam = redToplam + greenToplam + blueToplam
        toplam //= 3
        if toplam < 10:
            toplam = 10
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                if pixels[i, j][0] > (pixels[i, j][1] + pixels[i, j][2]) / (toplam / 253) and pixels[i, j][0] > 170:
                    pixels[i, j] = (255, 0, 0)
                if pixels[i, j][1] > (pixels[i, j][0] + pixels[i, j][2]) / (toplam / 150) and pixels[i, j][1] > 40:
                    pixels[i, j] = (0, 150, 0)

        image.show()
        #6.RESİM
        image = Image.open("lale.png")
        image.show()
        pixels = image.load()
        redToplam = 0
        greenToplam = 0
        blueToplam = 0
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                redToplam += pixels[i, j][0]
                greenToplam += pixels[i, j][1]
                blueToplam += pixels[i, j][2]
        redToplam //= image.size[0] * image.size[1]
        greenToplam //= image.size[0] * image.size[1]
        blueToplam //= image.size[0] * image.size[1]
        toplam = redToplam + greenToplam + blueToplam
        toplam //= 3
        if toplam < 10:
            toplam = 10
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                if pixels[i, j][0] > (pixels[i, j][1] + pixels[i, j][2]) / (toplam / 250) and pixels[i, j][0] > 50:
                    pixels[i, j] = (255, 0, 0)
                if pixels[i, j][1] > (pixels[i, j][0] + pixels[i, j][2]) / (toplam / 110) and pixels[i, j][1] > 40:
                    pixels[i, j] = (20, 120, 20)

        image.show()

    elif t_num>d_num and t_num>p_num and t_num>x_num:
        image = Image.open("normallego.png")
        image.show()
        pixels = image.load()
        redToplam = 0
        greenToplam = 0
        blueToplam = 0
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                redToplam += pixels[i, j][0]
                greenToplam += pixels[i, j][1]
                blueToplam += pixels[i, j][2]
        redToplam //= image.size[0] * image.size[1]
        greenToplam //= image.size[0] * image.size[1]
        blueToplam //= image.size[0] * image.size[1]
        toplam = redToplam + greenToplam + blueToplam
        toplam //= 3
        if toplam < 10:
            toplam = 10
        for i in range(image.size[0]):
            for j in range(image.size[1]):
                if pixels[i, j][1] > (pixels[i, j][0] + pixels[i, j][2]) / (toplam / 120) and pixels[i, j][1] > 50:
                    pixels[i, j] = (0, 255, 0)

        image.show()

    else:
        image = Image.open("mukemmel.jpg")
        image.show()

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)
tab6 = ttk.Frame(tabControl)

tabControl.add(tab1, text ='Tab 1')
tabControl.add(tab2, text ='Tab 2')
tabControl.add(tab3, text='Tab 3')
tabControl.add(tab4, text='Tab 4')
tabControl.add(tab5, text='Tab 5')
tabControl.add(tab6, text='SONUÇ')
tabControl.pack(expand = 1, fill ="both")

image1 = Image.open("normaltrafik.png").resize((250,250))
test = ImageTk.PhotoImage(image1)

image2 = Image.open("normalpa.png").resize((250, 250))
test1 = ImageTk.PhotoImage(image2)

image2 = Image.open("normalgun.png").resize((250, 250))
test2 = ImageTk.PhotoImage(image2)

image4 = Image.open("normallego.png").resize((250, 250))
test3 = ImageTk.PhotoImage(image4)

image5 = Image.open("normalkelebek.png").resize((250, 250))
test4 = ImageTk.PhotoImage(image5)

label1 = ttk.Label(tab1, image=test)
label2 = ttk.Label(tab2, image=test1)
label3 = ttk.Label(tab3, image=test2)
label4 = ttk.Label(tab4, image=test3)
label5 = ttk.Label(tab5, image=test4)

label1.pack(pady=10)
label2.pack(pady=10)
label3.pack(pady=10)
label4.pack(pady=10)
label5.pack(pady=10)

my_label = tk.Label(tab1, text="Yukarıdaki resimi nasıl görüyorsunuz?",font="Times 20 bold").pack(pady=15)
my_label1 = tk.Label(tab2, text="Yukarıdaki resimi nasıl görüyorsunuz?",font="Times 20 bold").pack(pady=15)
my_label2 = tk.Label(tab3, text="Yukarıdaki resimi nasıl görüyorsunuz?",font="Times 20 bold").pack(pady=15)
my_label3 = tk.Label(tab4, text="Yukarıdaki resimi nasıl görüyorsunuz?",font="Times 20 bold").pack(pady=15)
my_label4 = tk.Label(tab5, text="Yukarıdaki resimi nasıl görüyorsunuz?",font="Times 20 bold").pack(pady=15)
my_label5 = tk.Label(tab6,text="",font="Times 50 bold")
my_label5.pack(pady=100)

#1.TAB

image6 = Image.open("deutrafik.png").resize((250,250))
test5 = ImageTk.PhotoImage(image6)

image7 = Image.open("protrafik.png").resize((250,250))
test6 = ImageTk.PhotoImage(image7)

image8 = Image.open("tritrafik.png").resize((250,250))
test7 = ImageTk.PhotoImage(image8)

button = tk.Button(tab1, image=test5, command=d)
button.pack(side=tk.LEFT,padx=70)

button2 = tk.Button(tab1, image=test6, command=p)
button2.pack(side=tk.LEFT,padx=70)

button3 = tk.Button(tab1, image=test7, command=t)
button3.pack(side=tk.LEFT,padx=70)

button4 = tk.Button(tab1, text="HİÇBİRİ", width="30", height="16", font="Times 10 bold", command=x)
button4.pack(side=tk.RIGHT,padx=70)

#2.TAB

image9 = Image.open("deupa.png").resize((250,250))
test8 = ImageTk.PhotoImage(image9)

image10 = Image.open("propa.png").resize((250,250))
test9 = ImageTk.PhotoImage(image10)

image11 = Image.open("tripa.png").resize((250,250))
test10 = ImageTk.PhotoImage(image11)

button5 = tk.Button(tab2, image=test8, command=d)
button5.pack(side=tk.LEFT,padx=70)

button6 = tk.Button(tab2, image=test9, command=p)
button6.pack(side=tk.LEFT,padx=70)

button7 = tk.Button(tab2, image=test10, command=t)
button7.pack(side=tk.LEFT,padx=70)

button8 = tk.Button(tab2, text="HİÇBİRİ", width="30", height="16", font="Times 10 bold", command=x)
button8.pack(side=tk.RIGHT,padx=70)

#3.TAB

image12 = Image.open("deugun.png").resize((250,250))
test11 = ImageTk.PhotoImage(image12)

image13 = Image.open("progun.png").resize((250,250))
test12 = ImageTk.PhotoImage(image13)

image14 = Image.open("trıgun.png").resize((250,250))
test13 = ImageTk.PhotoImage(image14)

button9 = tk.Button(tab3, image=test11, command=d)
button9.pack(side=tk.LEFT,padx=70)

button10 = tk.Button(tab3, image=test12, command=p)
button10.pack(side=tk.LEFT,padx=70)

button11 = tk.Button(tab3, image=test13, command=t)
button11.pack(side=tk.LEFT,padx=70)

button12 = tk.Button(tab3, text="HİÇBİRİ", width="30", height="16", font="Times 10 bold", command=x)
button12.pack(side=tk.RIGHT,padx=70)

#4.TAB

image15 = Image.open("deulego.png").resize((250,250))
test14 = ImageTk.PhotoImage(image15)

image16 = Image.open("prolego.png").resize((250,250))
test15 = ImageTk.PhotoImage(image16)

image17 = Image.open("trılego.png").resize((250,250))
test16 = ImageTk.PhotoImage(image17)

button13 = tk.Button(tab4, image=test14, command=d)
button13.pack(side=tk.LEFT,padx=70)

button14 = tk.Button(tab4, image=test15, command=p)
button14.pack(side=tk.LEFT,padx=70)

button15 = tk.Button(tab4, image=test16, command=t)
button15.pack(side=tk.LEFT,padx=70)

button16 = tk.Button(tab4, text="HİÇBİRİ", width="30", height="16", font="Times 10 bold", command=x)
button16.pack(side=tk.RIGHT,padx=70)

#5.TAB

image18 = Image.open("deukelebek.png").resize((250,250))
test17 = ImageTk.PhotoImage(image18)

image19 = Image.open("prokelebek.png").resize((250,250))
test18 = ImageTk.PhotoImage(image19)

image20 = Image.open("trıkelebek.png").resize((250,250))
test19 = ImageTk.PhotoImage(image20)

button17 = tk.Button(tab5, image=test17, command=d)
button17.pack(side=tk.LEFT,padx=70)

button18 = tk.Button(tab5, image=test18, command=p)
button18.pack(side=tk.LEFT,padx=70)

button19 = tk.Button(tab5, image=test19, command=t)
button19.pack(side=tk.LEFT,padx=70)

button20 = tk.Button(tab5, text="HİÇBİRİ", width="30", height="16", font="Times 10 bold", command=x)
button20.pack(side=tk.RIGHT,padx=70)

my_button = tk.Button(tab6, text="TAMAM",width="10",height="4",background="black",fg="white",font="Times 10 bold", command=cikis).pack(pady=30)

root.bind('<<NotebookTabChanged>>',setpage)

root.mainloop()

