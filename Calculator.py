#Operasi Matematika pada Python

# Penjumlahan
def tambah(a, b):
    return a + b

# Pengurangan
def kurang(a, b):
    return a - b

# Perkalian
def kali(a, b):
    return a * b

# Pembagian
def bagi(a, b):
    return a / b 

# Modulo
def modulo(a, b):
    return a % b

# Pangkat
def pangkat(a, b):
    return a ** b

# Fungsi Sinus
import math
def sin(x):
    sine = 0
    for i in range(20):
        sign = (-1)**i
        pi = 3.1415926535897932384626433832795
        y= x*(pi/180)
        sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return sine

# Fungsi Cosinus
def cos(x):
    cosine = 0
    for i in range(20):
        sign = (-1)**i
        pi = 3.1415926535897932384626433832795
        y= x*(pi/180)
        cosine = cosine + ((y**(2.0*i))/math.factorial(2*i))*sign
    return cosine

# Fungsi Tangent
def tan(x):
    return sin(x)/cos(x)

# Fungsi Eksponensial
def exp():
    exp = 0
    x = 1
    for n in range(100):
        exp = exp + ((x**n)/math.factorial(n))
    return exp

# Fungsi Turunan 
# Menggunakan Metode Numerik
def maju(f,x,h):
    a = x+h
    maju = f(a)/h - f(x)/h
    return maju
def mundur(f,x,h):
    a = x-h
    mundur = f(x)/h - f(a)/h
    return mundur
def tengah(f,x,h):
    a = x+h
    b = x-h
    c = 2*h
    tengah = f(a)/c - f(b)/c
    return tengah

# Fungsi Integral
# Menggunakan Metode Numerik Simpson-Trapezoid
import numpy as np
def simpson(f,a,b,n):
    if n % 2 == 1:
        raise ValueError("n harus genap bapak!")
    h = (b-a)/n
    x = np.linspace(a,b,n+1)
    y = f(x)
    return (h/3)*np.sum(y[0:-1:2]+4*y[1::2]+y[2::2])

# Fungsi
def f(x):
    return x

# Pi
from math import factorial
from decimal import Decimal, getcontext
getcontext().prec=300
n = 1
def calc(n):
    t = Decimal(0)
    pi = Decimal(0)
    deno = Decimal(0)
    n = 1
    for k in range (n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)
    pi = pi*Decimal(12)/Decimal(640320**Decimal(1.5))
    pi = 1/pi
    return pi

#Eliminasi Gauss
def linearsolver(A,b):
  n = len(A)
  M = A

  i = 0
  for x in M:
   x.append(b[i])
   i += 1

  for k in range(n):
   for i in range(k,n):
     if abs(M[i][k]) > abs(M[k][k]):
        M[k], M[i] = M[i],M[k]
     else:
        pass

   for j in range(k+1,n):
       q = float(M[j][k]) / M[k][k]
       for m in range(k, n+1):
          M[j][m] -=  q * M[k][m]

  x = [0 for i in range(n)]

  x[n-1] =float(M[n-1][n])/M[n-1][n-1]
  for i in range (n-1,-1,-1):
    z = 0
    for j in range(i+1,n):
        z = z  + float(M[i][j])*x[j]
    x[i] = float(M[i][n] - z)/M[i][i]
  return x

#Random
import random

#Graph
import matplotlib.pyplot as plt

# Perintah opsional dan input
print("Selamat datang di Tools berbasis Command Line Interface aka CLI.")
print("1. Kalkulator Saintifik")
print("2. Generator Angka")
print("3. Gambar Grafik")
print("4. Kalender Hari Ini")
print("5. Tahun Kabisat")
print("99. About")
choice = input("Nomor:")

