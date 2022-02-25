cyfry = [
    ["dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternasie", "pietniascie", "szesnascie", "siedemnascie", #0
    "osiemnascie", "dziewietnascie"],
    ["x!", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec"], #1
    ["x!","x!", 'dwadzieścia','trzydzieści','czterdzieści','pięćdziesiąt','sześćdziesiąt','siedemdziesiąt',
    'osiemdziesiąt','dziewięćdziesiąt'], # 2
    ["x!",'sto','dwieście','trzysta','czterysta','pięćset','sześćset','siedemset','osiemset','dziewięćset'], #3
    ["tysiąc", "tysiace", "tysiecy"] # 4
]

konwersja = {
    "1": "jeden",
    "2": "dwa",
    "3": "trzy",
    "4": "cztery",
    "5": "pięć",
    "6": "sześć",
    "7": "siedem",
    "8": "osiem",
    "9": "dziewięć",
    "0": "zero",
    "10": "dziesięć",
    "11": "jedenaście",
    "12": "dwanaście",   
    "13": "trzynaście",
    "14": "czternaśie",
    "15": "piętnaście",
    "16": "szesnaście",
    "17": "siediemnaście",
    "18": "osiemnaście",
    "19": "dziewiętnaście"
} 

liczba = 999999999999
liczba = str(liczba)
liczba = list(liczba)
liczba = liczba[::-1] 
konwer = []


def rzad():
    if len(liczba) != 0:
        if len(liczba[0:3]) == 3 or len(liczba[0:2]) == 2:
            nastki = int(liczba[1] + liczba[0])
        if len(liczba[0:3]) == 1:
            nastki = int(liczba[0])
        
        
        if nastki < 20:
            konwer.append(konwersja[str(nastki)])
            if len(liczba[0:3]) == 3:
                konwer.append(cyfry[3][int(liczba[2])])

            
        else:
            m = -1
            n = 0
            for i in liczba[0:3]:
                m += 1
                n += 1
                konwer.append(cyfry[n][int(liczba[m])])

    
def tysiace():
    if len(liczba) != 0:
        if len(liczba[0:3]) == 1 and liczba[0] == "1":
            konwer.append("Tysiąc")
        if 1 < int(liczba[0]) < 5 and len(liczba[0:3]) == 1:
            konwer.append("Tysiące")
        try:
            if 1 < int(liczba[0]) < 5 and int(liczba[1]) > 1:
                konwer.append("Tysiące")
        except:
            pass
        if 2 <= len(liczba[0:3]) <= 3  and liczba[1] == 0:
            konwer.append("Tysięcy")
        
        if len(liczba) != 0:
            if len(liczba[0:3]) == 3 or len(liczba[0:2]) == 2:
                nastki = int(liczba[1] + liczba[0])
            if len(liczba[0:3]) == 1:
                nastki = int(liczba[0])
        if 4 < nastki <= 19:
            konwer.append("Tysięcy")
        if int(liczba[0]) == 1 and len(liczba[0:3]) > 1:
            konwer.append("Tysięcy")
        if int(liczba[0]) == 0 and len(liczba[0:3]) > 0:
            konwer.append("Tysięcy")
        
        if 4 < int(liczba[0]) <= 9:
            konwer.append("Tysięcy")
        
    
        
def miliony():
    if len(liczba) != 0:
        if len(liczba[0:3]) == 1 and liczba[0] == "1":
            konwer.append("Milion")
        if 1 < int(liczba[0]) < 5 and len(liczba[0:3]) == 1:
            konwer.append("miliony")
        try:
            if 1 < int(liczba[0]) < 5 and int(liczba[1]) > 1:
                konwer.append("miliony")
        except:
            pass
        if 2 <= len(liczba[0:3]) <= 3  and liczba[1] == 0:
            konwer.append("milionów")
        
        if len(liczba) != 0:
            if len(liczba[0:3]) == 3 or len(liczba[0:2]) == 2:
                nastki = int(liczba[1] + liczba[0])
            if len(liczba[0:3]) == 1:
                nastki = int(liczba[0])
        if 4 < nastki <= 19:
            konwer.append("milionów")
        if int(liczba[0]) == 1 and len(liczba[0:3]) > 1:
            konwer.append("milionów")
        if int(liczba[0]) == 0 and len(liczba[0:3]) > 0:
            konwer.append("milionów")
        if 4 < int(liczba[0]) <= 9:
            konwer.append("milionów")



def miliardy():
    if len(liczba) != 0:
        if len(liczba[0:3]) == 1 and liczba[0] == "1":
            konwer.append("Miliard")
        if 1 < int(liczba[0]) < 5 and len(liczba[0:3]) == 1:
            konwer.append("miliardy")
        try:
            if 1 < int(liczba[0]) < 5 and int(liczba[1]) > 1:
                konwer.append("miliardy")
        except:
            pass
        if 2 <= len(liczba[0:3]) <= 3  and liczba[1] == 0:
            konwer.append("miliardów")
        
        if len(liczba) != 0:
            if len(liczba[0:3]) == 3 or len(liczba[0:2]) == 2:
                nastki = int(liczba[1] + liczba[0])
            if len(liczba[0:3]) == 1:
                nastki = int(liczba[0])
        if 4 < nastki <= 19:
            konwer.append("miliardów")
        if int(liczba[0]) == 1 and len(liczba[0:3]) > 1:
            konwer.append("miliardów")
        if int(liczba[0]) == 0 and len(liczba[0:3]) > 0:
            konwer.append("miliardów")
        if 4 < int(liczba[0]) <= 9:
            konwer.append("miliardów")










def delete():
    del(liczba[0:3])    
    m = -1
    n = 0


rzad()
delete()
tysiace()
rzad()
delete()
miliony()
rzad()
delete()
miliardy()
rzad()


konwer = konwer[::-1]

wynik = []
for i in konwer:
    if i != "zero" and i != "x!":
        wynik.append(i)


if "Tysięcy" in wynik and wynik[wynik.index("Tysięcy") -1] == "milionów" and "miliony" and "Milion":
    wynik.remove("Tysięcy")


if "Milionów" in wynik and wynik[wynik.index("Milionów") -1] == "miliardów" and "miliardy" and "Miliard":
    wynik.remove("Milionów")

print(konwer)
print(wynik)



 













