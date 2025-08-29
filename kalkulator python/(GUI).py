import tkinter as tk

# Membuat jendela utama
jendela = tk.Tk()
jendela.title("Kalkulator Keren")

# Membuat kotak teks untuk tampilan
layar_input = tk.Entry(jendela, width=35, borderwidth=5)
# Menempatkan kotak teks di baris paling atas
layar_input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def klik_tombol(simbol):
    layar_input.insert(tk.END, simbol)
    print("Tombol ditekan")

#membuat tombol 
tombol7 = tk.Button(jendela, text="7", command=lambda: klik_tombol("7"))
tombol8 = tk.Button(jendela, text="8", command=lambda: klik_tombol("8"))
tombol9 = tk.Button(jendela, text="9", command=lambda: klik_tombol("9"))
tombolBagi = tk.Button(jendela, text="/", command=lambda: klik_tombol("/"))
tombol4 = tk.Button(jendela, text="4", command=lambda: klik_tombol("4"))
tombol5 = tk.Button(jendela, text="5", command=lambda: klik_tombol("5"))
tombol6 = tk.Button(jendela, text="6", command=lambda: klik_tombol("6"))
tombolKali = tk.Button(jendela, text="*", command=lambda: klik_tombol("*"))
tombol1 = tk.Button(jendela, text="1", command=lambda: klik_tombol("1"))
tombol2 = tk.Button(jendela, text="2", command=lambda: klik_tombol("2"))
tombol3 = tk.Button(jendela, text="3", command=lambda: klik_tombol("3"))
tombolKurang = tk.Button(jendela, text="-", command=lambda: klik_tombol("-"))
tombol0 = tk.Button(jendela, text="0", command=lambda: klik_tombol("0"))
tombolTitik = tk.Button(jendela, text=".", command=lambda: klik_tombol("."))
tombolSamaDengan = tk.Button(jendela, text="=", command=lambda: klik_tombol("="))
tombolTambah = tk.Button(jendela, text="+", command=lambda: klik_tombol("+"))

# menempatkan tombol dengan grid
tombol7.grid(row=1, column=0)
tombol8.grid(row=1, column=1)
tombol9.grid(row=1, column=2)
tombolBagi.grid(row=1, column=3)
tombol4.grid(row=2, column=0)
tombol5.grid(row=2, column=1)
tombol6.grid(row=2, column=2)
tombolKali.grid(row=2, column=3)
tombol1.grid(row=3, column=0)
tombol2.grid(row=3, column=1)
tombol3.grid(row=3, column=2)
tombolKurang.grid(row=3, column=3)
tombol0.grid(row=4, column=0)
tombolTitik.grid(row=4, column=1)
tombolSamaDengan.grid(row=4, column=2)
tombolTambah.grid(row=4, column=3)




# Menjalankan program
jendela.mainloop()