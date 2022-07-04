import tkinter as tk
from tkinter import ttk
from musiqueV2 import Musique
from GUI_help import Help
from noteV2 import Note
from tableV2 import createNote


class Clavier:
    def __init__(self, root, chaine, musique):
        self.musique = musique
        self.select = None

        self.chaine = chaine
        ch = "> " + chaine.get().replace("lf ", "\n> ").replace("end  ", "").replace("end", "")
        self.root = root
        self.clavier = tk.Toplevel(self.root)
        self.clavier.title("Clavier")
        self.bg = "#ccc"
        w = 1000
        h = 700
        self.clavier.configure(background=self.bg)
        pR = int(self.clavier.winfo_screenwidth() / 2 - w / 2)
        pD = int(self.clavier.winfo_screenheight() / 2 - h / 2 - 50)
        self.clavier.geometry("{}x{}+{}+{}".format(w, h, pR, pD))

        ###################### BEGIN menue ######################
        f_menue = tk.Frame(self.clavier)
        b_help = tk.Button(f_menue, text="Help", command=lambda: Help(self.clavier), relief='flat')
        self.simple_mode = tk.BooleanVar()
        self.simple_mode.set(True)
        self.c_simple = tk.Checkbutton(f_menue, text="Simple", variable=self.simple_mode, command=self.color_simple)
        self.color_simple()
        self.c_simple.pack(side=tk.LEFT)
        b_help.pack(side=tk.LEFT)
        f_menue.pack(anchor="w")
        ###################### END menue ######################

        ###################### BEGIN screen ######################
        f_screen = tk.LabelFrame(self.clavier)
        screen_yscroll = tk.Scrollbar(f_screen)
        screen_xscroll = tk.Scrollbar(f_screen)
        self.t_screen = tk.Text(f_screen, width=115, height=20, wrap="none")
        screen_yscroll.configure(command=self.t_screen.yview)
        screen_xscroll.configure(command=self.t_screen.xview, orient="horizontal")
        screen_yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        screen_xscroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.t_screen.pack(pady=10, side=tk.LEFT)
        self.t_screen.insert(tk.END, ch)
        self.t_screen.configure(state=tk.DISABLED, yscrollcommand=screen_yscroll.set)
        self.t_screen.configure(state=tk.DISABLED, xscrollcommand=screen_xscroll.set)
        f_screen.pack()
        ###################### END screen ######################

        ###################### BEGIN clavier ######################
        f_clavier = tk.Frame(self.clavier, bg=self.bg)
        self.f_clavier_note = tk.Frame(f_clavier, bg="#888")
        self.f_clavier_tools = tk.Frame(f_clavier)

        self.stack_notes = []
        self.combo = ttk.Combobox
        self.cases = []
        self.entries_cases = []

        self.w = 17
        self.h = 4

        self.buttons_notes()
        self.buttons_tools()

        self.f_clavier_note.grid(column=0, row=0, columnspan=6)
        self.f_clavier_tools.grid(column=6, row=0, columnspan=2)
        f_clavier.pack(fill=tk.Y)
        ###################### END clavier ######################
        self.clavier.grab_set()
        self.root.wait_window(self.clavier)

    def color_simple(self):
        if self.simple_mode.get():
            self.c_simple.configure(bg="#9f9")
        else:
            self.c_simple.configure(bg="#f99")

    def buttons_notes(self):
        frame = self.f_clavier_note
        bs = ["C", "Cm", "C#", "D", "Dm", "D#",
              "E", "Em", "E7", "F", "Fm", "F#",
              "G", "Gm", "G#", "A", "Am", "A#",
              "B", "Bm", "B7", "x", "0", "OK"]

        w = self.w
        h = self.h
        div = 6

        for b in bs:
            n = bs.index(b)
            if b != "OK":
                tk.Button(frame, text=b, width=w, height=h, command=lambda i=n: self.note(bs[i])).grid(column=n % div,
                                                                                                       row=int(n / div))
            elif b == "OK":
                tk.Button(frame, text=b, width=w, height=h, bg="#999", command=lambda: self.ok()).grid(
                    column=n % div,
                    row=int(n / div))

    def buttons_tools(self):
        frame = self.f_clavier_tools
        w = self.w
        h = self.h

        r = 2.5
        b_tools = ["Effets", "Perso", "\u2936", "<---"]
        for b in b_tools:
            n = b_tools.index(b)
            tk.Button(frame, text=b, width=int(w * r), height=h, bg="#999",
                      command=lambda bs=b: self.tools(bs)).grid(column=0, row=n)

    def note(self, n):
        if self.simple_mode.get() or n == "x" or n == "0":
            self.t_screen.configure(state=tk.NORMAL)
            text = self.t_screen
            text.insert(tk.END, n + " ")
            self.t_screen.configure(state=tk.DISABLED)
            # print("Simple")
        else:
            self.mode_Normal(n)
            # print("Normal")

    def mode_Normal(self, n):
        ns = n
        path = "notes/{}.txt".format(n)
        f = open(path, "r")
        catalogue = f.read().split("\n")
        catalogue.append("OK")
        # n = int(len(catalogue)/4)

        win = tk.Toplevel(self.clavier)
        win.title(ns)
        w = 400
        h = 300
        win.configure(background=self.bg)
        pR = int(win.winfo_screenwidth() / 2 - w / 2)
        pD = int(win.winfo_screenheight() / 2 - h / 2 - 50)
        win.geometry("{}x{}+{}+{}".format(w, h, pR, pD))

        self.select = Note("x:x|x,x,x,x,x,x|000000")

        f_notes = tk.Frame(win, bg=self.bg)
        f_touches = tk.LabelFrame(f_notes, text="Notes", bg=self.bg)
        t_accord = tk.Text(f_notes, width=15, height=10, state=tk.DISABLED)

        t_w = 7
        t_h = 1
        div = 3
        bs = []
        bs.clear()
        for c in catalogue:
            n = catalogue.index(c)
            if c != "OK":
                no = Note(c)
                bs.append(tk.Button(f_touches, text=no.getName(), width=t_w, height=t_h))
                bs[n].configure(command=lambda note=no: self.mode_Normal_note(note, t_accord))
                bs[n].grid(column=n % div, row=int(n / div))
            else:
                bs.append(tk.Button(f_touches, text=c, width=t_w, height=t_h))
                bs[n].configure(command=self.note_ok)
                bs[n].grid(column=n % div, row=int(n / div))

        f_touches.grid(column=0, row=0)
        t_accord.grid(column=1, row=0)
        f_notes.pack(padx=10, pady=10)
        win.grab_set()
        self.clavier.wait_window(win)

    def mode_Normal_note(self, note, text):
        text.configure(state=tk.NORMAL)
        text.replace(1.0, tk.END, note.diagrame_str())
        text.configure(state=tk.DISABLED)
        self.select = note

    def note_ok(self):
        n = self.select
        self.t_screen.configure(state=tk.NORMAL)
        self.t_screen.insert(tk.END, n.getName() + " ")
        self.t_screen.configure(state=tk.DISABLED)

        k = list(self.clavier.children.keys())
        s = self.clavier.children.get(k[len(k) - 1])
        s.destroy()

    def tools(self, t):
        text = self.t_screen
        if t == "<---":
            txt = text.get(1.0, tk.END).split(" ")
            if len(txt) > 2:
                n = len(txt)
                self.t_screen.configure(state=tk.NORMAL)
                text.delete(1.0, tk.END)
                for n in range(0, n - 2):
                    text.insert(tk.END, txt[n] + " ")
                self.t_screen.configure(state=tk.DISABLED)

        elif t == "\u2936":
            self.t_screen.configure(state=tk.NORMAL)
            text.insert(tk.END, "\n> ")
            self.t_screen.configure(state=tk.DISABLED)

        elif t == "Perso":
            self.note_perso()

    def note_perso(self):
        note = tk.Toplevel(self.clavier)
        note.title("Note perso")
        w = 400
        h = 200
        note.configure(background=self.bg)
        pR = int(note.winfo_screenwidth() / 2 - w / 2)
        pD = int(note.winfo_screenheight() / 2 - h / 2 - 50)
        note.geometry("{}x{}+{}+{}".format(w, h, pR, pD))

        accordage = self.musique.getAccordage()

        if accordage == "":
            accordage = "EADGBe"

        main = tk.LabelFrame(note, bg=self.bg)

        tk.Frame(main, bg=self.bg).grid(column=0, row=0)
        for a in range(0, len(accordage)):
            tk.Label(main, text=accordage[a], bg=self.bg).grid(column=a + 1, row=0)

        self.cases = []
        self.entries_cases = []
        tk.Label(main, text="Cases: ", bg=self.bg).grid(column=0, row=1)
        for c in range(0, len(accordage)):
            self.cases.append(tk.StringVar())
            self.entries_cases.append(tk.Entry(main, width=2, textvariable=self.cases[c]))
            self.entries_cases[c].grid(column=c + 1, row=1, padx=3)

        err = tk.Label(note, text="", bg=self.bg)
        err.pack(pady=10)
        main.pack()
        self.combo = ttk.Combobox(note, values=self.stack_notes)
        self.combo.bind("<<ComboboxSelected>>", self.boxChange)
        self.combo.pack()
        tk.Button(note, text="OK", width=10,
                  command=lambda: self.valide_note_perso(accordage, err, self.combo)).pack()

    def valide_note_perso(self, accordage, err, combo):
        n = 0
        note = ""
        err.configure(text="")
        for c in self.cases:
            if c.get().isdigit():
                if 0 <= int(c.get()) <= 24:
                    note += accordage[n] + c.get()
                else:
                    err.configure(text="cases should be 0<= c <= 24", fg="RED")
                    return

            n += 1

        if note == "":
            note = "x"
        # print(note)
        self.t_screen.configure(state=tk.NORMAL)
        self.t_screen.insert(tk.END, note + " ")
        self.t_screen.configure(state=tk.DISABLED)

        if not self.exists(note):
            self.stack_notes.append(note)

        combo.config(values=self.stack_notes)
        # print(self.stack_notes)

    def exists(self, note):
        if len(self.stack_notes) == 0:
            return False

        else:
            for n in self.stack_notes:
                if n == note:
                    return True

            return False

    def boxChange(self, event):
        note = createNote(self.combo.get(), self.musique.getAccordage()).getCases()
        i = 0
        for n in note:
            self.entries_cases[i].delete(0, tk.END)
            if n != "x":
                self.entries_cases[i].insert(tk.END, n)

            i += 1

    def ok(self):
        text = self.t_screen.get(1.0, tk.END).replace("\n", "lf ").replace("> ", "").split(" ")
        text[len(text) - 2] = "end"

        chaine = ""
        for n in text:
            chaine += n + " "

        chaine = chaine.replace("end", "").replace("  ", "")
        self.chaine.set(chaine)

        k = list(self.root.children.keys())
        s = self.root.children.get(k[len(k) - 1])
        s.destroy()
