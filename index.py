import customtkinter
print("Window Was Created!")

allinfo = ''

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  
app.geometry("600x650")
app.minsize(width=600, height=650)
app.wm_title("Maximos skaicialka")

inputbox = customtkinter.CTkTextbox(master=app, width=560, height=500)
inputbox.pack(pady=20)

def button_function():
    print("button pressed")
    duomenys = inputbox.get("0.0", "end")
    global allinfo
    if duomenys != "\n":
        allinfo = duomenys.split('\n')
        app.destroy()
    else:
        print("Irasyk kazka")

button = customtkinter.CTkButton(master=app, text="Submit", width=200,height=70, font=customtkinter.CTkFont(family="Helvetica", size=25), command=button_function)
button.pack()

app.mainloop()

# math -=-=-=-=-

info = []


Save = False
for x in allinfo:
    if "===============" in x:
        Save = False

    if Save == True:
        info.append(x.replace('\n', ''))

    if "Kvitas" in x:
        Save = True

productinfo = []
old = ''
for x in range(len(info)):
    if info[x].endswith(' A') or info[x].endswith(' N'):
        fullstringsplit = f'{old}{info[x]}'.split('  ')
        old = ''

        dict = {
            "Name": fullstringsplit[0],
            "Cost": float(fullstringsplit[-1].replace(' N', '').replace(' A', '').replace(' ', '').replace(',','.'))
        }
        productinfo.append(dict)
    else:
        old = old + ' ' + info[x]

def RemoveAndAdd(inf, String):
    Remove = []
    for x in range(len(inf)):
        dict = inf[x]

        if String in dict["Name"]:
            nuolaidoskaina = dict["Cost"]
            ogdict = inf[x - 1]
            ogkaina = ogdict["Cost"]

            newdict = {
                "Name": ogdict["Name"],
                "Cost": round(ogkaina + nuolaidoskaina, 2)
            }
            inf[x - 1] = newdict
            Remove.append(inf[x])
    
    for x in Remove:
        inf.remove(x)

    return inf


productinfo = RemoveAndAdd(productinfo ,'PET (depozitinis)')
productinfo = RemoveAndAdd(productinfo ,'Nuolaida')

# end window -=-=-=-=-

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.minsize(width=600, height=100)
app.wm_title("Maximos skaicialka")

AllCheckVar = []

label = customtkinter.CTkLabel(master=app, text="Bendra Suma: 0.0 €", font=customtkinter.CTkFont(family="Helvetica", size=50))

def ReloadCal():
    Sum = 0
    for x in AllCheckVar:
        Sum += float(x.get())
    round(Sum,2)
    label.configure(text = "Bendra suma: " + str(round(Sum,2)) + " €")

aukstis = len(productinfo)*45
if aukstis > 750:
    aukstis = 750
MyFrame = customtkinter.CTkScrollableFrame(master=app, width=600, height=aukstis)
MyFrame.pack(pady=20, padx=20)

for x in productinfo:
    check_var = customtkinter.StringVar(value="0")
    checkbox = customtkinter.CTkCheckBox(master=MyFrame, text=f"{x["Cost"]}€ | {x["Name"]}", variable=check_var, onvalue=f"{x["Cost"]}", offvalue="0", command=ReloadCal, font=customtkinter.CTkFont(family="Helvetica", size=18))
    checkbox.pack(pady=10, anchor="w", padx=10)
    AllCheckVar.append(check_var)

label.pack(pady=30, padx=20)


app.mainloop()