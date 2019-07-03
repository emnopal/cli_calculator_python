def main():
    #Menu
    print("Selamat datang di Kalkulator Saintifik berbasis Command Line Interface aka CLI.")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Modulo")
    print("6. Pangkat")
    print("7. Faktorial")
    print("8. Trigonometri")
    choice = input("Nomor:")

    #Penjumlahan
    if choice == '1':
        def tambah(a, b):
            return a + b
        print("Operasi: Penjumlahan")
        a = float(input("a: "))
        b = float(input("b: "))
        Hasil = print("Hasil dari ", a , "ditambah", b , "adalah: ", tambah(a,b))

    #Pengurangan
    elif choice == '2':
        def kurang(a, b):
            return a - b
        print("Operasi: Pengurangan")
        a = float(input("a: "))
        b = float(input("b: "))
        Hasil = print("Hasil dari ", a , "dikurang", b , "adalah: ", kurang(a,b))   

    #Perkalian
    elif choice == '3':
        def kali(a, b):
            return a * b
        print("Operasi: Perkalian")
        a = float(input("a: "))
        b = float(input("b: "))
        Hasil = print("Hasil dari ", a , "dikali", b , "adalah: ", kali(a,b))

    #Pembagian
    elif choice == '4':
        def bagi(a, b):
            return a / b
        print("Operasi: Pembagian")
        a = float(input("a: "))
        b = float(input("b: "))
        Hasil = print("Hasil dari ", a , "dibagi", b , "adalah: ", bagi(a,b))

    #Modulo atau Sisa Pembagian
    elif choice == '5':
        def mod(a, b):
            return a % b
        print("Operasi: Modulo")
        print("Keterangan: Modulo adalah Sisa Pembagian")
        a = float(input("a: "))
        b = float(input("b: "))
        Hasil = print("Modulo dari ", round(a) , "dibagi", round(b) , "adalah: ", round(mod(a,b)))

    #Pangkat
    elif choice == '6':
        def pangkat(a, b):
            return a ** b
        print("Operasi: Pangkat")
        a = float(input("a: "))
        b = float(input("b: "))
        Hasil = print(round(a) , "pangkat", round(b) , "adalah: ", round(pangkat(a,b)))

    #Faktorial
    elif choice == '7':
        def faktorial(n):
            faktorial = 1
            if n < 0:
                print("Gaada Faktorial Negatif!")
            elif n == 0:
                print("1")
            else:
                for i in range(1,n + 1):
                        faktorial = faktorial*i
            return faktorial
        print("Operasi: Faktorial")
        n = int(input('n: '))
        Hasil = print("Faktorial dari ", n , "adalah: ", faktorial(n))

    #Trigonometri
    elif choice == '8':
        import math
        def sin(x):
            sine = 0
            for i in range(50):
                sign = (-1)**i
                pi = math.pi
                y = x*(pi/180)
                sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
            return sine
        def cos(x):
            cosine = 0
            for i in range(50):
                sign = (-1)**i
                pi = math.pi
                y= x*(pi/180)
                cosine = cosine + ((y**(2.0*i))/math.factorial(2*i))*sign
            return cosine
        def tan(x):
            return sin(x)/cos(x)
        print("Operasi: Trigonometri")
        x = int(input("Nilai x dalam derajat: "))
        print("Nilai", x , "pada sudut Sin(X) adalah: ", round(sin(x),2))
        print("Nilai", x , "pada sudut Cos(X) adalah: ", round(cos(x),2))
        print("Nilai", x , "pada sudut Tan(X) adalah: ", round(tan(x),2))

    #Selain pilihan diatas
    else:
        print("Maaf tidak ada di menu")

    #Perintah Looping
    lanjut = input("Lanjut atau Tidak? ")
    if (lanjut == 'Tidak' 
        or lanjut == 'tidak' 
        or lanjut == 'tak' 
        or lanjut == 'Tak' 
        or lanjut == 'enggak' 
        or lanjut == 'Enggak' 
        or lanjut == 'No' 
        or lanjut == 'no' 
        or lanjut == 'n' 
        or lanjut == 'N' 
        or lanjut == 't' 
        or lanjut == 'T'):
        lanjut = False
    else:
        lanjut = True
        main()
main()