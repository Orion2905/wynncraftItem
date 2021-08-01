# Project modules
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
        canvas = tk.Canvas(self, borderwidth=0, highlightthickness = 0, relief="groove", width=1000, height=280, bg="#c8d6e5")
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

        canvas.pack(side="top", fill="both", expand=True)
        scrollbar.pack(side="bottom", fill="both")


class Root:
    def __init__(self, root):
        root.geometry("1300x430")
        # root.resizable(False, False)
        root.title("Wynncraft Items Selection")  # Window title


        self.page = 0

        font = ("Arial", 12)

        self.root = root
        self.root.config(background='#222f3e')
        self.frame2 = ScrollableFrame_x(root)
        self.frame_2 = tk.Frame(self.frame2.scrollable_frame)
        self.frame_2.config(background="#c8d6e5")

        self.frame_3 = tk.Frame(root)
        self.frame_3.config(background='#222f3e')

        self.title2 = tk.Label(self.root, text="", bg="#576574", padx=20, pady=5, font=("Arial", 16, "bold"))
        self.title2.pack(pady=5)

        self.combo_frame = tk.Frame(self.frame_2)
        self.combo_frame.config(background='#222f3e')
        self.show()

        forward = tk.Button(self.frame_3,
                            text=">>>", width=10, bg="#1dd1a1", command=self.next, font=("Arial", 12, "bold"), bd=4)
        forward.grid(row=0, column=1)

        back = tk.Button(self.frame_3,
                         text="<<<", width=10, bg="#ff6b6b", command=self.back, font=("Arial", 12, "bold"), bd=4)
        back.grid(row=0, column=0, padx=5, pady=5)

        self.page_s = tk.Entry(self.frame_3)
        self.page_s.grid(row=0, column=2)

        page_search = tk.Button(self.frame_3, text="Search", width=10, command=self.page_search)
        page_search.grid(row=1, column=2)

        csv = tk.Button(self.frame_3, text="CSV", width=20, command=self.create_csv, font=("Arial", 10, "bold"), bd=4,
                        bg="#54a0ff")
        csv.grid(row=1, column=0, columnspan=2)

        self.combo_frame.grid()
        self.frame_2.pack()

        self.frame2.pack()
        self.frame_3.pack()

    def page_search(self):
        self.page = int(self.page_s.get())
        self.root.update()
        self.show()
        print(self.page)

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
            'Name', 'Category', 'Type', 'Tier', 'Damage', 'fireDamage', 'waterDamage', 'airDamage', 'thunderDamage',
            'earthDamage', 'attackSpeed',
            'health', 'fireDefense', 'waterDefense', 'airDefense', 'thunderDefense', 'earthDefense', 'strength',
            'dexterity', 'intelligence', 'agility', 'defense', 'healthRegen', 'manaRegen', 'spellDamage', 'damageBonus',
            'lifeSteal', 'manaSteal', 'xpBonus', 'lootBonus',
            'reflection', 'strengthPoints', 'dexterityPoints', 'intelligencePoints',
            'agilityPoints', 'defensePoints', 'thorns', 'exploding',
            'speed', 'attackSpeedBonus', 'poison', 'healthBonus',
            'soulPoints', 'emeraldStealing', 'healthRegenRaw', 'spellDamageRaw',
            'damageBonusRaw', 'bonusFireDamage', 'bonusWaterDamage', 'bonusAirDamage',
            'bonusThunderDamage', 'bonusEarthDamage', 'bonusFireDefense', 'bonusWaterDefense',
            'bonusAirDefense', 'bonusThunderDefense', 'bonusEarthDefense'
        ]

        totalDict = {
            'Name' : 'TOTAL BUILD', 'Category' : 0, 'Type' : 0, 'Tier' : 0, 'Damage' : '', 'fireDamage' : '',
            'waterDamage' : '', 'airDamage' : '', 'thunderDamage' : '',
            'earthDamage' : '', 'attackSpeed' : '',
            'health' : 0, 'fireDefense' : 0, 'waterDefense' : 0, 'airDefense' : 0, 'thunderDefense' : 0,
            'earthDefense' : 0,
            'strength' : 0,
            'dexterity' : 0, 'intelligence' : 0, 'agility' : 0,
            'defense' : 0, 'healthRegen' : 0, 'manaRegen' : 0, 'spellDamage' : 0, 'damageBonus' : 0,
            'lifeSteal' : 0, 'manaSteal' : 0, 'xpBonus' : 0, 'lootBonus' : 0,
            'reflection' : 0, 'strengthPoints' : 0, 'dexterityPoints' : 0, 'intelligencePoints' : 0,
            'agilityPoints' : 0, 'defensePoints' : 0,
            'thorns' : 0, 'exploding' : 0, 'speed' : 0, 'attackSpeedBonus' : 0, 'poison' : 0, 'healthBonus' : 0,
            'soulPoints' : 0, 'emeraldStealing' : 0, 'healthRegenRaw' : 0, 'spellDamageRaw' : 0, 'damageBonusRaw' : 0,
            'bonusFireDamage' : 0,
            'bonusWaterDamage' : 0, 'bonusAirDamage' : 0, 'bonusThunderDamage' : 0, 'bonusEarthDamage' : 0,
            'bonusFireDefense' : 0,
            'bonusWaterDefense' : 0,
            'bonusAirDefense' : 0, 'bonusThunderDefense' : 0, 'bonusEarthDefense' : 0
        }


        r = open(f"{file}", "r")
        json_data = json.loads(r.read())
        cnt = 0
        self.title2['text'] = "combo_"+str(self.page)
        combos = json_data['combo_'+str(self.page)]
        cnt2 = 1
        cnt3 = 0
        sum1 = 0
        sum2 = 0
        for j in column_to_show:
            tk.Label(self.combo_frame, text=j, relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=0, column=cnt, pady=10)
            cnt += 1
        for i in combos:

            #print(i['damage'])
            tk.Label(self.combo_frame, text=i['name'], relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=cnt2, column=0)
            tk.Label(self.combo_frame, text=i['category'], relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=cnt2, column=1)

            try:
                tk.Label(self.combo_frame, text=i['type'], relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=cnt2, column=2)
            except:
                tk.Label(self.combo_frame, text=i['accessoryType'], relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=cnt2, column=2)


            tk.Label(self.combo_frame, text=i['tier'], relief="groove", width=15, font=("Arial", 8, "bold")).grid(row=cnt2, column=3)

            try:
                tk.Label(self.combo_frame, text=i['damage'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=4)

                pre = i['damage'].split("-")
                #print(str(pre))
                sum1 = sum1 + int(pre[0])
                sum2 = sum2 + int(pre[1])
                final = str(sum1) + "-" + str(sum2)
                #print(final)
                totalDict['Damage'] = totalDict['Damage'] + final

            except:
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=4)

            sum1, sum2 = 0, 0
            #fire damage
            try:
                tk.Label(self.combo_frame, text=i['fireDamage'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=5)

                pre = i['fireDamage'].split("-")
                # print(str(pre))
                sum1 = sum1 + int(pre[0])
                sum2 = sum2 + int(pre[1])
                final = str(sum1) + "-" + str(sum2)
                # print(final)
                totalDict['fireDamage'] = totalDict['fireDamage'] + final
            except:
                tk.Label(self.combo_frame, text='0', relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=5)

            #water
            sum1 = 0
            sum2 = 0
            try:
                tk.Label(self.combo_frame, text=i['waterDamage'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=6)
                pre = i['waterDamage'].split("-")
                # print(str(pre))
                sum1 = sum1 + int(pre[0])
                sum2 = sum2 + int(pre[1])
                final = str(sum1) + "-" + str(sum2)
                # print(final)
                totalDict['waterDamage'] = totalDict['waterDamage'] + final
            except:
                tk.Label(self.combo_frame, text='0', relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=6)

            #air
            sum1 = 0
            sum2 = 0
            try:
                tk.Label(self.combo_frame, text=i['airDamage'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=7)

                pre = i['airDamage'].split("-")
                # print(str(pre))
                sum1 = int(sum1) + int(pre[0])
                sum2 = int(sum2) + int(pre[1])
                final = str(sum1) + "-" + str(sum2)
                # print(final)
                totalDict['airDamage'] = totalDict['airDamage'] + final
            except:
                #print(e)
                tk.Label(self.combo_frame, text='0', relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=7)

            #thunder
            sum1 = 0
            sum2 = 0
            try:
                tk.Label(self.combo_frame, text=i['thunderDamage'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=8)
                pre = i['thunderDamage'].split("-")
                # print(str(pre))
                sum1 = int(sum1) + int(pre[0])
                sum2 = int(sum2) + int(pre[1])
                final = str(sum1) + "-" + str(sum2)
                # print(final)
                totalDict['thunderDamage'] = totalDict['thunderDamage'] + final
            except:
                tk.Label(self.combo_frame, text='0', relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=8)

            #earth
            sum1 = 0
            sum2 = 0
            try:
                tk.Label(self.combo_frame, text=i['earthDamage'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=9)
                pre = i['earthDamage'].split("-")
                # print(str(pre))
                sum1 = int(sum1) + int(pre[0])
                sum2 = int(sum2) + int(pre[1])
                final = str(sum1) + "-" + str(sum2)
                # print(final)
                totalDict['earthDamage'] = totalDict['earthDamage'] + final
            except:
                tk.Label(self.combo_frame, text='0', relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=9)

            try:
                tk.Label(self.combo_frame, text=i['attackSpeed'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=10)
                totalDict['attackSpeed'] = totalDict['attackSpeed'] + i['attackSpeed']
            except:
                tk.Label(self.combo_frame, text='0', relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=10)


            try:
                tk.Label(self.combo_frame, text=i['health'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=11)
                totalDict['health'] = totalDict['health'] + int(i['health'])
            except:
                tk.Label(self.combo_frame, text='0', relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=11)

            try:
                tk.Label(self.combo_frame, text=i['fireDefense'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=12)
                totalDict['fireDefense'] = totalDict['fireDefense'] + int(i['fireDefense'])
            except:
                tk.Label(self.combo_frame, text='0', relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=12)

            try:
                tk.Label(self.combo_frame, text=i['waterDefense'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=13)
                totalDict['waterDefense'] = totalDict['waterDefense'] + int(i['waterDefense'])
            except:
                tk.Label(self.combo_frame, text='0', relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=13)

            try:
                tk.Label(self.combo_frame, text=i['airDefense'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=14)
                totalDict['airDefense'] = totalDict['airDefense'] + int(i['airDefense'])
            except:
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=14)

            try :
                tk.Label(self.combo_frame, text=i['thunderDefense'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=15)
                totalDict['thunderDefense'] = totalDict['thunderDefense'] + int(i['thunderDefense'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=15)


            try :
                tk.Label(self.combo_frame, text=i['earthDefense'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=16)
                totalDict['earthDefense'] = totalDict['earthDefense'] + int(i['earthDefense'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=16)

            try :
                tk.Label(self.combo_frame, text=i['strength'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=17)
                totalDict['strength'] = totalDict['strength'] + int(i['strength'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=17)

            try :
                tk.Label(self.combo_frame, text=i['dexterity'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=18)
                totalDict['dexterity'] = totalDict['dexterity'] + int(i['dexterity'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=18)

            try :
                tk.Label(self.combo_frame, text=i['intelligence'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=19)
                totalDict['intelligence'] = totalDict['intelligence'] + int(i['intelligence'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=19)

            try :
                tk.Label(self.combo_frame, text=i['agility'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=20)
                totalDict['agility'] = totalDict['agility'] + int(i['agility'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=20)

            try:
                tk.Label(self.combo_frame, text=i['defense'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=21)
                totalDict['defense'] = totalDict['defense'] + int(i['defense'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=21)

            try :
                tk.Label(self.combo_frame, text=i['healthRegen'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=22)
                totalDict['healthRegen'] = totalDict['healthRegen'] + int(i['healthRegen'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=22)

            try :
                tk.Label(self.combo_frame, text=i['manaRegen'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=23)
                totalDict['manaRegen'] = totalDict['manaRegen'] + int(i['manaRegen'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=23)

            try :
                tk.Label(self.combo_frame, text=i['spellDamage'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=24)
                totalDict['spellDamage'] = totalDict['spellDamage'] + int(i['spellDamage'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=24)

            try :
                tk.Label(self.combo_frame, text=i['damageBonus'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=25)
                totalDict['damageBonus'] = totalDict['damageBonus'] + int(i['damageBonus'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=25)

            try :
                tk.Label(self.combo_frame, text=i['lifeSteal'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=26)
                totalDict['lifeSteal'] = totalDict['lifeSteal'] + int(i['lifeSteal'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=26)

            try :
                tk.Label(self.combo_frame, text=i['manaSteal'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=27)
                totalDict['manaSteal'] = totalDict['manaSteal'] + int(i['manaSteal'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=27)

            try :
                tk.Label(self.combo_frame, text=i['xpBonus'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=28)
                totalDict['xpBonus'] = totalDict['xpBonus'] + int(i['xpBonus'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=28)

            try :
                tk.Label(self.combo_frame, text=i['lootBonus'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=29)
                totalDict['lootBonus'] = totalDict['lootBonus'] + int(i['lootBonus'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=29)

            try :
                tk.Label(self.combo_frame, text=i['reflection'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=30)
                totalDict['reflection'] = totalDict['reflection'] + int(i['reflection'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=30)

            try :
                tk.Label(self.combo_frame, text=i['strengthPoints'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=31)
                totalDict['strengthPoints'] = totalDict['strengthPoints'] + int(i['strengthPoints'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=31)

            try :
                tk.Label(self.combo_frame, text=i['dexterityPoints'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=32)
                totalDict['dexterityPoints'] = totalDict['dexterityPoints'] + int(i['dexterityPoints'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=32)

            try :
                tk.Label(self.combo_frame, text=i['intelligencePoints'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=33)
                totalDict['intelligencePoints'] = totalDict['intelligencePoints'] + int(i['intelligencePoints'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=33)

            try :
                tk.Label(self.combo_frame, text=i['agilityPoints'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=34)
                totalDict['agilityPoints'] = totalDict['agilityPoints'] + int(i['agilityPoints'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=34)

            try :
                tk.Label(self.combo_frame, text=i['defensePoints'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=35)
                totalDict['defensePoints'] = totalDict['defensePoints'] + int(i['defensePoints'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=35)

            try :
                tk.Label(self.combo_frame, text=i['thorns'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=36)
                totalDict['thorns'] = totalDict['thorns'] + int(i['thorns'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=36)

            try :
                tk.Label(self.combo_frame, text=i['exploding'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=37)
                totalDict['exploding'] = totalDict['exploding'] + int(i['exploding'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=37)

            try :
                tk.Label(self.combo_frame, text=i['speed'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=38)
                totalDict['speed'] = totalDict['speed'] + int(i['speed'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=38)

            try :
                tk.Label(self.combo_frame, text=i['attackSpeedBonus'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=39)
                totalDict['attackSpeedBonus'] = totalDict['attackSpeedBonus'] + int(i['attackSpeedBonus'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=39)

            try :
                tk.Label(self.combo_frame, text=i['poison'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=40)
                totalDict['poison'] = totalDict['poison'] + int(i['poison'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=40)

            try :
                tk.Label(self.combo_frame, text=i['healthBonus'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=41)
                totalDict['healthBonus'] = totalDict['healthBonus'] + int(i['healthBonus'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=41)

            try :
                tk.Label(self.combo_frame, text=i['soulPoints'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=42)
                totalDict['soulPoints'] = totalDict['soulPoints'] + int(i['soulPoints'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=42)

            try :
                tk.Label(self.combo_frame, text=i['emeraldStealing'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=43)
                totalDict['emeraldStealing'] = totalDict['emeraldStealing'] + int(i['emeraldStealing'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=43)

            try :
                tk.Label(self.combo_frame, text=i['healthRegenRaw'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=44)
                totalDict['healthRegenRaw'] = totalDict['healthRegenRaw'] + int(i['healthRegenRaw'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=44)

            try :
                tk.Label(self.combo_frame, text=i['spellDamageRaw'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=45)
                totalDict['spellDamageRaw'] = totalDict['spellDamageRaw'] + int(i['spellDamageRaw'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=45)

            #Here
            try :
                tk.Label(self.combo_frame, text=i['damageBonusRaw'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=46)
                totalDict['damageBonusRaw'] = totalDict['damageBonusRaw'] + int(i['damageBonusRaw'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=46)

            try :
                tk.Label(self.combo_frame, text=i['bonusFireDamage'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=47)
                totalDict['bonusFireDamage'] = totalDict['bonusFireDamage'] + int(i['bonusFireDamage'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=47)

            try :
                tk.Label(self.combo_frame, text=i['bonusWaterDamage'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=48)
                totalDict['bonusWaterDamage'] = totalDict['bonusWaterDamage'] + int(i['bonusWaterDamage'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=48)

            try :
                tk.Label(self.combo_frame, text=i['bonusAirDamage'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=49)
                totalDict['bonusAirDamage'] = totalDict['bonusAirDamage'] + int(i['bonusAirDamage'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=49)

            try :
                tk.Label(self.combo_frame, text=i['bonusThunderDamage'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=50)
                totalDict['bonusThunderDamage'] = totalDict['bonusThunderDamage'] + int(i['bonusThunderDamage'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=50)

            try :
                tk.Label(self.combo_frame, text=i['bonusEarthDamage'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=51)
                totalDict['bonusEarthDamage'] = totalDict['bonusEarthDamage'] + int(i['bonusEarthDamage'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=51)

            try :
                tk.Label(self.combo_frame, text=i['bonusFireDefense'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=52)
                totalDict['bonusFireDefense'] = totalDict['bonusFireDefense'] + int(i['bonusFireDefense'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=52)

            try :
                tk.Label(self.combo_frame, text=i['bonusWaterDefense'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=53)
                totalDict['bonusWaterDefense'] = totalDict['bonusWaterDefense'] + int(i['bonusWaterDefense'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=53)

            try :
                tk.Label(self.combo_frame, text=i['bonusAirDefense'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=54)
                totalDict['bonusAirDefense'] = totalDict['bonusAirDefense'] + int(i['bonusAirDefense'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=54)

            try :
                tk.Label(self.combo_frame, text=i['bonusThunderDefense'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=55)
                totalDict['bonusThunderDefense'] = totalDict['bonusThunderDefense'] + int(i['bonusThunderDefense'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=55)

            try :
                tk.Label(self.combo_frame, text=i['bonusEarthDefense'], relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=56)
                totalDict['bonusEarthDefense'] = totalDict['bonusEarthDefense'] + int(i['bonusEarthDefense'])
            except :
                tk.Label(self.combo_frame, text="0", relief="groove", width=15,
                         font=("Arial", 8, "bold")).grid(row=cnt2, column=56)

            cnt2 += 1
            cnt3 += 1



        cnt4 = 0
        for o in totalDict:
            #print("QUI",totalDict['Damage'])
            tk.Label(self.combo_frame, text=totalDict[o],relief="groove", width=15,
                 font=("Arial", 8, "bold")).grid(row=cnt2, column=cnt4, pady=15)
            cnt4 += 1

        #function end



    def create_csv(self):
        import csv

        print("START CSV writing process")
        if len(customFile()) > 0:
            file = customFile()
            print("You are now using the file: %s" % file)
        else:
            messagebox.showwarning(title="Warning!", message="please choose a file name\nsettings -> custom file")
            file = "test.txt"

        self.file = filedialog.asksaveasfilename(filetypes=(
            ("CSV files", "*.csv"),
        ))
        if ".csv" in self.file :
            pass
        else :
            self.file = self.file + ".txt"

        print(f"CSV file : {self.file}")

        with open("config/custom_csv_file.txt", "w") as f:
            f.write(self.file)

        with open(self.file, mode='w') as csv_file :

            column_to_show = [
                'Build', 'Boots', 'Bracelet', 'Chestplate', 'Helmet', 'Leggings', 'Necklace', 'Ring1', 'Ring2', 'Weapon',
                'totDamage',  'totFireDamage', 'totWaterDamage', 'totAirDamage', 'totThunderDamage', 'totEarthDamage',
                'totAttackSpeed', 'totHealth', 'totFireDefense', 'totWaterDefense', 'totAirDefense', 'totThunderDefense',
                'totEarthDefense', 'totStrength', 'totDexterity', 'totIntelligence', 'totAgility', 'totDefense',
                'totHealthRegen', 'totManaRegen', 'totSpellDamage', 'totDamageBonus',
                'totLifeSteal', 'totManaSteal', 'totXpBonus', 'totLootBonus',
                'totReflection', 'totStrengthPoints', 'totDexterityPoints', 'totIntelligencePoints',
                'totAgilityPoints', 'totDefensePoints', 'totThorns', 'totExploding',
                'totSpeed', 'totAttackSpeedBonus', 'totPoison', 'totHealthBonus',
                'totSoulPoints', 'totEmeraldStealing', 'totHealthRegenRaw', 'totSpellDamageRaw',
                'totDamageBonusRaw', 'totBonusFireDamage', 'totBonusWaterDamage', 'totBonusAirDamage',
                'totBonusThunderDamage', 'totBonusEarthDamage', 'totBonusFireDefense', 'totBonusWaterDefense',
                'totBonusAirDefense', 'totBonusThunderDefense', 'totBonusEarthDefense'
            ]

            totalDict = {
                'Damage' : '', 'fireDamage' : '',
                'waterDamage' : '', 'airDamage' : '', 'thunderDamage' : '',
                'earthDamage' : '', 'attackSpeed' : '',
                'health' : 0, 'fireDefense' : 0, 'waterDefense' : 0, 'airDefense' : 0, 'thunderDefense' : 0,
                'earthDefense' : 0,
                'strength' : 0,
                'dexterity' : 0, 'intelligence' : 0, 'agility' : 0,
                'defense' : 0, 'healthRegen' : 0, 'manaRegen' : 0, 'spellDamage' : 0, 'damageBonus' : 0,
                'lifeSteal' : 0, 'manaSteal' : 0, 'xpBonus' : 0, 'lootBonus' : 0,
                'reflection' : 0, 'strengthPoints' : 0, 'dexterityPoints' : 0, 'intelligencePoints' : 0,
                'agilityPoints' : 0, 'defensePoints' : 0,
                'thorns' : 0, 'exploding' : 0, 'speed' : 0, 'attackSpeedBonus' : 0, 'poison' : 0, 'healthBonus' : 0,
                'soulPoints' : 0, 'emeraldStealing' : 0, 'healthRegenRaw' : 0, 'spellDamageRaw' : 0,
                'damageBonusRaw' : 0,
                'bonusFireDamage' : 0,
                'bonusWaterDamage' : 0, 'bonusAirDamage' : 0, 'bonusThunderDamage' : 0, 'bonusEarthDamage' : 0,
                'bonusFireDefense' : 0,
                'bonusWaterDefense' : 0,
                'bonusAirDefense' : 0, 'bonusThunderDefense' : 0, 'bonusEarthDefense' : 0
            }



            writer = csv.DictWriter(csv_file, fieldnames=column_to_show, delimiter=';', quotechar='"')
            writer.writeheader()
            r = open(f"{file}", "r")
            json_data = json.loads(r.read())
            sum1 = 0
            sum2 = 0
            for combo in json_data:
                sum1 = 0
                sum2 = 0
                totalDict['Damage'] = ''
                totalDict['health'] = 0
                totalDict['fireDefense'] = 0
                totalDict['waterDefense'] = 0
                totalDict['airDefense'] = 0
                totalDict['thunderDefense'] = 0
                totalDict['earthDefense'] = 0
                totalDict['fireDamage'] = ''
                totalDict['waterDamage'] = ''
                totalDict['airDamage'] = ''
                totalDict['thunderDamage'] = ''
                totalDict['earthDamage'] = ''
                totalDict['attackSpeed'] = ''

                totalDict['healthRegen'] = 0
                totalDict['manaRegen'] = 0
                totalDict['spellDamage'] = 0
                totalDict['damageBonus'] = 0

                totalDict['lifeSteal'] = 0
                totalDict['manaSteal'] = 0
                totalDict['xpBonus'] = 0
                totalDict['lootBonus'] = 0

                totalDict['reflection'] = 0
                totalDict['strengthPoints'] = 0
                totalDict['dexterityPoints'] = 0
                totalDict['intelligencePoints'] = 0

                totalDict['agilityPoints'] = 0
                totalDict['defensePoints'] = 0
                totalDict['thorns'] = 0
                totalDict['exploding'] = 0

                totalDict['speed'] = 0
                totalDict['attackSpeedBonus'] = 0
                totalDict['poison'] = 0
                totalDict['healthBonus'] = 0

                totalDict['soulPoints'] = 0
                totalDict['emeraldStealing'] = 0
                totalDict['healthRegenRaw'] = 0
                totalDict['spellDamageRaw'] = 0

                totalDict['damageBonusRaw'] = 0
                totalDict['bonusFireDamage'] = 0
                totalDict['bonusWaterDamage'] = 0
                totalDict['bonusAirDamage'] = 0

                totalDict['bonusThunderDamage'] = 0
                totalDict['bonusEarthDamage'] = 0
                totalDict['bonusFireDefense'] = 0
                totalDict['bonusWaterDefense'] = 0
                totalDict['bonusAirDefense'] = 0
                totalDict['bonusThunderDefense'] = 0
                totalDict['bonusEarthDefense'] = 0


                for i in range(9):
                    #print(i, totalDict['health'] + int(json_data[combo][i]['health']))
                    try:
                        totalDict['health'] = totalDict['health'] + int(json_data[combo][i]['health'])
                    except:
                        pass

                    try:
                        totalDict['fireDefense'] = totalDict['fireDefense'] + int(json_data[combo][i]['fireDefense'])
                    except:
                        pass

                    try:
                        totalDict['waterDefense'] = totalDict['waterDefense'] + int(json_data[combo][i]['waterDefense'])
                    except:
                        pass

                    try:
                        totalDict['airDefense'] = totalDict['airDefense'] + int(json_data[combo][i]['airDefense'])
                    except:
                        pass

                    try:
                        totalDict['thunderDefense'] = totalDict['thunderDefense'] + int(json_data[combo][i]['thunderDefense'])
                    except:
                        pass
                    try:
                        totalDict['earthDefense'] = totalDict['earthDefense'] + int(json_data[combo][i]['earthDefense'])
                    except:
                        pass

                    totalDict['strength'] = totalDict['strength'] + int(json_data[combo][i]['strength'])
                    #print(i, totalDict['strength'], int(json_data[combo][i]['strength']))
                    totalDict['dexterity'] = totalDict['dexterity'] + int(json_data[combo][i]['dexterity'])
                    totalDict['intelligence'] = totalDict['intelligence'] + int(json_data[combo][i]['intelligence'])
                    totalDict['agility'] = totalDict['agility'] + int(json_data[combo][i]['agility'])
                    totalDict['defense'] = totalDict['defense'] + int(json_data[combo][i]['defense'])

                    totalDict['healthRegen'] = totalDict['healthRegen'] + int(json_data[combo][i]['healthRegen'])
                    totalDict['manaRegen'] = totalDict['manaRegen'] + int(json_data[combo][i]['manaRegen'])
                    totalDict['spellDamage'] = totalDict['spellDamage'] + int(json_data[combo][i]['spellDamage'])
                    totalDict['damageBonus'] = totalDict['damageBonus'] + int(json_data[combo][i]['damageBonus'])

                    totalDict['lifeSteal'] = totalDict['lifeSteal'] + int(json_data[combo][i]['lifeSteal'])
                    totalDict['manaSteal'] = totalDict['manaSteal'] + int(json_data[combo][i]['manaSteal'])
                    totalDict['xpBonus'] = totalDict['xpBonus'] + int(json_data[combo][i]['xpBonus'])
                    totalDict['lootBonus'] = totalDict['lootBonus'] + int(json_data[combo][i]['lootBonus'])

                    totalDict['reflection'] = totalDict['reflection'] + int(json_data[combo][i]['reflection'])
                    totalDict['strengthPoints'] = totalDict['strengthPoints'] + int(json_data[combo][i]['strengthPoints'])
                    totalDict['dexterityPoints'] = totalDict['dexterityPoints'] + int(json_data[combo][i]['dexterityPoints'])
                    totalDict['intelligencePoints'] = totalDict['intelligencePoints'] + int(json_data[combo][i]['intelligencePoints'])

                    totalDict['agilityPoints'] = totalDict['agilityPoints'] + int(json_data[combo][i]['agilityPoints'])
                    totalDict['defensePoints'] = totalDict['defensePoints'] + int(json_data[combo][i]['defensePoints'])
                    totalDict['thorns'] = totalDict['thorns'] + int(json_data[combo][i]['thorns'])
                    totalDict['exploding'] = totalDict['exploding'] + int(json_data[combo][i]['exploding'])

                    totalDict['speed'] = totalDict['speed'] + int(json_data[combo][i]['speed'])
                    totalDict['attackSpeedBonus'] = totalDict['attackSpeedBonus'] + int(json_data[combo][i]['attackSpeedBonus'])
                    totalDict['poison'] = totalDict['poison'] + int(json_data[combo][i]['poison'])
                    totalDict['healthBonus'] = totalDict['healthBonus'] + int(json_data[combo][i]['healthBonus'])

                    totalDict['soulPoints'] = totalDict['soulPoints'] + int(json_data[combo][i]['soulPoints'])
                    totalDict['emeraldStealing'] = totalDict['emeraldStealing'] + int(json_data[combo][i]['emeraldStealing'])
                    totalDict['healthRegenRaw'] = totalDict['healthRegenRaw'] + int(json_data[combo][i]['healthRegenRaw'])
                    totalDict['spellDamageRaw'] = totalDict['spellDamageRaw'] + int(json_data[combo][i]['spellDamageRaw'])

                    totalDict['damageBonusRaw'] = totalDict['damageBonusRaw'] + int(json_data[combo][i]['damageBonusRaw'])
                    totalDict['bonusFireDamage'] = totalDict['bonusFireDamage'] + int(json_data[combo][i]['bonusFireDamage'])
                    totalDict['bonusWaterDamage'] = totalDict['bonusWaterDamage'] + int(json_data[combo][i]['bonusWaterDamage'])
                    totalDict['bonusAirDamage'] = totalDict['bonusAirDamage'] + int(json_data[combo][i]['bonusAirDamage'])

                    totalDict['bonusThunderDamage'] = totalDict['bonusThunderDamage'] + int(json_data[combo][i]['bonusThunderDamage'])
                    totalDict['bonusEarthDamage'] = totalDict['bonusEarthDamage'] + int(json_data[combo][i]['bonusEarthDamage'])
                    totalDict['bonusFireDefense'] = totalDict['bonusFireDefense'] + int(json_data[combo][i]['bonusFireDefense'])
                    totalDict['bonusWaterDefense'] = totalDict['bonusWaterDefense'] + int(json_data[combo][i]['bonusWaterDefense'])
                    totalDict['bonusAirDefense'] = totalDict['bonusAirDefense'] + int(json_data[combo][i]['bonusAirDefense'])
                    totalDict['bonusThunderDefense'] = totalDict['bonusThunderDefense'] + int(json_data[combo][i]['bonusThunderDefense'])
                    totalDict['bonusEarthDefense'] = totalDict['bonusEarthDefense'] + int(json_data[combo][i]['bonusEarthDefense'])

                #damage
                pre = json_data[combo][8]['damage'].split("-")
                # print(str(pre))
                sum1 = sum1 + int(pre[0])
                sum2 = sum2 + int(pre[1])
                final = str(sum1) + "-" + str(sum2)
                # print(final)
                totalDict['Damage'] = totalDict['Damage'] + final

                sum1 = 0
                sum2 = 0

                #fire damage
                pre = json_data[combo][8]['fireDamage'].split("-")
                # print(str(pre))
                sum1 = sum1 + int(pre[0])
                sum2 = sum2 + int(pre[1])
                final = str(sum1) + "-" + str(sum2)
                # print(final)
                totalDict['fireDamage'] = totalDict['fireDamage'] + final

                sum1 = 0
                sum2 = 0

                #water damage
                pre = json_data[combo][8]['waterDamage'].split("-")
                # print(str(pre))
                sum1 = sum1 + int(pre[0])
                sum2 = sum2 + int(pre[1])
                final = str(sum1) + "-" + str(sum2)
                # print(final)
                totalDict['waterDamage'] = totalDict['waterDamage'] + final

                sum1 = 0
                sum2 = 0

                # air damage
                pre = json_data[combo][8]['airDamage'].split("-")
                # print(str(pre))
                sum1 = sum1 + int(pre[0])
                sum2 = sum2 + int(pre[1])
                final = str(sum1) + "-" + str(sum2)
                # print(final)
                totalDict['airDamage'] = totalDict['airDamage'] + final

                sum1 = 0
                sum2 = 0

                # thunder damage
                pre = json_data[combo][8]['thunderDamage'].split("-")
                # print(str(pre))
                sum1 = sum1 + int(pre[0])
                sum2 = sum2 + int(pre[1])
                final = str(sum1) + "-" + str(sum2)
                # print(final)
                totalDict['thunderDamage'] = totalDict['thunderDamage'] + final

                sum1 = 0
                sum2 = 0

                # earth damage
                pre = json_data[combo][8]['earthDamage'].split("-")
                # print(str(pre))
                sum1 = sum1 + int(pre[0])
                sum2 = sum2 + int(pre[1])
                final = str(sum1) + "-" + str(sum2)
                # print(final)
                totalDict['earthDamage'] = totalDict['earthDamage'] + final

                totalDict['attackSpeed'] = totalDict['attackSpeed'] + json_data[combo][8]['attackSpeed']


                dictToWrite = {
                    'Build' : combo,
                    'Boots' : json_data[combo][0]['name'],
                    'Bracelet' : json_data[combo][1]['name'],
                    'Chestplate' : json_data[combo][2]['name'],
                    'Helmet' : json_data[combo][3]['name'],
                    'Leggings' : json_data[combo][4]['name'],
                    'Necklace' : json_data[combo][5]['name'],
                    'Ring1' : json_data[combo][6]['name'],
                    'Ring2' : json_data[combo][7]['name'],
                    'Weapon' : json_data[combo][8]['name'],
                    'totHealth' : totalDict['health'],

                    'totDamage' : totalDict['Damage'],
                    'totFireDamage' : totalDict['fireDamage'],
                    'totWaterDamage' : totalDict['waterDamage'],
                    'totAirDamage' : totalDict['airDamage'],
                    'totThunderDamage' : totalDict['thunderDamage'],
                    'totEarthDamage' : totalDict['earthDamage'],
                    'totAttackSpeed' : totalDict['attackSpeed'],

                    'totFireDefense' : totalDict['fireDefense'],
                    'totWaterDefense' : totalDict['waterDefense'],
                    'totAirDefense' : totalDict['airDefense'],
                    'totThunderDefense' : totalDict['thunderDefense'],
                    'totEarthDefense' : totalDict['earthDefense'],

                    'totStrength' : totalDict['strength'],
                    'totDexterity' : totalDict['dexterity'],
                    'totIntelligence' : totalDict['intelligence'],
                    'totAgility' : totalDict['agility'],
                    'totDefense' : totalDict['defense'],

                    'totHealthRegen' : totalDict['healthRegen'],
                    'totManaRegen' : totalDict['manaRegen'],
                    'totSpellDamage' : totalDict['spellDamage'],
                    'totDamageBonus' : totalDict['damageBonus'],

                    'totLifeSteal' : totalDict['lifeSteal'],
                    'totManaSteal' : totalDict['manaSteal'],
                    'totXpBonus' : totalDict['xpBonus'],
                    'totLootBonus' : totalDict['lootBonus'],

                    'totReflection' : totalDict['reflection'],
                    'totStrengthPoints' : totalDict['strengthPoints'],
                    'totDexterityPoints' : totalDict['dexterityPoints'],
                    'totIntelligencePoints' : totalDict['intelligencePoints'],

                    'totAgilityPoints' : totalDict['agilityPoints'],
                    'totDefensePoints' : totalDict['defensePoints'],
                    'totThorns' : totalDict['thorns'],
                    'totExploding' : totalDict['exploding'],

                    'totSpeed' : totalDict['speed'],
                    'totAttackSpeedBonus' : totalDict['attackSpeedBonus'],
                    'totPoison' : totalDict['poison'],
                    'totHealthBonus' : totalDict['healthBonus'],

                    'totSoulPoints' : totalDict['soulPoints'],
                    'totEmeraldStealing' : totalDict['emeraldStealing'],
                    'totHealthRegenRaw' : totalDict['healthRegenRaw'],
                    'totSpellDamageRaw' : totalDict['spellDamageRaw'],

                    'totDamageBonusRaw' : totalDict['damageBonusRaw'],
                    'totBonusFireDamage' : totalDict['bonusFireDamage'],
                    'totBonusWaterDamage' : totalDict['bonusWaterDamage'],
                    'totBonusAirDamage' : totalDict['bonusAirDamage'],

                    'totBonusThunderDamage' : totalDict['bonusThunderDamage'],
                    'totBonusEarthDamage' : totalDict['bonusEarthDamage'],
                    'totBonusFireDefense' : totalDict['bonusFireDefense'],
                    'totBonusWaterDefense' : totalDict['bonusWaterDefense'],
                    'totBonusAirDefense' : totalDict['bonusAirDefense'],
                    'totBonusThunderDefense' : totalDict['bonusThunderDefense'],
                    'totBonusEarthDefense' : totalDict['bonusEarthDefense']

                                }

                #print(dictToWrite)
                writer.writerow(dictToWrite)

                totalDict['strength'] = 0
                totalDict['dexterity'] = 0
                totalDict['intelligence'] = 0
                totalDict['agility'] = 0
                totalDict['defense'] = 0

            print("CSV process END")








