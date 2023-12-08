from tkinter import *
import ctypes as ct
from Hangman import *
from Instruction import *
from cpsnew import *
import pygame,customtkinter,sys,time
from PIL import Image as PIM, ImageTk

root = Tk()
root.title("The Game Complex") 

#Image Flies
exiT= PhotoImage(file=r".\exit.png")
intru = PhotoImage(file=r".\intru.png")
bg=PhotoImage(file=r".\MainBG.png")
sond= PhotoImage(file=r".\soundddd.png")
sonond= PhotoImage(file=r".\sound.png")
settings= PhotoImage(file=r".\setting.png")
MainMenu = PhotoImage(file=r".\main.png")
start = PhotoImage(file=r".\start (4).png")
retryy= PhotoImage(file=r".\retry_cps.png")
pygame.mixer.init()

my_canvas = Canvas(root,width=900,height=600)
my_canvas.pack(fill="both", expand=True)
my_canvas.create_image(0,0, image=bg,anchor="nw")

def play():
    pygame.mixer.music.load(r".\clouds.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=10) 

def volume(x):
    pygame.mixer.music.set_volume(1-(slider.get()))

paused = False
def pause(is_paused):
    global paused 
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

def countdown(count):
    global label,hi
    # change text in label 
    label = Label(root,text="Remaining time ", fg="indigo", bg="black", font=("Helvetica",25))
    label.place(x=249,y=255)    
    label['text'] = "Remaining time "+str(count)+" seconds"
    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)
    label.after(1000, label.destroy)



def instr(th=False):
    global x, my_canvas, bg, MainMenu
    my_canvas.delete("all")
    my_canvas["bg"] = "#000000"
    bg = PhotoImage(file=r".\intru.png")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")
    File = open(r".\Instr.txt")
    Str = File.read()
    File.close()
    mainbutton = customtkinter.CTkButton(master=root, text="<-- Home",width=110,corner_radius=20,bg_color="#001938",fg_color="#000d1d", height=40, compound="left",hover_color="#003255", command=lambda: mainmenu(True))
   
    my_canvas.create_window(90,550, window=mainbutton)
    my_canvas.create_text(440,270, text=Str,font=("Trajan Pro", 13, "bold"),fill="white")


def mainmenu(th=False):
    global bg, my_canvas, exiT, sond, sonond, settings, button5, b, xx, xyx, slider, b_window, button5_window, MainMenu,label
    if th:
        my_canvas.delete("all")
        bg=PhotoImage(file=r".\MainBG.png")
        my_canvas.create_image(0,0, image=bg,anchor="nw")

    my_canvas.create_text(450,220,text="WELCOME!",font=("Trajan pro", 50),fill="white")
    my_canvas.create_text(431,160,text="The Game Complex",font=("Ink Free", 30,"bold"),fill="cyan")
    my_canvas.create_text(450,440,text="Select one from the following options",font=("Segoe UI Light", 20,"bold"),fill="grey")

    b=customtkinter.CTkButton(master=root, image=start, text="START", width=110,corner_radius=20,bg_color="black",fg_color="#1F2022", height=40, compound="left",
                              hover_color="black",command=click)
    b_window=my_canvas.create_window(300,480, anchor="nw", window=b)

    button5=customtkinter.CTkButton(master=root, image=exiT,text="EXIT",width=110,corner_radius=20,bg_color="black",fg_color="#1F2022", height=39, compound="right",
                                    hover_color="black",command=exitFunc)
    button5_window=my_canvas.create_window(460,480, anchor="nw", window=button5)

    slider = customtkinter.CTkSlider(master=root, width=160,height=16,bg_color="black",fg_color="dark blue",button_color="dark blue",
                                     button_hover_color="blue",from_=0,to=1,command=volume)

    timE=customtkinter.CTkLabel(master=root, text="",bg_color="blue",text_font=('Helvetica',13),text_color="gray",fg_color="black",height=50)
    timE_window=my_canvas.create_window(390,3, anchor="nw", window=timE)
    def clock():
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        timE.configure(text=hour + ":" + minute + ":" + second)
        timE.after(1000,clock)
    clock()

    xx=Button(root, image=settings, command=setting,bg="black", borderwidth=0)
    xyx=my_canvas.create_window(860,10, anchor="nw", window=xx)

