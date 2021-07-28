# Project modules
import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk
import json
from tkinter import colorchooser
import itertools
from tkinter import simpledialog


# https://fiverr-res.cloudinary.com/image/upload/q_auto,f_pdf/v1/secured-attachments/message/attachments/98713d90f5d706ea9c8f6a3468d10ea3-1627171155154/Commission%20orionpy-%20wynncraft%20builds.pdf?__cld_token__=exp=1627220906~hmac=ff788bdca0d124ecfee26f0e8a2baf9e649381e87c3b723ed6bab3001a6308b8
# category = input("category name >> ")

# url = f"https://api.wynncraft.com/public_api.php?action=itemDB&category={category}"


#make the request
# r = requests.get(url)
#get the data
# json_r = r.json()
#Print the data
# f = open("item_name.txt", "w")
# with open(f"items_{category}.txt", "w") as f2:
    # f2.write(json.dumps(json_r))
# f.close()

class MenuBar:

    def __init__(self, parent):
        font = ('Corbel', 14)
        font_2 = ('Corbel', 10)

        menubar = tk.Menu(parent.root, font=font)
        parent.root.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_2, tearoff=0)

        file_dropdown.add_command(label="Background Color",
                                  command=parent.custom_color)

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

        self.frame_2 = tk.Frame(self.frame.scrollable_frame)

        self.frame_3 = tk.Frame(self.frame_2)

        self.frame_4 = tk.Frame(self.frame_2)


        # Search bar
        y = tk.StringVar()
        self.input_1 = tk.Entry(self.frame_2, textvariable=y, width=150)
        self.input_1.grid(sticky="S", ipady=15)

        item_search = tk.Button(self.frame_3, text="Search for a single item", command=self.search_item_by_name)
        item_search.grid(row=0, column=0)

        items_search = tk.Button(self.frame_3, text="Search items by category", command=self.search_items_by_category)
        items_search.grid(row=0, column=1)

        csv_btn = tk.Button(self.frame_3, text="Generate Csv", command=self.get_csv)
        csv_btn.grid(row=0, column=3)

        csv_btn = tk.Button(self.frame_3, text="Generate Csv", command=self.get_csv)
        csv_btn.grid(row=0, column=3)

        weapon_btn = tk.Button(self.frame_3, text="Combine item by weapon", command=self.combination_byWeapon)
        weapon_btn.grid(row=0, column=4)

        self.out_label = tk.Label(self.frame_4)
        self.out_label.pack(fill=BOTH, expand=True)

        self.frame_3.grid(row=3)
        self.frame_4.grid(row=4)
        self.frame_2.pack()


        self.items = tk.Listbox(root, width=35)
        self.scrollbar = Scrollbar(root)
        self.items.pack(side=LEFT, fill=BOTH)
        self.items.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.items.yview)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)

        self.menubar = MenuBar(self)
        self.frame.pack()

    # Class functions

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
                    print(f"{x} = {i[x]}")
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

    def test_func(self):
        r = open(f"items/test.txt", "r", encoding="utf-8", newline='')
        json_data = json.loads(r.read())
        f = open(f"test.txt", "w")
        items_list = []
        for i in json_data['items']:
            items_list.append(str(i))
        for L in range(0, len(items_list) + 1):
            # print(len(json_data['items']) + 1)
            for subset in set(itertools.combinations(items_list, L)):
                print(len(subset))
                if len(subset) >= 9:
                    f.write(f"{str(str(subset).encode('utf-8'))}\n")

        f.close()
        r.close()

    def combination_byWeapon(self):
        weapon = simpledialog.askstring(title="Choose the weapon", prompt="Choose the weapon")
        r = open(f"items/test.txt", "r", encoding="utf-8", newline='')
        json_data = json.loads(r.read())
        f = open(f"test.txt", "w")
        for L in range(0, len(json_data['items']) + 1):
            #print(len(json_data['items']) + 1)
            for subset in itertools.combinations(json_data['items'], 9):
                print(len(subset))
                if len(subset) >= 9:
                    if weapon in subset:
                        print("SIIII")
                    f.write(f"{str(str(subset).encode('utf-8'))}\n")

        f.close()
        r.close()

    def random_combination(self):
        # Finire da qui

        category_list = [
            'helmet', 'chestplate', 'leggings', 'boots', 'ring', 'necklace', 'bracelet', 'dagger', 'spear', 'bow', 'wand'
        ]

        helmet = None
        chestplate = None
        leggings = None
        boots = None
        weapon = None
        bracelet = None
        necklace = None
        ring1 = None
        ring2 = None

        r = open(f"items/items.txt", "r")
        json_data = json.loads(r.read())
        cnt = 0
        self.out_label['text'] = ""
        for i in json_data['items']:
            cnt += 1
            if i['type'] == "helmet":
                string = ""
                for x in i:
                    string = string + f"{x} = {i[x]}\n"
                    print(f"{x} = {i[x]}")
                self.out_label['text'] = string

        r.close()




    def get_csv(self):
        with open("combination.csv", "w") as f:
            pass

    def all_items(self):
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