#[[1, 2, 3],
#[4, 5, 6],
#[7, 8, 9]]

#[[3, 6, 9],
#[2, 5, 8],
#[1, 4, 7]]

 def counterClockwise(data):
     temp1 =data[0][0] #bagian pertama adalah bagian ke 0
     data[0][0]= data[1][0] #bagian 0 tersebut diubah ke bagian 3
     data[2][0]=temp1 #bagian 3 nomor 1

     temp2 =data [0][0] #bagian 0 diubah ke bagian 2 nomor 2
     data[0][1]=data[1][0]
     data[1][0]=tempt2

     tempt3 = data[0][0] #bagian 0 nomor 3 diubah ke bagian 1 nomor 1
     data[0][2]= data[0][0]
     data[0][0]=tempt3

     tempt4 =data[0][1] #data bagian 1
     data[1][1]=data[2][2] #yaitu data nomor 1 (4)
     data[2][2]=tempt4 #diubah menjadi nomor 1 bagian 3

     tempt5 =data [0][1] #data yang berada pada bagian 1 ke 1
     data [1][2]=data[0][1] #bagian 1 nomor 1 dipindahkan ke 0 bagian1
     data[0][1]=tempt5

     tempt6 =data [0][2] #data bagian 0 bagian 2
     data[2][0]=data[2][2] #data bagian 2 bagian 0 akan dipindahkan ke bagian 2 nomor 2
     data[2][2]=tempt6 

     tempt7 =data[0][2] #data bagian 0 nomor 2 
     data[2][2]=data[1][2] #data bagian 2 nomor 2 akan dipindakan ke bagian 2 nomor 2
     data[1][2]=tempt7

     tempt8= data[0][2] #data bagian 0 nomor 2
     data[2][2]=data[0][2] #data bagian 2 nomor 2 akan dipindakan ke baigan 0 baigan 2
     data[0][2]=tempt8


data = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

print(counterClockwise(data))
