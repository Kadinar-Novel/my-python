"""
Contoh perulangan
"""


# Dengan for
print("Perulangan dengan for")
jumlah_buku = 10
print(f"Jumlah buku: {jumlah_buku}")

jumlah_buku_yang_sudah_dibaca = 0
for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_sudah_dibaca}")

# Dengan while
print("Perulangan dengan while")
jumlah_buku_while = 10
print(f"Jumlah buku: {jumlah_buku_while}")

jumlah_buku_while_yang_sudah_dibaca = 0
while jumlah_buku_while_yang_sudah_dibaca < jumlah_buku_while:
    jumlah_buku_while_yang_sudah_dibaca = jumlah_buku_while_yang_sudah_dibaca + 1
    if jumlah_buku_while_yang_sudah_dibaca == 5:
        print(f"Buku ke {jumlah_buku_while_yang_sudah_dibaca} ini sulit dibaca")
        break
    else:
        print(f"Pake while Buku ke {jumlah_buku_while_yang_sudah_dibaca} sudah dibaca")
