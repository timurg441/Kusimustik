from Küsimustikku_Moodul import *

print("=" * 50)
print("   KÜSIMUSTIKU PROGRAMM")
print("=" * 50)

while True:
    print("\n" + "-" * 30)
    print("    VALI TEGEVUS:")
    print("-" * 30)
    print("1. Alusta küsimustikku")
    print("2. Lisa uus küsimus")
    print("3. Välju")
    print("-" * 30)
    
    valik = input("Sisesta number (1-3): ").strip()
    
    if valik == "1":
        print("\n=== KÜSIMUSTIKU ALGUS ===\n")
        
        kysimused, vastused, kysimus_sõnastik = loe_kysimused()
        
        if len(kysimused) < 3:
            print("Liiga vähe küsimusi! Lisa vähemalt 3 küsimust.")
            continue
        
        print(f"Küsimusi on kokku: {len(kysimused)}")
        
        try:
            inimeste_arv = int(input("\nMitu inimest soovid küsitleda (M)? "))
            if inimeste_arv <= 0:
                print("Arv peab olema positiivne!")
                continue
        except:
            print("Viga! Sisesta number.")
            continue
        
        try:
            kysimuste_arv = int(input("Mitu küsimust igale inimesele (N)? "))
            if kysimuste_arv <= 0:
                print("Arv peab olema positiivne!")
                continue
            if kysimuste_arv > len(kysimused):
                print(f"Viga! Max {len(kysimused)} küsimust.")
                continue
        except:
            print("Viga! Sisesta number.")
            continue
        
        kõik_tulemused_list = []
        
        for i in range(inimeste_arv):
            print(f"\n{'='*40}")
            print(f"VASTAJA {i+1}/{inimeste_arv}")
            print(f"{'='*40}")
            
            nimi = input("Sisesta oma nimi ja perekonnanimi: ").strip()
            if not nimi:
                print("Nimi ei tohi olla tühi!")
                continue
            
            if on_juba_testitud(nimi):
                print(f"{nimi} on juba testitud!")
                continue
            
            email = loo_email(nimi)
            print(f"Email: {email}")
            
            oigete_arv = kysi_kysimusi(nimi, kysimuste_arv, kysimused, vastused)
            
            edukas = oigete_arv > kysimuste_arv / 2
            
            tulemus = f"{nimi},{oigete_arv},{email}"
            kõik_tulemused_list.append(tulemus)
            
            lisa_failidesse(nimi, oigete_arv, email, edukas)
            
            print(f"\n{'='*40}")
            print(f"{nimi}, sinu tulemus:")
            print(f"Õigeid vastuseid: {oigete_arv}/{kysimuste_arv}")
            if edukas:
                print("TEST EDUKAS! Palju õnne!")
            else:
                print("Test ebaõnnestus.")
        
        if kõik_tulemused_list:
            saada_meilid_simulatsioon(kõik_tulemused_list)
            
            nayta_edukad_ekraanil()
        else:
            print("\nEi testitud ühtegi inimest.")
    
    elif valik == "2":
        print("\n=== UUE KÜSIMUSE LISAMINE ===")
        lisa_uus_kysimus()
    
    elif valik == "3":
        print("\nAitäh! Programmi lõpetamine.")
        break
    
    else:
        print("Vale valik! Vali 1, 2 või 3.")
