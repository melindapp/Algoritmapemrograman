#setting variable
nim  = input("masukkan nim  :")
lkp  = input("masukkan nama lengkap  :")
kls  = input("masukkan kelas  :")
prd  = input("masukkan nama prodi  :")

#setting variable nilai
plj_id  = int(input("Nilai Bahasa indonesia  :"))
plj_ig  = int(input("Nilai Bahasa Inggris    :"))
plj_pd     = int(input("Nilai Pemrograman Dasar :  "))
plj_mtk    = int(input("Nilai Matematika        :  "))
plj_kal1   = int(input("Nilai Kalkulus          :   "))


if(plj_id  > 0 and plj_id  <=60):
    hs_grd  =("C")
elif(plj_id >60 and plj_id  <=75) :
    hs_grd  = ("B")
elif(plj_id >75 and plj_id  <=85) :
    hs_grd  =("AB")
elif(plj_id  >85 and plj_id <=100) :
    hs_grd  =("A")
else: 
    hs_grd  =("Grade Anda Tidak ditemukan! ")
    
if(plj_ig> 0 and plj_ig <=60):
    hs_grd2 = ("C")
elif(plj_ig>60 and plj_ig<=75) :
    hs_grd2  = ("B")
elif(plj_ig>75 and plj_ig<=85) :
    hs_grd2 = ("AB")
elif(plj_ig>85 and plj_ig<=100) :
    hs_grd2 = ("A")
else: 
    hs_grd2 =("Grade Anda Tidak ditemukan! ")
  
if(plj_pd > 0 and plj_pd <=60):
    hs_grd3 = ("C")
elif(plj_pd >60 and plj_pd <=75) :
    hs_grd3  = ("B")
elif(plj_pd >75 and plj_pd <=85) :
    hs_grd3 = ("AB")
elif(plj_pd >85 and plj_pd <=100) :
    hs_grd3 = ("A")
else: 
    hs_grd3 =("Grade Anda Tidak ditemukan! ")
   
if(plj_mtk > 0 and plj_mtk <=60):
   hs_grd4  = ("C")
elif(plj_mtk>60 and plj_mtk <=75) :
    hs_grd4 =("B")
elif(plj_mtk >75 and plj_mtk<=85) :
    hs_grd4 = ("AB")
elif(plj_mtk>85 and plj_mtk<=100) :
    hs_grd4 = ("A")
else: 
    hs_grd4 =("Grade Anda Tidak ditemukan! ")
   
if(plj_kal1> 0 and plj_kal1 <=60):
    hs_grd5 = ("C")
elif(plj_kal1>60 and plj_kal1<=75) :
    hs_grd5 = ("B")
elif(kal1>75 and plj_kal1<=85) :
    hs_grd5 = ("AB")
elif(plj_kal1>85 and plj_kal1<=100) :
    hs_grd5 = ("A")
else: 
    hs_grd5 =("Grade Anda Tidak ditemukan! ")
   
   
#perhitungan
rata = (b_ind+b_ing+pd+mtk+kal1)/5

if(rata >0 and rata <=60) :
    grade_rata = ("C")
elif(rata >60 and rata <=75) :
    grade_rata = ("B")
elif(rata >75 and rata <=85) :
    grade_rata = ("AB")
elif(rata >85 and rata <=100) :
    grade_rata = ("A")
else: 
    grade_rata =("Grade Anda Tidak ditemukan! ")
   
#menampilkan
print("----------------------")
print("    kartu hasil studi     ")
print("----------------------")
print ("Nim           :",nim)
print ("nama lengkap  :",lkp)
print ("kelas         :",kls)
print ("program study :",prd)
print ("----------------------")
print ("No  Nama Makul   Nilai   Grade  ")
print ("----------------------")
print ("1.  bahasa Indonesia  ",plj_id,hs_grd ), 
print ("2.  bahasa Inggris    ",plj_ig, hs_grd2 )
print ("3.  Pemrograman Dasar ",plj_pd, hs_grd3)
print ("4.  matematika        ",plj_mtk, hs_grd4)
print ("5.  Kalkulus 1        ",plj_kal1, hs_grd5 )
print ("----------------------")
print ("Rata-Rata             ",rata," ",grade_rata)
print ("----------------------")