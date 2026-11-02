import modul_evaluasi


def input_angka_valid(prompt, min_val, max_val):
    """Meminta input angka (float) yang valid dalam rentang min_val - max_val."""
    while True:
        try:
            nilai = float(input(prompt))
        except ValueError:
            print("  [Error] Input harus berupa angka, bukan huruf/teks. Coba lagi.")
            continue

        if nilai < min_val or nilai > max_val:
            print(f"  [Warning] Angka harus di antara {min_val} sampai {max_val}. Coba lagi.")
            continue

        return nilai


def proses_kelayakan():
    """Meminta data calon aslab, menghitung, dan menampilkan hasilnya."""
    print("\n--- Input Data Calon Asisten ---")
    nama = input("Nama                    : ")
    nim = input("NIM                     : ")
    hadir = input_angka_valid("Jumlah kehadiran (0-14) : ", 0, 14)
    tugas = input_angka_valid("Nilai Tugas (0-100)     : ", 0, 100)
    ucp1 = input_angka_valid("Nilai UCP 1 (0-100)     : ", 0, 100)
    ucp2 = input_angka_valid("Nilai UCP 2 (0-100)     : ", 0, 100)

    persen = modul_evaluasi.hitung_persentase_presensi(hadir)
    nilai_akhir = modul_evaluasi.hitung_nilai_akhir(tugas, ucp1, ucp2)
    status = modul_evaluasi.cek_kelayakan_aslab(persen, nilai_akhir)

    print("\n" + "=" * 45)
    print("        HASIL EVALUASI KELAYAKAN ASLAB")
    print("=" * 45)
    print(f"Nama               : {nama}")
    print(f"NIM                : {nim}")
    print(f"Kehadiran          : {hadir:.0f} dari 14 pertemuan")
    print(f"Persentase Presensi: {persen:.2f}%")
    print(f"Nilai Akhir        : {nilai_akhir:.2f}")
    print(f"Status             : {status}")
    print("=" * 45)


def main():
    while True:
        print("\n===== SISTEM EVALUASI ASLAB AI =====")
        print("1. Hitung Kelayakan")
        print("2. Keluar")

        try:
            pilihan = int(input("Pilih menu (1/2): "))
        except ValueError:
            print("  [Error] Menu harus berupa angka 1 atau 2.")
            continue

        if pilihan == 1:
            proses_kelayakan()
        elif pilihan == 2:
            print("Terima kasih. Program selesai.")
            break
        else:
            print("  [Warning] Pilihan tidak tersedia. Pilih 1 atau 2.")


if __name__ == "__main__":
    main()