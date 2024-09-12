import os
import platform

todo_list = []

def clear_screen():
    """Membersihkan layar tergantung pada sistem operasi"""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def display_tasks():
    """Menampilkan semua tugas dalam daftar"""
    if not todo_list:
        print("Daftar tugas kosong.")
    else:
        print("\nDaftar Tugas:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task(task):
    """Menambahkan tugas baru ke daftar"""
    if any(task in t for t in todo_list):
        print(f"Tugas '{task}' sudah ada dalam daftar.")
    else:
        todo_list.append(task)
        print(f"Tugas '{task}' telah ditambahkan.")

def remove_task(task_index):
    """Menghapus tugas dari daftar berdasarkan indeks atau menghapus semua tugas jika input 'x'"""
    if task_index == 'x':
        todo_list.clear()
        print("Semua tugas telah dihapus.")
    else:
        try:
            removed_task = todo_list.pop(int(task_index) - 1)
            print(f"Tugas '{removed_task}' telah dihapus.")
        except (IndexError, ValueError):
            print("Indeks tugas tidak valid atau tidak ada.")

def mark_task_completed(task_index):
    """Menandai tugas sebagai selesai"""
    try:
        task = todo_list[task_index - 1]
        if " (selesai)" in task:
            print("Tugas yang anda pilih sudah selesai.")
        else:
            todo_list[task_index - 1] = f"{task} (selesai)"
            print(f"Tugas '{task}' telah ditandai sebagai selesai.")
    except IndexError:
        print("Indeks tugas tidak valid.")

def main():
    """Fungsi utama untuk menjalankan aplikasi"""
    while True:
        clear_screen()
        print("\n--- Menu ---")
        print("1. Tampilkan Tugas")
        print("2. Tambah Tugas")
        print("3. Hapus Tugas")
        print("4. Tandai Tugas Selesai")
        print("5. Keluar")

        choice = input("Pilih opsi (1-5): ")

        if choice == '1':
            display_tasks()
            input("Tekan Enter untuk kembali ke menu...")
        elif choice == '2':
            while True:
                task = input("Masukkan tugas baru: ")
                clear_screen()
                add_task(task)
                display_tasks()
                cont = input("Tambah tugas lagi? (y/n): ").lower()
                if cont != 'y':
                    break
            input("Tekan Enter untuk kembali ke menu...")
        elif choice == '3':
            display_tasks()
            task_index = input("Masukkan nomor tugas yang akan dihapus (atau 'x' untuk menghapus semua): ")
            remove_task(task_index)
            input("Tekan Enter untuk kembali ke menu...")
        elif choice == '4':
            display_tasks()
            try:
                task_index = int(input("Masukkan nomor tugas yang sudah selesai: "))
                mark_task_completed(task_index)
            except ValueError:
                print("Masukkan nomor tugas yang valid.")
            input("Tekan Enter untuk kembali ke menu...")
        elif choice == '5':
            print("Keluar dari aplikasi.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1 hingga 5.")
            input("Tekan Enter untuk kembali ke menu...")

if __name__ == "__main__":
    main()
