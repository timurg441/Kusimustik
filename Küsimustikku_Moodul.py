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

def andmete_lugemine_failidest():
    # Siin võiks olla kood, mis loeb andmeid failidest
    pass

def andmete_salvestamine_failidesse():
    # Siin võiks olla kood, mis salvestab andmeid failidesse
    pass

def testimine():
    # Siin võiks olla kood, mis teostab testimist
    pass
def emaili_saatmine():
    # Siin võiks olla kood, mis saadab e-kirju
    pass
def küsimuste_lsamine():
    # Siin võiks olla kood, mis lisab küsimusi
    pass