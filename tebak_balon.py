import random

welcome_message = "tebak balon"
balon_position = random.randint(1, 5)

print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = (input("masukan nama kamu:"))

bentuk_balon = "|__|"
balon_kosong =  [bentuk_balon] * 4

balon = balon_kosong.copy()  

balon[balon_position - 1] = "|0_0|"

balon_kosong ='---'.join(balon_kosong)

print(f'''
HALO {nama_user}! coba perhatikan balon dibawah ini!{balon_kosong}''')


pilihan_user = int(input(f" menurut kamu dimanakah balon bersembunyi? 1\ 2 \ 3 \ 4 \ 5 : "))

print(F"pilihan kamu adalah {pilihan_user}.")

confirm_answer = input(f"apakah kamu yakin dengan pilihan tersebut {pilihan_user} ?[yes \ no] : ")
 
if confirm_answer == "no" :
   print("program dihentikan!")
   exit()

elif confirm_answer == "yes" :
    if pilihan_user == balon_position :
       print(f"{balon} \n SELAMAT KAMU MENANG!")
    else :
       print(f"{balon} \n MAAF KAMU KALAH!")

else :
     print("coba lagi")
     exit()