def exitFunc():
    root.destroy()
    sys.exit()

def StartHangman():
    global x, my_canvas, bg, MainMenu
    my_canvas.delete("all")
    my_canvas["bg"] = "#000000"
    bg = PhotoImage(file=r".\111.png")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")
    try:
        if not x.word:
            x = Hangman()
            
    except:
        x = Hangman()
    print(x.word)  
    my_canvas.create_text(380,190, text=x.display_hangman(x.tries), fill="White", font=("Roboto", 25,"bold"))
    my_canvas.create_text(450,350, text=" ".join(x.word_completion), fill="Yellow", font=("Segoe UI Light", 20,"bold"))
    e = customtkinter.CTkEntry(my_canvas,width=200,height=40,placeholder_text=" Enter a letter or word")
    my_canvas.create_window(450, 400, window=e)
    b = Button(root, text="Enter",bg="#1F2022",fg="white", command=lambda: gs(e.get()), font=("bold",13))
    bwindow = my_canvas.create_window(600, 400, window=b)
    rb = customtkinter.CTkButton(master=root, text="Retry",corner_radius=30,bg_color="#1F2022",fg_color="red",text_color="white",hover_color="orange", command=Retry1, text_font=("bold",13))
    my_canvas.create_window(450, 480, window=rb)
    root.bind("<Return>", lambda m : gs(e.get()))
    mainbutton = Button(root, image=MainMenu, font=("Ink Free",15),borderwidth=0, command=lambda: mainmenu(True))
    my_canvas.create_window(40, 540, window=mainbutton)
    err=''
    try:
            
        if not x.guessed:           
            if x.guessedstat==0:
                err=my_canvas.create_text(450,550, text=f"You already guessed this!", fill="orange", font=("Segoe UI Light", 20,"bold"))
            elif x.guessedstat==1:
                err=my_canvas.create_text(450,550, text=f"Wrong word guessed!", fill="orange", font=("Segoe UI Light", 20,"bold"))
            elif x.guessedstat==2:
                err=my_canvas.create_text(450,550, text=f"Invalid guess! Use only alphabets!!", fill="orange", font=("Segoe UI Light", 20,"bold"))
            elif x.guessedstat==3 or guessedstat==-1:
                err=my_canvas.create_text(450,550, text=f"!", fill="orange", font=("Segoe UI Light", 20,"bold"))
            
    except:
        pass
    if x.tries == 0:
        my_canvas.delete(err)
        my_canvas.create_text(450,550, text=f"WRONG! Your word was {x.word}", fill="orange", font=("Segoe UI Light", 20,"bold"))
    if x.guessed:
        my_canvas.delete(bwindow)
        my_canvas.delete(err)
        my_canvas.create_text(450,550, text=f"YOU GUESSED THE WORD!", fill="orange", font=("Segoe UI Light", 20,"bold"))
    
def gs(word):
    x.guess(word.upper())
    StartHangman()

def Retry1():
    global x
    del x
    StartHangman()

def Retry2():
    global cps
    del cps
    StartCPS()

