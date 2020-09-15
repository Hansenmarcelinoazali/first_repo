
# import re
# def validasi(email):
#  if(re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email) != None): #jika di dalam email tersebut terdapat karakter yang ada di dalam maka akan print email salah
#      return True
#  return False
# if(validasi("hansenmarcelino54$@gmail.com") == True): #jika email tidak ada karakter yang sudah disebutkan di atas maka akan print email valid
#  print("email yang anda masukan valid")
# else:
#  print("email tidak valid! format ekstensi salah") #jika email salah 


word = 'andre$%^&@gmail.com'
# word = "John85_cap@yah$%.com"
# word = "tony_stark@avengers.wakanda"
if (word.find('$%^&') != -1):  #jika di dalam email terdapat format tersebut maka akan menampilkan email tidak valid
    print ("email tidak valid!! format username salah! ") 
elif(word.find("$%")!= -1): #jika di dalam email terdapat format tersebut maka format dari email tersebut salah
    print('email tidak valid!! format hosting salah')
elif (word.find("@wakanda")!=-1): #jika di dalam email terdapat kata wakanda maka format hostingnya salah
    print("email tidak valid!! format ekstensi salah")
elif (word.find("@gmail.com")!=-1):
    print('email yang anda masukan valid') #jika email tersebut terdapat kata gmail maka valid
elif(word.find("@yahoo.com")!=-1): #jika email mendapatkan kata yahoo.com maka email valid karena email ada gmail dan yahoo
    print("email yang anda masukan valid")
else :
    print("email yang anda masukan valid") #jika format format yang telah ditentukan diatas tidak terdapat kata yang dilarang maka akan valid