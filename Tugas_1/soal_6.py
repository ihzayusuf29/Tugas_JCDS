if __name__== '__main__':
    #question_6
    apel = float(input("masukan jumlah apel: "))
    jeruk = float(input("masukan jumlah jeruk: "))
    anggur = float(input("masukan jumlah anggur: "))

    harga_apel = 10000
    harga_jeruk = 15000
    harga_anggur = 20000

    total_belanja = ((apel*harga_apel)+(jeruk*harga_jeruk)+(anggur*harga_anggur))
    print (f"total harga = {total_belanja}")
