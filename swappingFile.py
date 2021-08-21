with open("./Project98/sample1.txt","r")as a:
    data_a=a.read()

with open("./Project98/sample2.txt","r")as b:
    data_b=b.read() 

with open("./Project98/sample1.txt","w")as a:
    a.write(data_b)

with open("./Project98/sample2.txt","w")as b:
    b.write(data_a)     

