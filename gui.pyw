import os as os
import tkinter as tk
from tkinter import filedialog
from musiqueV2 import *
from tableV2 import main1
from GUI_help import Help
from GUI_clavier import Clavier


class App:
    def __init__(self):
        self.bg = "#ccc"
        self.__root = tk.Tk()
        self.__root.title("Tabs")
        w = 1000
        h = 700
        self.__root.configure(background=self.bg)
        pR = int(self.__root.winfo_screenwidth() / 2 - w/2)
        pD = int(self.__root.winfo_screenheight() / 2 - h/2-50)
        self.__root.geometry("{}x{}+{}+{}".format(w, h, pR, pD))

        try:
            os.mkdir("musiques")
        except:
            pass

        ###################### BEGIN menue ######################
        f_menue = tk.Frame(self.__root, background=self.bg)

        b_import = tk.Button(f_menue, text="Import", command=self.__popup_Import, relief='flat')
        b_add_note = tk.Button(f_menue, text="Add note", command=self.__add_note, relief='flat')
        b_help = tk.Button(f_menue, text="Help", command=self.__Help, relief='flat')

        self.__import_file = tk.StringVar()
        b_import.pack(side=tk.LEFT)
        b_add_note.pack(side=tk.LEFT)
        b_help.pack(side=tk.LEFT)

        f_menue.pack(anchor="w")
        ###################### END menue ######################

        ###################### BEGIN bloc parameter ######################
        f_parameter = tk.LabelFrame(self.__root, background=self.bg, text="Parameters")

        l_accordage = tk.Label(f_parameter, text="Accordage : ", background=self.bg)

        self.__accordage = tk.StringVar()
        e_accordage = tk.Entry(f_parameter, textvariable=self.__accordage, width=10)

        b_accordage = tk.Button(f_parameter, text="Set parameters", command=self.__setParam)

        l_name = tk.Label(f_parameter, text="Name:", bg=self.bg)
        self.__s_name = tk.StringVar()
        e_name = tk.Entry(f_parameter, textvariable=self.__s_name, width=20)

        self.__l_param = tk.Label(f_parameter, text="Set", bg=self.bg)

        l_name.grid(column=0, row=0)
        e_name.grid(column=1, row=0)

        tk.Frame(f_parameter, bg=self.bg, width=50).grid(column=2, row=0)
        l_accordage.grid(column=3, row=0)
        e_accordage.grid(column=4, row=0)
        b_accordage.grid(column=5, row=0, pady=10, padx=10)
        self.__l_param.grid(column=6, row=0, padx=10)
        self.__l_param.grid_remove()

        f_parameter.pack(anchor="w", padx=10, pady=10)
        ###################### END bloc parameter ######################

        ###################### BEGIN bloc chaine accords ######################
        self.__chaine = tk.StringVar()
        f_chaine = tk.LabelFrame(self.__root, background=self.bg)

        b1_chaine = tk.Button(f_chaine, text="use file", command=self.__import_chaine)
        e_chaine = tk.Entry(f_chaine, textvariable=self.__chaine, width=100)
        e_chaine.bind("<space>", self.__updateTab)
        b_chaine = tk.Button(f_chaine, text="Update tab", command=self.__updateTab)
        b_clavier = tk.Button(f_chaine, text="Clavier", command=self.__Clavier)

        self.__l_err_chaine = tk.Label(f_chaine, text="Chaine empty, can not update tab", fg="RED", bg=self.bg)

        b1_chaine.grid(column=0, row=0, pady=10, padx=10)
        e_chaine.grid(column=1, row=0, pady=10, padx=10)
        b_chaine.grid(column=2, row=0, pady=10, padx=10)
        b_clavier.grid(column=3, row=0, pady=10, padx=10)
        self.__l_err_chaine.grid(column=0, row=1, columnspan=3)
        self.__l_err_chaine.grid_remove()

        f_chaine.pack(anchor="w", padx=10, pady=10)
        ###################### END bloc chaine accords ######################

        ###################### BEGIN bloc tablature ######################
        f_tab = tk.Frame(self.__root, background=self.bg)

        tab_yscroll = tk.Scrollbar(f_tab)
        tab_xscroll = tk.Scrollbar(f_tab)
        self.__tab = tk.Text(f_tab, width=100, height=28, wrap="none")

        tab_yscroll.configure(command=self.__tab.yview)
        tab_xscroll.configure(command=self.__tab.xview, orient="horizontal")
        self.__tab.configure(yscrollcommand=tab_yscroll.set, xscrollcommand=tab_xscroll.set)

        tab_yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        tab_xscroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.__tab.pack(side=tk.LEFT, fill=tk.Y)

        f_tab.pack(anchor="w", padx=10)
        ###################### END bloc tablature ######################

        ###################### BEGIN save bloc ######################
        f_save = tk.Frame(self.__root, background=self.bg)

        b_save = tk.Button(f_save, text="Save tab", command=self.__saveTab)
        self.__l_save_error = tk.Label(self.__root, text="the name has to be set before saving", fg="RED", bg=self.bg)

        b_save.grid(column=0, row=0, columnspan=2)
        self.__ok_save = None

        f_save.pack(padx=10, pady=10, side=tk.LEFT)
        self.__l_save_error.pack(anchor="w", side=tk.LEFT)
        self.__l_save_error.pack_forget()
        ###################### END save bloc ######################

        self.__musique = Musique()
        self.__root.mainloop()

    def __popup_Import(self):
        popup = tk.Toplevel()
        popup.title("Import")
        w = 550
        h = 150
        popup.configure(background=self.bg)
        pR = int(popup.winfo_screenwidth() / 2 - w/2)
        pD = int(popup.winfo_screenheight() / 2 - h/2-100)
        popup.geometry("{}x{}+{}+{}".format(w, h, pR, pD))

        ###################### BEGIN importation ######################
        f_import = tk.Frame(popup, background=self.bg)
        f_import1 = tk.Frame(f_import, background=self.bg)

        l1_import = tk.Label(f_import, background=self.bg, text="Import file")

        l2_import = tk.Label(f_import1, text="File", bg=self.bg)
        b1_import = tk.Button(f_import1, text="...", command=self.__browseFiles, width=5)
        e_import = tk.Entry(f_import1, textvariable=self.__import_file, width=50)

        b2_import = tk.Button(f_import, text="Load", command=self.__import)

        l2_import.pack(side=tk.LEFT)
        e_import.pack(side=tk.LEFT, padx=10)
        b1_import.pack(side=tk.LEFT)

        l1_import.pack()
        f_import1.pack()
        b2_import.pack(padx=10)

        f_import.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ###################### END importation ######################
        popup.grab_set()
        self.__root.wait_window(popup)

    def __Help(self):
        Help(self.__root)

    def __Clavier(self):
        Clavier(self.__root, self.__chaine, self.__musique)

    def __setParam(self):
        if self.__s_name.get() != "":
            self.__musique.setAccordage(self.__accordage.get())
            self.__musique.setName(self.__s_name.get())
            self.__l_param.grid()

    def __updateTab(self, event=None):
        self.__l_err_chaine.grid_remove()
        self.__l_save_error.pack_forget()

        if self.__chaine.get() != "":
            self.__l_err_chaine.grid_remove()

            main1(self.__chaine.get() + " end", self.__musique)
            self.__tab.delete(1.0, tk.END)
            self.__tab.insert(tk.END, self.__musique.table_to_str())
        else:
            self.__l_err_chaine.grid()

    def __add_note(self):
        diag = "x x x x x x\n" \
               "-----------\n" \
               "| | | | | |\n" \
               "| | | | | |\n" \
               "| | | | | |\n" \
               "| | | | | |\n" \
               "| | | | | |"

        note = tk.Toplevel(background=self.bg)
        note.title("Add note")
        w = 400
        h = 350
        note.configure(background=self.bg)
        pR = int(note.winfo_screenwidth() / 2 - w/2)
        pD = int(note.winfo_screenheight() / 2 - h/2-100)
        note.geometry("{}x{}+{}+{}".format(w, h, pR, pD))

        f_name = tk.LabelFrame(note, background=self.bg)
        self.v_name = tk.StringVar()
        l_name = tk.Label(f_name, text="Name:", bg=self.bg)
        e_name = tk.Entry(f_name, textvariable=self.v_name)
        self.l_err_note_name = tk.Label(f_name, text="", fg="RED", bg=self.bg)

        l_name.pack(side=tk.LEFT, padx=10, pady=10)
        e_name.pack(side=tk.LEFT, pady=10, padx=10)
        self.l_err_note_name.pack(pady=10)
        f_name.pack(pady=10, padx=10)

        self.t_note = tk.Text(note, width=11, height=10)
        self.t_note.insert(tk.END, diag)
        self.t_note.pack(padx=10, pady=10)

        b_note = tk.Button(note, text="Add", command=self.__read)
        b_note.pack(padx=10, pady=10)

        note.grab_set()
        self.__root.wait_window(note)

    def __read(self):
        if self.v_name.get() == "":
            self.l_err_note_name.configure(text="Name ?")
            return

        self.l_err_note_name.configure(text="")

        diag = self.t_note.get(1.0, tk.END).split("\n")
        cases = diag[0].split(" ")

        doights = []
        for d in range(0, 6):
            doights.append("0")

        for ca in range(2, len(diag)-1):
            cordes = diag[ca].split(" ")

            for co in range(0, len(cordes)):
                if cordes[co] != "|":
                    doights[co] = cordes[co]

        for i in range(0, len(cases)):
            if cases[i] != "0":
                if cases[i].isdigit() and int(doights[i]) != 0:
                    pass
                elif cases[i].isdigit() and int(doights[i]) == 0:
                    self.l_err_note_name.configure(text="Error fret/finger")
                    return

        note = self.v_name.get() + ":" + self.v_name.get() + "|"

        for c in range(0, len(cases)-1):
            note += cases[c]+","
        note += cases[len(cases)-1]+"|"

        for d in doights:
            note += d

        # print(note)
        self.__musique.addNote(Note(note))
        chaine = self.__chaine.get().split(" ")
        if chaine[len(chaine)-1].upper() == "END":
            chaine.insert(len(chaine)-1, self.v_name.get())
        else:
            chaine.append(self.v_name.get())

        new_cahine = ""
        for n in chaine:
            if n.upper() != "END" and n != "":
                new_cahine += n + " "
            elif n.upper() == "END":
                new_cahine += n

        self.__chaine.set(new_cahine)

        f = open("note.txt", "a+")
        f.write("\n"+note)
        f.close()

        k = list(self.__root.children.keys())
        s = self.__root.children.get(k[len(k)-1])
        s.destroy()

    def __saveTab(self):
        if self.__musique.getName() == "":
            self.__l_save_error.configure(text="Name has to be set before saving")
            self.__l_save_error.pack(side=tk.LEFT)
            return

        else:
            self.__l_save_error.grid_remove()
            path = "musiques/"+self.__musique.getName()
            try:
                os.mkdir(path)
            except:
                self.__err_save()
                return

            self.__save()

    def __save(self):
        path = "musiques/"+self.__musique.getName()

        f = open(path+"/{}_tablature.txt".format(self.__musique.getName()), "w")
        f.write(self.__tab.get(1.0, tk.END))
        f.close()

        self.__musique.setPath(path)
        self.__musique.saveDiag()
        self.__musique.saveProject()

        f = open(path+"/{}_chaine.txt".format(self.__musique.getName()), "w")
        f.write(self.__chaine.get())
        f.close()

        f = open(path+"/{}.tab".format(self.__musique.getName()), "w")
        f.write(self.__musique.getName()+"\n")
        f.write(self.__musique.getAccordage()+"\n")
        f.write("/{}_tablature.txt\n".format(self.__musique.getName()))
        f.write("/{}_accords.txt\n".format(self.__musique.getName()))
        f.write("/{}_save.txt\n".format(self.__musique.getName()))
        f.write("/{}_chaine.txt".format(self.__musique.getName()))
        f.close()

    def __err_save(self):
        save = tk.Toplevel()

        save.title("Save")
        w = 500
        h = 150
        save.configure(background=self.bg)
        pR = int(save.winfo_screenwidth() / 2 - w/2)
        pD = int(save.winfo_screenheight() / 2 - h/2-100)
        save.geometry("{}x{}+{}+{}".format(w, h, pR, pD))

        f_save = tk.Frame(save, background=self.bg)
        tk.Label(f_save, text="Musique '{}' already exists, do you want to replace it ?".format(self.__musique.getName()),
                 bg=self.bg).pack()

        f_buttons = tk.Frame(f_save, background=self.bg)
        tk.Button(f_buttons, text="Yes", command=self.__save_yes).pack(side=tk.LEFT)
        tk.Button(f_buttons, text="No", command=save.destroy).pack(side=tk.LEFT)
        f_buttons.pack()

        f_save.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        save.grab_set()

    def __save_yes(self):
        self.__save()
        k = list(self.__root.children.keys())
        s = self.__root.children.get(k[len(k)-1])
        s.destroy()

    def __import(self):
        self.__l_err_chaine.grid_remove()
        self.__l_save_error.pack_forget()

        if self.__import_file.get() != "":
            f = open(self.__import_file.get(), "r")
            files = f.read().split("\n")
            f.close()

            path = os.path.dirname(self.__import_file.get())

            self.__musique.setName(files[0])
            self.__s_name.set(files[0])

            self.__musique.setAccordage(files[1])
            self.__accordage.set(files[1])

            f = open(path+files[2], "r")
            self.__tab.delete(1.0, tk.END)
            self.__tab.insert(tk.END, f.read())
            f.close()

            f = open(path+files[5], "r")
            self.__chaine.set(f.read())
            f.close()

            self.__musique.load(path+files[4])

            self.__import_file.set("")
            self.__setParam()

            k = list(self.__root.children.keys())
            s = self.__root.children.get(k[len(k)-1])
            s.destroy()

    def __import_chaine(self):
        self.__l_err_chaine.grid_remove()
        self.__l_save_error.pack_forget()

        file = ""
        rep = os.path.abspath(os.getcwd())
        filename_s = filedialog.askopenfilename(initialdir=rep,
                                                title="Select a File",
                                                filetypes=(("JPEG files", "*.txt"),
                                                           ("all files", "*.*")))
        if filename_s != "":
            filename = filename_s
        else:
            filename = file
        # Change label contents
        file = filename

        f = open(file, "r")
        self.__chaine.set(f.read())
        f.close()

    def __browseFiles(self):
        rep = os.path.abspath(os.getcwd())
        filename_s = filedialog.askopenfilename(initialdir=rep,
                                                title="Select a File",
                                                filetypes=(("JPEG files", "*.tab"),
                                                           ("all files", "*.*")))
        if filename_s != "":
            filename = filename_s
        else:
            filename = self.__import_file.get()
        # Change label contents
        self.__import_file.set(filename)


if __name__ == '__main__':
    app = App()