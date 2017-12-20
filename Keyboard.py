#!/usr/bin/python3
# -*- coding:utf-8 -*-

import os

"Letiltando program neve alatta a xinput alapertelmeyet szoftver segitsegul hivasa es stringe alakitasa."
letiltando = "AT Translated Set 2 keyboard"
lista = os.popen("xinput list")
a = lista.read()

"Megkapott listabol kiszelektalom a felesleget"
listam = [f for f in a if f != "↳" and f != "\t" and f != "⎡" and f != "⎜" and f != "⎣" and f != " " and f != "\n"]
szoveg ="".join(listam)

"A letiltando nevu eszkoz neve csak kivettem belole a szokozoket"
listam2 = [k for k in letiltando if k != " "]
kereses = "".join(listam2)

"Letiltandot megkeresem a listaban es visszakapom a szoveg kezdetenek a helyet."
omega = szoveg.index(kereses)

"Megkeresem az id-t ami alapjan le tudom tiltani ay eszkozt."
listam3 = []
if szoveg[omega+len(kereses)] == "i" and szoveg[omega+len(kereses)+1] == "d" and szoveg[omega+len(kereses)+2] == "=":
    if szoveg[omega+len(kereses)+4] != "[":
        listam3.append(szoveg[omega+len(kereses)+3])
        listam3.append(szoveg[omega+len(kereses)+4])
    if szoveg[omega+len(kereses)+5] != "[":
        listam3.append(szoveg[omega+len(kereses)+3])
        listam3.append(szoveg[omega+len(kereses)+4])
        listam3.append(szoveg[omega+len(kereses)+5])


"Atalakitom a stringet int-e."
tilt = "".join(listam3)
nyeremeny = int(tilt)

os.system("xinput float {}".format(nyeremeny))
