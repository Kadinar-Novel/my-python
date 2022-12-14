"""
Ooh gini bikin komentar di python
Semua sintaksis dasar bahasa pemograman teridir dari:
1. Sekuensial: langkah berurutan
2. Percabangan: langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""
# Sequential
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang haru saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telor beli 6"')
print('Maka Budi berangkat ke toko')
print("Dan mulai berbelanja")

# Percabangan
jumlah_botol_susu = 0
jumlah_telur = 1587

print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    print("Budi membeli 1 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang kerumah")
print("Menyampaikan hasilnya kepada ibu")