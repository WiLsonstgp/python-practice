#Carikan index untuk setiap nilai yang dimasukkan oleh guru dalam skenario ini.
nilai_ulangan = int(input("Masukkan nilai ulangan Anda.")) #input nilai yang dimasukkan
while nilai_ulangan > 100 or nilai_ulangan < 0 : #memastikan tidak ada nilai yang lebih dari 100 atau kurang dari 0
  print("Nilai tidak valid. Masukkan nilai yang benar")
  nilai_ulangan = int(input())
if nilai_ulangan >= 90:
  print("Grade A")
elif nilai_ulangan >= 80 :
  print("Grade B")
elif nilai_ulangan >= 70:
  print("Grade C")
elif nilai_ulangan >= 60 :
  print("Grade D")
else:
  print("Grade F")