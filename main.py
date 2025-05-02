import random
from datetime import datetime, timedelta
from collections import defaultdict

# Penyimpanan referensi untuk menghindari duplikasi
nip_registry = defaultdict(int)


def generate_nip(
    tanggal_lahir: str, tanggal_pengangkatan: str, jenis_kelamin: str
) -> str:
    bagian_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d").strftime("%Y%m%d")
    bagian_angkat = datetime.strptime(
        tanggal_pengangkatan + "-01", "%Y-%m-%d"
    ).strftime("%Y%m")
    bagian_gender = jenis_kelamin

    base_key = bagian_lahir + bagian_angkat + bagian_gender
    nip_registry[base_key] += 1
    ref_number = f"{nip_registry[base_key]:03d}"  # Padding 3 digit

    return base_key + ref_number


def random_date(start: datetime, end: datetime) -> datetime:
    """Mengembalikan tanggal acak antara start dan end"""
    delta = end - start
    if delta.days <= 0:
        return start
    return start + timedelta(days=random.randint(0, delta.days))


def generate_random_nip() -> str:
    # Tentukan tanggal sekarang
    today = datetime.today()

    # Tetapkan rentang umur lahir: 1950 hingga (hari ini - 17 tahun)
    latest_lahir = today - timedelta(days=365 * 17)
    tanggal_lahir = random_date(datetime(1950, 1, 1), latest_lahir)

    # Tanggal pengangkatan minimal 17 tahun setelah lahir hingga hari ini
    min_pengangkatan = tanggal_lahir + timedelta(days=365 * 17)
    if min_pengangkatan > today:
        min_pengangkatan = today

    tanggal_pengangkatan = random_date(min_pengangkatan, today)

    tanggal_lahir_str = tanggal_lahir.strftime("%Y-%m-%d")
    tanggal_pengangkatan_str = tanggal_pengangkatan.strftime("%Y-%m")
    jenis_kelamin = random.choice(["1", "2"])

    return generate_nip(tanggal_lahir_str, tanggal_pengangkatan_str, jenis_kelamin)


if __name__ == "__main__":
    print("=== NIP Generator ===")
    try:
        jumlah = int(input("Masukkan jumlah NIP yang ingin digenerate: "))
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0.")

        print("\nHasil NIP yang digenerate:")
        for i in range(jumlah):
            nip = generate_random_nip()
            print(f"{nip}")

    except ValueError as e:
        print("Error:", e)