# Kalkulator 
if choice == '1':

    print("Silahkan pilih operasi Matematikanya!")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Modulo")
    print("6. Pangkat")
    print("7. Faktorial")
    print("8. Matriks")
    print("9. Sin x")
    print("10. Cos x")
    print("11. Tan x")
    print("12. Eksponensial")
    print("13. Pi")
    print("14. Turunan")
    print("15. Integral")
    print("16: Eliminasi Gauss")

    # Input Nomor
    choice = input("Nomor:")

    # Definisi dari setiap pilihan
    # Penjumlahan
    if choice == '1':
        a = float(input("a: "))
        b = float(input("b: "))
        Hasil = print("Hasil: ", tambah(a,b))

    #Pengurangan
    elif choice == '2':
        a = float(input("a: "))
        b = float(input("b: "))
        Hasil = print("Hasil: ", kurang(a,b))

    # Perkalian
    elif choice == '3':
        a = float(input("a: "))
        b = float(input("b: "))
        Hasil = print("Hasil: ", kali(a,b))

    # Pembagian
    elif choice == '4':
        a = float(input("a: "))
        b = float(input("b: "))
        Hasil = print("Hasil: ", bagi(a,b))

    # Modulo
    elif choice == '5':
        a = float(input("a: "))
        b = float(input("b: "))
        Hasil = print("Hasil: ", modulo(a,b))

    # Pangkat
    elif choice == '6':
        a = float(input("a: "))
        b = float(input("Pangkat: "))
        Hasil = print("Hasil: ", pangkat(a,b))

    # Faktorial
    elif choice == '7':
        n = int(input('Faktorial:'))
        faktorial = 1
        if n < 0:
            print("Gaada Faktorial Negatif!")
        elif n == 0:
            print("1")
        else:
            for i in range(1,n + 1):
                    faktorial = faktorial*i
                    print(faktorial)

    # Matriks
    elif choice == '8':
    
        # Pilihan operasi matriks
        print("Pilih operasi Matriks.")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Determinan")
        print("5. Inverse")
        choice = input("Pilih Operasi Matriks:")
    
        # Input nilai matriks
        a11 = float(input("a11: "))
        a12 = float(input("a12: "))
        a13 = float(input("a13: "))
        a21 = float(input("a21: "))
        a22 = float(input("a22: "))
        a23 = float(input("a23: "))
        a31 = float(input("a31: "))
        a32 = float(input("a32: "))
        a33 = float(input("a33: "))
        b11 = float(input("b11: "))
        b12 = float(input("b12: "))
        b13 = float(input("b13: "))
        b21 = float(input("b21: "))
        b22 = float(input("b22: "))
        b23 = float(input("b23: "))
        b31 = float(input("b31: "))
        b32 = float(input("b32: "))
        b33 = float(input("b33: "))
    
        # Definisi Matriksnya
        A = np.array([[a11,a12,a13], [a21,a22,a23], [a31,a32,a33]])
        B = np.array([[b11,b12,b13], [b21,b22,b23], [b31,b32,b33]])
    
        # Pilihan Operasi Matriks-nya
        if choice == '1':
            Add = A + B
            print(Add)
        elif choice == '2':
            Subtract = A - B
            print(Subtract)
        elif choice == '3':
            Multiplication = A.dot(B)
            print(Multiplication)
        elif choice == '4':
            Det_A = np.linalg.det(A)
            Det_B = np.linalg.det(B)
            print("Det A = ", Det_A)
            print("Det B = ", Det_B)
        elif choice == '5':
            Inv_A = np.linalg.inv(A)
            Inv_B = np.linalg.inv(B)
            print("Inverse A = ", Inv_A)
            print("Inverse B = ", Inv_B)
        else:
            print(" ")

    # Fungsi Trigonometri

    # Sin x
    elif choice == '9':
        x=int(input("Nilai x dalam derajat:"))
        print("sin x = ", round(sin(x),32))

    # Cos x
    elif choice == '10':
        x=int(input("Nilai x dalam derajat: "))
        print("cos x = ", round(cos(x),32))

    # Tan x
    elif choice == '11':
        x=int(input("Nilai x dalam derajat: "))
        print("tan x = ", round(tan(x),32))

    # Eksponensial
    elif choice == '12':
        print ("Eksponensial: ", round(exp(),32))

    #Pi
    elif choice == '13':
        print("Nilai Pi: ", round(calc(n),32))
        
    # Turunan
    elif choice == '14':
        print("Harus mengganti definisi def f(x) terlebih dahulu sebelum menurunkan dengan fungsi yang berbeda")
        x = float(input("x: "))
        h = float(input("h: "))
        result_1 = maju(f,x,h)
        result_2 = mundur(f,x,h)
        result_3 = tengah(f,x,h)
        print("Maju   = ", round(result_1,5))
        print("Mundur = ", round(result_2,5))
        print("Tengah = ", round(result_3,5))

    # Integral
    elif choice == '15':
        print("Harus mengganti definisi def f(x) terlebih dahulu sebelum mengintegralkan dengan fungsi yang berbeda")
        print("Menggunakan Metode Numerik Simpson-Trapezoid")
        a = float(input("Batas Awal: "))
        b = float(input("Batas Akhir: "))
        n = int(input("Iterasi: "))
        print ("Hasil Integrasi", simpson(f,a,b,n))

    #Eliminasi Gauss
    elif choice == '16':
        print("Pilih dimensi Matriks")
        print("1. 2x2")
        print("2. 3x3")
        print("3. 4x4")
        print("4. nxn")
        choice = input("Pilih dimensi Matriks:")

        # Matriks 2x2
        if choice == '1':
            a00 = float(input("a00: "))
            a01 = float(input("a01: "))
            a10 = float(input("a10: "))
            a11 = float(input("a11: "))
            b0 = float(input("b0: "))
            b1 = float(input("b1: "))
            A = [[a00, a01], [a10, a11]]
            b = [b0, b1]
            result = linearsolver(A,b)
            print(result)

        # Matriks 3x3
        elif choice == '2':
            a00 = float(input("a00: "))
            a01 = float(input("a01: "))
            a02 = float(input("a02: "))
            a10 = float(input("a10: "))
            a11 = float(input("a11: "))
            a12 = float(input("a12: "))
            a20 = float(input("a20: "))
            a21 = float(input("a21: "))
            a22 = float(input("a22: "))
            b0 = float(input("b0: "))
            b1 = float(input("b1: "))
            b2 = float(input("b2: "))
            A = [[a00, a01, a02], [a10, a11, a12], [a20, a21, a22]]
            b = [b0, b1, b2]
            result = linearsolver(A,b)
            print(result)

        # Matriks 4x4
        elif choice == '3':
            a00 = float(input("a00: "))
            a01 = float(input("a01: "))
            a02 = float(input("a02: "))
            a03 = float(input("a03: "))
            a10 = float(input("a10: "))
            a11 = float(input("a11: "))
            a12 = float(input("a12: "))
            a13 = float(input("a13: "))
            a20 = float(input("a20: "))
            a21 = float(input("a21: "))
            a22 = float(input("a22: "))
            a23 = float(input("a23: "))
            a30 = float(input("a30: "))
            a31 = float(input("a31: "))
            a32 = float(input("a32: "))
            a33 = float(input("a33: "))
            b0 = float(input("b0: "))
            b1 = float(input("b1: "))
            b2 = float(input("b2: "))
            b3 = float(input("b3: "))
            A = [[a00, a01, a02, a03], [a10, a11, a12, a13], [a20, a21, a22, a23], [a30, a31, a32, a33]]
            b = [b0, b1, b2, b3]
            result = linearsolver(A,b)
            print(result)

    # Jika tidak ada yang dipilih atau diluar pilihan itu
    else:
        print("Pilihlah aku jangan pilih dia")

