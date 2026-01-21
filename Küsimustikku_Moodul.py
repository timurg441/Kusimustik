import random

fail_kusimused = "kusimused_vastused.txt"
fail_oiged = "oiged.txt"
fail_valed = "valed.txt"
fail_koik = "koik.txt"

kusimused_list = []
vastused_list = []

def andmete_lugemine_failidest():
    global kusimused_list, vastused_list
    
    try:
        fail = open(fail_kusimused, "r", encoding="utf-8")
        
        for rida in fail:
            rida = rida.strip()
            
            if rida and ":" in rida:
                osad = rida.split(":", 1)
                kusimus = osad[0].strip()
                vastus = osad[1].strip()
                
                kusimused_list.append(kusimus)
                vastused_list.append(vastus)
        
        fail.close()
        
        if len(kusimused_list) == 0:
            print("Fail oli tühi. Lisasin näidisküsimused.")
            
            kusimused_list.append("Mis on Python?")
            vastused_list.append("programmeerimiskeel")
            
            kusimused_list.append("Mis värvi on lumi?")
            vastused_list.append("valge")
            
            kusimused_list.append("Mitu päeva on nädalas?")
            vastused_list.append("7")
            
            andmete_salvestamine_failidesse_kusimused()
        
        print(f"Laeti {len(kusimused_list)} küsimust")
        return True
        
    except:
        print("Faili ei leitud. Loon uue faili.")
        
        kusimused_list.append("Mis on Python?")
        vastused_list.append("programmeerimiskeel")
        
        kusimused_list.append("Mis värvi on lumi?")
        vastused_list.append("valge")
        
        kusimused_list.append("Mitu päeva on nädalas?")
        vastused_list.append("7")
        
        andmete_salvestamine_failidesse_kusimused()
        
        return True

def andmete_salvestamine_failidesse_kusimused():
    try:
        fail = open(fail_kusimused, "w", encoding="utf-8")
        
        for i in range(len(kusimused_list)):
            fail.write(f"{kusimused_list[i]}:{vastused_list[i]}\n")
        
        fail.close()
        print(f"Küsimused salvestati faili {fail_kusimused}")
        
    except:
        print("Viga küsimuste salvestamisel")

def andmete_salvestamine_failidesse():
    pass

def kysi_ymhe_inimese_jaoks(nimi, kusimuste_arv):
    """Küsib küsimusi ühe inimese jaoks"""
    print(f"\n--- Küsimused {nimi} jaoks ---")
    
    if kusimuste_arv > len(kusimused_list):
        kusimuste_arv = len(kusimused_list)
        print(f"Küsin kõik {kusimuste_arv} küsimust")
    
    valitud_indeksid = []
    
    kusimused_kokku = len(kusimused_list)
    for _ in range(kusimuste_arv):
        indeks = random.randint(0, kusimused_kokku - 1)
        while indeks in valitud_indeksid:
            indeks = random.randint(0, kusimused_kokku - 1)
        valitud_indeksid.append(indeks)
    
    oigete_arv = 0
    
    for i in range(kusimuste_arv):
        indeks = valitud_indeksid[i]
        
        print(f"\nKüsimus {i+1}: {kusimused_list[indeks]}")
        vastus = input("Sinu vastus: ").strip().lower()
        
        oige_vastus = vastused_list[indeks].lower()
        if vastus == oige_vastus:
            print("Õige!")
            oigete_arv += 1
        else:
            print(f"Vale. Õige vastus: {vastused_list[indeks]}")
    
    return oigete_arv

def testimine():
    andmete_lugemine_failidest()
    
    print("\n=== ALUSTAME TESTIMIST ===")
    
    try:
        inimeste_arv = int(input("Mitu inimest testime? "))
    except:
        print("Viga! Sisesta number.")
        return
    
    try:
        kusimuste_arv = int(input("Mitu küsimust igale inimesele? "))
    except:
        print("Viga! Sisesta number.")
        return
    
    testitud = []
    tulemused = []
    
    for i in range(inimeste_arv):
        print(f"\n=== INIMENE {i+1}/{inimeste_arv} ===")
        
        nimi = input("Sisesta nimi: ").strip()
        
        if not nimi:
            print("Nimi ei tohi olla tühi!")
            continue
        
        if nimi in testitud:
            print(f"{nimi} on juba testitud!")
            continue
        
        testitud.append(nimi)
        
        oigete_arv = kysi_ymhe_inimese_jaoks(nimi, kusimuste_arv)
        
        edukas = oigete_arv > kusimuste_arv / 2
        
        email = nimi.lower().replace(" ", ".") + "@example.com"
        
        tulemus = {
            "nimi": nimi,
            "oigete_arv": oigete_arv,
            "email": email,
            "edukas": edukas
        }
        tulemused.append(tulemus)
        
        print(f"\n{nimi}, sa said {oigete_arv}/{kusimuste_arv} õigesti!")
        if edukas:
            print("Palju õnne! Test edukas.")
        else:
            print("Test ei olnud edukas.")
    
    salvesta_tulemused_failidesse(tulemused)
    
    saada_meilid_simulatsioon(tulemused)
    
    nayta_tulemused(tulemused)

