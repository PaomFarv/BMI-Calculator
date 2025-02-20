import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("System")
ctk.set_default_color_theme('green')

def create_header(master):
    header_frame = ctk.CTkFrame(master=main_frame,fg_color="transparent")
    header_frame.pack(pady=40)

    headline1 = ctk.CTkLabel(master=header_frame,text="BMI",font=("Arial Black",45,"bold"),text_color="#3CB47E")
    headline1.pack(side='left',padx=5)

    headline2 = ctk.CTkLabel(master=header_frame,text="CALC.",font=("Arial Black",45))
    headline2.pack(side='right',padx=5)

def label_vanish():
    result_pop.configure(text="")

def bmi_calc():
    height = height_inp.get()
    weight = weight_inp.get()

    if height.isdigit() and weight.isdigit():
        height = float(height_inp.get())
        weight = float(weight_inp.get())
    
        unit1 = height_unit.get()
        unit2 = weight_unit.get()

        if unit2 == "lb":
            weight = weight*0.45359237
        if unit1 == "cm":
            height = height/100
        elif unit1 == "inch":
            height = (height*2.54)/100
        else:
            result_pop.configure(text="No Unit Selected.")
            app.after(3000,label_vanish)
            return

        bmi = round(weight/height**2,2)
        result_pop.configure(text=f"BMI is: {bmi}")
    else:
        result_pop.configure(text="No Valid Input Found.")
        app.after(3000,label_vanish)
        return
    
def home():
    global weight_inp, weight_unit, height_inp, height_unit, result_pop
    for widget in main_frame.winfo_children():
        widget.destroy()

    create_header(master=main_frame)
    
    weight_frame = ctk.CTkFrame(master=main_frame,fg_color="transparent")
    weight_frame.pack()

    weight_inp = ctk.CTkEntry(master=weight_frame,placeholder_text="Weight",width=230,height=30,font=("Arial",18))
    weight_inp.pack(side="left",pady=20)

    weight_unit = ctk.StringVar()
    weight_menu = ctk.CTkOptionMenu(master=weight_frame,values=["Kg","lb"],font=("Arial",20),text_color="black",width=70,variable=weight_unit)
    weight_menu.pack(side="right",pady=20)
    weight_menu.set("Unit")

    height_frame = ctk.CTkFrame(master=main_frame,fg_color="transparent")
    height_frame.pack()

    height_inp = ctk.CTkEntry(master=height_frame,placeholder_text="Height",width=225,height=30,font=("Arial",18))
    height_inp.pack(side="left",pady=10)

    height_unit = ctk.StringVar()
    height_menu = ctk.CTkOptionMenu(master=height_frame,values=["cm","inch","meter"],font=("Arial",20),text_color="black",width=50,variable=height_unit)
    height_menu.pack(side="right",pady=10)
    height_menu.set("Unit")

    calc_button = ctk.CTkButton(master=main_frame,text="Calculate",width=100,height=20,font=("Arial",20,"bold"),text_color="black",command=bmi_calc)
    calc_button.pack(pady=20)

    result_pop = ctk.CTkLabel(master=main_frame,text="",font=("Arial",20,"bold"))
    result_pop.pack(pady=10)

    chart_btn = ctk.CTkButton(master=main_frame,text="BMI Scale Guide",fg_color="transparent",command=sec_page)
    chart_btn.pack(pady=10)


def sec_page():
    for widget in main_frame.winfo_children():
        widget.destroy()
    png = ctk.CTkImage(light_image=Image.open("bmichart.png"),dark_image=Image.open("bmichart.png"),size=(300,150))
    bmi_chart = ctk.CTkLabel(master=main_frame,text="",image=png)
    bmi_chart.pack(pady=50)

    back_btn = ctk.CTkButton(master=main_frame,text="Back To BMI CALC.",fg_color="transparent",command=home)
    back_btn.pack(pady=10)

app = ctk.CTk()
app.geometry("400x500")
app.title('BMI Calculator')
app.iconbitmap("bmicalc.ico")

main_frame = ctk.CTkFrame(master=app,border_width=1)
main_frame.pack(expand=True, fill="both", padx=20, pady=20)

create_header(master=main_frame)

weight_frame = ctk.CTkFrame(master=main_frame,fg_color="transparent")
weight_frame.pack()

weight_inp = ctk.CTkEntry(master=weight_frame,placeholder_text="Weight",width=230,height=30,font=("Arial",18))
weight_inp.pack(side="left",pady=20)

weight_unit = ctk.StringVar()
weight_menu = ctk.CTkOptionMenu(master=weight_frame,values=["Kg","lb"],font=("Arial",20),text_color="black",width=70,variable=weight_unit)
weight_menu.pack(side="right",pady=20)
weight_menu.set("Unit")

height_frame = ctk.CTkFrame(master=main_frame,fg_color="transparent")
height_frame.pack()

height_inp = ctk.CTkEntry(master=height_frame,placeholder_text="Height",width=225,height=30,font=("Arial",18))
height_inp.pack(side="left",pady=10)

height_unit = ctk.StringVar()
height_menu = ctk.CTkOptionMenu(master=height_frame,values=["cm","inch","meter"],font=("Arial",20),text_color="black",width=50,variable=height_unit)
height_menu.pack(side="right",pady=10)
height_menu.set("Unit")

calc_button = ctk.CTkButton(master=main_frame,text="Calculate",width=100,height=20,font=("Arial",20,"bold"),text_color="black",command=bmi_calc)
calc_button.pack(pady=20)

result_pop = ctk.CTkLabel(master=main_frame,text="",font=("Arial",20,"bold"))
result_pop.pack(pady=10)

chart_btn = ctk.CTkButton(master=main_frame,text="BMI Scale Guide",fg_color="transparent",command=sec_page)
chart_btn.pack(pady=10)

app.mainloop()

#Do the ERROR HANDLING
#create a header function
#look for areas of improvements