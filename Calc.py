def Tam(A, B):
    return A + B
def Kal(A, B):
    return A * B
def Bag(A, B):
    return A / B
def Kur(A, B):
    return A - B
def Pang(A, B):
    return A ** B
while True:
    var = input("Pilih mode [Calc]ulator, [Conv]ersion, atau [Exit] (Keluar): ").lower()
    if var == "exit":
        break
    elif var == "conv":
        mode = input("Masukkan Jenis Konversi: (Suhu, Byte, Jarak): (Ketik [Exit] untuk kembali ke menu utama)\n").lower()
        if mode == "suhu":
            shu = input("°C ke °F [1], °F ke °C [2]: ")
            if shu == "1":
                C1 = float(input("Masukkan Celcius: "))
                F1 = (C1 * 9/5) + 32
                print(f"{C1}°C dalam Fahrenheit adalah {F1}°F")
            elif shu == "2":
                F2 = float(input("Masukkan Fahrenheit: "))
                C2 = (F2 - 32) * 5/9
                print(f"{F2}°F dalam Celcius adalah {C2}°C")
            elif shu == "exit":
                continue
        elif mode == "byte":
            dat = input("Pilih konversi:\n"
                        "1. KB ke MB\n"
                        "2. MB ke GB\n"
                        "3. KB ke GB\n"
                        "4. GB ke KB\n"
                        "5. GB ke MB\n"
                        "6. MB ke KB\n"
                        "Pilihan: ")
            if dat == "1":
                kb = float(input("Masukkan jumlah kilobyte (KB): "))
                mb = kb / 1024
                print(f"{kb} KB sama dengan {mb} MB")
            elif dat == "2":
                mb = float(input("Masukkan jumlah megabyte (MB): "))
                gb = mb / 1024
                print(f"{mb} MB sama dengan {gb} GB")
            elif dat == "3":
                kb = float(input("Masukkan jumlah kilobyte (KB): "))
                gb = kb / 1024**2
                print(f"{kb} KB sama dengan {gb} GB")
            elif dat == "4":
                gb = float(input("Masukkan jumlah gigabyte (GB): "))
                kb = gb * 1024**2
                print(f"{gb} GB sama dengan {kb} KB")
            elif dat == "5":
                gb = float(input("Masukkan jumlah gigabyte (GB): "))
                mb = gb * 1024
                print(f"{gb} GB sama dengan {mb} MB")
            elif dat == "6":
                mb = float(input("Masukkan jumlah megabyte (MB): "))
                kb = mb * 1024
                print(f"{mb} MB sama dengan {kb} KB")
            elif dat == "exit":
                continue
        elif mode == "jarak":
            jar = input("Pilih konversi jarak:\n"
            "1. KM ke M\n"
            "2. M ke CM\n"
            "3. CM ke MM\n"
            "4. MM ke CM\n"
            "5. CM ke M\n"
            "6. M ke KM\n"
            "7. KM ke MM\n"
            "8. MM ke KM\n"
            "Pilihan: ")
            if jar == "1":
                km = float(input("Masukkan jumlah kilometer (KM): "))
                m = km * 1000
                print(f"{km} KM sama dengan {m} M")
            elif jar == "2":
                m = float(input("Masukkan jumlah meter (M): "))
                cm = m * 100
                print(f"{m} M sama dengan {cm} CM")
            elif jar == "3":
                cm = float(input("Masukkan jumlah sentimeter (CM): "))
                mm = cm * 10
                print(f"{cm} CM sama dengan {mm} MM")
            elif jar == "4":
                mm = float(input("Masukkan jumlah milimeter (MM): "))
                cm = mm / 10
                print(f"{mm} MM sama dengan {cm} CM")
            elif jar == "5":
                cm = float(input("Masukkan jumlah sentimeter (CM): "))
                m = cm / 100
                print(f"{cm} CM sama dengan {m} M")
            elif jar == "6":
                m = float(input("Masukkan jumlah meter (M): "))
                km = m / 1000
                print(f"{m} M sama dengan {km} KM")
            elif jar == "7":
                km = float(input("Masukkan jumlah kilometer (KM): "))
                mm = km * 1000000
                print(f"{km} KM sama dengan {mm} MM")
            elif jar == "8":
                mm = float(input("Masukkan jumlah milimeter (MM): "))
                km = mm / 1000000
                print(f"{mm} MM sama dengan {km} KM")
            elif jar == "exit":
                continue
        elif mode == "exit":
            continue
        else:
            print("Pilihan tidak valid.")
    elif var == "calc":
        A1 = float(input("Masukkan Angka1: "))
        var = "y"
        while True:
            if var.lower() == "n":
                break
            elif var.lower() == "y":
                A2 = float(input("Masukkan Angka2: "))
                OP = input("Masukkan Operator (+, -, *, /, **): ")
                if OP == "*":
                    hasil = Kal(A1, A2)
                    print("Hasil:", hasil)
                elif OP == "+":
                    hasil = Tam(A1, A2)
                    print("Hasil:", hasil)
                elif OP == "**":
                    hasil = Pang(A1, A2)
                    print("Hasil:", hasil)
                elif OP == "-":
                    hasil = Kur(A1, A2)
                    print("Hasil:", hasil)
                elif OP == "/":
                    hasil = Bag(A1, A2)
                    print("Hasil:", hasil)
                A1 = hasil
            var = input("Lanjut? (Y/N): ")
            if var.lower() == "n":
                break