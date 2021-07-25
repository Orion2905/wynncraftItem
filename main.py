# Project modules
import requests
import tkinter as tk
from tkinter import *
from tkinter import ttk
import json

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

    def all_items(self):
        pass

    def download_items(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    run = MainApp(root)
    root.mainloop()