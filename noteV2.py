class Note:
    def __init__(self, note):
        note = list(note.split("|"))
        cases = note[1]
        doights = note[2].split("\n")[0]
        name = list(note[0].split(":"))

        self.__cases = cases.split(",")
        self.__doights = doights

        self.__nameL = name[0]
        self.__name = name[1]

    def get__E(self):
        return self.__cases[0]

    def get__A(self):
        return self.__cases[1]

    def get__D(self):
        return self.__cases[2]

    def get__G(self):
        return self.__cases[3]

    def get__B(self):
        return self.__cases[4]

    def get__e(self):
        return self.__cases[5]

    def get__D_E(self):
        return self.__doights[0]

    def get__D_A(self):
        return self.__doights[1]

    def get__D_D(self):
        return self.__doights[2]

    def get__D_G(self):
        return self.__doights[3]

    def get__D_B(self):
        return self.__doights[4]

    def get__D_e(self):
        return self.__doights[5]

    def getCases(self):
        return self.__cases

    def getDoights(self):
        return self.__doights

    def getNameL(self):
        return self.__nameL

    def getName(self):
        return self.__name

    def __casesStr(self):
        s = ""
        for c in range(0, 5):
            s += self.__cases[c]+","
        s += self.__cases[5]

        return s

    @staticmethod
    def maxi(accord):
        maxi = 0
        for c in accord:
            if c != "x" and c != "0":
                if int(c) > maxi:
                    maxi = int(c)

        return maxi

    @staticmethod
    def mini(accord):
        min = 999
        for c in accord:
            if c != "x" and c != "0":
                if int(c) < min:
                    min = int(c)

        return min

    def diagrame_str(self):
        diag = "[{}]\n".format(self.__name)

        for c in range(0, 5):
            if len(self.__cases[c]) == 1:
                diag += self.__cases[c]+" "
            else:
                diag += self.__cases[c]

        diag += self.__cases[len(self.__cases)-1] + "\n"
        diag += "-----------\n"

        max = self.maxi(self.__cases)
        min = self.mini(self.__cases)
        for ca in range(min, min+5):
            case = ""
            for co in range(0, 6):
                if self.__cases[co] != "x" and self.__cases[co] != "0":
                    if int(self.__cases[co]) == ca:
                        case += self.__doights[co] + " "

                    else:
                        case += "| "
                else:
                    case += "| "

            if ca == min:
                if min > 100:
                    diag += case + ":x\n"
                else:
                    diag += case + ":" + str(min) + "\n"
            else:
                diag += case + "\n"

        return diag

    def save(self):
        return self.__nameL + ":" + self.__name + "|" + self.__casesStr() + "|" + self.__doights

    def __str__(self):
        return "note:[" + self.__nameL + "/"+self.__name + ";\tcases:" + str(self.__cases) + ";\tdoights="+self.__doights+"]"