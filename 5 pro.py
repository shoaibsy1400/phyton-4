16.04

n = int(input())
spaces=n-1
stars=1
for i in range(n):
  for j in range(spaces):
      print(" ",end=" ")
  for j in range(stars):
      print("*",end=" ")
  print()
  spaces=spaces-1
  stars=stars+2




g=[18,12,13,15,18,20,26]
n=len(g)
target=18
r=0
for i in range(n):
    if g[i]==target:
        r=r+1
print(r)





def totaloccurences(list):
    r=0
    n=len(g)
    for i in range(n):
        if g[i]%2==0:
            print(g[i])
            r=r+1
    return r

g=[18,12,13,15,18,20,26,3,5,7,5]
n=len(g)

result=totaloccurences(g)
print(result)




def greatest(list):
    r=0
    
    n=len(g)
    for i in range(n):
        if g[i]>r:
            r=g[i]
    return r
g=[8,12,13,15,31,21,51,3,5,7,5]
n=len(g)

result=greatest(g)
print("Greatest: ",result)





word=input()
print(word)
l=word[::-1]
print(l)
m=word[-10:-16:-1]
print(m)
n=word[5:10]
print(n[::-1])












17.04.24



word=input()
print(word)
n=len(word)
print(n)
store=dict()
print(store)
store['p']=12
store['s']=9
store['t']=8
store['s']=9
store['q']="abcf"
store["store"]=5
print(store)
keys=store.keys()
print(keys)
for ele in keys:
    print(ele,store[ele])






word=input()
print(word)
store=dict()
for ch in word:
    if ch in store:
        store[ch]=store[ch]+1
    else:
        store[ch]=1
print(store)

resultchar='#'
resultfrequency=0

allkeys=store.keys()//stores all the keys present in the dictionaries
for ele in allkeys:
    if store[ele] > resultfrequency://repitition of each letter
       resultfrequency=store[ele]//stores the frequency of each letter in resultfrequency
       resultchar=ele//stores the highest frequency letter
print(resultchar,resultfrequency)



i=12
while i < 57:
    if i%2==0:
        print(i)
    i+=1


i=56
while i < 98:
 print(i)
 i+=1






class Box:
    def _init_(self,currname,currroll,currmarks):
       self.name=currname
       self.roll=currroll
       self.marks=currmarks

student1=Box("ABC",78,89)
print(student1.name)
print(student1.roll)
print(student1.marks)

student2=Box("EDE",54,68)
print(student2.name)
print(student2.roll)
print(student2.marks)

student3=Box("FKJ",12,78)
print(student3.name)
print(student3.roll)
print(student3.marks)

student4=Box("SDJK",45,56)
print(student4.name)
print(student4.roll)
print(student4.marks)

student5=Box("CJI",25,80)
print(student5.name)
print(student5.roll)
print(student5.marks)






class Card:
    def _init_(self,imageURL,price,rating,description,delivery,comment,brand):
       self.imageURL=imageURL
       self.price=price
       self.rating=rating
       self.description=description
       self.delivery=delivery
       self.comment=comment
       self.brand=brand

    def printalldetails(self):
      print("IMAGE URL:",self.imageURL)
      print("PRICE:",self.price)
      print("RATING:",self.rating)
      print("DESCRIPTION:",self.description)
      print("DELIVERY:",self.delivery)
      print("COMMENTS:",self.comment)
      print("BRAND:",self.brand)

laptop=Card("1-dummy-url1", 50000, 4, "ABD","4days",['good','best'], "DELL")
laptop.printalldetails()


phone=Card("2-dummy-url2",25000, 4.5, "DEF","2days",['better','best'], "samsung")
phone.printalldetails()

smartwatch=Card("3-dummy-url3", 6000, 4, "FGH","5days",['good','best'], "boat")
smartwatch.printalldetails()








class Card:
    def _init_(self,imageURL,price,rating,description,delivery,comment,brand):
       self.imageURL=imageURL
       self.price=price
       self.rating=rating
       self.description=description
       self.delivery=delivery
       self.comment=comment
       self.brand=brand

    def printalldetails(self):
      print("IMAGE URL:",self.imageURL)
      print("PRICE:",self.price)
      print("RATING:",self.rating)
      print("DESCRIPTION:",self.description)
      print("DELIVERY:",self.delivery)
      print("COMMENTS:",self.comment)
      print("BRAND:",self.brand)

    def printbasicdetails(self):
        print("BRAND:",self.brand)
        print("PRICE:",self.price)
        print("RATING:",self.rating)
    
    def calculateGST(self):
      print("Calculating GST")
     
    def printInvoice(self,extraprice):
        print("Printing Invoice")

laptop=Card("1-dummy-url1", 50000, 4, "ABD","4days",['good','best'], "DELL")
laptop.printbasicdetails()
laptop.calculateGST()
laptop.printInvoice(1250)

