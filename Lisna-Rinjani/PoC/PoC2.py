import requests

def hapus_barang_keluar():
    # Meminta input dari user
    phpsessid = input("Masukkan PHPSESSID: ").strip()
    barang_id = input("Masukkan ID Barang: ").strip()

    if not phpsessid or not barang_id:
        print("[!] PHPSESSID dan ID tidak boleh kosong.")
        return

    # URL target
    url = "https://inventory.rinjaniproject.my.id/e-inventory/petugas/function/barang-keluar.php"

    # Parameter query
    params = {
        'aksi': 'hapus',
        'id': barang_id
    }

    # Cookie sesi
    cookies = {
        'PHPSESSID': phpsessid
    }

    # Header menyerupai request browser/curl
    headers = {
        'User-Agent': 'curl/8.0.1'
    }

    try:
        # Mengirim request GET (ekuivalen dengan perintah curl)
        response = requests.get(url, params=params, cookies=cookies, headers=headers)

        print("\n--- Status Request ---")
        print(f"Status Code: {response.status_code}")
        print(f"Final URL  : {response.url}")
        
        print("\n--- Response Body ---")
        print(response.text)

    except requests.RequestException as e:
        print(f"[!] Terjadi kesalahan koneksi: {e}")

if __name__ == "__main__":
    hapus_barang_keluar()