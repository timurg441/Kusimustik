from Küsimustikku_Moodul import *

print("=" * 50)
print("   TERE TULEMAST KÜSIMUSTIKKU!")
print("=" * 50)

while True:
    print("\n" + "=" * 30)
    print("    PEAMENÜÜ")
    print("=" * 30)
    print("1. Alusta testi")
    print("2. Logi sisse adminina")
    print("3. Välju programmist")
    print("=" * 30)
    
    valik = input("Vali number (1-3): ").strip()
    
    if valik == "1":
        alusta_testi()
        
    elif valik == "2":
        kasutajanimi = input("Kasutajanimi: ").strip()
        parool = input("Parool: ").strip()
        
        if kontrolli_sisselogimist(kasutajanimi, parool):
            print("\nSisselogimine õnnestus! Tere tulemast, admin!")
            
            while True:
                print("\n" + "=" * 30)
                print("    ADMINI MENÜÜ")
                print("=" * 30)
                print("1. Näita küsimusi")
                print("2. Lisa uus küsimus")
                print("3. Alusta testi")
                print("4. Lisa 10 näidisküsimust")
                print("5. Kustuta kõik tulemused")
                print("6. Logi välja")
                print("=" * 30)
                
                admin_valik = input("Vali number (1-6): ").strip()
                
                if admin_valik == "1":
                    kysimused = loe_kysimused_failist()
                    näita_kysimusi(kysimused)
                    
                elif admin_valik == "2":
                    lisa_uus_kysimus()
                    
                elif admin_valik == "3":
                    alusta_testi()
                    
                elif admin_valik == "4":
                    lisa_10_kysimust()
                    
                elif admin_valik == "5":
                    kustuta_kõik_tulemused()
                    
                elif admin_valik == "6":
                    print("Administ välja logitud.")
                    break
                    
                else:
                    print("Vigane valik! Proovi uuesti.")
        
        else:
            print("Vale kasutajanimi või parool!")
            
    elif valik == "3":
        print("\nAitäh programmi kasutamast! Head aega!")
        break
        
    else:
        print("Palun vali 1, 2 või 3!")
