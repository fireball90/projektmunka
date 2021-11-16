def belepes():
    name=str(input("Kérem a felhasználó nevét: "))
    password=str(input("Kérem a jelszavát: "))

    nameList=["fireball","norbert","kyywa"]
    passwordList=["asd123","LekiBOI","allinkah69"]

    check=0

    for i in range(len(nameList)):
        if (nameList[i] == name) and (passwordList[i] == password):
            check=1
        else:
            pass


    if check == 1:
        print("Sikeres bejelentkezés!")
    else:
        print("Hibás felhasználónév / jelszó!")
        ujra()
    

def ujra():
    again=input("Akar újra próbálkozni? (i/n)  ")

    if again == 'i' or again == 'I':
        belepes()
    elif again == 'n' or again == 'N':
        print("Viszlát!")
        print("______________________________________")
    else:
        ujra()


belepes()
