import random

fail1 = "kysimused.txt"
fail2 = "oiged.txt" 
fail3 = "valed.txt"
fail4 = "koik.txt"

def loe():
    k = []
    v = []
    
    try:
        f = open(fail1, "r")
        for rida in f:
            if ":" in rida:
                a = rida.split(":")
                k.append(a[0].strip())
                v.append(a[1].strip())
        f.close()
    except:
        f = open(fail1, "w")
        f.write("Mis on Python?:programmeerimiskeel\n")
        f.write("Mis värvi on lumi?:valge\n")
        f.close()
        k = ["Mis on Python?", "Mis värvi on lumi?"]
        v = ["programmeerimiskeel", "valge"]
    
    return k, v

def email(nimi):
    a = nimi.split()
    if len(a) > 1:
        return a[0].lower() + "." + a[1].lower() + "@example.com"
    else:
        return nimi.lower() + "@example.com"

def alusta():
    k, v = loe()
    
    if len(k) < 2:
        print("Vaja rohkem küsimusi")
        return
    
    try:
        mitu_inimest = int(input("Mitu inimest? "))
        mitu_kysimust = int(input("Mitu küsimust? "))
    except:
        print("Viga")
        return
    
    tulemused = []
    
    for x in range(mitu_inimest):
        print("\nInimene", x+1)
        nimi = input("Nimi: ")
        if nimi == "":
            continue
        
        em = email(nimi)
        print("Email:", em)
        
        olemas = False
        try:
            f = open(fail4, "r")
            for rida in f:
                if nimi in rida:
                    olemas = True
            f.close()
        except:
            pass
        
        if olemas:
            print("Juba oli")
            continue
        
        oige = 0
        for y in range(mitu_kysimust):
            nr = random.randint(0, len(k)-1)
            print("Küsimus:", k[nr])
            vastus = input("Vastus: ").lower()
            
            if vastus == v[nr].lower():
                print("Õige")
                oige += 1
            else:
                print("Vale. Õige on:", v[nr])
        
        print(nimi, "sai", oige, "/", mitu_kysimust)
        
        if oige > mitu_kysimust / 2:
            print("Läbis")
            eduka = True
        else:
            print("Ei läbinud")
            eduka = False
        
        print("Email:", em)
        print("Tere", nimi)
        print("Sul on", oige, "õiget")
        if eduka:
            print("Oled edukas")
        else:
            print("Ei ole edukas")
        
        tulemused.append([nimi, oige, em, eduka])
    
    if tulemused:
        salvesta(tulemused)
        nayta(tulemused)

def salvesta(t):
    o = []
    for x in t:
        if x[3]:
            o.append([x[0], x[1]])
    
    for i in range(len(o)):
        for j in range(i+1, len(o)):
            if o[i][1] < o[j][1]:
                o[i], o[j] = o[j], o[i]
    
    f = open(fail2, "w")
    for x in o:
        f.write(x[0] + " - " + str(x[1]) + " õigesti\n")
    f.close()
    
    v = []
    for x in t:
        if not x[3]:
            v.append([x[0], x[1]])
    
    for i in range(len(v)):
        for j in range(i+1, len(v)):
            if v[i][0] > v[j][0]:
                v[i], v[j] = v[j], v[i]
    
    f = open(fail3, "w")
    for x in v:
        f.write(x[0] + " - " + str(x[1]) + " õigesti\n")
    f.close()
    
    f = open(fail4, "a")
    for x in t:
        f.write(x[0] + "," + str(x[1]) + "," + x[2] + "\n")
    f.close()
    
    print("Salvestatud")

def nayta(t):
    print("\nEdukad:")
    for x in t:
        if x[3]:
            print(x[0], x[1], "õigesti")
    
    print("\nAruanne:")
    print("tootaja@firma.ee")
    
    for i in range(len(t)):
        x = t[i]
        if x[3]:
            s = "SOBIS"
        else:
            s = "EI SOBINUD"
        print(i+1, ".", x[0], "-", x[1], "-", x[2], "-", s)
    
    if t:
        parim = t[0]
        for x in t:
            if x[1] > parim[1]:
                parim = x
        print("Parim:", parim[0], "(", parim[1], ")")
    
    print("Emailid saadetud")

def lisa():
    k = input("Küsimus: ")
    v = input("Vastus: ")
    
    f = open(fail1, "a")
    f.write("\n" + k + ":" + v)
    f.close()
    
    print("Lisatud")
