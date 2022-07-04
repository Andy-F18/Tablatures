from noteV2 import Note
from musiqueV2 import Musique
import os


def main2():
    musique = Musique()
    musique.load("saves/test.txt")
    musique.displayTable()


def main():
    notes_o = open("notes/note.txt", "r")
    note = "INIT"

    accords = []
    while note != "" and note != "\n":
        note = notes_o.readline()
        if note != "" and note != "\n":
            accords.append(Note(note))

    notes_o = input("chaine : ")
    notes = notes_o.split(" ")

    mu = input("saisir nom musique : ")

    a = input("Saisir accordage : ")

    try:
        os.mkdir("musiques/"+mu)

    except :
        print(mu + " already exits")

    path = "musiques/"+mu

    if a != "" and len(a) == 6:
        musique = Musique(mu, accordage=a, path=path)
    else:
        musique = Musique(mu, path=path)
        a = "EADGBe"

    chaine = open(path+"/chaine_"+mu+".txt", "w")
    chaine.write(a+"\n")
    chaine.write(notes_o)
    chaine.close()

    for n in notes:
        if getAccord(n, accords) is not None:
            musique.addNote(getAccord(n, accords))
        else:
            new = createNote(n)
            if new is not None:
                musique.addNote(new)

    # musique.displayTable()
    # musique.displayDiag()
    musique.saveTable()
    musique.saveDiag()
    musique.saveProject()


def getAccord(name, accord):
    for a in accord:
        if a.getName() == name:
            return a

    return None


def createNote(note, accordage):
    cordes = accordage

    if 2 <= len(note) <= 3 and note.upper() != "LF" and note.upper() != "END":
        for c in cordes:
            if note.find(c, 0) != -1:
                if len(note) == 3:
                    if note[1].isdigit() and note[2].isdigit():
                        nb = cordes.index(c)
                        n = note + ":" + note + "|" + createCase(nb, note[1]+note[2]) + "|" + createDoights(nb)
                        return Note(n)
                elif len(note) == 2:
                    if note[1].isdigit():
                        nb = cordes.index(c)
                        n = note + ":" + note + "|" + createCase(nb, note[1]) + "|" + createDoights(nb)
                        return Note(n)

    elif len(note) > 3 and note.upper() != "LF" and note.upper() != "END":
        cords = []
        c = 1
        while c < len(note):
            corde = "" + note[c-1]
            while c < len(note) and cordes.find(note[c]) < 0:
                corde += note[c]
                c += 1
            c += 1
            cords.append(corde)

        if len(cords) <= 6:
            accord = ["x", "x", "x", "x", "x", "x"]
            for c in cords:
                n = cordes.find(c[0])
                if n != -1:
                    accord[n] = c.replace(c[0], "")

            no = note + ":" + note + "|"
            for a in range(0, len(accord)-1):
                no += accord[a] + ","
            no += accord[len(accord)-1] + "|"
            # print(no)

            maxi = Note.maxi(accord)
            mini = Note.mini(accord)

            doights = ["0", "0", "0", "0", "0", "0"]
            d = [1, 2, 3, 4]
            for ca in range(mini, maxi+1):
                for co in range(0, 6):
                    if accord[co].isdigit():
                        if int(accord[co]) == ca:
                            if len(d) > 0:
                                doights[co] = str(d[0])
                                d.remove(d[0])
                            else:
                                return

            for d in doights:
                no += d

            return Note(no)

    elif note.upper() == "LF" or note.upper() == "END":
        return Note(note + ":" + note + "|" + "x,x,x,x,x,x" + "|" + "000000")

    return None


def createCase(n, c):
    note = ""
    for i in range(0, 5):
        if n == i:
            note += c+","
        else:
            note += "x,"
    i = 5
    if n == i:
        note += c
    else:
        note += "x"

    return note


def createDoights(n):
    doight = ""
    for i in range(0, 6):
        if i == n:
            doight += "1"
        else:
            doight += "0"

    return doight


if __name__ == '__main__':
    main()


def main1(notes, musique):
    notes_o = open("notes/note.txt", "r")
    note = "INIT"

    accords = []
    while note != "" and note != "\n":
        note = notes_o.readline()
        if note != "" and note != "\n":
            accords.append(Note(note))

    notes = notes.split(" ")

    musique.emptyNotes()

    for n in notes:
        if getAccord(n, accords) is not None:
            musique.addNote(getAccord(n, accords))
        else:
            new = createNote(n, musique.getAccordage())
            if new is not None:
                musique.addNote(new)
