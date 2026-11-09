class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class SLL:
    def __init__(self,head=None):
        self.head = head

    def insert_at_first(self,data):
        n = Node(data,self.head)
        self.head=n
        


    def is_empty(self):
    
            return self.head == None

    def insert_at_last(self,data):
        n=Node(data,None)

        if self.is_empty():
            self.head = n
        else:
            temp =  self.head
            while temp.next != None:
                temp = temp.next
            temp.next = n


    def search_a_node(self,item):
        if self.is_empty():
            return None
        else:
            temp = self.head
            while temp is not None:
                if temp.data == item:
                    return temp.data
                temp=temp.next
            return None


    def insert_at_any_position(self,pos,data):
        n=Node(data)
        if self.is_empty():
            return None
        else:
            temp = self.head
            count = 0
            while temp != None:
                if count < pos:
                    break
                count+=1
                temp=temp.next
            temp2=temp.next
            temp.next = n
            n.next=temp2

    def print_list(self):
        if self.is_empty():
            print("Empty SLL")
        else:
            temp = self.head
            while temp != None:
                print(temp.data,end='-->')
                temp = temp.next
            print("NULL")



    def delete_at_first(self):
        if self.is_empty():
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp = None
    
    def delete_at_last(self):
        if self.is_empty():
            return None
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp2 = temp.next
            temp.next = None
            temp2 = None

    def delete_at_particular_node(self,item):
        if self.is_empty():
            return None
        else:
            temp = self.head
            while temp != None:
                if temp.next.data == item:
                    break
                temp=temp.next
            temp2 = temp.next
            temp.next = temp.next.next
            temp2 = None

    def delete_at_any_position(self,pos):
        if self.is_empty():
            return None

        elif pos == 1:
            self.delete_at_first()
        else:
            count = 0
            temp = self.head
            while temp != None:
                count+=1
                if count == pos-1:
                    break
                temp=temp.next
            temp.next = temp.next.next


obj:SLL = SLL()
obj.insert_at_first(10)
obj.insert_at_first(5)
obj.insert_at_last(20)
obj.print_list()
print(obj.search_a_node(100))
obj.insert_at_any_position(2,100)
# obj.print_list()
# obj.delete_at_first()
# obj.print_list()
# obj.delete_at_last()
# obj.print_list()
# obj.delete_at_particular_node(10)
obj.print_list()
obj.delete_at_any_position(4)
obj.print_list()