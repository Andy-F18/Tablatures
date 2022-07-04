import tkinter as tk
from musiqueV2 import *


class Help:
    def __init__(self, master):
        self.bg = "#ccc"
        self.bg_default = "#eee"

        self.__tk_help = tk.Toplevel(master)
        self.__tk_help.title("Help")
        w = 1000
        h = 700
        self.__tk_help.configure(background=self.bg)
        pR = int(self.__tk_help.winfo_screenwidth() / 2 - w/2+50)
        pD = int(self.__tk_help.winfo_screenheight() / 2 - h/2-50)
        self.__tk_help.geometry("{}x{}+{}+{}".format(w, h, pR, pD))

        ###################### BEGIN menu ######################
        f_menu = tk.Frame(self.__tk_help, background="#ccf")

        self.b_syntax = tk.Button(f_menu, text="Syntax", command=self.__h_syntax, relief='flat', bg=self.bg)
        self.b_notes = tk.Button(f_menu, text="Notes", command=self.__h_note, relief='flat')

        self.b_syntax.pack(side=tk.LEFT)
        self.b_notes.pack(side=tk.LEFT)

        self.l_help = tk.Label(self.__tk_help, text="HELP syntax", bg=self.bg)

        f_menu.pack(anchor="w")
        self.l_help.pack()
        ###################### END menu ######################

        ###################### BEGIN help ######################
        f_help = tk.LabelFrame(self.__tk_help, background=self.bg)

        self.t_help = tk.Text(f_help, width=100, height=30)
        screen_yscroll = tk.Scrollbar(f_help)
        screen_yscroll.configure(command=self.t_help.yview)

        self.t_help.pack(side=tk.LEFT, pady=10)
        screen_yscroll.pack(side=tk.LEFT, fill=tk.Y)
        self.t_help.insert(tk.END, "help syntax")
        self.t_help.configure(state=tk.DISABLED, yscrollcommand=screen_yscroll.set)

        f_help.pack()
        ###################### END help ######################

        self.__tk_help.mainloop()

    def __h_syntax(self):
        self.l_help.configure(text="HELP syntax")
        self.b_syntax.configure(bg=self.bg)
        self.b_notes.configure(bg=self.bg_default)

        self.t_help.configure(state=tk.NORMAL)
        self.t_help.replace(1.0, tk.END, "Syntax Help")
        self.t_help.configure(state=tk.DISABLED)

    def __h_note(self):
        self.l_help.configure(text="HELP note")
        self.b_notes.configure(bg=self.bg)
        self.b_syntax.configure(bg=self.bg_default)

        f = open("notes/note.txt", "r")
        notes = f.read().split("\n")
        f.close()

        # print(Note(notes[0]).diagram_str())

        h = ""
        for n in range(0, int(len(notes)/4)):
            line = ""
            n1 = Note(notes[n*4]).diagrame_str().split("\n")
            n2 = Note(notes[n*4+1]).diagrame_str().split("\n")
            n3 = Note(notes[n*4+2]).diagrame_str().split("\n")
            n4 = Note(notes[n*4+3]).diagrame_str().split("\n")

            for c in range(0, len(n1)-1):
                line += n1[c] + "\t\t\t" + n2[c] + "\t\t\t" + n3[c] + "\t\t\t" + n4[c] + "\n"

            h += line + "\n\n\n"

        if len(notes) % 4 == 1:
            n1 = Note(notes[len(notes)-1]).diagrame_str()
            h += n1 + "\n\n\n"

        elif len(notes) % 4 == 2:
            line = ""
            n1 = Note(notes[len(notes)-2]).diagrame_str().split("\n")
            n2 = Note(notes[len(notes)-1]).diagrame_str().split("\n")

            for c in range(0, len(n1)-1):
                line += n1[c] + "\t\t\t" + n2[c] + "\n"

            h += line + "\n\n\n"

        elif len(notes) % 4 == 3:
            line = ""
            n1 = Note(notes[len(notes)-3]).diagrame_str().split("\n")
            n2 = Note(notes[len(notes)-2]).diagrame_str().split("\n")
            n3 = Note(notes[len(notes)-1]).diagrame_str().split("\n")

            for c in range(0, len(n1)-1):
                line += n1[c] + "\t\t\t" + n2[c] + "\t\t\t" + n3[c] + "\n"

            h += line + "\n\n\n"

        self.t_help.configure(state=tk.NORMAL)
        self.t_help.replace(1.0, tk.END, h)
        self.t_help.configure(state=tk.DISABLED)
