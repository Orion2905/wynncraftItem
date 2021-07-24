# Project modules
import requests
import tkinter as tk

category = input("category name >> ")

url = f"https://api.wynncraft.com/public_api.php?action=itemDB&category={category}"


#make the request
r = requests.get(url)
#get the data
json = r.json()
#Print the data
f = open("item_name.txt", "w")
f2 = open("items.json", "w")
f2.write(json)
f.close()
f2.close()



class MainApp: # The main class of the project
    def __init__(self, root):
        root.geometry("500x600")
        # root.resizable(False, False)
        root.title("Wynncraft Items Selection") # Window title

        font = ("Arial", 12)

        # Title
        title = tk.Label(root, text="Wynncraft Items Selection")
        title.pack()

        # Search bar
        y = tk.StringVar()
        self.input_1 = tk.Entry(root, textvariable=y)
        self.input_1.pack()

        item_search = tk.Button(root, text="explore the data: ", command=self.search_item)
        item_search.pack()

        items_search = tk.Button(root, text="explore the data: ", command=self.search_items)
        items_search.pack()

        self.items = tk.Listbox(root, width=50, font=font)

    # Class functions

    def search_item(self): # search single item
        pass

    def search_items(self): # search multiple items
        url = f"https://api.wynncraft.com/public_api.php?action=itemDB&category={self.input_1.get()}"
        r = requests.get(url)
        json = r.json()
        cnt = 0
        for i in json['items']:
            cnt += 1
            string = f"[{cnt}] {i['name']}"
            self.items.insert(cnt, string)

        self.items.pack()


    def all_items(self):
        pass

    def download_items(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    run = MainApp(root)
    root.mainloop()