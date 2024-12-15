with open("practice.txt","w") as f:
    f.write("hello everyone \nwe are learning File I/O\n") #so here it has created an file and written here....
    f.write("using java\n i like programming java")
    f.close()
#if we want to overwrite pyhton instead of java
#open file in read mode and then change and overwrite
with open("practice.txt","r") as f:
    data=f.read()
new_data=data.replace("java","python")
print(new_data)
#check word learning is present or not
with open("practice.txt","r") as f:
    data=f.read()
    if(data.find("learning")!=-1):
        print("Found")
    else:
        print("not found")