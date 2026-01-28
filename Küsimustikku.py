import Küsimustikku_Moodul

while True:
    print("\n1. Test")
    print("2. Lisa küsimus")
    print("3. Välju")
    
    v = input("Valik: ")
    
    if v == "1":
        Küsimustikku_Moodul.alusta()
    elif v == "2":
        Küsimustikku_Moodul.lisa()
    elif v == "3":
        print("Head aega")
        break
    else:
        print("Vale")
