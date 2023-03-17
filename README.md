# Tugas Post Test 3
## Linked List (In Game Friend List)

#### Cara Kerja Program
Linked list adalah struktur data linear yang terdiri dari serangkaian node atau simpul, di mana setiap node terdiri dari dua komponen: data dan pointer ke node berikutnya dalam linked list. Pointer di sini adalah suatu variabel yang menunjuk ke alamat memori dari node berikutnya dalam linked list.

Linked list dapat diimplementasikan dalam dua cara: singly linked list dan doubly linked list. Pada singly linked list, setiap node hanya memiliki satu pointer yang menunjuk ke node berikutnya dalam linked list, sedangkan pada doubly linked list, setiap node memiliki dua pointer, yaitu satu pointer yang menunjuk ke node sebelumnya dan satu pointer yang menunjuk ke node berikutnya dalam linked list. 

Untuk menambahkan sebuah node ke linked list, kita dapat melakukan operasi insert pada linked list. Operasi insert ini dapat dilakukan di awal, tengah, atau akhir linked list, tergantung dari implementasi yang diinginkan. Selain itu, linked list juga dapat menghapus sebuah node dari linked list dengan melakukan operasi delete pada linked list.

Pada program ini, implementasi linked list menggunakan singly linked list. Dengan penambahan node di akhir linked list, dan penghapusan node di sembarang posisi dalam linked list.

#### Fungsionalitas Program
Linked list memiliki fungsionalitas dasar seperti insertion, deletion, traversal, searching, sorting, dan merging, serta dapat diimplementasikan dalam berbagai bahasa pemrograman untuk mengelola data secara dinamis.

#### Elemen - Elemen dalam Program

import os: digunakan untuk mengimpor modul os yang akan digunakan untuk membersihkan konsol.

class FriendList: digunakan untuk mendefinisikan kelas FriendList.

class FriendNode: digunakan untuk mendefinisikan kelas FriendNode.

def __init__(self, name, id_char, level, total_achievement): adalah konstruktor kelas FriendNode yang menginisialisasi atribut dari kelas tersebut, yaitu name, id_char, level, total_achievement, dan next. Atribut next digunakan untuk menunjuk ke node berikutnya dalam linked list.

def __init__(self): adalah konstruktor kelas FriendList yang menginisialisasi atribut head dengan None. Atribut head digunakan untuk menunjuk ke node pertama dalam linked list.

def add_friend(self, name, id_char, level, total_achievement): adalah fungsi untuk menambahkan teman baru ke linked list. Fungsi ini membuat objek FriendNode baru dengan atribut yang diberikan, dan menambahkannya ke akhir linked list jika linked list tidak kosong, atau membuatnya sebagai head jika linked list kosong.

def remove_friend(self, name): adalah fungsi untuk menghapus teman dari linked list. Fungsi ini mencari node dengan nama yang diberikan dan menghapusnya dari linked list.

def print_friends(self): adalah fungsi untuk mencetak daftar teman dalam linked list ke dalam sebuah string, dengan memanfaatkan atribut name dari setiap node.

def print_detail(self, name): adalah fungsi untuk mencetak detail teman yang memiliki nama yang diberikan. Fungsi ini mencari node dengan nama yang diberikan dan mencetak atributnya, yaitu name, id_char, level, dan total_achievement.