def salvesta_tulemused_failidesse(tulemused):
    
    try:
        fail = open(fail_oiged, "w", encoding="utf-8")
        
        edukad = [t for t in tulemused if t["edukas"]]
        
        for tulemus in edukad:
            fail.write(f"{tulemus['nimi']} – {tulemus['oigete_arv']} õigesti\n")
        
        fail.close()
        print(f"Salvestasin {len(edukad)} edukat faili {fail_oiged}")
        
    except:
        print("Viga õigete faili salvestamisel")
    
    try:
        fail = open(fail_valed, "w", encoding="utf-8")
        
        valed = [t for t in tulemused if not t["edukas"]]
        
        valed_sorteeritud = sorted(valed, key=lambda x: x["nimi"])
        
        for tulemus in valed_sorteeritud:
            fail.write(f"{tulemus['nimi']} – {tulemus['oigete_arv']} õigesti\n")
        
        fail.close()
        print(f"Salvestasin {len(valed)} ebaedukat faili {fail_valed}")
        
    except:
        print("Viga vigade faili salvestamisel")
    
    try:
        fail = open(fail_koik, "w", encoding="utf-8")
        
        for tulemus in tulemused:
            fail.write(f"{tulemus['nimi']}, {tulemus['oigete_arv']}, {tulemus['email']}\n")
        
        fail.close()
        print(f"Salvestasin {len(tulemused)} inimest faili {fail_koik}")
        
    except:
        print("Viga kõikide faili salvestamisel")

def saada_meilid_simulatsioon(tulemused):
    print("\n=== MEILIDE SAATMINE ===")
    
    for t in tulemused:
        print(f"\nSaadetud: {t['email']}")
        print(f"Tere {t['nimi']}!")
        print(f"Sinu tulemus: {t['oigete_arv']} õiget vastust.")
        
        if t["edukas"]:
            print("Test oli edukas!")
        else:
            print("Test ei olnud edukas.")
    
    print(f"\nSaadetud: tootaja@firma.ee")
    print("Tere!")
    print("Tänased tulemused:")
    
    for i, t in enumerate(tulemused):
        print(f"{i+1}. {t['nimi']} – {t['oigete_arv']} õigesti")

def nayta_tulemused(tulemused):
    print("\n=== KOKKUVÕTE ===")
    
    edukad = [t for t in tulemused if t["edukas"]]
    
    if edukad:
        print("\nEdukad vastajad:")
        for t in edukad:
            print(f"- {t['nimi']} ({t['oigete_arv']} õigesti)")
    else:
        print("\nEdukaid vastajaid ei olnud.")
    
    print(f"\nKokku testiti: {len(tulemused)} inimest")
    print(f"Edukaid: {len(edukad)}")
    print("\nTulemused saadetud meilidele.")

def emaili_saatmine():
    print("Meilide saatmine on testimise osa.")

def küsimuste_lisamine():
    print("\n=== UUE KÜSIMUSE LISAMINE ===")
    
    uus_kusimus = input("Sisesta uus küsimus: ").strip()
    
    if not uus_kusimus:
        print("Küsimus ei tohi olla tühi!")
        return
    
    oige_vastus = input("Sisesta õige vastus: ").strip()
    
    if not oige_vastus:
        print("Vastus ei tohi olla tühi!")
        return
    
    kusimused_list.append(uus_kusimus)
    vastused_list.append(oige_vastus)
    
    andmete_salvestamine_failidesse_kusimused()
    
    print(f"Küsimus '{uus_kusimus}' lisatud!")
