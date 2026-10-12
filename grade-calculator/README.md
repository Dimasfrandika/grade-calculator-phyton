# Grade Calculator

Mini program Python untuk menghitung nilai akhir mahasiswa, dilengkapi **Test Case Design** dan **Unit Test** (pytest).

## Fungsi

| Fungsi | Deskripsi |
|---|---|
| `hitung_rata_rata(nilai)` | Rata-rata dari list nilai (0-100) |
| `hitung_nilai_akhir(tugas, uts, uas)` | Nilai akhir berbobot: tugas 30%, UTS 30%, UAS 40% |
| `tentukan_grade(nilai_akhir)` | Konversi ke grade A (>=85), B (>=70), C (>=60), D (>=50), E |
| `is_lulus(nilai_akhir, batas=60)` | Cek kelulusan berdasarkan batas nilai |

## Cara menjalankan

```bash
pip install pytest
python grade_calculator.py     # demo program
pytest -v                      # jalankan unit test
```

## Struktur repository

```
grade-calculator/
├── grade_calculator.py        # source code
├── test_grade_calculator.py   # unit test (pytest)
└── README.md
```
