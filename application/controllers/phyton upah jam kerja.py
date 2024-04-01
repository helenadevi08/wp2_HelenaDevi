upah_perjam=5000 #inisialisasi upah per jam
jml_jam_kerja=int("masukan jumlah jam kerja : ") #proses
jml_upah=jml__jam_kerja*upah_perjam*30 #proses
if jml_upah>150000: #decision
    pajak=0.05*jml_upah #proses
else:
    pajak=0
jml_terima=jml_upah-pajak #proses
print("Jumlah upah yang di terima adalah Rp, ",jml_terima) #output