import Küsimustikku_Moodul as km

while True:
    print("\n1. Alusta küsimustikku")
    print("2. Lisa uus küsimus")
    print("3. Välju")

    valik = input("Vali: ")

    if valik == "1":
        km.alusta_kusimustik()
    elif valik == "2":
        km.lisa_kusimus()
    elif valik == "3":
        print("Programm lõpetatud.")
        break
    else:
        print("Vale valik!")
