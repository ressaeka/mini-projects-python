print(20* " =")
print("kalkulator sederhana dengan python")
print(20* "=")

angka1 = float(input("Masukan angka pertama :"))
operator = input( "Masukan operator (+ , - , * , / , % , ** , // ) :")
angka2 = float(input("Masukan angka kedua :"))

if operator == "+":
    hasil = angka1 + angka2
elif operator == "-":
    hasil = angka1 - angka2
elif operator == "x" or operator == "*":
    hasil = angka1 * angka2
elif operator == "/":
    if angka2 == 0:
        hasil = "Error: pembagian dengan no; tidak boleh 0"
    else:
        hasil = angka1 / angka2
elif operator == "%":
    if angka2 == 0:
         hasil = "Error: pembagian dengan no; tidak boleh 0"
    else:
        hasil = angka1 % angka2
elif operator == "**":
    hasil = angka1 ** angka2        
elif operator == "//":
    if angka2 == 0:
        hasil = "Error: pembagian dengan no; tidak boleh 0"
    else:
        hasil = angka1 // angka2        
else:
    hasil = "Error: operator tidak valid"   

print(f"Hasil dari {angka1} {operator} {angka2} = {hasil}")

print(20* "=")

print("Terima kasih telah menggunakan kalkulator sederhana ini!")