def Tampil_Tuple(tuple):
    for i in range(len(tuple)): # tuplee diganti dengan tuple
       print(i+1,'.',tuple[i])   # tuplee diganti dengan tuple  

def Tampil_List(list):
    for i in list:              # listing diganti dengan list   
        print(i)

def Utama():
    list=[1,2,3,4,5,6,7,8,9]
    tuple=('Aria Hendrawan','Basworo Ardi Pramono','Khoirudin','April Firman Daru','Whisnumurti')
    print("\nBerikut adalah angka keberuntungan saya ")
    Tampil_List(list)
    print("\n-----------------------------------------")
    print("Daftar Nama Dosen FTIK USM ")
    Tampil_Tuple(tuple)

Utama();         #args dihapus           
