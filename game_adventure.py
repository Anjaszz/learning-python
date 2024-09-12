import random

rooms = {
    'Hall': {
        'description': 'Anda berada di Hall. Ada pintu ke utara menuju Dapur, dan pintu ke timur menuju Ruang Belajar.',
        'timur': 'Ruang Belajar',
        'utara': 'Dapur',
        'item': None
    },
    'Ruang Belajar': {
        'description': 'Ini adalah Ruang Belajar. Ada pintu ke barat kembali ke Hall, dan Anda melihat sebuah buku.',
        'barat': 'Hall',
        'selatan': 'Ruang Musuh',
        'item': 'buku'
    },
    'Dapur': {
        'description': 'Anda berada di Dapur. Ada pintu ke selatan kembali ke Hall, dan pisau di atas meja.',
        'selatan': 'Hall',
        'item': 'pisau'
    },
    'Ruang Musuh': {
        'description': 'Anda berada di Ruang Musuh. Ada musuh yang menghadang! Lawanlah atau kabur!',
        'item': None
    }
}

# Fungsi untuk mencetak instruksi kepada pemain
def show_instructions():
    print("""
Selamat datang di Game Petualangan Teks!
Anda dapat bergerak dengan mengetik 'go [arah]' (timur,utara,barat,selatan).
Untuk mengambil item, ketik 'ambil [nama item]'.
Untuk bertarung ketik 'fight'.
Untuk kabur dari musuh ketik 'run'.
Untuk keluar dari game, ketik 'quit'.
Tugas Anda adalah menemukan item, bertahan hidup, dan mengalahkan musuh di Ruang Musuh.
Semoga beruntung!
""")

# Fungsi untuk mencetak status pemain (lokasi, item, dan kesehatan)
def show_status(location, inventory, health):
    print(f"\nAnda sekarang berada di {location}.")
    print(rooms[location]['description'])
    print(f"Kesehatan: {health}")
    print(f"Inventory: {inventory}")
    if rooms[location]['item']:
        print(f"Ada {rooms[location]['item']} di sini.")

# Fungsi untuk bertarung
def fight_enemy(inventory):
    if 'pisau' in inventory:
        print("Anda menggunakan pisau untuk mengalahkan musuh. Anda menang!")
        return True
    else:
        print("Anda tidak memiliki senjata! Musuh menyerang Anda!")
        return False

# Fungsi untuk kabur dari musuh
def run_away():
    if random.choice([True, False]):
        print("Anda berhasil melarikan diri!")
        return True
    else:
        print("Anda gagal melarikan diri. Musuh menyerang!")
        return False

# Fungsi utama game
def main():
    # Pemain mulai di Hall dengan kesehatan 100 dan inventory kosong
    location = 'Hall'
    inventory = []
    health = 100

    # Tampilkan instruksi
    show_instructions()

    # Loop utama game
    while True:
        # Tampilkan status pemain
        show_status(location, inventory, health)

        # Ambil input dari pemain
        action = input("\nApa yang ingin Anda lakukan? ").lower().split()

        # Jika pemain mengetik 'quit', keluar dari game
        if action[0] == 'quit':
            print("Terima kasih telah bermain! Selamat tinggal!")
            break

        # Jika pemain ingin bergerak (perintah 'go')
        if action[0] == 'go':
            direction = action[1]
            if direction in rooms[location]:
                location = rooms[location][direction]
            else:
                print("Anda tidak bisa pergi ke sana!")

        # Jika pemain ingin mengambil item (perintah 'ambil')
        elif action[0] == 'ambil':
            item = action[1]
            if rooms[location]['item'] == item:
                inventory.append(item)
                print(f"Anda mengambil {item}.")
                rooms[location]['item'] = None  # Hapus item dari ruangan
            else:
                print(f"Tidak ada {item} di sini.")

        # Jika pemain berada di Ruang Musuh
        elif location == 'Ruang Musuh':
            if action[0] == 'fight':
                if fight_enemy(inventory):
                    break
                else:
                    health -= 30
                    if health <= 0:
                        print("Anda kalah! Permainan berakhir.")
                        break

            elif action[0] == 'run':
                if run_away():
                    location = 'Ruang Belajar'
                else:
                    health -= 20
                    if health <= 0:
                        print("Anda kalah! Permainan berakhir.")
                        break

        else:
            print("Perintah tidak dikenal. Coba lagi.")

# Jalankan game
if __name__ == "__main__":
    main()
