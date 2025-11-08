import os
import csv

def header() :
    print("************************************")
    print("*       Welcome to AgroRent        *")
    print("************************************")
    print("silahkan pilih menu dibawah ini :")
    print("1. login admin")
    print("2. login user")
    print("3. register")
    menu = int(input())
    if menu == 1 :
        login_admin()
    elif menu == 2 :
        login_user()
    elif menu == 3 :
        register()
    else :
        print("menu tidak tersedia, tekan enter untuk mengulangi")
        header()

def register() :
    os.system("cls")
    print("************************************")
    print("*            Register              *")
    print("************************************")
    cek_username()
    with open('data_pengguna.csv' , mode='r') as file:
        username_terdaftar ={row['username'] for row in csv.DictReader(file)}
        
    username = input("masukkan username : ")
    if username in username_terdaftar :
        print("username sudah terdaftar, silahkan coba lagi")
        input("tekan enter untuk melanjutkan")
        register()

    while True :
        password = input("masukkan password : ")
        if len(password) < 5 :
            print("password minimal 5 karakter, silahkan coba lagi")
            continue

        konfirmasi_password = input("konfirmasi password : ")
        if password == konfirmasi_password :
            break
        else :
            print("password tidak sesuai, silahkan coba lagi")

    with open('data_pengguna.csv' , mode='a' , newline='') as file :
        writer = csv.writer(file)
        writer.writerow([username , password , 'user'])
    print("registrasi berhasil, silahkan login")
    input("tekan enter untuk melanjutkan")
    header()        

def login_admin():
    print("Fitur login admin belum diimplementasikan.")
    input("Tekan enter untuk kembali ke menu.")
    header()


def login_user():
    print("Fitur login user belum diimplementasikan.")
    input("Tekan enter untuk kembali ke menu.")
    header()

def cek_username():
    # Placeholder: currently only ensures the data file exists and has a header row
    if not os.path.exists('data_pengguna.csv'):
        with open('data_pengguna.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password', 'role'])  

if __name__ == "__main__": #artinya jika file ini dijalankan secara langsung, maka kode di dalam blok ini akan dieksekusi.
    header()