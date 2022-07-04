from noteV2 import Note


class Musique:

    def __init__(self, name="", accordage="EADGBe", path="musiques"):
        self.__E = []
        self.__A = []
        self.__D = []
        self.__G = []
        self.__B = []
        self.__e = []

        self.__name = name

        self.__accords = []

        self.__accordage = accordage

        self.__path = path

    def addNote(self, n):
        if isinstance(n, Note):
            self.__E.append(n.get__E())
            self.__A.append(n.get__A())
            self.__D.append(n.get__D())
            self.__G.append(n.get__G())
            self.__B.append(n.get__B())
            self.__e.append(n.get__e())

            self.__accords.append(n)
        else:
            print("Type error")

    @staticmethod
    def table(n, a):
        if n == "x":
            lm=0
            for c in a.getCases():
                if len(c)>lm:
                    lm = len(c)

            out = ""
            for i in range(0, lm):
                out += "-"
            return out
        elif len(n) == 1 and n != "x":
            lm=0
            for c in a.getCases():
                if len(c)>lm:
                    lm = len(c)

            out = n
            for i in range(1, lm):
                out += "-"
            return out

        else:
            return n

    @staticmethod
    def maxi(accord):
        maxi = 0
        for c in accord:
            if c != "x" and c != "0":
                if int(c) > maxi:
                    maxi = int(c)

        return maxi

    def setAccordage(self, accordage):
        if isinstance(accordage, str):
            if len(accordage) == 6:
                self.__accordage = accordage
                return
            elif accordage == "":
                self.__accordage = "EADGBe"
                return

        print("Erreur dans l'accordage")

    def getAccordage(self):
        return self.__accordage

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setPath(self, path):
        self.__path = path

    def emptyNotes(self):
        self.__E = []
        self.__A = []
        self.__D = []
        self.__G = []
        self.__B = []
        self.__e = []

        self.__accords =[]

    def displayTable(self):
        n = 0

        while n == 0 or self.__accords[n - 1].getName().upper() != "END":

            E = self.__accordage[0] + "||"
            A = self.__accordage[1] + "||"
            D = self.__accordage[2] + "||"
            G = self.__accordage[3] + "||"
            B = self.__accordage[4] + "||"
            e = self.__accordage[5] + "||"

            while self.__accords[n].getName().upper() != "END" and self.__accords[n].getName().upper() != "LF":
                E += self.table(self.__E[n], self.__accords[n])
                A += self.table(self.__A[n], self.__accords[n])
                D += self.table(self.__D[n], self.__accords[n])
                G += self.table(self.__G[n], self.__accords[n])
                B += self.table(self.__B[n], self.__accords[n])
                e += self.table(self.__e[n], self.__accords[n])
                n += 1

            print(e)
            print(B)
            print(G)
            print(D)
            print(A)
            print(E + "\n\n")
            n += 1

    def displayDiag(self):
        mu = ""
        for a in self.__accords:
            accord = ""
            accord += "    [{}]\n".format(a.getName())
            for c in a.getCases():
                accord += c + " "
            accord += "\n-----------\n"

            t = self.maxi(a.getCases())

            if a.getName() != "x" and a.getName.upper() != "LF" and a.getName().upper() != "END":
                mu += a.diagrame_str() + "\n\n"

        print(mu)

    def saveTable(self):
        file = self.__path + "/" + self.__name + "_tablature.txt"
        mu = open(file, "w")

        mu.write("Name : " + self.__name + "\n----------\n\n")

        n = 0

        while n == 0 or self.__accords[n - 1].getName().upper() != "END":
            E = self.__accordage[0] + "||"
            A = self.__accordage[1] + "||"
            D = self.__accordage[2] + "||"
            G = self.__accordage[3] + "||"
            B = self.__accordage[4] + "||"
            e = self.__accordage[5] + "||"

            while self.__accords[n].getName().upper() != "END" and self.__accords[n].getName().upper() != "LF":
                E += self.table(self.__E[n], self.__accords[n])
                A += self.table(self.__A[n], self.__accords[n])
                D += self.table(self.__D[n], self.__accords[n])
                G += self.table(self.__G[n], self.__accords[n])
                B += self.table(self.__B[n], self.__accords[n])
                e += self.table(self.__e[n], self.__accords[n])
                n += 1

            mu.write(e + "\n")
            mu.write(B + "\n")
            mu.write(G + "\n")
            mu.write(D + "\n")
            mu.write(A + "\n")
            mu.write(E + "\n\n")
            n += 1

        mu.close()

    def saveDiag(self):
        file = self.__path + "/" + self.__name + "_accords.txt"
        mus = open(file, "w")

        mu = "Name : " + self.__name + "\n-----------\n\n"
        for a in self.__accords:
            accord = ""
            accord += "    [{}]\n".format(a.getName())
            for c in a.getCases():
                accord += c + " "
            accord += "\n-----------\n"

            t = self.maxi(a.getCases())

            if a.getName() != "x" and a.getName().upper() != "LF" and a.getName().upper() != "END":
                mu += a.diagrame_str() + "\n\n"

        mus.write(mu)
        mus.close()

    def saveProject(self):
        file = self.__path + "/" + self.__name + "_save.txt"
        mu = open(file, "w")

        for a in self.__accords:
            mu.write(a.save() + "\n")

        mu.close()

    def table_to_str(self):
        mu = ""
        n = 0

        while n == 0 or self.__accords[n - 1].getName().upper() != "END":
            E = self.__accordage[0] + "||"
            A = self.__accordage[1] + "||"
            D = self.__accordage[2] + "||"
            G = self.__accordage[3] + "||"
            B = self.__accordage[4] + "||"
            e = self.__accordage[5] + "||"

            while self.__accords[n].getName().upper() != "END" and self.__accords[n].getName().upper() != "LF":
                E += self.table(self.__E[n], self.__accords[n])
                A += self.table(self.__A[n], self.__accords[n])
                D += self.table(self.__D[n], self.__accords[n])
                G += self.table(self.__G[n], self.__accords[n])
                B += self.table(self.__B[n], self.__accords[n])
                e += self.table(self.__e[n], self.__accords[n])
                n += 1

            mu += e + "\n"
            mu += B + "\n"
            mu += G + "\n"
            mu += D + "\n"
            mu += A + "\n"
            mu += E + "\n\n"
            n += 1

        return mu

    def load(self, file):
        mu = open(file, "r")

        note = "INIT"

        self.__name = file

        while note != "" and note != "\n":
            note = mu.readline()
            if note != "" and note != "\n":
                self.addNote(Note(note))

        mu.close()
