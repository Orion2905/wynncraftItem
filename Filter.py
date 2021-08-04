# Project modules
import tkinter as tk
from tkinter import *
import os
from tkinter import ttk
import json
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import filedialog
from tkinter import messagebox
import Check

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self, borderwidth=0, highlightthickness = 0, height=500,relief="flat")
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

class FilterGUI:

    def __init__(self, root):
        root.geometry("500x650")
        # root.resizable(False, False)
        root.title("Wynncraft Items Selection")  # Window title
        root.config(background='#222f3e')
        root.resizable(0, 0)

        self.root = root
        self.frame = ScrollableFrame(root)

        self.frame_2 = tk.Frame(self.frame.scrollable_frame)
        self.frame_2.config(background='#222f3e')

        self.photo = PhotoImage(file=r"img/on.png").subsample(1, 1)
        self.photo_2 = PhotoImage(file=r"img/off.png").subsample(1, 1)

        title_1 = tk.Label(root, text="Wynncraft Items Filter", font=("Arial", 20, "bold"),
                         pady=10, relief="groove", border=5, padx=20, bg="#576574")
        title_1.pack(pady=10)

        self.on_off_btn = tk.Button(root, image=self.photo_2,
                             command=self.on_off, width=200,font=("Arial", 10, "bold"), bd=4,
                             bg="#222f3e", fg="#c8d6e5", border=2)
        self.on_off_btn.pack(fill=BOTH)

        self.min_health = tk.Scale(self.frame_2, from_=0, to=30000, orient=HORIZONTAL, relief="groove", troughcolor="#5f27cd", bd=4,
                              font=("Arial", 10, "bold"), highlightcolor="#00d2d3", label="min Health", sliderlength=20
                                   , activebackground="#f368e0", bg="#8395a7")
        self.min_health.grid(ipadx=170, padx=10, pady=5)

        self.min_damage = tk.Scale(self.frame_2, from_=0, to=1000, orient=HORIZONTAL, relief="groove", troughcolor="#5f27cd",
                                   bd=4,
                                   font=("Arial", 10, "bold"), highlightcolor="#00d2d3", label="min Damage",
                                   sliderlength=20, activebackground="#f368e0", bg="#8395a7")
        self.min_damage.grid(ipadx=170, padx=10, pady=5)

        self.min_defence = tk.Scale(self.frame_2, from_=0, to=1000, orient=HORIZONTAL, relief="groove",
                                   troughcolor="#5f27cd",
                                   bd=4,
                                   font=("Arial", 10, "bold"), highlightcolor="#00d2d3", label="min Defence",
                                   sliderlength=20, activebackground="#f368e0", bg="#8395a7")
        self.min_defence.grid(ipadx=170, padx=10, pady=5)

        self.min_points = tk.Scale(self.frame_2, from_=0, to=1000, orient=HORIZONTAL, relief="groove",
                                    troughcolor="#5f27cd",
                                    bd=4,
                                    font=("Arial", 10, "bold"), highlightcolor="#00d2d3", label="min Points",
                                    sliderlength=20, activebackground="#f368e0", bg="#8395a7")
        self.min_points.grid(ipadx=170, padx=10, pady=5)


        self.attack_speed_btn = tk.Scale(self.frame_2, from_=0, to=6,
                                         orient=HORIZONTAL, relief="groove",
                                   troughcolor="#5f27cd",
                                   bd=4,
                                   font=("Arial", 10, "bold"), highlightcolor="#00d2d3", label="Attack Speed",
                                   sliderlength=70, activebackground="#f368e0", bg="#8395a7")

        self.attack_speed_btn.grid(ipadx=170, padx=10, pady=5)


        self.save_change = tk.Button(root, text="Save changes",
                             command=self.save_changes, width=200,font=("Arial", 14, "bold"), bd=4,
                             bg="#ff9f43", fg="#222f3e", border=6)
        self.save_change.pack(fill=BOTH, side=BOTTOM, padx=20, pady=20)




        self.frame_2.pack(fill=BOTH)
        self.frame.pack(pady=20, fill=BOTH)

    def on_off(self):
        #print(Check.openFile("config/filter.txt", "r")[0])
        if Check.openFile("config/filter.txt", "r")[0] == "status=off":
            self.on_off_btn['image'] = self.photo
            Check.openFile("config/filter.txt", "w", text="status=on")
            print(f"Filter : {Check.openFile('config/filter.txt', 'r')}")
        else:
            Check.openFile("config/filter.txt", "w", text="status=off")
            self.on_off_btn['image'] = self.photo_2
            print(f"Filter : {Check.openFile('config/filter.txt', 'r')[0]}")

    def save_changes(self):
        #"SUPER_SLOW", "VERY_SLOW", "SLOW", "NORMAL", "FAST", "VERY_FAST", "SUPER_FAST"
        speed_list = [0, 1, 2, 3, 4, 5, 6]
        health = self.min_health.get()
        min_damage = self.min_damage.get()
        min_attack_speed = speed_list[self.attack_speed_btn.get()]
        min_defence = self.min_defence.get()
        min_points = self.min_points.get()

        if Check.openFile("config/filter.txt", "r")[0] == "status=off":
            print("Before you can save you need to enable filters")
        else:
            filter_list = [
                f'status=on\n', f'health={str(health)}\n', f'allDamage={str(min_damage)}\n',
                f'allDefence={str(min_defence)}\n',
                f'allPoints={str(min_points)}\n', f'attackSpeed={str(min_attack_speed)}\n'
            ]

            Check.openFile("config/filter.txt", "w", filter_list)

            print("Changes saved!")
            for appy_filter in filter_list:
                print(appy_filter.replace("\n", ""))