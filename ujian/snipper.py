def counterclockwise(data):
    tempt1=data[0][0]
    data[0][0]=data[2][0]
    data[2][0]=tempt1
    
    tempt2= data[0][0]
    data[0][1]=data[1][0]
    data[1][0]=tempt2
    
    tempt3=data[0][0]
    data[0][2]=data[0][0]
    data[0][0]=tempt3
    
    tempt4=data[0][1]
    data[0][1]=data[2][1]
    data[2][1]=tempt4
    
    tempt5=data[0][2]
    data[1][2]=data[1][2]
    data[1][2]=data[1][2]
    
    tempt6=data[0][2]
    data[1][2]=data[0][1]
    data[0][1]=tempt6
    
    tempt7=data[0][2]
    data[2][0]=data[2][2]
    data[2][2]=tempt7
    
    tempt8=data[0][2]
    data[2][1]=data[1][2]
    data[1][2]=tempt8
    
    tempt9=data[0][2]
    data[2][2]=data[0][2]
    data[0][2]=tempt9

data = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    
print(counterclockwise(data))
