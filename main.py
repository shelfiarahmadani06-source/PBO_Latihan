from hash_manager import HashManager

from md5_hash import MD5Hash
from sha1_hash import SHA1Hash
from sha256_hash import SHA256Hash
from sha512_hash import SHA512Hash


def tampilkan_menu():
    print("\n=== PROGRAM HASH STRING ===")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA512")
    print("0. Keluar")


def pilih_algoritma(pilihan):

    if pilihan == "1":
        return MD5Hash()

    elif pilihan == "2":
        return SHA1Hash()

    elif pilihan == "3":
        return SHA256Hash()

    elif pilihan == "4":
        return SHA512Hash()

    else:
        return None


def main():

    manager = HashManager()

    while True:

        tampilkan_menu()

        pilihan = input("Pilih algoritma: ")

        if pilihan == "0":
            print("Program selesai")
            break

        algoritma = pilih_algoritma(pilihan)

        if algoritma is None:
            print("Pilihan tidak valid")
            continue

        manager.set_algorithm(algoritma)

        text = input("Masukkan text: ")

        hasil = manager.generate_hash(text)

        print("\nAlgoritma :", algoritma.name)
        print("Hash      :", hasil)


if __name__ == "__main__":
    main()