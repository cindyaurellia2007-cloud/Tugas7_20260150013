def hitung_persentase_presensi(hadir, total_pertemuan=14):
    """Menghitung persentase kehadiran (0-100)."""
    return(hadir / total_pertemuan) * 100

def hitung_nilai_akhir(tugas, ucp1, ucp2):
    """Menghitung nilai akhir berdasarkan bobot tugas, UCP1, dan UCP2."""
    return (tugas * 0.20) + (ucp1 * 0.40) + (ucp2 * 0.40)

def cek_kelayakan_aslab(persentase_presensi, nilai_akhir):
    """Mengembalikan status kelayakan calon asisten laboratorium."""
    if persentase_presensi >= 75.0:
        return "DITOLAK (Kehadiran dibawah 75%)"
    elif nilai_akhir >= 75.0:
        return "DITERIMA (memenuhi syarat)"
    else:
        return "DITOLAK (Nilai akhir kurang)"