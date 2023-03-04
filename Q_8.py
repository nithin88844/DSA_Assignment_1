from collections import deque

class stack:
    def __init__(self):
        self.data = deque()

    def push(self,element):
        self.data.append(element)
        return self.data
    
    def view(self):
        if self.isEmpty():
            print("your stack is empty")
        else:
            return self.data
    
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        return False 
    
    def reverse(self):
        data_ = self.data.reverse()
        return(data_)
   
        

                
                


             
    
    
    


obj = stack()
obj.push(9)
obj.push(13)
obj.push(34)
obj.push(456)
obj.push(344)
print(obj.view())
obj.reverse()
print(obj.view())