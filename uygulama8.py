ogrenciler={
    "101":"yiğit bilgi",
    "102": "ada bilgi",
    "103": "çinar turan"

}
dogumyil={
    "101":2010,
    "102":2012,
    "103":2017,
    
}

notlar={
    "101":(40+80+90)/3,
    "102":(80+80+80)/3,
    "103":(70+70+70)/3
}
numara=input("ogrenci numarasini giriniz: ")
yashesap=(2025-dogumyil[numara])
orthesap=int(notlar[numara])  #remove int to see fraction
     

 
    
#msj=f"{numara} numarali {ogrenciler[numara]} ismindeki ogrencinin yaşi {yashesap} ve not ortalamasi {orthesap}"
msj=f"The age of the student named {ogrenciler[numara]} number {numara}, is {yashesap} and his GPA is {orthesap}"
print(msj)