# Generator Angka
elif choice == '2':
    n = int(input("Masukkan Angka Sebanyak2nya: "))
    if n > 10000001 :
        print("Kebanyakan Bossss!")
    elif n <= 0 :
        print("Anjay negatif")
    else:
        a = random.randrange(n)
        print("Generating....")
        print("Hasilnya: ",a)

# Gambar Grafik
elif choice == '3':
    a = 0
    b = 4*np.pi
    c = 0.1
    n = np.arange(a,b,c)
    x = np.sin(n)
    y = np.cos(n)
    z = np.tan(n)
    u = np.exp(n)
    print("")
    print("1. Sin Graph")
    plt.plot(n,x,color='g') 
    plt.show()
    print("")
    print("2. Cos Graph")
    plt.plot(n,y,color='g')
    plt.show()
    print("")
    print("3. Tan Graph")
    plt.plot(n,z,color='g')
    plt.show()
    print("")
    print("4. Exponential Graph")
    plt.plot(n,u,color='g')
    plt.show()
    print("kalo mau grafik lain, ganti sendiri yak fungsinya")

#Kalender Hari ini
elif choice == '4':
    from datetime import datetime
    now = datetime.now()
    now_str = now.strftime("%A, %d %B %Y"+" Pukul "+"%H:%M:%S")
    print("Hari ini: ",now_str)

#Tahun Kabisat
elif choice == '5':
    def check_year(year):
        if year%4==0 and year%100!=0 or year%400==0:
            print('Tahun Kabisat')
        else:
            print('Bukan Tahun Kabisat')
    year = int(input('Masukkan Tahun Disini:'))
    print(check_year(year))

#About Me
elif choice == '99':
    print("Terimakasih telah menggunakan aplikasi ini")
    print("Program ini dibuat dengan menggunakan bahasa Python")
    print("Dibuat oleh: Muhammad Naufal, Tahun 2019")
    print("Instagram: mu.naufal_")
    print("Facebook: m.naufal99")
    print("Twitter: munaufal__")

else:
    print("Pilihlah aku jangan pilih dia")