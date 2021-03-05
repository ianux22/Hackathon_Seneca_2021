import tkinter as tk
from tkinter import END
from PIL import ImageTk,Image
import pandas as pd

window = tk.Tk()
window.title("hackathon")
window.geometry("850x600")
window.resizable(0,0)

return_info_listbox = tk.Listbox(window, height=14, width=133)
return_info_listbox.place(x=25, y=360)

genes_df = pd.read_excel('.\Disorder_Genes.xlsx', index_col=None)

df_disease = genes_df[['Disorder_id_2', 'Disorder_name', 'Disorder_type', 'Disorder_group', 'Gene_name',
                       'Gene_symbol', 'Gene_locus', 'Disorder_gene_association',
                       'Disorder_gene_association_status']]

disability_df = pd.read_excel('.\df_disea.xlsx', index_col=None)
hpo_df = pd.read_excel('.\df_dis.xlsx', index_col=None)
prevalence_df = pd.read_excel('.\Geo_dis.xlsx', index_col=None)
age_df = pd.read_excel('.\df_age_disorder.xlsx', index_col=None)

genes_disorder = ["gene1.png", "gene2.png"]
age_disorder = ["age1.png", "age2.png", "age3.png"]
disability_disorder = ["disability1.png", "disability2.png", "disability3.png", "disability4.png", "disability5.png", "disability6.png"]
hpo_disorder = ["hpo1.png", "hpo2.png", "hpo3.png", "hpo4.png", "hpo5.png", "hpo6.png", "hpo7.png", "hpo8.png", "hpo9.png"]
prevalence_geo_disorders = ["prevalence1.png", "prevalence2.png", "prevalence3.png", "prevalence4.png", "prevalence5.png", "prevalence6.png"]
image_number = 0

def next(panel, category):
    global image_number
    image_number+=1
    if image_number > len(category)-1:
        image_number = 0
    img = ImageTk.PhotoImage(Image.open(category[image_number]).resize((800,300), Image.ANTIALIAS))
    panel.configure(image=img)
    panel.image = img # keep a reference!
    panel.place(x=25, y=20)

def clear_text_box():
    return_info_listbox.delete(0, return_info_listbox.size())

def gene_search():
    entry_text = search_bar.get()
    search_bar.delete(0, len(entry_text))
    info = df_disease[df_disease['Disorder_id_2'] == int(entry_text)]
    display_gene_info(info)
    return None

def disability_search():
    entry_text = search_bar.get()
    search_bar.delete(0, len(entry_text))
    info = disability_df[disability_df['Disorder_id_2'] == int(entry_text)]
    display_disability_info(info)
    return None

def hpo_search():
    entry_text = search_bar.get()
    search_bar.delete(0, len(entry_text))
    info = hpo_df[hpo_df['Disorder_id_2'] == int(entry_text)]
    display_hpo_info(info)
    return None

def prevalence_search():
    entry_text = search_bar.get()
    search_bar.delete(0, len(entry_text))
    entry_items = entry_text.split(":")
    entry_ID = entry_items[1]
    entry_type = entry_items[0]
    info = prevalence_df[(prevalence_df['Prevalence_type'] == str(entry_type)) & (prevalence_df['Disorder_id_2'] == int(entry_ID) )]
    display_prevalence_info(info)
    return None

def age_search():
    entry_text = search_bar.get()
    search_bar.delete(0, len(entry_text))
    info = age_df[age_df['Disorder_id_2'] == int(entry_text)]
    display_age_info(info)
    return None

def display_age_info(info):
    global return_info_listbox
    clear_text_box()
    title = "Disorder ID:   " + str(info.values[0][1]) + "   Disorder Name:   " + str(info.values[0][2]) + "   Disorder Type:   " + str(info.values[0][3]) + "   Disorder Group:   " + str(info.values[0][4]) + "Inheritence Type:   " + str(info.values[i][5])
    return_info_listbox.insert(END, title)
    for i in range(len(info)-1):
        text = "Averge Age Onset:   " + str(info.values[i][6]) + "   Average Age Death:   " + str(info.values[i][7])
        return_info_listbox.insert(END, text)

def display_prevalence_info(info):
    global return_info_listbox
    clear_text_box()
    title = "Prevalence Type:  " + str(info.values[1][1]) + "   Disorder Name:  " + str(info.values[1][2]) + "   Disorder ID:  " + str(info.values[1][3])
    return_info_listbox.insert(END, title)
    for i in range(len(info)-1):
        text = "Prevalence Geo:   " + str(info.values[i][4]) + "   Prevalence Class:   " + str(info.values[i][5]) + "   ValMoy:   " + str(info.values[i][6])
        return_info_listbox.insert(END, text)

