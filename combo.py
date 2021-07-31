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
        canvas = tk.Canvas(self, borderwidth=0, highlightthickness = 0, relief="groove", width=1000, height=300)
        scrollbar = ttk.Scrollbar(self, orient="horizontal", command=canvas.xview)
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
        scrollbar.pack(side="bottom", fill="both")


class Root:
    def __init__(self, root):
        root.geometry("1300x400")
        # root.resizable(False, False)
        root.title("Wynncraft Items Selection")  # Window title

        self.page = 0

        font = ("Arial", 12)

        self.root = root
        self.frame2 = ScrollableFrame_x(root)
        self.frame_2 = tk.Frame(self.frame2.scrollable_frame)

        self.frame_3 = tk.Frame(root)

        self.title2 = tk.Label(self.root, text="")
        self.title2.pack()

        self.combo_frame = tk.Frame(self.frame_2)
        self.show()

        forward = tk.Button(self.frame_3, text=">>>", width=10, bg="green", command=self.next)
        forward.grid(row=0, column=1)

        back = tk.Button(self.frame_3, text="<<<", width=10, bg="red", command=self.back)
        back.grid(row=0, column=0)

        csv = tk.Button(self.frame_3, text="CSV", width=10)
        csv.grid(row=1, column=0)

        star = tk.Button(self.frame_3, text="★", width=10)
        star.grid(row=1, column=1)

        self.combo_frame.grid()
        self.frame_2.pack()

        self.frame2.pack()
        self.frame_3.pack()

    def next(self):
        self.page += 1
        self.root.update()
        self.show()
        print(self.page)

    def back(self):
        self.page -= 1
        self.root.update()
        self.show()
        print(self.page)


    def show(self):
        if len(customFile()) > 0:
            file = customFile()
            print("You are now using the file: %s" % file)
        else:
            messagebox.showwarning(title="Warning!", message="please choose a file name\nsettings -> custom file")
            file = "test.txt"

        column_to_show = [
            'Name', 'Category', 'Type','Health', 'Health regen', 'Health regen(%)', 'Life Steal', 'Defense', 'Intelligence',
            'Strenght', 'Dexterity',
            'Agility', 'Tier', 'Attack speed', 'Mana Regeneration', 'Mana steal', 'Skill points', 'Soul Point regen',
            'Walk Speed', 'Sprint', 'Sprint regen', 'Jump', 'Loot bonus', 'Xp Bonus', 'Loot quality', 'Spell cost',
            'Poison', 'Exploding', 'Main attack', 'Spell damage',
            'Neutral', 'Fire', 'Earth', 'Water', 'Air', 'Thunder',
            'Neutral', 'Fire', 'Earth', 'Water', 'Air', 'Thunder',
            'Neutral', 'Fire', 'Earth', 'Water', 'Air', 'Thunder',
            'Neutral', 'Fire', 'Earth', 'Water', 'Air', 'Thunder',
            'Neutral', 'Fire', 'Earth', 'Water', 'Air', 'Thunder'
        ]

        totalDict = {'Health':0, 'Health regen':0, 'Health regen(%)':0, 'Life Steal':0, 'Defense':0, 'Intelligence':0,
            'Strenght':0, 'Dexterity':0,
            'Agility':0, 'Tier':0, 'Attack speed':0, 'Mana Regeneration':0, 'Mana steal':0, 'Skill points':0, 'Soul Point regen':0,
            'Walk Speed':0, 'Sprint':0, 'Sprint regen':0, 'Jump':0, 'Loot bonus':0, 'Xp Bonus':0, 'Loot quality':0, 'Spell cost':0,
            'Poison':0, 'Exploding':0, 'Main attack':0, 'Spell damage':0,
            'Neutral':0, 'Fire':0, 'Earth':0, 'Water':0, 'Air':0, 'Thunder':0,
            'Neutral1':0, 'Fire1':0, 'Earth1':0, 'Water1':0, 'Air1':0, 'Thunder1':0,
            'Neutral2':0, 'Fire2':0, 'Earth2':0, 'Water2':0, 'Air2':0, 'Thunder2':0,
            'Neutral3':0, 'Fire3':0, 'Earth3':0, 'Water3':0, 'Air3':0, 'Thunder3':0,
            'Neutral4':0, 'Fire4':0, 'Earth4':0, 'Water4':0, 'Air4':0, 'Thunder4':0}


        r = open("test.txt", "r")
        json_data = json.loads(r.read())
        cnt = 0
        self.title2['text'] = "combo_"+str(self.page)
        combos = json_data['combo_'+str(self.page)]
        cnt2 = 1
        cnt3 = 0
        for j in column_to_show:
            tk.Label(self.combo_frame, text=j, relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=0, column=cnt, pady=10)
            cnt += 1
        for i in combos:
            #print(i['healthRegen'])
            tk.Label(self.combo_frame, text=i['name'], relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=cnt2, column=0)
            tk.Label(self.combo_frame, text=i['category'], relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=cnt2, column=1)

            try:
                tk.Label(self.combo_frame, text=i['type'], relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=cnt2, column=2)
            except:
                tk.Label(self.combo_frame, text=i['accessoryType'], relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=cnt2, column=2)

            try:
                tk.Label(self.combo_frame, text=i['health'], relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=cnt2, column=3)
            except:
                tk.Label(self.combo_frame, text="0", relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=cnt2, column=3)

            tk.Label(self.combo_frame, text=i['healthRegen'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=4)

            tk.Label(self.combo_frame, text=i['healthRegenRaw'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=5)

            tk.Label(self.combo_frame, text=i['lifeSteal'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=6)

            tk.Label(self.combo_frame, text=i['defense'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=7)

            tk.Label(self.combo_frame, text=i['intelligence'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=8)

            tk.Label(self.combo_frame, text=i['strength'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=9)

            tk.Label(self.combo_frame, text=i['dexterity'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=10)

            tk.Label(self.combo_frame, text=i['agility'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=11)

            tk.Label(self.combo_frame, text=i['tier'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=12)

            try:
                tk.Label(self.combo_frame, text=i['attackSpeed'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=13)
            except:
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=13)

            tk.Label(self.combo_frame, text=i['manaRegen'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=14)

            tk.Label(self.combo_frame, text=i['manaSteal'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=15)

            tk.Label(self.combo_frame, text="none", relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=16)

            tk.Label(self.combo_frame, text=i['soulPoints'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=17)

            tk.Label(self.combo_frame, text=i['speed'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=18)

            tk.Label(self.combo_frame, text=i['sprint'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=19)

            tk.Label(self.combo_frame, text=i['sprintRegen'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=20)

            tk.Label(self.combo_frame, text=i['jumpHeight'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=21)

            tk.Label(self.combo_frame, text=i['lootBonus'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=22)

            tk.Label(self.combo_frame, text=i['xpBonus'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=23)

            tk.Label(self.combo_frame, text=i['lootQuality'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=24)

            tk.Label(self.combo_frame, text=i['spellCostPct1'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=25)

            tk.Label(self.combo_frame, text=i['poison'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=26)

            tk.Label(self.combo_frame, text=i['exploding'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=27)

            tk.Label(self.combo_frame, text='none', relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=28)

            tk.Label(self.combo_frame, text=i['spellDamage'], relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=29)

            tk.Label(self.combo_frame, text='none', relief="groove", width=15,
                     font=("Arial", 8, "bold")).grid(row=cnt2, column=30)

            cnt2 += 1
            cnt3 += 1

