      
responses = {
    "string": (
        "Tipe data `string` di Python adalah urutan karakter. Anda dapat membuat string dengan menuliskannya di antara tanda kutip (' ' atau \" \"). "
        "Contoh: `s = 'hello'`. Metode umum untuk string termasuk `lower()`, `upper()`, `strip()`, dan `replace()`. "
        "Contoh penggunaan: `s.lower()` akan mengubah semua karakter dalam string menjadi huruf kecil."
    ),
    "upper": (
        "Metode `.upper()` mengubah semua karakter dalam string menjadi huruf kapital. Contoh: "
        "`s = 'hello'` dan `s.upper()` akan menghasilkan 'HELLO'."
    ),
    "lower": (
        "Metode `.lower()` mengubah semua karakter dalam string menjadi huruf kecil. Contoh: "
        "`s = 'HELLO'` dan `s.lower()` akan menghasilkan 'hello'."
    ),
    "split": (
        "Metode `.split()` memecah string menjadi list berdasarkan separator yang diberikan. Jika tidak ada separator, default-nya adalah spasi. "
        "Contoh: `s = 'hello world'` dan `s.split()` akan menghasilkan `['hello', 'world']`."
    ),
    "format": (
        "Metode `.format()` memungkinkan Anda untuk menyisipkan nilai ke dalam string. Contoh: "
        "`'Hello, {}'.format('world')` akan menghasilkan 'Hello, world'."
    ),
    "isnumeric": (
        "Metode `.isnumeric()` memeriksa apakah semua karakter dalam string adalah angka. Contoh: "
        "`s = '123'` dan `s.isnumeric()` akan menghasilkan True, sedangkan `s = 'abc'` akan menghasilkan False."
    ),
    "isalpha": (
        "Metode `.isalpha()` memeriksa apakah semua karakter dalam string adalah huruf. Contoh: "
        "`s = 'hello'` dan `s.isalpha()` akan menghasilkan True, sedangkan `s = 'hello123'` akan menghasilkan False."
    ),
    "replace": (
        "Metode `.replace()` menggantikan semua kemunculan substring yang diberikan dengan substring yang baru. Contoh: "
        "`s = 'hello world'` dan `s.replace('world', 'Python')` akan menghasilkan 'hello Python'."
    ),
    "string index": (
        "Mengakses karakter dalam string dengan indeks. Indeks dimulai dari 0. Contoh: "
        "`s = 'hello'` dan `s[0]` akan menghasilkan 'h'."
    ),
    "len": (
        "Fungsi `len()` mengembalikan panjang dari string, list, atau koleksi lainnya. Contoh: "
        "`s = 'hello'` dan `len(s)` akan menghasilkan 5."
    ),
    "list": (
        "Tipe data `list` di Python adalah koleksi yang dapat diubah (mutable) dan berurutan. Anda dapat membuat list dengan menuliskannya di antara tanda kurung siku [ ]. "
        "Contoh: `my_list = [1, 2, 3]`. Metode umum untuk list termasuk `append()`, `extend()`, `remove()`, `sort()`, `reverse()`, dan `insert()`. "
        "Contoh penggunaan: `my_list.append(4)` akan menambahkan elemen 4 ke akhir list."
    ),
    "reverse": (
        "Metode `.reverse()` membalik urutan elemen dalam list. Contoh: "
        "`my_list = [1, 2, 3]` dan `my_list.reverse()` akan mengubah `my_list` menjadi `[3, 2, 1]`."
    ),
    "extend": (
        "Metode `.extend()` menambahkan semua elemen dari iterable (seperti list) ke akhir list. Contoh: "
        "`my_list = [1, 2]` dan `my_list.extend([3, 4])` akan mengubah `my_list` menjadi `[1, 2, 3, 4]`."
    ),
    "insert": (
        "Metode `.insert()` menyisipkan elemen pada posisi indeks tertentu dalam list. Contoh: "
        "`my_list = [1, 2, 3]` dan `my_list.insert(1, 4)` akan mengubah `my_list` menjadi `[1, 4, 2, 3]`."
    ),
    "append": (
        "Metode `.append()` menambahkan elemen ke akhir list. Contoh: "
        "`my_list = [1, 2]` dan `my_list.append(3)` akan mengubah `my_list` menjadi `[1, 2, 3]`."
    ),
    "remove": (
        "Metode `.remove()` menghapus elemen pertama yang ditemukan dengan nilai yang diberikan dari list. Contoh: "
        "`my_list = [1, 2, 3]` dan `my_list.remove(2)` akan mengubah `my_list` menjadi `[1, 3]`."
    ),
    "sort": (
        "Metode `.sort()` mengurutkan elemen dalam list secara in-place. Contoh: "
        "`my_list = [3, 1, 2]` dan `my_list.sort()` akan mengubah `my_list` menjadi `[1, 2, 3]`."
    ),
    "list comprehensions": (
        "List comprehensions adalah cara singkat untuk membuat list baru dengan menggunakan ekspresi. Contoh: "
        "`[x*2 for x in range(5)]` akan menghasilkan `[0, 2, 4, 6, 8]`."
    ),
    "dictionary": (
        "Tipe data `dictionary` di Python adalah koleksi pasangan kunci-nilai yang tidak berurutan. Anda dapat membuat dictionary dengan menggunakan tanda kurung kurawal { }. "
        "Contoh: `my_dict = {'key1': 'value1', 'key2': 'value2'}`. Metode umum untuk dictionary termasuk `get()`, `keys()`, `values()`, `items()`, dan `update()`. "
        "Contoh penggunaan: `my_dict.get('key1')` akan mengembalikan 'value1'."
    ),
    "items": (
        "Metode `.items()` mengembalikan view objek yang berisi pasangan kunci-nilai dari dictionary. Contoh: "
        "`my_dict = {'key1': 'value1'}` dan `my_dict.items()` akan menghasilkan `dict_items([('key1', 'value1')])`."
    ),
    "update": (
        "Metode `.update()` memperbarui dictionary dengan pasangan kunci-nilai dari dictionary lain atau iterable. Contoh: "
        "`my_dict = {'key1': 'value1'}` dan `my_dict.update({'key2': 'value2'})` akan mengubah `my_dict` menjadi `{'key1': 'value1', 'key2': 'value2'}`."
    ),
    "keys": (
        "Metode `.keys()` mengembalikan view objek yang berisi kunci-kunci dari dictionary. Contoh: "
        "`my_dict = {'key1': 'value1'}` dan `my_dict.keys()` akan menghasilkan `dict_keys(['key1'])`."
    ),
    "values": (
        "Metode `.values()` mengembalikan view objek yang berisi nilai-nilai dari dictionary. Contoh: "
        "`my_dict = {'key1': 'value1'}` dan `my_dict.values()` akan menghasilkan `dict_values(['value1'])`."
    ),
    "copy": (
        "Metode `.copy()` mengembalikan salinan dari dictionary. Contoh: "
        "`my_dict = {'key1': 'value1'}` dan `my_dict.copy()` akan menghasilkan `{'key1': 'value1'}`."
    ),
    "dictionary[key]": (
        "Mengakses nilai dari dictionary dengan kunci tertentu. Contoh: "
        "`my_dict = {'key1': 'value1'}` dan `my_dict['key1']` akan menghasilkan 'value1'."
    ),
    "dictionary[key] = value": (
        "Menetapkan nilai untuk kunci tertentu dalam dictionary. Contoh: "
        "`my_dict = {'key1': 'value1'}` dan `my_dict['key1'] = 'new_value'` akan mengubah `my_dict` menjadi `{'key1': 'new_value'}`."
    ),
    "default": (
        "Maaf, saya tidak memiliki informasi tentang itu. Silakan coba tanyakan tentang metode Python yang lain atau tipe data seperti 'string', 'list', 'tuple', 'dictionary', 'int', atau 'float'."
    )
}

def get_response(user_input):
    """Mendapatkan respons dari chatbot berdasarkan input pengguna"""
    user_input = user_input.lower()  # Ubah input pengguna menjadi huruf kecil
    return responses.get(user_input, responses["default"])

def main():
    """Fungsi utama untuk menjalankan chatbot"""
    print("Chatbot Tipe Data dan Metode Python\n")
    print("Tanyakan tentang tipe data atau metode Python seperti 'string', 'list', 'tuple', 'dictionary', 'int', 'float', atau metode spesifik lainnya. Ketik 'bye' untuk keluar.")

    while True:
        user_input = input("Anda: ")
        if user_input.lower() == "bye":
            print("Chatbot: Selamat tinggal! Semoga hari Anda menyenangkan!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
