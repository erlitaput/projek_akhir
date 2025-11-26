import os
import csv
import pandas as pd
from tabulate import tabulate
from datetime import date, timedelta
 
MONTHS_ID = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
] 

def header() :
    os.system("cls")
    print("************************************")
    print("*       Welcome to AgroRent        *")
    print("************************************")
    print("silahkan pilih menu dibawah ini :")
    print("1. login admin")
    print("2. login user")
    print("3. register")
    menu = input("masukkan pilihan menu : ")
    if menu == '1' :
        login_admin()
    elif menu == '2' :
        login_user()
    elif menu == '3' :
        register()
    else :
        input("menu tidak tersedia, tekan enter untuk mengulangi")
        header()

def register() :
    os.system("cls")
    print("************************************")
    print("*            REGISTER              *")
    print("************************************")
    cek_username()
    with open('data_pengguna.csv' , mode='r') as file:
        username_terdaftar ={row['username'] for row in csv.DictReader(file)} #
        
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
    os.system("cls")
    global admin_username
    print("************************************")
    print("*           LOGIN ADMIN            *")
    print("************************************")
    username = input("masukkan username : ")
    password = input("masukkan password : ")   

    loginsukses = False 
    role_valid = False
    with open('data_pengguna.csv' , mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                loginsukses = True
                if row['role'] == 'admin':
                    role_valid = True
                break
    if loginsukses and role_valid: 
        
        admin_username = username
        print("login berhasil, selamat datang admin", username)
        input('tekan entek untuk melanjutkan')
        os.system('cls')
        menuadmin()
    elif loginsukses and not role_valid:
        print("anda bukan admin, silahkan login sebagai user")
        input("tekan enter untuk melanjutkan")
        os.system('cls')
        header()
    else :
        print("username atau password salah, silahkan coba lagi")
        input("tekan enter untuk melanjutkan")
        os.system('cls')
        header()


def login_user():
    os.system('cls')
    global penyewa_username
    print("************************************")
    print("*           LOGIN USER             *")
    print("************************************")
    global username
    username = input("masukkan username : ")
    password = input("masukkan password : ")   

    loginsukses = False 
    role_valid = False
    with open('data_pengguna.csv' , mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                loginsukses = True
                if row['role'] == 'user':
                    role_valid = True
                break
    if loginsukses and role_valid:
        penyewa_username = username
        print("login berhasil, selamat datang ", username)
        input('tekan enter untuk melanjutkan')
        os.system('cls')
        tampilan_user()
    elif loginsukses and not role_valid:
        print("anda bukan user, silahkan login sebagai admin")
        input("tekan enter untuk melanjutkan")
        os.system('cls')
        header()
    else :
        print("username atau password salah, silahkan coba lagi")
        input("tekan enter untuk melanjutkan")
        os.system('cls')
        login_user()

def cek_username():
    if not os.path.exists('data_pengguna.csv'):
        with open('data_pengguna.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'password', 'role'])  


def cek_riwayat():
    if not os.path.exists('riwayat.csv'):
        with open('riwayat.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['username', 'id alat', 'nama alat', 'jumlah', 'tanggal sewa', 'tanggal kembali', 'hari sewa', 'total harga', 'alamat', 'nomor telepon', 'status', 'denda', 'kritik/saran'])  



def tampilan_user():
    while True :
        os.system('cls')
        print("************************************")
        print("*          TAMPILAN USER           *")
        print("************************************")
        print("silahkan pilih menu dibawah ini :")
        print("1. sewa alat")
        print("2. konfirmasi pengembalian")
        print("3. logout")
        pilihan = input("masukkan pilihan menu : ")
        if pilihan == '1' :
            os.system('cls')
            sewa_alat()
        elif pilihan == '2' :
            os.system('cls')
            konfirmasi_pengembalian()
        elif pilihan == '3' :
            os.system('cls')
            print("anda telah logout")
            input("tekan enter untuk melanjutkan")
            header()
            break
        else :
            input("pilihan tidak ditemukan, tekan enter untuk mengulangi")
            continue
    

def sewa_alat() :
    while True:
        os.system('cls')
        daftar_alat = pd.read_csv('data_alat.csv', sep=',')
        print("************************************")
        print("*          PENYEWAAN ALAT          *")
        print("************************************") 
        print("\n=== Daftar Alat yang Tersedia ===\n")
        print(tabulate(daftar_alat, headers='keys', tablefmt='psql', showindex=False))
        id_alat = input("masukkan ID alat yang ingin disewa:")
        if not id_alat.isdigit():
            print("Input harus angka! Silakan masukkan angka yang benar")
            input("tekan enter untuk mengulang")
            continue
        id_alat = int(id_alat)
        alat_dipilih = daftar_alat[daftar_alat['id'] == id_alat]
        if alat_dipilih.empty:
            print("Alat tersebut tidak ditemukan.")
            input("Tekan enter untuk kembali ke menu.")
            continue
        break
        
    os.system('cls')
    print("\n=== Detail Alat ===")
    print(tabulate(alat_dipilih, headers="keys", tablefmt="fancy_grid", showindex=False) )
    while True:
        jumlah_sewa = input("Masukkan jumlah alat yang ingin disewa: ")
        if not jumlah_sewa.isdigit():
            print("Input harus angka! Silakan masukkan angka yang benar")
            input("tekan enter untuk mengulang")
            continue
        jumlah_sewa = int(jumlah_sewa)
        if jumlah_sewa > int(alat_dipilih['stok'].values[0]):
            print("mohon maaf stok tidak mencukupi.")
            input("Tekan enter untuk kembali ke menu.")
            sewa_alat()
            return

        os.system('cls')
        print("silahkan pilih :")
        print("1. sewa hari ini")
        print("2. sewa untuk tanggal tertentu")
        input_pilih = input("Masukkan pilihan (1/2): ")
        
        if input_pilih == '2':
            while True :
                try:
                    tanggal_penyewaan = int(input("masukkan tanggal penyewaan : "))
                    bulan_penyewaan = input("masukkan bulan : ").lower()
                    tahun_penyewaan = int(input("masukkan tahun : "))
                    bulan_index = next((i+1 for i, m in enumerate(MONTHS_ID) if m.lower() == bulan_penyewaan), None)
                    if bulan_index is None:
                        print("Bulan tidak dikenali, gunakan nama bulan contoh (januari).")
                        input("tekan enter untuk mengulangi")
                        continue
                    tanggal_penyewaan_date = date(tahun_penyewaan, bulan_index, tanggal_penyewaan)

                    if tanggal_penyewaan_date < date.today():
                        print ("tanggal harus lebih dari hari ini")
                        input("tekan enter untuk mengulangi")
                        continue
                    break                
                except Exception as e:
                    print(f"Input tanggal tidak valid ({e}),")
                    input("tekan enter untuk mengulangi")
                    continue
        elif input_pilih == "1":
            tanggal_penyewaan_date = date.today()
        else :
            print("pilihan invalid")
            input("tekan enter untuk kembali ke menu")
            sewa_alat()

        hari_sewa = int(input("berapa lama sewa (harian dalam bentuk angka): "))
        if hari_sewa <= 0 or "":
            print("Lama sewa harus lebih dari 0 hari.")
            input("Tekan enter untuk kembali ke menu.")
            sewa_alat()

        tanggal_pengembalian_date = tanggal_penyewaan_date + timedelta(days=hari_sewa)

        def format_id(d: date) -> str:
            return f"{d.day}/{MONTHS_ID[d.month-1].lower()} {d.year}"

        tanggal_sewa_full = format_id(tanggal_penyewaan_date)
        tanggal_kembali_full = format_id(tanggal_pengembalian_date)

        tanggal_penyewaan = tanggal_penyewaan_date.day
        bulan_tahun_penyewaan = f"{MONTHS_ID[tanggal_penyewaan_date.month-1].lower()} {tanggal_penyewaan_date.year}"

        harga_per_hari = int(alat_dipilih['harga/hari'].values[0].replace('Rp. ', '').replace('.', ''))
        total_harga = harga_per_hari * jumlah_sewa * hari_sewa
        nama_alat = alat_dipilih['nama'].values[0]
        while True:
            os.system('cls')
            print(f'''\nTotal harga sewa untuk {jumlah_sewa} unit {nama_alat} selama {hari_sewa} hari adalah: Rp. {total_harga}. Disewa pada {tanggal_sewa_full} dan harus dikembalikan pada {tanggal_kembali_full}''' )

            konfirmasi = input("Apakah Anda ingin melanjutkan penyewaan? (y/n): ")
            if konfirmasi.lower() == 'y':
                cek_riwayat()
                while True:
                    os.system('cls')
                    alamat = input("Masukkan alamat pengiriman alat: ")
                    nomor_telepon = input("Masukkan nomor telepon yang dapat dihubungi: ")
                    if not alamat or not nomor_telepon :
                        print("Alamat dan nomor telepon tidak boleh kosong.")
                        input("Tekan enter untuk mengulangi.")
                        continue
                    id_alat = int(alat_dipilih['id'].values[0])
                    nama_alat = alat_dipilih['nama'].values[0]
                    with open('riwayat.csv', mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([
                            penyewa_username,
                            id_alat,
                            nama_alat,
                            jumlah_sewa,
                            tanggal_sewa_full,
                            tanggal_kembali_full,
                            hari_sewa,
                            total_harga,
                            alamat,
                            nomor_telepon,
                            'belum_dikembalikan',
                            '0',
                            ''
                        ])
                    print("Penyewaan berhasil! Terima kasih telah menggunakan layanan kami.")
                    input("Tekan enter untuk kembali ke menu.")
                    daftar_alat.loc[daftar_alat['id'] == id_alat, 'stok'] = \
                        daftar_alat.loc[daftar_alat['id'] == id_alat, 'stok'].values[0] - jumlah_sewa
                    daftar_alat.to_csv('data_alat.csv', index=False)
                    break
                break
            elif konfirmasi.lower() == 'n':
                print("Penyewaan dibatalkan.")
                input("Tekan enter untuk kembali ke menu.")
                tampilan_user()
                return
            else:
                print("Pilihan tidak valid. pilihan tidak boleh kosong.")
                input("Tekan enter untuk kembali ke menu.")
                continue 
        break
    return      

def konfirmasi_pengembalian():
    riwayat = pd.read_csv('riwayat.csv', sep=',')
    
    username_penyewa = username
    penyewaan_user = riwayat[(riwayat['username'] == username_penyewa) & (riwayat['status'] == 'belum_dikembalikan')]
    
    if penyewaan_user.empty:
        print("Tidak ada riwayat penyewaan yang belum dikembalikan untuk username tersebut.")
        input("Tekan enter untuk kembali ke menu.")
        tampilan_user()
    else:
        while True:
            os.system('cls')
            print("************************************")
            print("*      KONFIRMASI PENGEMBALIAN     *")
            print("************************************")
            print("\n=== Daftar Penyewaan yang Belum Dikembalikan ===")
            penyewa_username = penyewaan_user[['id alat', 'nama alat', 'jumlah', 'tanggal sewa', 'tanggal kembali', 'total harga']]
            print(tabulate(penyewa_username, headers="keys", tablefmt="fancy_grid", showindex=False) )
            print()

            id_alat = input("masukkan ID alat yang dikembalikan:")
            if not id_alat.isdigit():
                print("Input tidak boleh kosong dan harus angka! Silakan masukkan angka yang benar")
                input("tekan enter untuk mengulang")
                continue
            id_alat = int(id_alat)
            penyewaan_dipilih = penyewaan_user[penyewaan_user['id alat'] == id_alat]

            if penyewaan_dipilih.empty:
                print("Alat dengan ID tersebut tidak ditemukan dalam riwayat penyewaan Anda.")
                input("Tekan enter untuk kembali ke menu.")
                continue
            break
    
        os.system('cls')
        print("\n=== Detail Pengembalian ===")
        print(f"Nama Alat: {penyewaan_dipilih['nama alat'].values[0]}")
        print(f"Jumlah: {penyewaan_dipilih['jumlah'].values[0]} unit")
        print(f"Tanggal Seharusnya Dikembalikan: {penyewaan_dipilih['tanggal kembali'].values[0]}")
        print(f"Total Biaya Sewa: Rp. {penyewaan_dipilih['total harga'].values[0]}")
        print()
            
        while True:
            gunakan_hari_ini = input("Gunakan tanggal hari ini sebagai tanggal pengembalian? (y/n): ").strip().lower()
            
            if gunakan_hari_ini == 'y' :
                actual_date = date.today()
                break

            elif gunakan_hari_ini == 'n':
                while True:
                    try:
                        hari_input = int(input("masukkan tanggal pengembalian (angka hari): "))
                        bulan_tahun_input = input("masukkan bulan dan tahun pengembalian (contoh: maret 2025): ").strip()
                        parts = bulan_tahun_input.split()
                        if len(parts) < 2:
                            print("Format harus berisi bulan dan tahun. Contoh: maret 2025")
                            continue
                        bulan_name = parts[0].lower()
                        tahun_input = int(parts[1]) if len(parts) > 1 else date.today().year
                        bulan_index = next((i+1 for i, m in enumerate(MONTHS_ID) if m.lower() == bulan_name), None)
                        if bulan_index is None:
                            print("Bulan tidak dikenali,Contoh: januari, februari, maret.")
                            continue
                        actual_date = date(tahun_input, bulan_index, hari_input)
                    except ValueError:
                        print("Input tanggal tidak valid, coba lagi")
                        continue
                    break

            elif gunakan_hari_ini != 'n' or gunakan_hari_ini != 'y':
                os.system('cls')
                print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")
                input("Tekan enter untuk mengulang.")
                continue  
            break
    
        try:
            t_kembali_str = penyewaan_dipilih['tanggal kembali'].values[0]
            day_str, rest = t_kembali_str.split(' ', 1)
            day_expected = int(day_str)
            month_part = rest.strip()
            month_name_expected = month_part.split()[0].lower()
            year_expected = int(month_part.split()[1]) if len(month_part.split()) > 1 else date.today().year
            month_expected = next((i+1 for i, m in enumerate(MONTHS_ID) if m.lower() == month_name_expected), date.today().month)
            expected_date = date(year_expected, month_expected, day_expected)
        except Exception:
            expected_date = date.today()

        hari_terlambat = max(0, (actual_date - expected_date).days)
        denda_per_hari = 50000
        total_denda = hari_terlambat * denda_per_hari
        
        if hari_terlambat > 0:
            print(f"\n TERLAMBAT {hari_terlambat} hari!")
            print(f"Denda: {hari_terlambat} hari × Rp. 50.000 = Rp. {total_denda}")
        else:
            print("\n Pengembalian tepat waktu, tidak ada denda.")
        
        print("\nmasukkan kritik/saran (optional, tekan Enter jika tidak ada):")
        kritik_saran = input().strip()
        while True:
            print("\nApakah Anda yakin ingin melanjutkan pengembalian? (y/n):")
            konfirmasi = input().lower()
            
            if konfirmasi == 'y':
                riwayat.loc[(riwayat['username'] == username_penyewa) & 
                        (riwayat['id alat'] == id_alat) & 
                        (riwayat['status'] == 'belum_dikembalikan'), 'status'] = 'sudah_dikembalikan'
                riwayat.loc[(riwayat['username'] == username_penyewa) & 
                        (riwayat['id alat'] == id_alat) & 
                        (riwayat['status'] == 'sudah_dikembalikan'), 'denda'] = total_denda
                riwayat.loc[(riwayat['username'] == username_penyewa) & 
                        (riwayat['id alat'] == id_alat) & 
                        (riwayat['status'] == 'sudah_dikembalikan'), 'kritik/saran'] = kritik_saran
                
                riwayat.to_csv('riwayat.csv', index=False)
                
                daftar_alat = pd.read_csv('data_alat.csv', sep=',')
                jumlah_kembali = int(penyewaan_dipilih['jumlah'].values[0])
                daftar_alat.loc[daftar_alat['id'] == id_alat, 'stok'] = \
                    daftar_alat.loc[daftar_alat['id'] == id_alat, 'stok'].values[0] + jumlah_kembali
                daftar_alat.to_csv('data_alat.csv', index=False)
                
                os.system('cls')
                print("\n" + "="*50)
                print("Pengembalian Berhasil Diproses!")
                print("="*50)
                print(f"Alat: {penyewaan_dipilih['nama alat'].values[0]}")
                print(f"Jumlah: {jumlah_kembali} unit")
                print(f"Total Biaya Sewa: Rp. {penyewaan_dipilih['total harga'].values[0]}")
                print(f"Denda Keterlambatan: Rp. {total_denda}")
                print(f"Total Pembayaran: Rp. {int(penyewaan_dipilih['total harga'].values[0]) + total_denda}")
                print("="*50)
                input("Tekan enter untuk kembali ke menu.")
                tampilan_user()
                

            elif konfirmasi == 'n':
                print("Pengembalian dibatalkan.")
                input("Tekan enter untuk kembali ke menu.")
                tampilan_user()

            else:
                print("Pilihan tidak valid. pilihan tidak boleh kosong.")
                input("Tekan enter untuk mengulang.")
                continue


def lihat_barang():
    os.system('cls')
    print("************************************")
    print("*          DAFTAR BARANG           *")
    print("************************************")
    df = pd.read_csv("data_alat.csv")
    if df.empty:
        print("Belum ada barang.\n")
    else:
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
    input("\nTekan Enter untuk kembali ke menu.")

def tambah_barang():
    os.system('cls')
    print("************************************")
    print("*          TAMBAH BARANG           *")
    print("************************************")
    nama = input("Nama: ")
    merk = input("Merk: ")
    deskripsi = input("Deskripsi: ")
    while True:
        stok = input("Stok: ")
        if stok.isdigit():
            stok = int(stok)
            break
        else:
            print("Stok harus berupa angka!")
    while True:
        harga = input("Harga/hari: ")
        if harga.isdigit():
            harga = f"Rp. {harga}"
            break
        else:
            print("Harga harus berupa angka!")
    if os.path.exists("data_alat.csv"):
        df = pd.read_csv("data_alat.csv")
        if df.empty:
            next_id = 1
        else:
            next_id = df['id'].max() + 1
    else:
        next_id = 1
        df = pd.DataFrame(columns=["id", "nama", "merk", "deskripsi", "stok", "harga/hari"])
    data_baru = pd.DataFrame([{
        "id": next_id,
        "nama": nama,
        "merk": merk,
        "deskripsi": deskripsi,
        "stok": stok,
        "harga/hari": harga
    }])
    df = pd.concat([df, data_baru], ignore_index=True)
    df.to_csv("data_alat.csv", index=False)
    print(f"\nBarang '{nama}' berhasil ditambahkan!\n")
    input("Tekan Enter untuk kembali ke menu.")

def edit_barang():
    while True:
        os.system('cls')
        print("************************************")
        print("*            EDIT BARANG           *")
        print("************************************")
        df = pd.read_csv("data_alat.csv")
        if df.empty:
            print("Belum ada barang untuk diedit.\n")
            input("Tekan Enter untuk kembali.")
            break
        for i, row in df.iterrows():
            print(f"{i+1}. {row['nama']} ({row['merk']})")
        try:
            idx = int(input("Pilih nomor barang yang ingin diedit: ")) - 1
            if 0 <= idx < len(df):
                barang = df.loc[idx]
                print("\nTekan Enter jika tidak ingin mengubah nilai.")
                df.loc[idx, "nama"] = input(f"Nama [{barang['nama']}]: ") or barang['nama']
                df.loc[idx, "merk"] = input(f"Merk [{barang['merk']}]: ") or barang['merk']
                df.loc[idx, "deskripsi"] = input(f"Deskripsi [{barang['deskripsi']}]: ") or barang['deskripsi']

                while True:
                    stok_baru = input(f"Stok [{barang['stok']}]: ")
                    if stok_baru == "":
                        df.loc[idx, "stok"] = barang["stok"]
                        break
                    if stok_baru.isdigit():
                        df.loc[idx, "stok"] = int(stok_baru)
                        break
                    else:
                        print("Stok harus berupa angka")

                while True:
                    harga_baru = input(f"Harga/hari [{barang['harga/hari']}]: ")

                    if harga_baru == "":
                        df.loc[idx, "harga/hari"] = barang["harga/hari"]
                        break

                    if harga_baru.isdigit():
                        df.loc[idx, "harga/hari"] = f"Rp. {harga_baru}"
                        break
                    else:
                        print("Harga/hari harus berupa angka")

                df.to_csv("data_alat.csv", index=False)
                print(f"\nBarang '{df.loc[idx, 'nama']}' berhasil diperbarui!\n")
                input("Tekan Enter untuk kembali.")
                break
                
            else:
                input("Pilihan invalid, tekan enter untuk ulang")
                os.system('cls')
        except ValueError:
            input("Inputan harus berupa angka")
            os.system('cls')

def hapus_barang():
    while True:
        os.system('cls')
        print("************************************")
        print("*           HAPUS BARANG           *")
        print("************************************")

        df = pd.read_csv("data_alat.csv")
        if df.empty:
            print("Belum ada barang untuk dihapus.\n")
            input("Tekan Enter untuk kembali.")
            return

        for i, row in df.iterrows():
            print(f"{i+1}. {row['nama']} ({row['merk']})")
        try:
            idx = int(input("Pilih barang yang ingin dihapus: ")) - 1
            if 0 <= idx < len(df):
                nama = df.loc[idx, "nama"]
                df = df.drop(idx).reset_index(drop=True)
                df.to_csv("data_alat.csv", index=False)
                print(f"\nBarang '{nama}' berhasil dihapus!\n")
                input("Tekan Enter untuk kembali.")
                break
            else:
                input("Pilihan invalid, tekan enter untuk ulang")
                os.system('cls')
        
        except ValueError:
            input("Inputan harus berupa angka")
            os.system('cls')

def history_penyewaan() :
    os.system('cls')
    print("************************************")
    print("*        HISTORY PENYEWAAN         *")
    print("************************************") 
    riwayat = pd.read_csv('riwayat.csv', sep=',')
    print(tabulate(riwayat, headers='keys', tablefmt='fancy_grid', showindex=False))
    input("Tekan enter untuk kembali ke menu")


def menuadmin():
    while True:
        os.system('cls')
        print("************************************")
        print("*         MENU ADMIN AGRORENT      *")
        print("************************************")
        print("1. Daftar Barang")
        print("2. Tambah Barang")
        print("3. Edit Barang")
        print("4. Hapus Barang")
        print("5. History")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            lihat_barang()
        elif pilihan == "2":
            tambah_barang()
        elif pilihan == "3":
            edit_barang()
        elif pilihan == "4":
            hapus_barang()
        elif pilihan == "5":
            history_penyewaan()
        elif pilihan == "6":
            print("Anda telah keluar dari menu admin.")
            input("Tekan enter untuk kembali ke menu utama.")
            os.system('cls')
            header()
            break
        else:
            input("Pilihan invalid, tekan enter untuk kembali ke menu.")
            os.system('cls')
        menuadmin()

if __name__ == "__main__":
    header()