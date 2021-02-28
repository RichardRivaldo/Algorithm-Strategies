# Tugas Kecil 2 IF2211 Strategi Algoritma
Penyusunan Rencana Kuliah dengan _Topological Sort_

### Algoritma Decrease and Conquer
* _Decrease and Conquer_ adalah algoritma yang pada setiap iterasinya memiliki jumlah upa-persoalan yang selalu berkurang, baik berkurang dalam jumlah konstan (_decrease by a constant_), berkurang dalam jumlah faktor konstanta (_decrease by a constant factor_), atau berkurang dalam jumlah yang bervariasi (_decrease by a variable size_).
* Algoritma _Topological Sort_ merupakan algoritma yang digunakan untuk melakukan pengurutan pada sebuah graf yang memenuhi syarat sebagai graf DAG (_Directed Acyclic Graph_) yang tidak memiliki siklus sama sekali untuk semua simpulnya. _Topological Sort_ bisa dimasukkan ke dalam jenis pertama dari algoritma DnC.
* Algoritma _topological sort_ dalam program ini dilakukan dengan menggunakan struktur data _list_ secara analog dengan representasi graf DAG. Dalam hal ini, algoritma akan mencari terlebih dahulu elemen _list_ yang hanya memiliki satu buah elemen saja, atau dalam kata lain tidak memiliki _input edges_ untuk simpulnya jika direpresentasikan ke dalam graf.
* Kemudian, program juga akan mengecek apakah ada mata kuliah lain yang pada iterasi yang sama tidak memiliki prasyarat sama sekali dan juga tidak memiliki _dependency_ dengan simpul lain yang sudah dipilih sebelumnya. Selain itu, program akan mengeluarkan simpul atau elemen tersebut dari daftar mata kuliah yang ada sebelumnya, termasuk dari _list_ yang mengandung mata kuliah tersebut. Hal ini sama dengan menghilangkan sisi-sisi dari simpul mata kuliah terpilih yang berkaitan dengan simpul lainnya di dalam graf.
* Setelah itu, hasil akan disimpan juga dalam sebuah _list_ yang nantinya akan digunakan dalam _output_ program. Hal ini dilakukan secara rekursif sampai tidak ada lagi mata kuliah yang tersisa dalam _list_ (dalam kata lain graf sudah menjadi graf kosong). Selain itu, algoritma juga membatasi penyusunan rencana kuliah sampai dengan delapan semester saja. Jika file yang dimasukkan kosong, _invalid_, atau bukan merupakan DAG, maka algoritma akan berhenti dan mengeluarkan pesan kesalahan yang terkait dengan _error_ yang ada.

### Requirements
* ```Python 3```
* Setup ```Path``` untuk Python
* File masukan dalam format ```.txt```, atau dengan menggunakan file yang ada dalam folder ```test```.

### How to Use
* Lakukan _change directory_ Terminal atau Command Prompt sampai dengan direktori yang berisi _source code_ program (dalam struktur folder ini, ```src```).
* Pindahkan atau masukkan file .txt yang menjadi input ke dalam direktori yang sama dengan kode program ```Abyss_13519185```.
* Eksekusi program dengan menggunakan perintah ```python Abyss_13519185.py``` atau ```py Abyss_13519185.py```.
* Program akan meminta masukkan berupa nama file yang ingin diproses. Berikan masukan dalam format ```nama_file.txt```.

### Author 
* Richard Rivaldo / 13519185 - K04