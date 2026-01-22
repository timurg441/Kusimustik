import random

KUSIMUSED_FAIL = "kusimused_vastused.txt"
OIGED_FAIL = "oiged.txt"
VALED_FAIL = "valed.txt"
KOIK_FAIL = "koik.txt"

# Küsime M ja N kasutajalt, mitte fikseeritud
# M = 3
# N = 3


def loe_kusimused():
    kus_vas = {}
    with open(KUSIMUSED_FAIL, "r", encoding="utf-8") as f:
        for rida in f:
            rida = rida.strip()
            if ":" in rida:
                k, v = rida.split(":", 1)  # Lisage ", 1" et mitte jagada mitmes koolonis
                kus_vas[k] = v
    return kus_vas


def genereeri_email(nimi):
    osad = nimi.split()
    if len(osad) >= 2:
        return f"{osad[0].lower()}.{osad[-1].lower()}@example.com"
    else:
        return f"{nimi.lower()}@example.com"


def alusta_kusimustik():
    kus_vas = loe_kusimused()
    
    # Kui vähe küsimusi
    if len(kus_vas) < 3:
        print("Liiga vähe küsimusi! Lisa enne rohkem.")
        return
    
    # Küsi M ja N (nagu ülesandes)
    try:
        M = int(input("Mitu inimest testime (M)? "))
        N = int(input("Mitu küsimust igale inimesele (N)? "))
        
        if N > len(kus_vas):
            print(f"Viga! Failis on ainult {len(kus_vas)} küsimust.")
            return
    except:
        print("Viga! Sisesta arvud.")
        return
    
    vastajad = []
    juba_testitud = []

    for i in range(M):
        nimi = input(f"\nVastaja {i+1}/{M} nimi: ")

        if nimi in juba_testitud:
            print("See inimene on juba testitud!")
            continue

        # Genereeri email automaatselt (nagu ülesandes)
        email = genereeri_email(nimi)
        print(f"Email: {email}")
        
        juba_testitud.append(nimi)

        kysimused = random.sample(list(kus_vas.keys()), N)
        oiged = 0

        for k in kysimused:
            vastus = input(f"{nimi}, {k} ")
            if vastus.lower() == kus_vas[k].lower():
                oiged += 1

        vastajad.append([nimi, oiged, email])

        # "E-kiri" vastajale
        print(f"\nSaadetud: {email}")
        print(f"Tere {nimi}!")
        print(f"Sinu õigete vastuste arv: {oiged}.")

        if oiged > N / 2:
            print("Sa sooritasid testi edukalt.")
        else:
            print("Kahjuks testi ei sooritatud edukalt.")

    if vastajad:  # Kui on vähemalt üks vastaja
        salvesta_failidesse(vastajad, N)
        saada_raport(vastajad, N)
    else:
        print("\nEi testitud ühtegi inimest.")


def salvesta_failidesse(vastajad, N):
    oiged = []
    valed = []

    for v in vastajad:
        if v[1] > N / 2:
            oiged.append(v)
        else:
            valed.append(v)

    oiged.sort(key=lambda x: x[1], reverse=True)
    valed.sort(key=lambda x: x[0])

    with open(OIGED_FAIL, "w", encoding="utf-8") as f:
        for v in oiged:
            f.write(f"{v[0]} – {v[1]} õigesti\n")

    with open(VALED_FAIL, "w", encoding="utf-8") as f:
        for v in valed:
            f.write(f"{v[0]} – {v[1]} õigesti\n")  # Lisa ka punktid

    with open(KOIK_FAIL, "w", encoding="utf-8") as f:
        for v in vastajad:
            f.write(f"{v[0]}, {v[1]}, {v[2]}\n")

    print("\nEdukalt vastanud:")
    for v in oiged:
        print(f"{v[0]} - {v[1]} õigesti")

    print("\nTulemused saadetud e-posti aadressidele.")


def saada_raport(vastajad, N):
    print("\nSaadetud: tootaja@firma.ee")
    print("\nTänased küsimustiku tulemused:\n")

    if vastajad:
        parim = max(vastajad, key=lambda x: x[1])

        nr = 1
        for v in vastajad:
            tulemus = "SOBIS" if v[1] > N / 2 else "EI SOBINUD"
            print(f"{nr}. {v[0]} – {v[1]} õigesti – {v[2]} – {tulemus}")
            nr += 1

        print(f"\nParim vastaja: {parim[0]} ({parim[1]} õigesti)")
    
    print("\nLugupidamisega,\nKüsimustiku Automaatprogramm")


def lisa_kusimus():
    k = input("Sisesta uus küsimus: ")
    v = input("Sisesta õige vastus: ")

    with open(KUSIMUSED_FAIL, "a", encoding="utf-8") as f:
        f.write(f"\n{k}:{v}")

    print("Küsimus lisatud!")
