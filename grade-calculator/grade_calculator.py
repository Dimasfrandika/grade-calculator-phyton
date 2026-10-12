"""Mini program: Kalkulator Nilai Mahasiswa.

Berisi 4 fungsi yang akan diuji dengan unit test:
- hitung_rata_rata(nilai)
- tentukan_grade(nilai_akhir)
- hitung_nilai_akhir(tugas, uts, uas)
- is_lulus(nilai_akhir, batas=60)
"""

BOBOT_TUGAS = 0.30
BOBOT_UTS = 0.30
BOBOT_UAS = 0.40


def _validasi_nilai(nilai):
    """Pastikan nilai berupa angka antara 0 dan 100."""
    if isinstance(nilai, bool) or not isinstance(nilai, (int, float)):
        raise TypeError("Nilai harus berupa angka")
    if nilai < 0 or nilai > 100:
        raise ValueError("Nilai harus berada di rentang 0-100")


def hitung_rata_rata(nilai):
    """Hitung rata-rata dari daftar nilai (0-100)."""
    if not isinstance(nilai, (list, tuple)):
        raise TypeError("Input harus berupa list atau tuple")
    if len(nilai) == 0:
        raise ValueError("Daftar nilai tidak boleh kosong")
    for n in nilai:
        _validasi_nilai(n)
    return sum(nilai) / len(nilai)


def hitung_nilai_akhir(tugas, uts, uas):
    """Hitung nilai akhir: tugas 30%, UTS 30%, UAS 40%."""
    for n in (tugas, uts, uas):
        _validasi_nilai(n)
    return round(tugas * BOBOT_TUGAS + uts * BOBOT_UTS + uas * BOBOT_UAS, 2)


def tentukan_grade(nilai_akhir):
    """Konversi nilai akhir menjadi grade huruf A-E."""
    _validasi_nilai(nilai_akhir)
    if nilai_akhir >= 85:
        return "A"
    if nilai_akhir >= 70:
        return "B"
    if nilai_akhir >= 60:
        return "C"
    if nilai_akhir >= 50:
        return "D"
    return "E"


def is_lulus(nilai_akhir, batas=60):
    """True jika nilai akhir >= batas kelulusan."""
    _validasi_nilai(nilai_akhir)
    return nilai_akhir >= batas


def _input_angka(prompt):
    """Ambil input angka dari keyboard dengan validasi sederhana."""
    while True:
        try:
            nilai = input(prompt).strip()
            if nilai == "":
                raise ValueError("Input tidak boleh kosong")
            angka = float(nilai)
            if angka.is_integer():
                return int(angka)
            return angka
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")


def _input_daftar_nilai(prompt):
    """Ambil daftar nilai dari keyboard dengan format 80,90,100."""
    while True:
        try:
            teks = input(prompt).strip()
            if teks == "":
                raise ValueError("Input tidak boleh kosong")
            nilai = [
                float(n.strip())
                for n in teks.replace(" ", "").split(",")
                if n.strip()
            ]
            if not nilai:
                raise ValueError("Daftar nilai kosong")
            return nilai
        except ValueError:
            print("Format tidak valid. Contoh: 80,90,100")


def tampil_menu():
    """Tampilkan menu interaktif untuk user."""
    print("\n=== Kalkulator Nilai Mahasiswa ===")
    print("1. Hitung rata-rata nilai")
    print("2. Hitung nilai akhir")
    print("3. Tentukan grade")
    print("4. Cek kelulusan")
    print("5. Keluar")


def main():
    """Program utama dengan menu interaktif."""
    while True:
        try:
            tampil_menu()
            pilihan = input("Pilih menu [1-5]: ").strip()
        except EOFError:
            print("\nInput keyboard ditutup. Program selesai.")
            break

        try:
            if pilihan == "1":
                daftar = _input_daftar_nilai(
                    "Masukkan nilai dipisahkan koma (contoh: 80,90,100): "
                )
                rata_rata = hitung_rata_rata(daftar)
                print(f"Rata-rata: {rata_rata}")

            elif pilihan == "2":
                tugas = _input_angka("Masukkan nilai tugas: ")
                uts = _input_angka("Masukkan nilai UTS: ")
                uas = _input_angka("Masukkan nilai UAS: ")
                akhir = hitung_nilai_akhir(tugas, uts, uas)
                grade = tentukan_grade(akhir)
                lulus = is_lulus(akhir)
                print(f"Nilai akhir: {akhir}")
                print(f"Grade: {grade}")
                status_lulus = "Ya" if lulus else "Tidak"
                print(f"Lulus: {status_lulus}")

            elif pilihan == "3":
                nilai_akhir = _input_angka("Masukkan nilai akhir: ")
                print(f"Grade: {tentukan_grade(nilai_akhir)}")

            elif pilihan == "4":
                nilai_akhir = _input_angka("Masukkan nilai akhir: ")
                batas = _input_angka(
                    "Masukkan batas kelulusan (default 60): "
                )
                status = (
                    "Lulus" if is_lulus(nilai_akhir, batas)
                    else "Tidak Lulus"
                )
                print(f"Status kelulusan: {status}")

            elif pilihan == "5":
                print("Terima kasih, program selesai.")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih 1-5.")

        except (TypeError, ValueError) as e:
            print(f"Error: {e}")

        print()


if __name__ == "__main__":
    main()
