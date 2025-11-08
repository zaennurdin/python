from pddiktipy import api
from pprint import pprint


def main():
    # Minta input nama dari user
    nama = input("Masukkan nama mahasiswa yang ingin dicari: ")

    # Validasi agar tidak kosong
    if not nama.strip():
        print("Nama tidak boleh kosong.")
        return

    # Gunakan context manager API
    with api() as client:
        print(f"\n🔍 Mencari data mahasiswa dengan nama: {nama}\n")
        try:
            hasil = client.search_mahasiswa(nama)
            if hasil:
                pprint(hasil)
            else:
                print("⚠️ Tidak ditemukan data untuk nama tersebut.")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")


if __name__ == "__main__":
    main()
