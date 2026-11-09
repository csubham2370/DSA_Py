class Node: 
    def __init__(self,prev=None,data=None,next=None):
        self.prev=prev
        self.data=data
        self.next=next
        
    
class DLL:
    def __init__(self,head=None):
        self.head = head
        
    def isEmpty(self):
        return self.head == None
        
    def insertAtFirst(self,data):
        n=Node(None,data,None)
        if self.isEmpty():
            self.head=n
            
        else:
            temp=self.head
            self.head=n 
            self.head.next=temp
            self.head.next.prev=self.head
            
            
            
    def insertAtEnd(self,data):
        n=Node(None,data,None)
        if self.isEmpty():
            self.head = n 
        else:
            temp=self.head
            while temp.next != None:
                temp=temp.next
            temp.next=n 
           # temp.next.prev=temp
            n.prev=temp
            
            
    def insertAfterAItem(self,data,item):
        n=Node(None,data,None)
        if self.isEmpty():
            print("DLL is Empty!!!")
        else:
            temp=self.head
            while temp != None:
                if temp.data == item:
                    if temp.next == None:
                        temp.next=n 
                        n.prev=temp
                        break
                    n.next=temp.next
                    temp.next.prev=n 
                    n.prev=temp
                    temp.next=n 
                    break
                temp=temp.next
                
            
            
    def oprintFun(self):
        if self.isEmpty():
            print("None")
            
        else:
            temp=self.head
            while temp !=None:
                print(temp.data,end='--->')
                temp=temp.next
            print('None')
            
            
            
            
            
            
obj:DLL=DLL()
obj.insertAtFirst(10)
obj.insertAtFirst(20)
obj.insertAtEnd(90)
obj.insertAtEnd(100)
obj.insertAfterAItem(100,10)
obj.oprintFun()
        