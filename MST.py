class List1:
    def __init__(self,data):
        self.data=data
        self.next=None
a=List1(10)
b=List1(20)
c=List1(30)
a.next=b
b.next=c     
print(b)