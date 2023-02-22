nam = input("Masukan Nama Lengkap Anda: ")
pro = input("Masukan Prodi Anda: ")
nil = input("Masukan Nilai (dalam huruf) yang Anda Dapat: ")
try:   
    if nil == 'A':
        print("Nilai masbro 4.00, Mantap kali masbro satu ini")
    elif nil == 'A-':
        print("Nilai masbro 3.75, kamu keren!")
    elif nil == 'B+':
        print("Nilai masbro 3.25, Lumayan bang")
    elif nil == 'B':
        print("Nilai masbro 3.0, ya masi okelah masbro")
    elif nil == 'B-':
        print("Nilai masbro 2.75, ayo masbro belajar lagi")
    elif nil == 'C+':
        print("Nilai masbro 2.25, okela bang masih lulus")
    elif nil == 'C':
        print("Nilai masbro 2.0, ada masalah apa masbro")
    elif nil == 'D':
        print("Nilai masbro 1.0, wadoo massbro kenapa ini")
    elif nil == 'E':
        print("Nilai masbro 0, sudah tidak tertolong")
    else:
        print("inputan masbro ga valid")
except:
    ()

    