phone=Card("2-dummy-url2",25000, 4.5, "DEF","2days",['better','best'], "samsung")
phone.printbasicdetails()
phone.calculateGST()
phone.printInvoice(1350)

smartwatch=Card("3-dummy-url3", 6000, 4, "FGH","5days",['good','best'], "boat")
smartwatch.printbasicdetails()
smartwatch.calculateGST()
smartwatch.printInvoice(1200)






password=2387
n=3
w=int(input())
for i in range(3):
    if(w==password):
         print("successfully logged in")
    else:
        if n==1:
            print("Your account is blocked, try after 24 hours")
        else:
            print("incorrect password, you are left with",n-1,"attempts")


18.04

try:
    a=10/2
except:
    print("division by zero exception occured")
else:
    print(a,"No exception occured")
finally:
    print("Finally is executed")
print("outside the try block")





a=[0,1,2,3]
try:
    print(y)
except:
    print("exception occured")
else:
    print(a,"No exception occured")
finally:
    print("Finally is executed")
print("outside the try block")




a=[0,1,2,3]
try:
    print(a[5])
except:
    print("exception occured")
else:
    print(a,"No exception occured")
finally:
    print("Finally is executed")
print("outside the try block")



a=[0,1,2,3]
try:
    #a=10/0
    #print(y)
    print(a[5])
except IndexError:
    print("Exception occured due to index out of bound")
except ZeroDivisionError:
    print("Exception occured due to division by zero")
except NameError:
    print("Exception occured due to undefined variable")
except:
    print("Exception occured")
else:
    print(a,"No exception occured")
finally:
    print("Finally is executed")
print("outside the try block")





-->multilevel inheritence
class Box:
    def _init_(self,name,roll):
        self.name=name
        self.roll=roll

class Student:
    def _init_(self,fees):
        self.fees=fees

class Box2(Box,Student):
    def _init_(self,name,roll,marks,fees):
        self.marks=marks
        Box._init_(self,name,roll)
        Student._init_(self,fees)

class Box3(Box2):
    def _init_(self,sem):
        self.sem=sem
        Box2._init_(self,"ABCD",25,80,52000)

b1=Box2("riya",52,92,58000)
print(b1.name)
print(b1.roll)
print(b1.marks)
print(b1.fees)


b2=Box3("3rd sem")
print(b2.sem)



-->multiple inheritence

class Box:
    def _init_(self,name,roll):
        self.name=name
        self.roll=roll

class Student:
    def _init_(self,fees):
        self.fees=fees

class Box2(Box,Student):
    def _init_(self,name,roll,marks,fees):
        self.marks=marks
        Box._init_(self,name,roll)
        Student._init_(self,fees)



b1=Box2("riya",52,92,58000)
print(b1.name)
print(b1.roll)
print(b1.marks)
print(b1.fees)




-->single inheritence

class Box:
    def _init_(self,name,roll):
        self.name=name
        self.roll=roll

class Box2(Box):
    def _init_(self,name,roll,marks):
        self.marks=marks
        Box._init_(self,name,roll)

b1=Box2("riya",52,92)
print(b1.name)
print(b1.roll)
print(b1.marks)




-->single linked list

class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
b1=Node(10)
b2=Node(20)
b3=Node(30)
b4=Node(40)
b5=Node(50)
b6=Node(60)
b7=Node(70)
b8=Node(80)
b9=Node(90)
b10=Node(100)

b1.next=b2
b2.next=b3
b3.next=b4
b4.next=b5
b5.next=b6
b6.next=b7
b7.next=b8
b8.next=b9
b9.next=b10
curr=b1
while curr!=None:
    print(curr.data,end="-->")
    curr=curr.next



-->operations on the list of elements

class Node:
    def _init_(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print()
 
def insertAtEndOfTail(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    return head

def insertNodeAtHeadOfLinkedList(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    newBlock.next = head 
    return newBlock
 
def insertAtSpecificPosition(head, position, value):
    newBlock = Node(value)
    if position == 1:
        newBlock.next = head 
        return newBlock
 
    index = 1 
    curr = head 
    while index != position - 1:
        curr = curr.next 
        index += 1 
 
    newBlock.next = curr.next
    curr.next = newBlock
    return head

def deleteAtEnd(head):
    curr = head
    previous = None
    while curr.next != None:
        previous = curr
        curr = curr.next
    previous.next = None
    return head

 
l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertAtEndOfTail(head, ele) 
head = deleteAtEnd(head)  
printLinkedList(head)  

l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertAtEndOfTail(head, ele) 
head = insertAtSpecificPosition(head, 10, 109)
printLinkedList(head)  

l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertAtEndOfTail(head, ele)  
printLinkedList(head)  

l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    head = insertNodeAtHeadOfLinkedList(head, ele)  
printLinkedList(head)
