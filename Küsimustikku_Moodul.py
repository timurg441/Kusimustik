import random
import os

admin_nimed = ["admin", "kasutaja"]
admin_paroolid = ["admin123", "parool"]

kysimused_fail = "kysimused_vastused.txt"
koik_fail = "koik_tulemused.txt"
oiged_fail = "oiged.txt"
valed_fail = "valed.txt"

def kontrolli_sisselogimist(nimi, parool):
    if nimi in admin_nimed:
        indeks = admin_nimed.index(nimi)
        if parool == admin_paroolid[indeks]:
            return True
    return False

def loe_kysimused_failist():
    kysimused = []
    
    if not os.path.exists(kysimused_fail):
        print("Faili pole. Loon uue koos näidisküsimustega.")
        
        näidis_kysimused = [
            "Mis on Eesti pealinn?:Tallinn",
            "Mis värvi on lumi?:valge", 
            "Mitu päeva on nädalas?:7",
            "Milline number on suurim?:9",
            "Kas koer on loom?:jah"
        ]
        
        with open(kysimused_fail, "w", encoding="utf-8") as f:
            for kysimus in näidis_kysimused:
                f.write(kysimus + "\n")
    
    try:
        with open(kysimused_fail, "r", encoding="utf-8") as f:
            for rida in f:
                rida = rida.strip()
                if rida:
                    kysimused.append(rida)
        
        print(f"Leiti {len(kysimused)} küsimust")
        return kysimused
        
    except:
        print("Viga faili lugemisel")
        return []

def näita_kysimusi(kysimused_list):
    if not kysimused_list:
        print("Küsimusi pole.")
        return
    
    print("\nKÕIK KÜSIMUSED")
    for i, kysimus in enumerate(kysimused_list, 1):
        print(f"{i}. {kysimus}")
    print("=====================\n")

def lisa_uus_kysimus():
    print("\nUUE KÜSIMUSE LISAMINE")
    
    uus_kysimus = input("Sisesta uus küsimus: ").strip()
    if not uus_kysimus:
        print("Küsimus ei tohi olla tühi!")
        return False
    
    oige_vastus = input("Sisesta õige vastus: ").strip()
    if not oige_vastus:
        print("Vastus ei tohi olla tühi!")
        return False
    
    with open(kysimused_fail, "a", encoding="utf-8") as f:
        f.write(f"{uus_kysimus}:{oige_vastus}\n")
    
    print(f"Küsimus '{uus_kysimus}' lisatud!")
    return True

def kustuta_kysimused():
    vastus = input("Kas oled kindel, et tahad KÕIK küsimused kustutada? (jah/ei): ")
    
    if vastus.lower() == "jah":
        with open(kysimused_fail, "w", encoding="utf-8") as f:
            f.write("")
        
        with open(kysimused_fail, "a", encoding="utf-8") as f:
            f.write("Mis on Eesti pealinn?:Tallinn\n")
            f.write("Mis värvi on lumi?:valge\n")
        
        print("Kõik küsimused kustutatud. Jätsin 2 põhiküsimust.")
        return True
    else:
        print("Kustutamine katkestatud.")
        return False

