import numpy as np

# Daftar buah, jumlah kalori per buah, harga per buah, dan stok buah
buah = ['Apel', 'Jeruk', 'Pisang', 'Kiwi', 'Mangga']
kalori_buah = [91, 71, 103, 105, 96]
harga_buah = [2360, 2120, 1890, 3870, 2870]
stok_buah = [5, 10, 5, 10, 5]

# Jumlah uang yang dimiliki oleh Pak Blangkon
uang_pak_blangkon = 25000

# Menghitung jumlah maksimal buah yang dapat dibeli
jumlah_buah_dibeli = np.minimum(stok_buah, np.floor(uang_pak_blangkon / np.array(harga_buah)))

# Menghitung jumlah maksimal kalori yang bisa didapatkan
total_kalori = np.sum(jumlah_buah_dibeli * np.array(kalori_buah))

print(int(total_kalori))  # Menampilkan jumlah maksimal kalori yang dapat didapatkan oleh Pak Blangkon

print(jumlah_buah_dibeli)

a = (5*2360)+(10*2120)+(5*1890)+(6*3870)+(5*2870)
print(a)