def display_hpo_info(info):
    global return_info_listbox
    clear_text_box()
    title = "Disorder ID:   " + str(info.values[0][1]) + "   Name:   " + str(info.values[0][2]) + "   Disorder Type:   " + str(info.values[0][3]) + "   Disorder Group:   " + str(info.values[0][4])
    return_info_listbox.insert(END, title)
    for i in range(len(info)-1):
        text = "frequency class   " + str(info.values[i][5]) + "   HPO term:   " + str(info.values[i][6])
        return_info_listbox.insert(END, text)

def display_disability_info(info):
    global return_info_listbox
    clear_text_box()
    title = "Disorder ID:   " + str(info.values[0][1]) + "   Disorder Name:   " + str(info.values[0][2])
    return_info_listbox.insert(END, title)
    for i in range(len(info)-1):
        text = "disability:   " + str(info.values[i][3]) + "   frequency:   " + str(info.values[i][4])
        return_info_listbox.insert(END, text)

def display_gene_info(info):
    global return_info_listbox
    clear_text_box()
    text = "Disorder ID: " + str(info.values[0][0])
    return_info_listbox.insert(END, text)
    text2 = "Disorder Name: " + str(info.values[0][1])
    return_info_listbox.insert(END, text2)
    text3 = "Disorder Type: " + str(info.values[0][2])
    return_info_listbox.insert(END, text3)
    text4 = "Disorder Group: " + str(info.values[0][3])
    return_info_listbox.insert(END, text4)
    text5 = "Gene Name: " + str(info.values[0][4])
    return_info_listbox.insert(END, text5)
    text6 = "Gene Symbol: " + str(info.values[0][5])
    return_info_listbox.insert(END, text6)
    text7 = "Gene Locus: " + str(info.values[0][6])
    return_info_listbox.insert(END, text7)
    text8 = "Disorder Gene Association: " + str(info.values[0][7])
    return_info_listbox.insert(END, text8)
    text9 = "Disorder Gene Association Status: " + str(info.values[0][8])
    return_info_listbox.insert(END, text9)

def callback(*args):
    labelTest.configure(text="{}".format(clicked.get()))

    if clicked.get() != "Choose":
        if clicked.get() == "Gene x Disorder":
            clear_text_box()
            search_bar_label = tk.Label(text="Disorder ID")
            search_bar_label.place(x=25, y=325)
            search_button = tk.Button(window, text="search", command=gene_search)
            search_button.place(x=570, y=325)
            displayImages(genes_disorder)
        elif clicked.get() == "Age x Disorder":
            clear_text_box()
            search_bar_label = tk.Label(text="Disorder ID")
            search_bar_label.place(x=270, y=325)
            search_button = tk.Button(window, text="search", command=age_search)
            search_button.place(x=570, y=325)
            displayImages(age_disorder)
        elif clicked.get() == "Disability x Disorder":
            clear_text_box()
            search_bar_label = tk.Label(text="Disorder ID")
            search_bar_label.place(x=270, y=325)
            search_button = tk.Button(window, text="search", command=disability_search)
            search_button.place(x=570, y=325)
            displayImages(disability_disorder)
        elif clicked.get() == "HPO x Disorder":
            clear_text_box()
            search_bar_label = tk.Label(text="Disorder ID")
            search_bar_label.place(x=270, y=325)
            search_button = tk.Button(window, text="search", command=hpo_search)
            search_button.place(x=570, y=325)
            displayImages(hpo_disorder)
        elif clicked.get() == "Prevalence Geo Disorders":
            clear_text_box()
            search_bar_label = tk.Label(text="Prevalence Type:Disorder ID")
            search_bar_label.place(x=200, y=325)
            search_button = tk.Button(window, text="search", command=prevalence_search)
            search_button.place(x=570, y=325)
            displayImages(prevalence_geo_disorders)

def displayImages(category):
    img = ImageTk.PhotoImage(Image.open(category[image_number]).resize((800,300), Image.ANTIALIAS))
    panel = tk.Label(window, image = img)
    panel.image = img # keep a reference
    panel.place(x=25, y=20)
    next_button = tk.Button(window, text="Next", command=lambda: next(panel, category))
    next_button.place(x=950, y=125)

search_bar = tk.Entry(window, font=30)
search_bar.place(x=380, y=325)

labelTest = tk.Label(text="")
labelTest.place(x=460, y=0)
option_list = ['Age x Disorder', 'Gene x Disorder', 'Disability x Disorder', 'HPO x Disorder', 'Prevalence Geo Disorders']
clicked = tk.StringVar()
clicked.set("Choose")
category_choice = tk.OptionMenu(window, clicked, *option_list)
category_choice.place(x=650, y=325)
clicked.trace("w", callback)

window.mainloop()
