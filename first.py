'''d = {1:'vishwa',2:'mohan',3:'raj',4:'bhuvan',6:{1:2343,2:'fdbhhd',3:323443}}
print(d)
print(d.keys())
print(d.values())
d[3]= 'shashi'
print(d[6][3])
s={1,2,2,3,4,5,5,5}
len(s)
print(s'''
class House:
    def __init__(self,key,owner,flatno,no_of_members):
        self.key = key
        self.owner  = owner
        self.flatno = flatno
        self.no_of_members = no_of_members
    def display_owner(self,key):
        if self.key == key:
            print("the owner is:",self.owner)
        else:
            print("the key dismatched")
    def total_no(self):
        print("the total member in the family is:",self.no_of_members)


h1 = House(22,'siddamma','#275',3)
h1.display_owner(22)
h1.total_no()