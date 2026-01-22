import random
import os

KYSIMUSED_FAIL = "kusimused_vastused.txt"
OIGED_FAIL = "oiged.txt"
VALED_FAIL = "valed.txt"
KOIK_FAIL = "koik.txt"

def loe_kysimused():
    kysimused = []
    vastused = []
    kysimus_sõnastik = {}
    
    if not os.path.exists(KYSIMUSED_FAIL):
        print("Faili pole, loome näidisküsimused...")
        with open(KYSIMUSED_FAIL, "w", encoding="utf-8") as f:
            f.write("Mis on Python?:programmeerimiskeel\n")
            f.write("Mis värvi on lumi?:valge\n")
            f.write("Mitu päeva on nädalas?:7\n")
            f.write("Milline on Eesti pealinn?:Tallinn\n")
            f.write("Mitu kuud on aastas?:12\n")
    
    with open(KYSIMUSED_FAIL, "r", encoding="utf-8") as f:
        for rida in f:
            rida = rida.strip()
            if ":" in rida:
                kysimus, vastus = rida.split(":", 1)
                kysimus = kysimus.strip()
                vastus = vastus.strip()
                
                kysimused.append(kysimus)
                vastused.append(vastus)
                
                kysimus_sõnastik[kysimus] = vastus
    
    print(f"Laeti {len(kysimused)} küsimust")
    return kysimused, vastused, kysimus_sõnastik

def loo_email(nimi):
    nimi = nimi.strip()
    osad = nimi.split()
    
    if len(osad) >= 2:
        eesnimi = osad[0].lower()
        perenimi = osad[-1].lower()
        eesnimi = eesnimi.replace("ä", "a").replace("ö", "o").replace("õ", "o").replace("ü", "u")
        perenimi = perenimi.replace("ä", "a").replace("ö", "o").replace("õ", "o").replace("ü", "u")
        return f"{eesnimi}.{perenimi}@example.com"
    else:
        nimi_simple = nimi.lower().replace(" ", ".")
        nimi_simple = nimi_simple.replace("ä", "a").replace("ö", "o").replace("õ", "o").replace("ü", "u")
        return f"{nimi_simple}@example.com"

def on_juba_testitud(nimi):
    if not os.path.exists(KOIK_FAIL):
        return False
    
    with open(KOIK_FAIL, "r", encoding="utf-8") as f:
        for rida in f:
            if rida.strip():
                andmed = rida.strip().split(",")
                if len(andmed) > 0 and andmed[0] == nimi:
                    return True
    return False

def kysi_kysimusi(inimene_nimi, kysimuste_arv, kysimused_list, vastused_list):
    print(f"\n{inimene_nimi}, alustame sinu testi!")

    if kysimuste_arv > len(kysimused_list):
        kysimuste_arv = len(kysimused_list)
    
    kogus = len(kysimused_list)
    valitud_indeksid = []
    
    while len(valitud_indeksid) < kysimuste_arv:
        juhuslik = random.randint(0, kogus-1)
        if juhuslik not in valitud_indeksid:
            valitud_indeksid.append(juhuslik)
    
    oigete_arv = 0
    for i, idx in enumerate(valitud_indeksid, 1):
        print(f"\nKüsimus {i}:")
        print(f"  {kysimused_list[idx]}")
        kasutaja_vastus = input("  Sinu vastus: ").strip().lower()
        
        oige_vastus = vastused_list[idx].lower()
        if kasutaja_vastus == oige_vastus:
            print("Õige!")
            oigete_arv += 1
        else:
            print(f"Vale. Õige vastus: {vastused_list[idx]}")
    
    return oigete_arv

def sorteeri_failid():

    if os.path.exists(OIGED_FAIL):
        with open(OIGED_FAIL, "r", encoding="utf-8") as f:
            read = f.readlines()
        
        andmed = []
        for rida in read:
            if " – " in rida:
                nimi, punktid = rida.strip().split(" – ")
                punktid_arv = int(punktid.replace(" õigesti", ""))
                andmed.append((nimi, punktid_arv))
        
        andmed.sort(key=lambda x: x[1], reverse=True)
        
        with open(OIGED_FAIL, "w", encoding="utf-8") as f:
            for nimi, punktid in andmed:
                f.write(f"{nimi} – {punktid} õigesti\n")
    
    if os.path.exists(VALED_FAIL):
        with open(VALED_FAIL, "r", encoding="utf-8") as f:
            read = f.readlines()
        
        andmed = []
        for rida in read:
            if " – " in rida:
                nimi, punktid = rida.strip().split(" – ")
                punktid_arv = int(punktid.replace(" õigesti", ""))
                andmed.append((nimi, punktid_arv))
        
        andmed.sort(key=lambda x: x[0])
        
        with open(VALED_FAIL, "w", encoding="utf-8") as f:
            for nimi, punktid in andmed:
                f.write(f"{nimi} – {punktid} õigesti\n")

