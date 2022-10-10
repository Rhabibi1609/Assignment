import tkinter as tk
import os
from tkinter import filedialog

listex = []

class ext_slice:

    def __init__(self, fpath):
        self.fpath = fpath

    def cutter(self):
        for fe in fpath:
            print(fe)
            ext = os.path.splitext(fe)[-1].lower()
            listex.append(ext)
            print(ext)


        return listex

    def check(self,cont):
        ext = cont
        if ext == ".pdf":
            return True
        elif ext == ".json":
            return True
        else:
            return False

    def check_name(self,cont):
        if cont == ".pdf":
            print("is an pdf!")
        elif cont == ".json":
            print("is a JSON!")
        else:
            print("is an unknown file format.")



select = tk.Tk()
select.withdraw()

fpath = filedialog.askopenfilenames()
print(fpath)
print("\n\n")
if len(fpath)<3:
    for i in range(len(fpath)):
            obj = ext_slice(fpath[i])
            cont=obj.cutter()
            obj.check_name(cont[i])
            if obj.check(cont[i]) == True:
                os.system(fpath[i])
            else:
                print("not correct ext")
else:
    print("Atmost 2 can be opened")



