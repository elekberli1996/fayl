eklenecek=""
with open("newfile.txt",mode="r",encoding="utf-8") as data:
    data=data.readline()
    eklenecek=data.upper()
    print(eklenecek)
  

with open("newfile2.txt",mode="w",encoding="utf-8") as yeni:
    yeni.write(eklenecek)
    yeni.close()
    
   
    