def lisa_failidesse(nimi, oigete_arv, email, edukas):

    with open(KOIK_FAIL, "a", encoding="utf-8") as f:
        f.write(f"{nimi},{oigete_arv},{email}\n")
    
    if edukas:
        fail_nimi = OIGED_FAIL
    else:
        fail_nimi = VALED_FAIL
    
    with open(fail_nimi, "a", encoding="utf-8") as f:
        f.write(f"{nimi} – {oigete_arv} õigesti\n")
    
    sorteeri_failid()

def lisa_uus_kysimus():
    uus_kysimus = input("Sisesta uus küsimus: ").strip()
    if not uus_kysimus:
        print("Küsimus ei tohi olla tühi!")
        return False
    
    oige_vastus = input("Sisesta õige vastus: ").strip()
    if not oige_vastus:
        print("Vastus ei tohi olla tühi!")
        return False
    
    with open(KYSIMUSED_FAIL, "a", encoding="utf-8") as f:
        f.write(f"\n{uus_kysimus}:{oige_vastus}")
    
    print(f"Küsimus '{uus_kysimus}' lisatud!")
    return True

def saada_meilid_simulatsioon(kõik_tulemused):
    print("\n" + "="*60)
    print("E-KIRJADE SAATMINE")
    print("="*60)
    
    for tulemus in kõik_tulemused:
        osad = tulemus.split(",")
        nimi = osad[0]
        oiged = osad[1]
        email = osad[2]
        
        edukad = []
        if os.path.exists(OIGED_FAIL):
            with open(OIGED_FAIL, "r", encoding="utf-8") as f:
                for rida in f:
                    if nimi in rida:
                        edukad.append(nimi)
        
        edukas = nimi in edukad
        
        print(f"\n📧 Saadetud: {email}")
        print(f"Tere {nimi}!")
        print(f"Sinu õigete vastuste arv: {oiged}.")
        if edukas:
            print("Sa sooritasid testi edukalt.")
        else:
            print("Kahjuks testi ei sooritatud edukalt.")
    
    print(f"\n📊 Saadetud: tootaja@firma.ee")
    print("Tere!")
    print("\nTänased küsimustiku tulemused:")
    
    if os.path.exists(KOIK_FAIL):
        with open(KOIK_FAIL, "r", encoding="utf-8") as f:
            read = f.readlines()
        
        edukad_nimed = []
        if os.path.exists(OIGED_FAIL):
            with open(OIGED_FAIL, "r", encoding="utf-8") as f:
                for rida in f:
                    if " – " in rida:
                        edukad_nimed.append(rida.split(" – ")[0])
        
        for i, rida in enumerate(read, 1):
            if rida.strip():
                andmed = rida.strip().split(",")
                if len(andmed) >= 3:
                    nimi = andmed[0]
                    oiged = andmed[1]
                    email = andmed[2]
                    tulemus = "SOBIS" if nimi in edukad_nimed else "EI SOBINUD"
                    print(f"{i}. {nimi} – {oiged} õigesti – {email} – {tulemus}")
        
        if read:
            parim_nimi = ""
            parim_punktid = 0
            
            for rida in read:
                if rida.strip():
                    andmed = rida.strip().split(",")
                    if len(andmed) >= 2:
                        try:
                            punktid = int(andmed[1])
                            if punktid > parim_punktid:
                                parim_punktid = punktid
                                parim_nimi = andmed[0]
                        except:
                            pass
            
            if parim_nimi:
                print(f"\nParim vastaja: {parim_nimi} ({parim_punktid} õigesti)")
    
    print("\nLugupidamisega,")
    print("Küsimustiku Automaatprogramm")

def nayta_edukad_ekraanil():
    print("\n" + "="*50)
    print("EDUKAD VASTAJAD")
    print("="*50)
    
    if os.path.exists(OIGED_FAIL):
        with open(OIGED_FAIL, "r", encoding="utf-8") as f:
            read = f.readlines()
        
        if read:
            print("Nimi ja õigete vastuste arv:")
            for rida in read:
                print(f"  {rida.strip()}")
        else:
            print("Edukaid vastajaid ei olnud.")
    else:
        print("Tulemusi pole veel.")
    
    print("\nTulemused saadetud e-posti aadressidele.")
