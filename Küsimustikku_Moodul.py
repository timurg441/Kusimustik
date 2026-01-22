import random

KUSIMUSED_FAIL = "kusimused_vastused.txt"
OIGED_FAIL = "oiged.txt"
VALED_FAIL = "valed.txt"
KOIK_FAIL = "koik.txt"

M = 3
N = 3


def loe_kusimused():
    kus_vas = {}
    with open(KUSIMUSED_FAIL, "r", encoding="utf-8") as f:
        for rida in f:
            rida = rida.strip()
            if ":" in rida:
                k, v = rida.split(":")
                kus_vas[k] = v
    return kus_vas


def alusta_kusimustik():
    kus_vas = loe_kusimused()
    vastajad = []
    juba_testitud = []

    for i in range(M):
        nimi = input("\nSisesta vastaja nimi: ")

        if nimi in juba_testitud:
            print("See inimene on juba testitud!")
            continue

        email = input("Sisesta oma e-post: ")
        juba_testitud.append(nimi)

        kysimused = random.sample(list(kus_vas.keys()), N)
        oiged = 0

        for k in kysimused:
            vastus = input(f"{nimi}, {k} ")
            if vastus.lower() == kus_vas[k].lower():
                oiged += 1

        vastajad.append([nimi, oiged, email])

        print("\nSaadetud:", email)
        print("Tere", nimi + "!")
        print("Sinu õigete vastuste arv:", oiged)

        if oiged > N / 2:
            print("Sa sooritasid testi edukalt.")
        else:
            print("Kahjuks testi ei sooritatud edukalt.")

    salvesta_failidesse(vastajad)
    saada_raport(vastajad)


def salvesta_failidesse(vastajad):
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
            f.write(v[0] + "\n")

    with open(KOIK_FAIL, "w", encoding="utf-8") as f:
        for v in vastajad:
            f.write(f"{v[0]}, {v[1]}, {v[2]}\n")

    print("\nEdukalt vastanud:")
    for v in oiged:
        print(v[0], "-", v[1])

    print("\nTulemused saadetud e-posti aadressidele.")


def saada_raport(vastajad):
    print("\nSaadetud: tootaja@firma.ee")
    print("\nTänased küsimustiku tulemused:\n")

    parim = max(vastajad, key=lambda x: x[1])

    nr = 1
    for v in vastajad:
        tulemus = "SOBIS" if v[1] > N / 2 else "EI SOBINUD"
        print(f"{nr}. {v[0]} – {v[1]} õigesti – {v[2]} – {tulemus}")
        nr += 1

    print("\nParim vastaja:", parim[0], f"({parim[1]} õigesti)")
    print("\nLugupidamisega,\nKüsimustiku Automaatprogramm")


def lisa_kusimus():
    k = input("Sisesta uus küsimus: ")
    v = input("Sisesta õige vastus: ")

    with open(KUSIMUSED_FAIL, "a", encoding="utf-8") as f:
        f.write(f"\n{k}:{v}")

    print("Küsimus lisatud!")
