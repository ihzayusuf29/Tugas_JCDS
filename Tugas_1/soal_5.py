if __name__== '__main__':
    #question_5
    jarak = 120
    kecepatan_a = 60
    kecepatan_b = 40
    waktu_temu = jarak / (kecepatan_a + kecepatan_b)
    
    waktu_temu_menit = waktu_temu * 60
    jam = waktu_temu_menit // 60
    sisa_menit = waktu_temu_menit % 60
    jam_mulai = 9

    print (f"mobil akan bertabrakan pada jam {int(jam_mulai) + int(jam)} lewat {int(sisa_menit)} menit waktu indonesia barat ")
