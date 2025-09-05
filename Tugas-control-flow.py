randomnum = int(input("Masukkan Angka"))
while randomnum < 0 :
  print("Angka negatif, mohon coba lagi")
  randomnum= int(input("Masukkan Angka positif"))
if randomnum % 2 == 0: #Even
  evennumbers = 0
  while evennumbers <= randomnum:
    print(evennumbers)
    evennumbers+=2
else:
    oddnumbers=1
    while oddnumbers <= randomnum:
      print(oddnumbers)
      oddnumbers+=2