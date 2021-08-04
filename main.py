# Project modules
import tkinter as tk
from tkinter import *
from tkinter import ttk
import json
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox
import Check
import os
import random
import combo
import Filter

from tkinter.ttk import *

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

        file_dropdown.add_command(label="About",
                                  command=parent.about)

        file_dropdown.add_command(label="Update Items",
                                  command=parent.update_items)

        menubar.add_cascade(label="Settings", menu=file_dropdown)


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, borderwidth=0, highlightthickness = 0,relief="flat", width=1000, height=800)
        canvas.config(background='#222f3e')
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
        root.geometry("1320x600")
        # root.resizable(False, False)
        root.title("Wynncraft Items Selection") # Window title
        root.config(background='#222f3e')

        self.root = root
        self.photo = PhotoImage(file=r"img/more.png").subsample(2, 2)
        self.photo_2 = PhotoImage(file=r"img/filter.png").subsample(2, 2)

        # Title
        title = tk.Label(root, text="Wynncraft Items Selection", font=("Arial", 20, "bold"),
                         pady=20, relief="groove", border=5, padx=20, bg="#576574")
        title.pack(pady=10)

        self.frame = ScrollableFrame(root)

        self.frame_2 = tk.Frame(self.frame.scrollable_frame)
        self.frame_2.config(background='#222f3e')

        self.frame_3 = tk.Frame(self.frame_2)
        self.frame_3.config(background='#222f3e')

        self.frame_4 = tk.Frame(self.frame_2)
        self.frame_4.config(background='#222f3e')

        #self.combo_frame = tk.Frame(self.frame_2)


        # Search bar
        y = tk.StringVar()
        self.input_1 = tk.Entry(self.frame_2, textvariable=y, width=100, bg="#8395a7", font=("Arial", 13, "bold"),
                                justify=CENTER, relief="sunken", border=3)
        self.input_1.grid(sticky="S", ipady=15)

        item_search = tk.Button(self.frame_3, text="Search for a single item",
                                command=self.search_item_by_name, width=25, height=2,
                                font=("Arial", 10, "bold"), bd=4, bg="#341f97", fg="#c8d6e5")
        item_search.grid(row=0, column=0, padx=4)

        item_clear = tk.Button(self.frame_3, text="Clear", command=self.clear, width=50, height=2,
                               font=("Arial", 10, "bold"), bg="#ff6b6b", bd=4)
        item_clear.grid(row=1, column=0, columnspan=2)

        items_search = tk.Button(self.frame_3, text="Search items by category",
                                 command=self.search_items_by_category, width=25, height=2, font=("Arial", 10, "bold"),
                                 bd=4, bg="#341f97", fg="#c8d6e5")
        items_search.grid(row=0, column=1)

        weapon_btn = tk.Button(self.frame_3, text="Combine random item",
                               command=self.combination_All, width=25, height=2, font=("Arial", 10, "bold"),
                               bd=4, bg="#341f97", fg="#c8d6e5")
        weapon_btn.grid(row=0, column=3, padx=4)

        show_combo = tk.Button(self.frame_3, text="Show combos",
                               command=self.show_combo, width=50, height=2, font=("Arial", 10, "bold"), bg="#10ac84",
                               bd=4)
        show_combo.grid(row=1, column=3, columnspan=2, pady=4)

        all_btn = tk.Button(self.frame_3, text="Combine item by weapon",
                            command=self.combination_byWeapon, width=25, height=2, font=("Arial", 10, "bold"), bd=4,
                            bg="#341f97", fg="#c8d6e5")
        all_btn.grid(row=0, column=4)

        more_btn = tk.Button(self.frame_3, image=self.photo,
                            command=self.more, width=40, height=37, font=("Arial", 10, "bold"), bd=4,
                            bg="#c8d6e5", fg="#c8d6e5", border=4)
        more_btn.grid(row=0, column=5)

        self.combine_by_item_name = tk.Button(self.frame_3, text="Combine item by item name",
                            command=self.combination_byitemname, width=25, height=2, font=("Arial", 10, "bold"), bd=4,
                            bg="#341f97", fg="#c8d6e5")

        self.filter_btn = tk.Button(self.frame_3, image=self.photo_2,
                             command=self.filter, width=40, height=37, font=("Arial", 10, "bold"), bd=4,
                             bg="#c8d6e5", fg="#c8d6e5", border=4)


        self.out_label = tk.Label(self.frame_4, font=("Arial", 10, "bold"), bg="#c8d6e5")
        self.out_label.pack(fill=BOTH, expand=True)

        scroll = Scrollbar(self.frame_4)
        scroll.pack(side=RIGHT, fill=Y)

        self.t = tk.Text(self.frame_4, state=tk.DISABLED, fg="#c8d6e5", height=13, width=110,
                         border=3, yscrollcommand=scroll.set, bg="#576574", font=("Arial", 10))
        self.t.pack()

        self.clear_console = tk.Button(self.frame_4,
                                       text="Clear console",
                                       border=1,
                                       width=50,
                                       bg = "#ff6b6b",
                                       height = 1,
                                       command = self.clear_console,
                                        font = ("Arial", 10, "bold"),
                                       bd = 4

                                       )
        self.clear_console.pack(fill="both", pady=5)

        scroll.config(command=self.t.yview)

        self.frame_3.grid(row=3, pady=10)
        self.frame_4.grid(row=5, pady=10)
        #self.combo_frame.grid(row=4, pady=30)
        self.frame_2.pack()


        self.items = tk.Listbox(root, width=30, relief="groove", bd=6, bg="#8395a7", font=("Arial", 9, "bold"))

        self.scrollbar = Scrollbar(root)
        self.items.pack(side=LEFT, fill=BOTH, pady=20, padx=10)
        self.items.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.items.yview)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)

        self.menubar = MenuBar(self)
        self.frame.pack()

        pl = PrintLogger(self.t)
        sys.stdout = pl

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
                    if len(str(i[x])) > 100:
                        s = i[x][:100]
                        s1 = i[x][100:]
                        i[x] = s + "\n" + s1

                        #print(s)
                        #print(s1)


                    string = string + f"{x} = {i[x]}\n"
                    #print(f"{x} = {i[x]}")
                self.out_label['text'] = string
        r.close()

        # function end

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

        #function end

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
        self.items.delete(0, END)
        self.out_label['text'] = ""

    def more(self):
        if Check.openFile("config/more.txt", "r")[0] == "off":
            self.combine_by_item_name.grid(column=0, row=4)
            self.filter_btn.grid(row=4, column=1, sticky="W")
            Check.openFile("config/more.txt", "w", text="on")
            print(f"More actions : {Check.openFile('config/more.txt', 'r')}")
        else:
            self.combine_by_item_name.grid_forget()
            self.filter_btn.grid_forget()
            Check.openFile("config/more.txt", "w", text="off")
            print(f"More actions : {Check.openFile('config/more.txt', 'r')}")

    def filter(self):
        root = tk.Toplevel()
        run = Filter.FilterGUI(root)
        root.mainloop()


    def combination_byWeapon(self):
        print("START")
        if Check.customFile():
            print(Check.customFile())
            file = Check.customFile()
            temp_file = file.split('.txt')[0] + "_temp.txt"
        else:
            print("No file selected")
            file = ""
            temp_file = ""

        count = simpledialog.askinteger(title="number of combinations",
                                        prompt="How many combinations do you want to get?")
        weapon = simpledialog.askstring(title="weapon",
                                        prompt="which weapon do you want to include in the combo?")

        combination_files = [
            'boots', 'bracelet', 'chestplate', 'helmet', 'leggings', 'necklace', 'ring', 'ring', weapon
        ]
        fo = open(f"{temp_file}", "w")
        fo.close()
        f = open(f"{temp_file}", "a", encoding="utf-8")
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
                if value == len(items):
                    value = value - 1
                #print("Lunghezza:",len(items))
                #print("valore random:",value)
                r.close()
                break_count = 0
                for j in items:
                    self.root.update()
                    #print("A")
                    break_count += 1
                    to_add = j
                    if break_count > value:
                        combo_list.append(to_add)
                        #print(to_add)
                        break

            print(Check.checkCombo(tuple(combo_list)))

            # adding columns
            tot_damage = "0-0"
            tot_defence = 0
            damage_list = ['damage', 'fireDamage', 'waterDamage', 'airDamage', 'thunderDamage', 'earthDamage']
            defence_list = ['fireDefense', 'waterDefense', 'airDefense', 'thunderDefense', 'earthDefense']
            point_list = ['strengthPoints', 'dexterityPoints', 'intelligencePoints', 'agilityPoints', 'defensePoints']
            for dictobjects in combo_list :
                tot_points = 0
                tot_defence = 0
                # print(dictobjects)
                sum1, sum2 = 0, 0
                sum3, sum4 = 0, 0
                if dictobjects['category'] == "weapon" :
                    tot_damage = ""
                    for damages in damage_list :
                        pre = dictobjects[damages].split("-")
                        # print(str(pre))
                        sum1 = sum1 + int(pre[0])
                        sum2 = sum2 + int(pre[1])

                    final = str(sum1) + "-" + str(sum2)
                    tot_damage = tot_damage + final

                if dictobjects['category'] != "weapon" :

                    for defences in defence_list :
                        tot_defence = tot_defence + int(dictobjects[defences])

                # tot_points = 0
                for points in point_list :
                    tot_points = tot_points + int(dictobjects[points])
                    # print("somma:", dictobjects['name'], tot_points, dictobjects[points], points)
                # print(dict(dictobjects)['tier'])

                # print(tot_damage)
                tot_damage_col = f'{tot_damage}'
                tot_defence_col = f'{tot_defence}'
                tot_points_col = f'{tot_points}'

                # print(dictobjects['name'], tot_points_col, tot_defence_col)

                dictobjects['allDamage'] = tot_damage_col
                dictobjects['allDefense'] = tot_defence_col
                dictobjects['allPoints'] = tot_points_col
                # print(dictobjects['name'], tot_points_col)
                # print(dictobjects)

            # filter
            if Check.openFile("config/filter.txt", "r")[0].replace("\n", "") == "status=on" :
                print("Active Filters")
                print("Applying filters ...")

                print(Check.openFile("config/filter.txt", "r"))
                health_to_compare = Check.openFile("config/filter.txt", "r")[1].replace("\n", "").split("=")[1]
                damage_to_compare = Check.openFile("config/filter.txt", "r")[2].replace("\n", "").split("=")[1]
                defense_to_compare = Check.openFile("config/filter.txt", "r")[3].replace("\n", "").split("=")[1]
                points_to_compare = Check.openFile("config/filter.txt", "r")[4].replace("\n", "").split("=")[1]
                attackspeed_to_compare = Check.openFile("config/filter.txt", "r")[5].replace("\n", "").split("=")[1]

                # HEALTH
                tot_health = 0
                tot_damage1 = ''
                ad1 = 0
                ad2 = 0
                tot_points1 = 0
                tot_defense1 = 0
                attack_speed = 0
                for items2 in combo_list :
                    # print(items2)
                    if items2['category'] != "weapon" :
                        tot_health = tot_health + int(items2['health'])
                    # print(items2)

                    # DAMAGE
                    to_split = items2['allDamage'].split("-")
                    ad1 = ad1 + int(to_split[0])
                    ad2 = ad2 + int(to_split[1])
                    # last = str(ad1) + "-" + str(ad2)
                    tot_damage1 = (ad1 + ad2) / 2

                    # POINTS
                    tot_points1 = tot_points1 + int(items2['allPoints'])

                    # DEFENSE
                    tot_defense1 = tot_defense1 + int(items2['allDefense'])

                    # ATTACK SPEED
                    if items2["category"] == "weapon" :
                        if items2["attackSpeed"] == "SUPER_SLOW" :
                            attack_speed = 0
                        elif items2["attackSpeed"] == "VERY_SLOW" :
                            attack_speed = 1
                        elif items2["attackSpeed"] == "SLOW" :
                            attack_speed = 2
                        elif items2["attackSpeed"] == "NORMAL" :
                            attack_speed = 3
                        elif items2["attackSpeed"] == "FAST" :
                            attack_speed = 4
                        elif items2["attackSpeed"] == "VERY_FAST" :
                            attack_speed = 5
                        elif items2["attackSpeed"] == "SUPER_FAST" :
                            attack_speed = 6

                #
                if tot_health >= int(health_to_compare) and tot_damage1 >= int(damage_to_compare) \
                        and tot_points1 < int(points_to_compare) and tot_defense1 >= int(
                    defense_to_compare) and attack_speed \
                        >= int(attackspeed_to_compare) :

                    if " 'addedLore': " in str(combo_list) :
                        for y in combo_list :
                            if " 'addedLore': '" in str(y) :
                                a = str(y).find(" 'addedLore': '")
                                b = str(y).find(", 'sockets':")

                                combo_list = str(combo_list).replace(str(y)[a :b + 1], "")

                    # print(type(combo_list), combo_list)
                    f.write(
                        '"combo_' + str(i) + '":'
                        + str(combo_list).replace("'", '"')
                        .replace('None', 'null').replace('Durum"s', "Durum's")
                        .replace('True', 'true').replace('"s', "'s").replace(" 's", ' "s')
                        .replace('""', '"').replace('"ll', "'ll")
                        .replace("\\", "")
                        .replace('"re', "'re").replace(" 'r", ' "r')
                        .replace('s"', "s'").replace("Boots'", 'Boots"')
                        .replace("restrictions'", 'restrictions"').replace("Treads'", 'Treads"').replace('"a', "'a")
                        .replace("intelligencePoints'", 'intelligencePoints"').replace("sockets'", 'sockets"')
                        .replace("dexterityPoints'", 'dexterityPoints"').replace("',", '",')
                        .replace("':", '":').replace(" 'a", ' "a').replace('"t ', "'t ")
                        .replace('"enhanced"', "'enhanced'").replace('," t', ",' t")
                        .replace('"ve', "'ve").replace('" -', "' -").replace('"one with the wind"',
                                                                             "'one with the wind'")
                        .replace('"gem"', 'gem').replace('"  ', '').replace('"is', "is").replace(' "I ', " I ")
                        .replace('T-shirt"', "T-shirt").replace(' "A ', " 'A ").replace('"GREED"', 'GREED')
                        .replace(" 'A r", ' "A r').replace(" 'A l", ' "A l').replace('I"m', "I'm")
                        .replace('[GREED]', '"[GREED]"').replace(" 'A s", ' "A s').replace(" 'A F", ' "A F')
                        .replace(" 'A G", ' "A G').replace(" 'A m", ' "A m').replace('"r', "'r").replace(" 'r",
                                                                                                         ' "r')
                        .replace('Ol" H', "Ol' H").replace('"Beware', 'Beware') + ','
                    )

                continue

            else :
                print("Filters off")

                if " 'addedLore': " in str(combo_list) :
                    for y in combo_list :
                        if " 'addedLore': '" in str(y) :
                            a = str(y).find(" 'addedLore': '")
                            b = str(y).find(", 'sockets':")

                            combo_list = str(combo_list).replace(str(y)[a :b + 1], "")

                # print(type(combo_list), combo_list)
                f.write(
                    '"combo_' + str(i) + '":'
                    + str(combo_list).replace("'", '"')
                    .replace('None', 'null').replace('Durum"s', "Durum's")
                    .replace('True', 'true').replace('"s', "'s").replace(" 's", ' "s')
                    .replace('""', '"').replace('"ll', "'ll")
                    .replace("\\", "")
                    .replace('"re', "'re").replace(" 'r", ' "r')
                    .replace('s"', "s'").replace("Boots'", 'Boots"')
                    .replace("restrictions'", 'restrictions"').replace("Treads'", 'Treads"').replace('"a', "'a")
                    .replace("intelligencePoints'", 'intelligencePoints"').replace("sockets'", 'sockets"')
                    .replace("dexterityPoints'", 'dexterityPoints"').replace("',", '",')
                    .replace("':", '":').replace(" 'a", ' "a').replace('"t ', "'t ")
                    .replace('"enhanced"', "'enhanced'").replace('," t', ",' t")
                    .replace('"ve', "'ve").replace('" -', "' -").replace('"one with the wind"',
                                                                         "'one with the wind'")
                    .replace('"gem"', 'gem').replace('"  ', '').replace('"is', "is").replace(' "I ', " I ")
                    .replace('T-shirt"', "T-shirt").replace(' "A ', " 'A ").replace('"GREED"', 'GREED')
                    .replace(" 'A r", ' "A r').replace(" 'A l", ' "A l').replace('I"m', "I'm")
                    .replace('[GREED]', '"[GREED]"').replace(" 'A s", ' "A s').replace(" 'A F", ' "A F')
                    .replace(" 'A G", ' "A G').replace(" 'A m", ' "A m').replace('"r', "'r").replace(" 'r", ' "r')
                    .replace('Ol" H', "Ol' H").replace('"Beware', 'Beware') + ','
                )

        self.root.update()
        f.write("}")
        f.close()
        with open(f"{file}", "w") as f1:
            with open(f"{temp_file}", "r") as f2:
                for lines in f2:
                    #print(lines)
                    f1.write(lines.replace('}],}', '}]}'))

        if ".txt" in temp_file :
            os.remove(f"{temp_file}")
        else :
            os.remove(f"{temp_file}.txt")
        print("END")

        #function end

    def combination_All(self):
        print("START")
        if Check.customFile() :
            print(Check.customFile())
            file = Check.customFile()
            temp_file = file.split('.txt')[0] + "_temp.txt"
        else :
            print("No file selected")
            file = ""
            temp_file = ""
        count = simpledialog.askinteger(title="number of combinations",
                                        prompt="How many combinations do you want to get?")
        weapon = "bow"

        weapon_file = ['bow', 'dagger', 'spear', 'wand']

        combination_files = [
            'boots', 'bracelet', 'chestplate', 'helmet', 'leggings', 'necklace', 'ring', 'ring', weapon
        ]
        fo = open(f"{temp_file}", "w")
        fo.close()
        f = open(f"{temp_file}", "a", encoding="utf-8")
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
                #value = len(items)
                if value == len(items):
                    value = value - 1

                #print("Lunghezza:",len(items))
                #print("valore random:",value)
                r.close()
                #break_count = 0
                break_count = 0
                for j in items:
                    self.root.update()
                    # print("A")
                    break_count += 1
                    to_add = j
                    #print(x, break_count, value)
                    if break_count > value:
                        #print(to_add)
                        combo_list.append(to_add)
                        # print(to_add)
                        break

            print(Check.checkCombo(tuple(combo_list)))
            #print(combo_list)
            #print(str(combo_list))

            # adding columns
            tot_damage = "0-0"
            tot_defence = 0
            damage_list = ['damage', 'fireDamage', 'waterDamage', 'airDamage', 'thunderDamage', 'earthDamage']
            defence_list = ['fireDefense', 'waterDefense', 'airDefense', 'thunderDefense', 'earthDefense']
            point_list = ['strengthPoints', 'dexterityPoints', 'intelligencePoints', 'agilityPoints', 'defensePoints']
            for dictobjects in combo_list:
                tot_points = 0
                tot_defence = 0
                #print(dictobjects)
                sum1, sum2 = 0, 0
                sum3, sum4 = 0, 0
                if dictobjects['category'] == "weapon":
                    tot_damage = ""
                    for damages in damage_list:
                        pre = dictobjects[damages].split("-")
                        # print(str(pre))
                        sum1 = sum1 + int(pre[0])
                        sum2 = sum2 + int(pre[1])

                    final = str(sum1) + "-" + str(sum2)
                    tot_damage = tot_damage + final

                if dictobjects['category'] != "weapon":

                    for defences in defence_list:
                        tot_defence = tot_defence + int(dictobjects[defences])

                #tot_points = 0
                for points in point_list:
                    tot_points = tot_points + int(dictobjects[points])
                    #print("somma:", dictobjects['name'], tot_points, dictobjects[points], points)
                # print(dict(dictobjects)['tier'])


            #print(tot_damage)
                tot_damage_col = f'{tot_damage}'
                tot_defence_col = f'{tot_defence}'
                tot_points_col = f'{tot_points}'

                #print(dictobjects['name'], tot_points_col, tot_defence_col)

                dictobjects['allDamage'] = tot_damage_col
                dictobjects['allDefense'] = tot_defence_col
                dictobjects['allPoints'] = tot_points_col
                #print(dictobjects['name'], tot_points_col)
                #print(dictobjects)

            #print(combo_list)
            test = ""


            #filter
            if Check.openFile("config/filter.txt", "r")[0].replace("\n", "") == "status=on" :
                print("Active Filters")
                print("Applying filters ...")

                print(Check.openFile("config/filter.txt", "r"))
                health_to_compare = Check.openFile("config/filter.txt", "r")[1].replace("\n", "").split("=")[1]
                damage_to_compare = Check.openFile("config/filter.txt", "r")[2].replace("\n", "").split("=")[1]
                defense_to_compare = Check.openFile("config/filter.txt", "r")[3].replace("\n", "").split("=")[1]
                points_to_compare = Check.openFile("config/filter.txt", "r")[4].replace("\n", "").split("=")[1]
                attackspeed_to_compare = Check.openFile("config/filter.txt", "r")[5].replace("\n", "").split("=")[1]



                # HEALTH
                tot_health = 0
                tot_damage1 = ''
                ad1 = 0
                ad2 = 0
                tot_points1 = 0
                tot_defense1 = 0
                attack_speed = 0
                for items2 in combo_list:
                    #print(items2)
                    if items2['category'] != "weapon":
                        tot_health = tot_health + int(items2['health'])
                    #print(items2)

                    # DAMAGE
                    to_split = items2['allDamage'].split("-")
                    ad1 = ad1 + int(to_split[0])
                    ad2 = ad2 + int(to_split[1])
                    #last = str(ad1) + "-" + str(ad2)
                    tot_damage1 = (ad1 + ad2)/2

                    # POINTS
                    tot_points1 = tot_points1 + int(items2['allPoints'])

                    # DEFENSE
                    tot_defense1 = tot_defense1 + int(items2['allDefense'])

                    # ATTACK SPEED
                    if items2["category"] == "weapon":
                        if items2["attackSpeed"] == "SUPER_SLOW":
                            attack_speed = 0
                        elif items2["attackSpeed"] == "VERY_SLOW":
                            attack_speed = 1
                        elif items2["attackSpeed"] == "SLOW":
                            attack_speed = 2
                        elif items2["attackSpeed"] == "NORMAL":
                            attack_speed = 3
                        elif items2["attackSpeed"] == "FAST":
                            attack_speed = 4
                        elif items2["attackSpeed"] == "VERY_FAST":
                            attack_speed = 5
                        elif items2["attackSpeed"] == "SUPER_FAST":
                            attack_speed = 6

                #print(attack_speed)
                if tot_health >= int(health_to_compare) and tot_damage1 >= int(damage_to_compare)\
                    and tot_points1 < int(points_to_compare) and tot_defense1 >= int(defense_to_compare) and attack_speed\
                        >= int(attackspeed_to_compare):

                    if " 'addedLore': " in str(combo_list) :
                        for y in combo_list :
                            if " 'addedLore': '" in str(y) :
                                a = str(y).find(" 'addedLore': '")
                                b = str(y).find(", 'sockets':")

                                combo_list = str(combo_list).replace(str(y)[a :b + 1], "")

                    # print(type(combo_list), combo_list)
                    f.write(
                        '"combo_' + str(i) + '":'
                        + str(combo_list).replace("'", '"')
                        .replace('None', 'null').replace('Durum"s', "Durum's")
                        .replace('True', 'true').replace('"s', "'s").replace(" 's", ' "s')
                        .replace('""', '"').replace('"ll', "'ll")
                        .replace("\\", "")
                        .replace('"re', "'re").replace(" 'r", ' "r')
                        .replace('s"', "s'").replace("Boots'", 'Boots"')
                        .replace("restrictions'", 'restrictions"').replace("Treads'", 'Treads"').replace('"a', "'a")
                        .replace("intelligencePoints'", 'intelligencePoints"').replace("sockets'", 'sockets"')
                        .replace("dexterityPoints'", 'dexterityPoints"').replace("',", '",')
                        .replace("':", '":').replace(" 'a", ' "a').replace('"t ', "'t ")
                        .replace('"enhanced"', "'enhanced'").replace('," t', ",' t")
                        .replace('"ve', "'ve").replace('" -', "' -").replace('"one with the wind"',
                                                                             "'one with the wind'")
                        .replace('"gem"', 'gem').replace('"  ', '').replace('"is', "is").replace(' "I ', " I ")
                        .replace('T-shirt"', "T-shirt").replace(' "A ', " 'A ").replace('"GREED"', 'GREED')
                        .replace(" 'A r", ' "A r').replace(" 'A l", ' "A l').replace('I"m', "I'm")
                        .replace('[GREED]', '"[GREED]"').replace(" 'A s", ' "A s').replace(" 'A F", ' "A F')
                        .replace(" 'A G", ' "A G').replace(" 'A m", ' "A m').replace('"r', "'r").replace(" 'r", ' "r')
                        .replace('Ol" H', "Ol' H").replace('"Beware', 'Beware') + ','
                    )

                continue

            else :
                print("Filters off")

                if " 'addedLore': " in str(combo_list) :
                    for y in combo_list :
                        if " 'addedLore': '" in str(y) :
                            a = str(y).find(" 'addedLore': '")
                            b = str(y).find(", 'sockets':")

                            combo_list = str(combo_list).replace(str(y)[a :b + 1], "")

                #print(type(combo_list), combo_list)
                f.write(
                    '"combo_' + str(i) + '":'
                    + str(combo_list).replace("'", '"')
                    .replace('None', 'null').replace('Durum"s', "Durum's")
                    .replace('True', 'true').replace('"s', "'s").replace(" 's", ' "s')
                    .replace('""', '"').replace('"ll', "'ll")
                    .replace("\\", "")
                    .replace('"re', "'re").replace(" 'r", ' "r')
                    .replace('s"', "s'").replace("Boots'", 'Boots"')
                    .replace("restrictions'", 'restrictions"').replace("Treads'", 'Treads"').replace('"a', "'a")
                    .replace("intelligencePoints'", 'intelligencePoints"').replace("sockets'", 'sockets"')
                    .replace("dexterityPoints'", 'dexterityPoints"').replace("',", '",')
                    .replace("':", '":').replace(" 'a", ' "a').replace('"t ', "'t ")
                    .replace('"enhanced"', "'enhanced'").replace('," t', ",' t")
                    .replace('"ve', "'ve").replace('" -', "' -").replace('"one with the wind"', "'one with the wind'")
                    .replace('"gem"', 'gem').replace('"  ', '').replace('"is', "is").replace(' "I ', " I ")
                    .replace('T-shirt"', "T-shirt").replace(' "A ', " 'A ").replace('"GREED"', 'GREED')
                    .replace(" 'A r", ' "A r').replace(" 'A l", ' "A l').replace('I"m', "I'm")
                    .replace('[GREED]', '"[GREED]"').replace(" 'A s", ' "A s').replace(" 'A F", ' "A F')
                    .replace(" 'A G", ' "A G').replace(" 'A m", ' "A m').replace('"r', "'r").replace(" 'r", ' "r')
                    .replace('Ol" H', "Ol' H").replace('"Beware', 'Beware') + ','
                )

        self.root.update()
        f.write("}")
        f.close()
        with open(f"{file}", "w", encoding="utf-8") as f1 :
            with open(f"{temp_file}", "r", encoding="utf-8") as f2 :
                for lines in f2:
                    # print(lines)
                    f1.write(lines.replace('}],}', '}]}'))

        if ".txt" in temp_file :
            os.remove(f"{temp_file}")
        else :
            os.remove(f"{temp_file}.txt")


        print("END")


        #function end


    # Da finire da qui
    def combination_byitemname(self):

        count = simpledialog.askinteger(title="number of combinations",
                                        prompt="How many combinations do you want to get?")
        item_to_search = simpledialog.askstring(title="custom item",
                                        prompt="which item(name) do you want to include in the combo?")

        r = open(f"items/items.txt", "r")
        json_data = json.loads(r.read())
        cnt = 0
        item_type = ""
        item_cat = ""
        for i in json_data['items'] :
            cnt += 1
            if i['name'] == item_to_search :
                try:
                    item_cat = i['category']
                    item_type= i['type']
                except:
                    item_type = i['accessoryType']

                #print(item_type, item_cat)
        r.close()

        print("START")
        if Check.customFile() :
            print(Check.customFile())
            file = Check.customFile()
            temp_file = file.split('.txt')[0] + "_temp.txt"
        else :
            print("No file selected")
            file = ""
            temp_file = ""

        weapon_list = ['bow', 'dagger', 'spear', 'wand']

        items_category = [
            'boots', 'bracelet', 'chestplate', 'helmet', 'leggings', 'necklace', 'ring', 'ring'
        ]

        weapon = "bow"
        if item_cat == "weapon":
            weapon = item_type

        combination_files = [
            'boots', 'bracelet', 'chestplate', 'helmet', 'leggings', 'necklace', 'ring', 'ring2', weapon
        ]

        fo = open(f"{temp_file}", "w")
        fo.close()
        f = open(f"{temp_file}", "a", encoding="utf-8")
        f.write("{")
        to_add = ""
        break_count = 0
        combo_list = []
        for i in range(count):
            print("Combo:", i)
            # print("dove mi trovo:",i)
            self.root.update()
            combo_list = []
            if weapon == "bow":
                combination_files[8] = random.choice(weapon_list)
            for x in combination_files:
                self.root.update()
                # print("lista:",x)
                if x == "ring2":
                    ring = "ring"
                    r = open(f"items/items_{ring}.txt", "r", encoding="utf-8", newline='')
                else:
                    r = open(f"items/items_{x}.txt", "r", encoding="utf-8", newline='')

                json_data = json.loads(r.read())
                items = json_data['items']
                #print(x, item_type)
                if x.capitalize() == item_type:
                    p = 0
                    for item in items:
                       if item['name'] == item_to_search:
                           value = p
                           break

                       p += 1
                else:
                    value = random.randint(0, len(items))

                if value == len(items) :
                    value = value - 1
                # print("Lunghezza:",len(items))
                # print("valore random:",value)
                r.close()
                break_count = 0
                for j in items :
                    self.root.update()
                    # print("A")
                    break_count += 1
                    to_add = j
                    if break_count > value :
                        combo_list.append(to_add)
                        # print(to_add)
                        break

            print(Check.checkCombo(tuple(combo_list)))

            # adding columns
            tot_damage = "0-0"
            tot_defence = 0
            damage_list = ['damage', 'fireDamage', 'waterDamage', 'airDamage', 'thunderDamage', 'earthDamage']
            defence_list = ['fireDefense', 'waterDefense', 'airDefense', 'thunderDefense', 'earthDefense']
            point_list = ['strengthPoints', 'dexterityPoints', 'intelligencePoints', 'agilityPoints', 'defensePoints']
            for dictobjects in combo_list :
                tot_points = 0
                tot_defence = 0
                # print(dictobjects)
                sum1, sum2 = 0, 0
                sum3, sum4 = 0, 0
                if dictobjects['category'] == "weapon" :
                    tot_damage = ""
                    for damages in damage_list :
                        pre = dictobjects[damages].split("-")
                        # print(str(pre))
                        sum1 = sum1 + int(pre[0])
                        sum2 = sum2 + int(pre[1])

                    final = str(sum1) + "-" + str(sum2)
                    tot_damage = tot_damage + final

                if dictobjects['category'] != "weapon" :

                    for defences in defence_list :
                        tot_defence = tot_defence + int(dictobjects[defences])

                # tot_points = 0
                for points in point_list :
                    tot_points = tot_points + int(dictobjects[points])
                    # print("somma:", dictobjects['name'], tot_points, dictobjects[points], points)
                # print(dict(dictobjects)['tier'])

                # print(tot_damage)
                tot_damage_col = f'{tot_damage}'
                tot_defence_col = f'{tot_defence}'
                tot_points_col = f'{tot_points}'

                # print(dictobjects['name'], tot_points_col, tot_defence_col)

                dictobjects['allDamage'] = tot_damage_col
                dictobjects['allDefense'] = tot_defence_col
                dictobjects['allPoints'] = tot_points_col
                # print(dictobjects['name'], tot_points_col)
                # print(dictobjects)

            # filter
            if Check.openFile("config/filter.txt", "r")[0].replace("\n", "") == "status=on" :
                print("Active Filters")
                print("Applying filters ...")

                print(Check.openFile("config/filter.txt", "r"))
                health_to_compare = Check.openFile("config/filter.txt", "r")[1].replace("\n", "").split("=")[1]
                damage_to_compare = Check.openFile("config/filter.txt", "r")[2].replace("\n", "").split("=")[1]
                defense_to_compare = Check.openFile("config/filter.txt", "r")[3].replace("\n", "").split("=")[1]
                points_to_compare = Check.openFile("config/filter.txt", "r")[4].replace("\n", "").split("=")[1]
                attackspeed_to_compare = Check.openFile("config/filter.txt", "r")[5].replace("\n", "").split("=")[1]

                # HEALTH
                tot_health = 0
                tot_damage1 = ''
                ad1 = 0
                ad2 = 0
                tot_points1 = 0
                tot_defense1 = 0
                attack_speed = 0
                for items2 in combo_list :
                    # print(items2)
                    if items2['category'] != "weapon" :
                        tot_health = tot_health + int(items2['health'])
                    # print(items2)

                    # DAMAGE
                    to_split = items2['allDamage'].split("-")
                    ad1 = ad1 + int(to_split[0])
                    ad2 = ad2 + int(to_split[1])
                    # last = str(ad1) + "-" + str(ad2)
                    tot_damage1 = (ad1 + ad2) / 2

                    # POINTS
                    tot_points1 = tot_points1 + int(items2['allPoints'])

                    # DEFENSE
                    tot_defense1 = tot_defense1 + int(items2['allDefense'])

                    # ATTACK SPEED
                    if items2["category"] == "weapon" :
                        if items2["attackSpeed"] == "SUPER_SLOW" :
                            attack_speed = 0
                        elif items2["attackSpeed"] == "VERY_SLOW" :
                            attack_speed = 1
                        elif items2["attackSpeed"] == "SLOW" :
                            attack_speed = 2
                        elif items2["attackSpeed"] == "NORMAL" :
                            attack_speed = 3
                        elif items2["attackSpeed"] == "FAST" :
                            attack_speed = 4
                        elif items2["attackSpeed"] == "VERY_FAST" :
                            attack_speed = 5
                        elif items2["attackSpeed"] == "SUPER_FAST" :
                            attack_speed = 6

                #print(attack_speed)
                if tot_health >= int(health_to_compare) and tot_damage1 >= int(damage_to_compare) \
                        and tot_points1 < int(points_to_compare) and tot_defense1 >= int(
                    defense_to_compare) and attack_speed \
                        >= int(attackspeed_to_compare) :

                    if " 'addedLore': " in str(combo_list) :
                        for y in combo_list :
                            if " 'addedLore': '" in str(y) :
                                a = str(y).find(" 'addedLore': '")
                                b = str(y).find(", 'sockets':")

                                combo_list = str(combo_list).replace(str(y)[a :b + 1], "")

                    # print(type(combo_list), combo_list)
                    f.write(
                        '"combo_' + str(i) + '":'
                        + str(combo_list).replace("'", '"')
                        .replace('None', 'null').replace('Durum"s', "Durum's")
                        .replace('True', 'true').replace('"s', "'s").replace(" 's", ' "s')
                        .replace('""', '"').replace('"ll', "'ll")
                        .replace("\\", "")
                        .replace('"re', "'re").replace(" 'r", ' "r')
                        .replace('s"', "s'").replace("Boots'", 'Boots"')
                        .replace("restrictions'", 'restrictions"').replace("Treads'", 'Treads"').replace('"a', "'a")
                        .replace("intelligencePoints'", 'intelligencePoints"').replace("sockets'", 'sockets"')
                        .replace("dexterityPoints'", 'dexterityPoints"').replace("',", '",')
                        .replace("':", '":').replace(" 'a", ' "a').replace('"t ', "'t ")
                        .replace('"enhanced"', "'enhanced'").replace('," t', ",' t")
                        .replace('"ve', "'ve").replace('" -', "' -").replace('"one with the wind"',
                                                                             "'one with the wind'")
                        .replace('"gem"', 'gem').replace('"  ', '').replace('"is', "is").replace(' "I ', " I ")
                        .replace('T-shirt"', "T-shirt").replace(' "A ', " 'A ").replace('"GREED"', 'GREED')
                        .replace(" 'A r", ' "A r').replace(" 'A l", ' "A l').replace('I"m', "I'm")
                        .replace('[GREED]', '"[GREED]"').replace(" 'A s", ' "A s').replace(" 'A F", ' "A F')
                        .replace(" 'A G", ' "A G').replace(" 'A m", ' "A m').replace('"r', "'r").replace(" 'r",
                                                                                                         ' "r')
                        .replace('Ol" H', "Ol' H").replace('"Beware', 'Beware') + ','
                    )

                continue

            else :
                print("Filters off")

                if " 'addedLore': " in str(combo_list) :
                    for y in combo_list :
                        if " 'addedLore': '" in str(y) :
                            a = str(y).find(" 'addedLore': '")
                            b = str(y).find(", 'sockets':")

                            combo_list = str(combo_list).replace(str(y)[a :b + 1], "")

                # print(type(combo_list), combo_list)
                f.write(
                    '"combo_' + str(i) + '":'
                    + str(combo_list).replace("'", '"')
                    .replace('None', 'null').replace('Durum"s', "Durum's")
                    .replace('True', 'true').replace('"s', "'s").replace(" 's", ' "s')
                    .replace('""', '"').replace('"ll', "'ll")
                    .replace("\\", "")
                    .replace('"re', "'re").replace(" 'r", ' "r')
                    .replace('s"', "s'").replace("Boots'", 'Boots"')
                    .replace("restrictions'", 'restrictions"').replace("Treads'", 'Treads"').replace('"a', "'a")
                    .replace("intelligencePoints'", 'intelligencePoints"').replace("sockets'", 'sockets"')
                    .replace("dexterityPoints'", 'dexterityPoints"').replace("',", '",')
                    .replace("':", '":').replace(" 'a", ' "a').replace('"t ', "'t ")
                    .replace('"enhanced"', "'enhanced'").replace('," t', ",' t")
                    .replace('"ve', "'ve").replace('" -', "' -").replace('"one with the wind"',
                                                                         "'one with the wind'")
                    .replace('"gem"', 'gem').replace('"  ', '').replace('"is', "is").replace(' "I ', " I ")
                    .replace('T-shirt"', "T-shirt").replace(' "A ', " 'A ").replace('"GREED"', 'GREED')
                    .replace(" 'A r", ' "A r').replace(" 'A l", ' "A l').replace('I"m', "I'm")
                    .replace('[GREED]', '"[GREED]"').replace(" 'A s", ' "A s').replace(" 'A F", ' "A F')
                    .replace(" 'A G", ' "A G').replace(" 'A m", ' "A m').replace('"r', "'r").replace(" 'r", ' "r')
                    .replace('Ol" H', "Ol' H").replace('"Beware', 'Beware') + ','
                )

        self.root.update()
        f.write("}")
        f.close()
        with open(f"{file}", "w") as f1 :
            with open(f"{temp_file}", "r") as f2 :
                for lines in f2 :
                    # print(lines)
                    f1.write(lines.replace('}],}', '}]}'))

        if ".txt" in temp_file:
            os.remove(f"{temp_file}")
        else:
            os.remove(f"{temp_file}.txt")
        print("END")

        # function end

        # function end

    # MenuBar functions for custom color
    def custom_color(self):
        color_code = colorchooser.askcolor(title="Choose color")
        if color_code[1] == "#000000":
            print(1)
        else:
            self.root['background'] = color_code[1]
        print(color_code)

    #function end

    def about(self):
        messagebox.showinfo(
            title="About", message="Wynncraft Item Combination\nAuthor : Orionpy\nYoutube : OrionDev\nVersion = 1.0")

    def update_items(self):
        print("Items Updating. Wait please")

        category_to_download = [
            'all', 'boots', 'bow', 'bracelet', 'chestplate', 'dagger',
            'helmet', 'leggings', 'necklace', 'ring', 'spear', 'wand'
        ]

        file_to_write = [
            'items', 'items_boots', 'items_bow', 'items_bracelet', 'items_chestplate', 'items_dagger',
            'items_helmet', 'items_leggings', 'items_necklace', 'items_ring', 'items_spear', 'items_wand'
        ]

        #os.system("cd .venv/scripts & activate & cd ../../")
        try:
            import urllib.request
        except Exception as e:
            print(e)

        for category in category_to_download:
            self.root.update()
            if category == "all":
                url = f"https://api.wynncraft.com/public_api.php?action=itemDB&category=all"
                file_name = f"items"

            else:
                url = f"https://api.wynncraft.com/public_api.php?action=itemDB&category={category}"
                file_name = f"items_{category}"

            # make the request
            uh = urllib.request.urlopen(url)
            r = uh.read().decode()
            self.root.update()
            # get the data
            category_to_write = json.loads(r)
            self.root.update()
            with open(f"items/{file_name}.txt", "w", encoding="utf-8") as f:
                f.write(json.dumps(category_to_write))


                self.root.update()


        print("Items Updated")

if __name__ == "__main__":
    root = tk.Tk()
    run = MainApp(root)
    root.mainloop()