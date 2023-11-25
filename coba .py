import sqlite3
import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menambahkan data ke database
def tambah_data():
    nama = entry_nama.get()
    nilai_biologi = float(entry_biologi.get())
    nilai_fisika = float(entry_fisika.get())
    nilai_inggris = float(entry_inggris.get())
    nilai_matematika = float(entry_matematika.get())
    nilai_pjok = float(entry_pjok.get())
    nilai_aik = float(entry_aik.get())
    nilai_jawa = float(entry_jawa.get())
    nilai_ekonomi = float(entry_ekonomi.get())
    nilai_akuntansi = float(entry_akuntansi.get())
    nilai_jepang = float(entry_jepang.get())

    # Menentukan prediksi fakultas
    
        
    if nilai_biologi >= nilai_fisika and nilai_biologi >= nilai_inggris:
            prediksi = 'Kedokteran'
    elif nilai_fisika >= nilai_biologi and nilai_fisika >= nilai_inggris:
        prediksi = 'Teknik'
    elif nilai_inggris >= nilai_biologi and nilai_inggris >= nilai_fisika:
        prediksi = 'Bahasa'
    elif nilai_matematika >= nilai_biologi and nilai_matematika >= nilai_fisika:
        prediksi = 'Matematika'
    elif nilai_pjok >= nilai_biologi and nilai_pjok >= nilai_fisika:
        prediksi = 'Pendidikan Jasmani'
    elif nilai_aik >= nilai_biologi and nilai_aik >= nilai_fisika:
        prediksi = 'Ilmu Komputer'
    elif nilai_jawa >= nilai_biologi and nilai_jawa >= nilai_fisika:
        prediksi = 'Sastra Jawa'
    elif nilai_ekonomi >= nilai_biologi and nilai_ekonomi >= nilai_fisika:
        prediksi = 'Ekonomi'
    elif nilai_akuntansi >= nilai_biologi and nilai_akuntansi >= nilai_fisika:
        prediksi = 'Akuntansi'
    elif nilai_jepang >= nilai_biologi and nilai_jepang >= nilai_fisika:
        prediksi = 'Sastra Jepang'
    else:
        prediksi = 'Tidak Dapat Diprediksi'
    messagebox.showinfo("Hasil Prediksi", f"Prediksi Fakultas: {prediksi}")

    # Menyimpan data ke database
    conn = sqlite3.connect('dtb2.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS nilai_siswa (
                        nama_siswa TEXT,
                        biologi FLOAT,
                        fisika FLOAT,
                        inggris FLOAT,
                        matematika FLOAT,
                        pjok FLOAT,
                        aik FLOAT,
                        jawa FLOAT,
                        ekonomi FLOAT,
                        akuntansi FLOAT,
                        jepang FLOAT,
                        prediksi_fakultas TEXT
                    )''')
    cursor.execute("INSERT INTO nilai_siswa VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   (nama, nilai_biologi, nilai_fisika, nilai_inggris, nilai_matematika, nilai_pjok, nilai_aik, nilai_jawa, nilai_ekonomi, nilai_akuntansi, nilai_jepang, prediksi))
    conn.commit()
    conn.close()



# Membuat GUI menggunakan Tkinter
root = tk.Tk()
root.title("Input Nilai Siswa")

label_nama = tk.Label(root, text="Nama Siswa")
label_nama.grid(row=0, column=0)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

#1
label_biologi = tk.Label(root, text="Nilai Biologi")
label_biologi.grid(row=1, column=0)
entry_biologi = tk.Entry(root)
entry_biologi.grid(row=1, column=1)

#2
label_fisika = tk.Label(root, text="Nilai Fisika")
label_fisika.grid(row=2, column=0)
entry_fisika = tk.Entry(root)
entry_fisika.grid(row=2, column=1)

#3
label_inggris = tk.Label(root, text="Nilai Inggris")
label_inggris.grid(row=3, column=0)
entry_inggris = tk.Entry(root)
entry_inggris.grid(row=3, column=1)

#4
label_matematika = tk.Label(root, text="Nilai Matematika")
label_matematika.grid(row=4, column=0)
entry_matematika = tk.Entry(root)
entry_matematika.grid(row=4, column=1)

#5
label_pjok = tk.Label(root, text="Nilai Pjok")
label_pjok.grid(row=5, column=0)
entry_pjok = tk.Entry(root)
entry_pjok.grid(row=5, column=1)

#6
label_aik = tk.Label(root, text="Nilai AIK")
label_aik.grid(row=6, column=0)
entry_aik = tk.Entry(root)
entry_aik.grid(row=6, column=1)

#7
label_jawa = tk.Label(root, text="Nilai Jawa")
label_jawa.grid(row=7, column=0)
entry_jawa = tk.Entry(root)
entry_jawa.grid(row=7, column=1)

#8
label_ekonomi = tk.Label(root, text="Nilai Ekonomi")
label_ekonomi.grid(row=8, column=0)
entry_ekonomi = tk.Entry(root)
entry_ekonomi.grid(row=8, column=1)

#9
label_akuntansi = tk.Label(root, text="Nilai Akuntansi")
label_akuntansi.grid(row=9, column=0)
entry_akuntansi = tk.Entry(root)
entry_akuntansi.grid(row=9, column=1)

#10
label_jepang = tk.Label(root, text="Nilai Jepang")
label_jepang.grid(row=10, column=0)
entry_jepang = tk.Entry(root)
entry_jepang.grid(row=10, column=1)

button_submit = tk.Button(root, text="Submit", command=tambah_data)
button_submit.grid(row=11, column=0, columnspan=2)



root.mainloop()