# Project modules
import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk
import json
from tkinter import colorchooser
import itertools
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox
from test import checkCombo
from test import customFile
import os
import random
import combo

# https://fiverr-res.cloudinary.com/image/upload/q_auto,f_pdf/v1/secured-attachments/message/attachments/98713d90f5d706ea9c8f6a3468d10ea3-1627171155154/Commission%20orionpy-%20wynncraft%20builds.pdf?__cld_token__=exp=1627220906~hmac=ff788bdca0d124ecfee26f0e8a2baf9e649381e87c3b723ed6bab3001a6308b8
# category = input("category name >> ")

#url = f"https://api.wynncraft.com/public_api.php?action=itemDB&category=all"


#make the request
#r = requests.get(url)
#get the data
#json_r = r.json()
#Print the data
# f = open("item_name.txt", "w")
#with open(f"items.txt", "w") as f2:
    #f2.write(json.dumps(json_r))
# f.close()

class PrintLogger(): # create file like object
    def __init__(self, textbox): # pass reference to text widget

        self.textbox = textbox # keep ref

    def write(self, text):
        self.textbox.config(state=tk.NORMAL)
        self.textbox.insert(tk.END, text) # write text to textbox
            # could also scroll to end of textbox here to make sure always visible
        self.textbox.config(state=tk.DISABLED)

    def flush(self): # needed for file like object
        pass

class MenuBar:

    def __init__(self, parent):
        font = ('Corbel', 14)
        font_2 = ('Corbel', 10)

        menubar = tk.Menu(parent.root, font=font)
        parent.root.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_2, tearoff=0)

        file_dropdown.add_command(label="Background Color",
                                  command=parent.custom_color)
        file_dropdown.add_command(label="Custom file",
                                  command=parent.custom_folder)

        menubar.add_cascade(label="Settings", menu=file_dropdown)


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, borderwidth=0, highlightthickness = 0,relief="flat", width=1000, height=800)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class ScrollableFrame_x(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, borderwidth=0, highlightthickness = 0,relief="flat", width=1000, height=800)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.xview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(xscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="x")


