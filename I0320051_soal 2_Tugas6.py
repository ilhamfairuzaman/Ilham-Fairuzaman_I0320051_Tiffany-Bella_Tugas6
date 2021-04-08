def nomer2():
    # Data nilai murid
    datanile = []

    nile_murid = ' '

    # Input nilai
    while nile_murid != 'quit':
        nile_murid = input('Masukkan nilai murid, ketik "quit" jika sudah selesai\n>> ')
    #
        if nile_murid != 'quit':
            datanile.append(int(nile_murid))

    jumlah = len(datanile)
    rataan = sum(datanile)/jumlah
    print(rataan)


nomer2()