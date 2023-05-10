if __name__== '__main__':
    #question_3
    x = 485
    _1tahun = 360
    _1bulan = 30
    _1minggu = 7

    jumlah_tahun = x // _1tahun
    jumlah_bulan = ((x % _1tahun) // _1bulan)
    jumlah_minggu = (x % _1tahun) % _1bulan // _1minggu 
    jumlah_hari = (x % _1tahun) % _1bulan % _1minggu 

    print (f"{jumlah_tahun} tahun {jumlah_bulan} bulan {jumlah_minggu} minggu {jumlah_hari} hari")
