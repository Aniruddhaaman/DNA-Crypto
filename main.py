from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from tkinter import *
from tkinter import filedialog
from numpy import average
import pickle
import math
import numpy as np
import random
import itertools
import binascii as ba
from queue import Queue

Window.size = (700, 500)

kv = Builder.load_file('my.kv')


class FirstWindow(Screen):
    def clear(self):
        self.ids.put.text = ''

    # def save(self):
    #     pass
    #
    # def brows(self):
    #     ext = self.ids.put.text
    #     ext = filedialog.askopenfilename(initialdir="", title="Open Text File", filetypes=(("Text Files", "*.txt"),))
    #     ext = open('', 'r')
    #     stuf = ext.read()
    #
    #     self.ids.put.text.insert(END, stuf)
    #     self.ids.put.text.close()

    def encrypt(self):
        A = '00'
        T = '01'
        C = '10'
        G = '11'
        i = 0
        j = 1
        k = 0
        l = 0
        m = 0
        array1 = [[A, A], [A, T], [A, C], [A, G], [T, A], [T, T], [T, C], [T, G], [C, A], [C, T], [C, C], [C, G],
                  [G, A], [G, T], [G, C], [G, G]]
        random.shuffle(array1)
        # print("arraye 1")
        # print(array1)
        y = [] * 8
        z = [] * 8
        while j < len(array1):
            z.append(array1[j])
            j += 2
        # print("Rail fence 2nd list")
        # print(z)
        while i < len(array1):
            y.append(array1[i])
            i += 2
        # print("Rail fence 1st list")
        # print(y)
        array2 = [] * 16
        array2 = y + z
        # print("Rail fence final list")
        # print(array2)
        sep_list = list(itertools.chain(*array2))
        # print("seperated poped element list")
        # print(sep_list)
        a = [] * 8
        p = []
        q = []
        b = []
        d = []
        while l < len(sep_list):
            a = (sep_list[l] + sep_list[l + 1] + sep_list[l + 2] + sep_list[l + 3])
            p.append(a)
            l += 4
        # print(p)
        while m < len(p):
            b = p.pop(m)
            (int(b, 2))
            c = chr(int(b, 2))
            # print(c)
            d.append(c)
        print("Encrypted Key")
        wxyz = "".join(d)
        print(wxyz)
        self.ids.key_put.text = str(wxyz)

        # -=====================================INPUT SCTION======================================
        o = 0
        # n = input('Enter the input from keyboard:\n\t')
        n = self.ids.put.text

        def split(abc):
            return [char for char in abc]

        (split(n))
        w = []
        x = []
        r = 0
        s = 1
        while r < len(n):
            w.append(n[r])
            r += 2
        # print("Rail fence 1nd list")
        # print(w)
        while s < len(n):
            x.append(n[s])
            s += 2
        # print("Rail fence 2st list")
        # print(x)
        array4 = w + x
        # print("Rail Fence Final List")
        # print(array4)
        u = []
        u = ''.join(format(ord(i), '08b') for i in array4)
        # print(u)
        h = 0
        r = []
        t = []
        # print("Array3 after Pairing:")
        while h < len(u):
            r = (u[h] + u[h + 1])
            if r == A:
                t.append(A)
            elif r == T:
                t.append(T)
            elif r == C:
                t.append(C)
            else:
                t.append(G)
            h += 2
        # print(t)
        zy = 0
        ab = []
        ac = []
        ad = []
        while zy < len(t):
            ab = [t[zy], t[zy + 1]]
            ac.append(array2.index(ab))
            zy += 2
        # print("Index position of respective values")
        # print(ac)
        zx = 0
        while zx < len(ac):
            af = ac.pop(zx)
            while af < len(array1):
                ad.append(array1[af])
                break
        # print(ad)
        kl = 0
        km = 0
        cc = []
        cd = []
        ce = []
        while kl < len(ad):
            cc = (ad[kl] + ad[kl + 1])
            while km < len(cc):
                ce.append("".join(cc))
                break
            kl += 2
        # print(ce)
        kn = 0
        cf = []
        array6 = []
        while kn < len(ce):
            array6.append(chr(int((ce.pop(kn)), 2)))
        print("Encrypted Messege")
        print(array6)
        enc = (''.join(array6))
        # with open('*.txt', "w") as out_file:
        #     out_file.write(enc)
        self.ids.put.text = str(enc)


