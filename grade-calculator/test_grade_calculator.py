"""Unit test untuk grade_calculator.py (pytest).

Setiap test diberi ID (TC-xx) agar selaras dengan dokumen Test Case Design.
"""
import pytest

from grade_calculator import (
    hitung_rata_rata,
    hitung_nilai_akhir,
    tentukan_grade,
    is_lulus,
)


# ---------- hitung_rata_rata ----------
def test_tc01_rata_rata_normal():
    assert hitung_rata_rata([80, 90, 100]) == 90


def test_tc02_rata_rata_satu_nilai():
    assert hitung_rata_rata([75]) == 75


def test_tc03_rata_rata_list_kosong():
    with pytest.raises(ValueError):
        hitung_rata_rata([])


def test_tc04_rata_rata_nilai_di_luar_rentang():
    with pytest.raises(ValueError):
        hitung_rata_rata([80, 120])


def test_tc05_rata_rata_input_bukan_list():
    with pytest.raises(TypeError):
        hitung_rata_rata("80,90")


# ---------- hitung_nilai_akhir ----------
def test_tc06_nilai_akhir_normal():
    # 80*0.3 + 75*0.3 + 90*0.4 = 24 + 22.5 + 36 = 82.5
    assert hitung_nilai_akhir(80, 75, 90) == 82.5


def test_tc07_nilai_akhir_semua_nol():
    assert hitung_nilai_akhir(0, 0, 0) == 0


def test_tc08_nilai_akhir_semua_seratus():
    assert hitung_nilai_akhir(100, 100, 100) == 100


def test_tc09_nilai_akhir_negatif():
    with pytest.raises(ValueError):
        hitung_nilai_akhir(-1, 80, 80)


def test_tc10_nilai_akhir_tipe_salah():
    with pytest.raises(TypeError):
        hitung_nilai_akhir("80", 80, 80)


# ---------- tentukan_grade ----------
@pytest.mark.parametrize(
    "nilai, grade",
    [
        (100, "A"),    # TC-11 batas atas
        (85, "A"),     # TC-12 batas bawah A
        (84.99, "B"),  # TC-13 tepat di bawah batas A
        (70, "B"),     # TC-14 batas bawah B
        (60, "C"),     # TC-15 batas bawah C
        (50, "D"),     # TC-16 batas bawah D
        (49.99, "E"),  # TC-17 tepat di bawah batas D
        (0, "E"),      # TC-18 batas bawah
    ],
)
def test_tc11_18_grade_boundary(nilai, grade):
    assert tentukan_grade(nilai) == grade


def test_tc19_grade_nilai_invalid():
    with pytest.raises(ValueError):
        tentukan_grade(101)


# ---------- is_lulus ----------
def test_tc20_lulus_tepat_di_batas():
    assert is_lulus(60) is True


def test_tc21_tidak_lulus_di_bawah_batas():
    assert is_lulus(59.99) is False


def test_tc22_lulus_dengan_batas_custom():
    assert is_lulus(65, batas=70) is False
    assert is_lulus(70, batas=70) is True
