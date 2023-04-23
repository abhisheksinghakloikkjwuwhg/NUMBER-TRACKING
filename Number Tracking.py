from tkinter import*
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone


root=Tk()
root.title(" Tracking phone number location")
root.geometry("365x500")
root.resizable(False,False)


def TRACK():
    enter_number=enter.get()
    number = phonenumbers.parse(enter_number)
    #country
    locate=geocoder.description_for_number(number,'en')
    country.configure(text=locate)

    #operator like Idea,airtel,jio etc...
    operator = carrier.name_for_number(number,'en')
    sim.config(text=operator)

    #phone TimeZone....
    time=timezone.time_zones_for_number(number)
    TimeZone.config(text=time)






#icon image
icon = PhotoImage(file="logo image.png")
root.iconphoto(False,icon)



#logo

logo = PhotoImage(file="logo image.png")
Label(root, image=logo).place(x=240,y=70)

Eback = PhotoImage(file="search.pnj.png")
Label(root, image=Eback).place(x=20,y=190)

#heading
Heading = Label(root,text="TRACK NUMBER",font=('arial',15,"bold"))
Heading.place(x=90,y=110)

#bottom box
Box =PhotoImage(file='bot.png.png')
Label(root,image=Box).place(x=-2,y=300)



#enter
enter=StringVar()
enter_number=Entry(root,textvariable=enter,width=17,justify="center",bd=0,font=("arial",20))
enter_number.place(x=50,y=220)

#search button
search_image=PhotoImage(file="search.pnj (3).png")
search = Button(root,image=search_image,borderwidth=0,cursor="hand2",bd=0,command=TRACK)
search.place(x=35,y=300)



#lable (imformation)
country = Label(root,text="Country:",bg="#57adff",fg="black",font=("arial",10,'bold'))
country.place(x=50,y=400)

sim = Label(root,text="SIM:",bg="#57adff",fg="black",font=("arial",10,'bold'))
sim.place(x=200,y=400)

TimeZone = Label(root,text="TimeZone:",bg="#57adff",fg="black",font=("arial",10,'bold'))
TimeZone.place(x=50,y=450)

root.mainloop()



root.mainloop()