class SecondWindow(Screen):

    def clear(self):
        self.ids.dec.text = ''
        self.ids.key_dec.text = ''

    def decrypt(self):
        A = '00'
        T = '01'
        C = '10'
        G = '11'
        ae = []
        af = []
        ag = []
        zv = 0
        zu = 0
        wxyz = self.ids.key_dec.text
        ae = ''.join(format(ord(zv), '08b') for zv in wxyz)
        print(ae)
        while zu < len(ae):
            af = (ae[zu] + ae[zu + 1])

            if af == A:
                ag.append(A)
            elif af == T:
                ag.append(T)
            elif af == C:
                ag.append(C)
            else:
                ag.append(G)
            zu += 2
        print(ag)
        zt = 0
        ah = []
        ai = []
        while zt < len(ag):
            ah = [ag[zt], ag[zt + 1]]
            ai.append(ah)
            zt += 2
        print("Decrypted Array2")
        print(ai)
        def split_list(a_list):
            half = len(a_list) // 2
            return a_list[:half], a_list[half:]
        aj = []
        ak = []
        zs = 0
        aj, ak = split_list(ai)
        print(aj)
        print(ak)
        al = []
        am = []
        while zs < len(aj):
            al.append(aj.pop(zs))
            al.append(ak.pop(zs))
        print("Decrypted Array1")
        print(al)
        # ===================================INPUT DECRYPTION===========================================
        print("Encrypted Data")
        efgh = self.ids.dec.text
        an = []
        an = ''.join(format(ord(zs), '08b') for zs in efgh)
        print(an)
        zr = 0
        ao = []
        ap = []
        while zr < len(an):
            ao = (an[zr] + an[zr + 1])
            if ao == A:
                ap.append(A)
            elif ao == T:
                ap.append(T)
            elif ao == C:
                ap.append(C)
            else:
                ap.append(G)
            zr += 2
        print(ap)
        aq = []
        zq = 0
        ba = []
        zp = 0
        bb = []
        zo = 0
        bc = []
        while zq < len(ap):
            aq = [ap[zq], ap[zq + 1]]
            ba.append(al.index(aq))
            zq += 2
        print(ba)
        while zp < len(ba):
            bb = ba.pop(zp)
            while zo < len(ai):
                bc.append(ai[bb])
                break
        print(bc)
        zn = 0
        km = 0
        bd = []
        be = []
        while zn < len(bc):
            bd = (bc[zn] + bc[zn + 1])
            while km < len(bd):
                be.append("".join(bd))
                break
            zn += 2
        print(be)
        zl = 0
        cf = []
        array7 = []
        while zl < len(be):
            array7.append(chr(int((be.pop(zl)), 2)))
        print("Encrypted code")
        print(array7)
        def split_list_D(a_list):
            if (len(a_list) % 2) == 0:
                half = len(a_list) // 2
                return a_list[:half], a_list[half:]
            else:
                a_list.append(' ')
                half = len(a_list) // 2
                return a_list[:half], a_list[half:]
        bh = []
        B = []
        C = []
        d = []
        if (len(array7) % 2) == 0:
            B, C = split_list_D(array7)
            print(B)
            print(C)
            zk = 0
            while zk < len(B):
                bh.append(B.pop(zk))
                bh.append(C.pop(zk))
            print("Decrypted Array1")
            print(bh)
            ijk = (''.join(bh))
            self.ids.dec.text = str(ijk)
            self.ids.key_dec.text = ''
        else:
            B, C = split_list_D(array7)
            print(B)
            print(C)
            zk = 0
            while zk < len(B):
                bh.append(B.pop(zk))
                bh.append(C.pop(zk))
            print("Decrypted Array1")
            i = (len(bh) - 1)
            while i < len(bh):
                bh.pop(i)
            print(bh)
            print("Decrypted Messege")
            ijk = ''.join(bh)
            #
            # print(ijk)
            self.ids.dec.text = str(ijk)
            self.ids.key_dec.text = ''


class WindowManager(ScreenManager):
    pass


class RFTApp(App):
    def build(self):
        Window.clearcolor = (240/250,240/250,240/250,240/250)
        return kv


if __name__ == '__main__':
    RFTApp().run()