def alusta_testi():
    print("\nTESTI ALGUS\n")
    
    nimi = input("Sisesta oma nimi: ").strip()
    if not nimi:
        print("Nimi on kohustuslik!")
        return
    
    testitud_nimed = []
    if os.path.exists(koik_fail):
        with open(koik_fail, "r", encoding="utf-8") as f:
            for rida in f:
                if rida.strip():
                    olemas_nimi = rida.split(",")[0].strip()
                    testitud_nimed.append(olemas_nimi)
    
    if nimi in testitud_nimed:
        print(f"{nimi}, sa oled juba testi teinud!")
        return
    
    nime_osad = nimi.split()
    if len(nime_osad) >= 2:
        email = f"{nime_osad[0].lower()}.{nime_osad[-1].lower()}@example.com"
    else:
        email = f"{nimi.lower()}@example.com"
    
    print(f"Tere, {nimi}! Sinu email: {email}")
    
    kysimused = loe_kysimused_failist()
    
    if len(kysimused) < 3:
        print("Liiga vähe küsimusi! Lisa rohkem küsimusi.")
        return
    
    kysimuste_arv = min(5, len(kysimused))
    print(f"Sulle esitatakse {kysimuste_arv} küsimust.\n")
    
    valitud_indeksid = random.sample(range(len(kysimused)), kysimuste_arv)
    
    oigete_arv = 0
    
    for i, indeks in enumerate(valitud_indeksid, 1):
        kysimus_rida = kysimused[indeks]
        if ":" in kysimus_rida:
            kysimus, oige_vastus = kysimus_rida.split(":", 1)
            
            print(f"Küsimus {i}: {kysimus.strip()}")
            kasutaja_vastus = input("Sinu vastus: ").strip().lower()
            
            if kasutaja_vastus == oige_vastus.strip().lower():
                print("Õige!")
                oigete_arv += 1
            else:
                print(f"Vale. Õige vastus: {oige_vastus.strip()}")
        print()
    
    protsent = (oigete_arv / kysimuste_arv) * 100
    edukas = protsent >= 60
    
    print(f"\nTESTI LÕPP")
    print(f"{nimi}, sa said {oigete_arv}/{kysimuste_arv} õigesti ({protsent:.1f}%)")
    
    if edukas:
        print("🎉 Palju õnne! Test edukas!")
        tulemus_tekst = "EDUKAS"
    else:
        print("😔 Kahjuks test ebaõnnestus.")
        tulemus_tekst = "EI OLE EDUKAS"
    
    salvesta_tulemus(nimi, oigete_arv, email, tulemus_tekst, edukas)
    
    saada_email_simulatsioon(nimi, email, oigete_arv, edukas)
    
    return edukas

def salvesta_tulemus(nimi, oigete_arv, email, tulemus, edukas):
    
    with open(koik_fail, "a", encoding="utf-8") as f:
        f.write(f"{nimi}, {oigete_arv}, {email}, {tulemus}\n")
    
    if edukas:
        fail_nimi = oiged_fail
    else:
        fail_nimi = valed_fail
    
    with open(fail_nimi, "a", encoding="utf-8") as f:
        f.write(f"{nimi} - {oigete_arv} õigesti - {email}\n")
    
    print(f"Tulemus salvestati faili {fail_nimi}")

def saada_email_simulatsioon(nimi, email, oigete_arv, edukas):
    print("\nEMAILI SAATMINE")
    
    print(f"📧 Saadetakse: {email}")
    print(f"Tere {nimi}!")
    print(f"Sinu tulemus: {oigete_arv} õiget vastust.")
    
    if edukas:
        print("Test oli edukas! Hästi tehtud! 🎉")
    else:
        print("Test ei olnud edukas. Proovi uuesti! 💪")
    
    try:
        with open(koik_fail, "r", encoding="utf-8") as f:
            read_lines = f.readlines()
        
        if len(read_lines) >= 3:
            print(f"\n📊 Adminile saadetakse kokkuvõte:")
            print(f"Viimased 3 tulemust:")
            
            for i, line in enumerate(read_lines[-3:], 1):
                osad = line.strip().split(",")
                if len(osad) >= 4:
                    print(f"{i}. {osad[0]} - {osad[1]} õigesti")
    except:
        pass
    
    print("(See on simulatsioon - päris emaili ei saadeta)")

def lisa_10_kysimust():
    näidis_kysimused = [
        "Mis on 2+2?:4",
        "Kes on Eesti president?:Alar Karis",
        "Mitu kuud on aastas?:12",
        "Mis värvi on taevas?:sinine",
        "Kes ütleb mjäu?:kass",
        "Mis on veepiima värv?:valge",
        "Mitu käppa on koeral?:4",
        "Mis on kooli number 2?:2",
        "Kas päike paisteb?:jah",
        "Mis on aasta esimene kuu?:jaanuar"
    ]
    
    with open(kysimused_fail, "a", encoding="utf-8") as f:
        for kysimus in näidis_kysimused:
            f.write(kysimus + "\n")
    
    print("10 näidisküsimust lisatud!")

def kustuta_kõik_tulemused():
    failid = [koik_fail, oiged_fail, valed_fail]
    
    for fail in failid:
        if os.path.exists(fail):
            with open(fail, "w", encoding="utf-8") as f:
                f.write("")
    
    print("Kõik tulemused kustutatud!")