class MainApp: # The main class of the project
    def __init__(self, root):
        root.geometry("1300x600")
        # root.resizable(False, False)
        root.title("Wynncraft Items Selection") # Window title

        font = ("Arial", 12)

        self.root = root

        # Title
        title = tk.Label(root, text="Wynncraft Items Selection")
        title.pack()

        self.frame = ScrollableFrame(root)
        self.frame2 = ScrollableFrame_x(root)

        self.frame_2 = tk.Frame(self.frame.scrollable_frame)

        self.frame_3 = tk.Frame(self.frame_2)

        self.frame_4 = tk.Frame(self.frame_2)

        self.combo_frame = tk.Frame(self.frame_2)


        # Search bar
        y = tk.StringVar()
        self.input_1 = tk.Entry(self.frame_2, textvariable=y, width=166)
        self.input_1.grid(sticky="S", ipady=15)

        item_search = tk.Button(self.frame_3, text="Search for a single item", command=self.search_item_by_name)
        item_search.grid(row=0, column=0)

        item_clear = tk.Button(self.frame_3, text="Clear", command=self.clear)
        item_clear.grid(row=1, column=0)

        items_search = tk.Button(self.frame_3, text="Search items by category", command=self.search_items_by_category)
        items_search.grid(row=0, column=1)

        weapon_btn = tk.Button(self.frame_3, text="Combine random item", command=self.combination_All)
        weapon_btn.grid(row=0, column=3)

        show_combo = tk.Button(self.frame_3, text="Show random combo", command=self.show_combo)
        show_combo.grid(row=1, column=3)

        all_btn = tk.Button(self.frame_3, text="Combine item by weapon", command=self.combination_byWeapon)
        all_btn.grid(row=0, column=4)

        self.csv_btn = tk.Button(self.frame_3, text="Generate Csv", command=self.get_csv)

        self.out_label = tk.Label(self.frame_4)
        self.out_label.pack(fill=BOTH, expand=True)

        scroll = Scrollbar(self.frame_4)
        scroll.pack(side=RIGHT, fill=Y)

        self.t = tk.Text(self.frame_4, state=tk.DISABLED, fg="black", height=15, width=110,
                         border=3, yscrollcommand=scroll.set)
        self.t.pack()

        self.clear_console = tk.Button(self.frame_4,
                                       text="Clear console",
                                       fg="black",
                                       border=1,
                                       width=50,
                                       bg="red",
                                       height=2,
                                       command=self.clear_console
                                       )
        self.clear_console.pack()

        scroll.config(command=self.t.yview)

        self.frame_3.grid(row=3, pady=10)
        self.frame_4.grid(row=5, pady=10)
        self.combo_frame.grid(row=4, pady=30)
        self.frame_2.pack()


        self.items = tk.Listbox(root, width=35)
        self.scrollbar = Scrollbar(root)
        self.items.pack(side=LEFT, fill=BOTH)
        self.items.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.items.yview)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)

        self.menubar = MenuBar(self)
        self.frame.pack()

        pl = PrintLogger(self.t)
        sys.stdout = pl

    # Class functions

    def custom_folder(self):
        self.file = filedialog.asksaveasfilename(filetypes=(
                    ("Text files", "*.txt"),
                ))
        if ".txt" in self.file:
            pass
        else:
            self.file = self.file+".txt"

        with open("config/custom_file.txt", "w") as f:
            f.write(self.file)

    def show_combo(self):
        root = tk.Tk()
        run = combo.Root(root)
        root.mainloop()

    def clear_console(self):
        self.t.config(state=NORMAL)
        self.t.delete(1.0, END)
        self.t.config(state=DISABLED)

    def clear(self):
        self.out_label['text'] = ""

    def search_item_by_name(self): # search single item
        r = open(f"items/items.txt", "r")
        json_data = json.loads(r.read())
        cnt = 0
        self.out_label['text'] = ""
        for i in json_data['items']:
            cnt += 1
            if i['name'] == self.input_1.get():
                string = ""
                for x in i:
                    string = string + f"{x} = {i[x]}\n"
                    #print(f"{x} = {i[x]}")
                self.out_label['text'] = string
        r.close()

    def search_items_by_category(self): # search multiple items by category
        # url = f"https://api.wynncraft.com/public_api.php?action=itemDB&category={self.input_1.get()}"
        # r = requests.get(url)
        r = open(f"items/items_{self.input_1.get()}.txt", "r")
        json_data = json.loads(r.read())
        cnt = 0
        self.items.delete(0, END)
        for i in json_data['items']:
            cnt += 1
            string = f"[{cnt}] {i['name']}"
            self.items.insert(cnt, string)

        self.items.pack()
        self.items.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.items.yview)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)
        r.close()

    def print_combo(self):
        f = open('test.txt', 'r')


    def combination_byWeapon(self):

        if customFile():
            print(customFile())
        else:
            print("No file selected")

        count = simpledialog.askinteger(title="number of combinations",
                                        prompt="How many combinations do you want to get?")
        weapon = simpledialog.askstring(title="weapon",
                                        prompt="which weapon do you want to include in the combo?")

        combination_files = [
            'boots', 'bracelet', 'chestplate', 'helmet', 'leggings', 'necklace', 'ring', 'ring', weapon
        ]
        f = open(f"test_temp.txt", "a", encoding="utf-8")
        f.write("{")
        to_add = ""
        break_count = 0
        combo_list = []
        for i in range(count):
            print("Combo:",i)
            #print("dove mi trovo:",i)
            self.root.update()
            combo_list = []
            for x in combination_files:
                self.root.update()
                #print("lista:",x)
                r = open(f"items/items_{x}.txt", "r", encoding="utf-8", newline='')
                json_data = json.loads(r.read())
                items = json_data['items']
                value = random.randint(0, len(items))
                #print("Lunghezza:",len(items))
                #print("valore random:",value)
                r.close()
                for j in items:
                    self.root.update()
                    #print("A")
                    break_count += 1
                    to_add = j
                    if break_count > value:
                        combo_list.append(to_add)
                        #print(to_add)
                        break

            print(checkCombo(tuple(combo_list)))
        #print(combo_list)
            f.write(
                '"combo_'+str(i)+'":'
                +str(combo_list).replace("'", '"')
                .replace('None', 'null').replace('Durum"s', "Durum's")
                .replace('True', 'true').replace('"s', "'s").replace(" 's", ' "s').replace('""', '"')+','
            )

        self.root.update()
        f.write("}")
        f.close()
        with open("test.txt", "w") as f1:
            with open("test_temp.txt", "r") as f2:
                for lines in f2:
                    #print(lines)
                    f1.write(lines.replace('}],}', '}]}'))
        print("END")

    def combination_All(self):
        if customFile() :
            print(customFile())
        else :
            print("No")
        count = simpledialog.askinteger(title="number of combinations",
                                        prompt="How many combinations do you want to get?")
        weapon = "bow"

        weapon_file = ['bow', 'dagger', 'spear', 'wand']

        combination_files = [
            'boots', 'bracelet', 'chestplate', 'helmet', 'leggings', 'necklace', 'ring', 'ring', weapon
        ]
        f = open(f"test_temp.txt", "a", encoding="utf-8")
        f.write("{")
        to_add = ""
        break_count = 0
        combo_list = []
        for i in range(count) :
            print("Combo:", i)
            # print("dove mi trovo:",i)
            self.root.update()
            combo_list = []
            combination_files[8] = random.choice(weapon_file)
            for x in combination_files:
                self.root.update()
                # print("lista:",x)
                r = open(f"items/items_{x}.txt", "r", encoding="utf-8", newline='')
                json_data = json.loads(r.read())
                items = json_data['items']
                value = random.randint(0, len(items))
                # print("Lunghezza:",len(items))
                # print("valore random:",value)
                r.close()
                for j in items :
                    self.root.update()
                    # print("A")
                    break_count += 1
                    to_add = j
                    if break_count > value :
                        combo_list.append(to_add)
                        # print(to_add)
                        break

            print(checkCombo(tuple(combo_list)))
            # print(combo_list)
            f.write(
                '"combo_' + str(i) + '":'
                + str(combo_list).replace("'", '"')
                .replace('None', 'null').replace('Durum"s', "Durum's")
                .replace('True', 'true').replace('"s', "'s").replace(" 's", ' "s').replace('""', '"') + ','
            )

        self.root.update()
        f.write("}")
        f.close()
        with open("test.txt", "w") as f1 :
            with open("test_temp.txt", "r") as f2 :
                for lines in f2 :
                    # print(lines)
                    f1.write(lines.replace('}],}', '}]}'))
        print("END")

    def get_csv(self):
        with open("combination.csv", "w") as f:
            pass

    def download_items(self):
        pass

    # MenuBar functions

    def custom_color(self):
        color_code = colorchooser.askcolor(title="Choose color")
        if color_code[1] == "#000000":
            print(1)
        else:
            self.root['background'] = color_code[1]
        print(color_code)

if __name__ == "__main__":
    root = tk.Tk()
    run = MainApp(root)
    root.mainloop()