def StartCPS():
    global cps,my_canvas, bg, cpsbutton, MainMenu, retryy,label2
    my_canvas.delete("all")
    my_canvas["bg"] = "#000000"
    bg = PhotoImage(file=r".\cpsBG.png")
    my_canvas.create_image(0, 0, image=bg, anchor="nw")
    #to update the text of cps game
    def update():
        label2.config(text = "Lets play CPS test!",font=("Helvetica", 30))
    def update2():
        label2.config(text = "ENJOY!",font=("Helvetica", 30))  
    label2 = Label(root,text="WELCOME!",bg="black",fg="violet",font=("Helvetica", 30))
    my_canvas.create_window(450,140, window=label2)
    label2.after(1700,update)
    label2.after(4500,update2)
    cps = CPS()  
    cpsbutton = customtkinter.CTkButton(master=root,width=0,height=116, text="Start CPS Test", text_font=("Times",15),corner_radius=50,bg_color="black",hover_color="purple", command=lambda: cpsTest(cps))
    my_canvas.create_window(450, 400, window=cpsbutton)
    mainbutton = Button(root, image=MainMenu,borderwidth=0,bg="black" , font=("Ink Free",15), command=lambda: mainmenu(True))
    my_canvas.create_window(30,550, window=mainbutton)

def gethighscore():
    with open(r".\highscore.txt",'r') as f:
        return f.read()

def cpsTest(cpsobj):
    global cpsbutton, my_canvas,high,highestscore
    try:
        highestscore=gethighscore()
    except:
        highscore=0
    if cpsobj.num == 0:
        cpsobj.runcps()
        countdown(5)
        cpsbutton.configure(text="KEEP CLICKING!",fg_color="indigo",bg_color="black")
    else:
        cpsobj.numadd()
    if cpsobj.status:
        cpsbutton.configure(text="GREAT JOB!",fg_color="#301934",bg_color="black",corner_radius=20,height=100,width=150,hover_color='#301934')
        texty="YOUR SCORE ="+cpsobj.cps+"CPS"
        a=cpsobj.cps
        if highestscore<a:
            highestscore=a
            with open(r".\text files\highscore.txt",'w') as f:
                f.write(highestscore)
            print(highestscore)
        my_canvas.create_text(430,500,text=texty,font=("Times", 22,"bold"),fill="yellow")
        rb = Button(root, image=retryy,borderwidth=0,bg="black", command=Retry2)
        my_canvas.create_window(660, 400, window=rb)
    HIGH="Highest score = "+highestscore
    label2 = Label(root,text=HIGH,bg="black",fg="violet",font=("Helvetica", 15))
    my_canvas.create_window(179,85, window=label2)

def click():
    global b_window, button1, button2, button3, button4, my_canvas, button5_window
    my_canvas.delete(b_window)
    my_canvas.delete(button5_window)
    button1=customtkinter.CTkButton(master=root, text="HANGMAN",height=40,bg_color="black", fg_color="dark blue",text_color="white", text_font=("bold",10),command=StartHangman)
    button2=customtkinter.CTkButton(master=root, text="CPS TEST", height=40,bg_color="black",fg_color="dark blue",text_color="white", text_font=("bold",10), command=StartCPS)
    button3=customtkinter.CTkButton(master=root, text="INSTRUCTIONS", height=40,bg_color="black",fg_color="dark blue",text_color="white", text_font=("bold",10), command=instr)
    button4=customtkinter.CTkButton(master=root, text="BACK", height=40,bg_color="black",fg_color="dark blue",text_color="white", text_font=("bold",10), command=lambda: mainmenu(True))
    my_canvas.create_window(155,500, anchor="nw", window=button1)
    my_canvas.create_window(300,500, anchor="nw", window=button2)
    my_canvas.create_window(444,500, anchor="nw", window=button3)
    my_canvas.create_window(588,500, anchor="nw", window=button4)

def setting():
    global xyx
    my_canvas.delete(xyx)
    global sond, sonond, slider
    c=Button(root, image=sond,bg="black", command=play)
    c_window=my_canvas.create_window(863,10, anchor="nw", window=c)
    c=Button(root, image=sonond,bg="black", command=lambda: pause(paused))
    c_window=my_canvas.create_window(828,10, anchor="nw", window=c)
    v_window=my_canvas.create_window(665,18, anchor="nw", window=slider)

mainmenu()

#DARK TITLE BAR (EXTRA)
def dark_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
dark_title_bar(root)

root.mainloop()