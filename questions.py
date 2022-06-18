input: [1,2,3,4,5,6,7,8,9,10]
output: [1,2,3,4,5,10,9,8,7,6]
	
_____________________________________________

input: [1,2,3,4,5,6,7,8,9,10]
output: [1,2,3,4,6,7,8,10]
	
_____________________________________________

Least frequent charater in string

input: "pythonprogramming"
output:["y","t","h","a","i"]
	
______________________________________________

Removing duplicates from list

list1 = [10,10,20,30,40]
list2 = [10,20,40,50,60]

output: [10,10,20,30,40,20,30,50,60]
	
_______________________________________________
Using slicing:
	
a=[1,2,3,4,5]
print(a[10:])

_______________________________________________

def extendlist(val,list=[]):
	list.append(val)
	return list

list1 = extendlist(10)
list2 = extendlist(123,[])
list3 = extendlist('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)

_______________________________________________

list1 = ['a','b','c','d']
list2 = []
list2 = list1
list2.append('e')
print(list1)
print(list2)

_________________________________________________

a="santra techspot"
while i in a:
	print(i)
	

a="santra techspot"
i = 'i'
while i in a:
	print(i)
	

a="image"
while i in a:
	print(i)
	
___________________________________________________

list1 = ['hi']
tuple1 = ('hi')
tuple2 = ('hi',)
print(type(list1))
print(type(tuple1))
print(type(tuple2))

___________________________________________________

print(format('welcome','10s'),en='#')
print(format(924.656,'3.2f'))

___________________________________________________

False = True
if False:
	print('hi')

___________________________________________________

x = 'abcd'
for i in range(x):
	print(i)
	
____________________________________________________

d = {'name':'vijay','place':'chennai','college':'xyz'}
for x in d:
	print(x)
	
_____________________________________________________

def demo(x, y=[]):
	y.append(x)
	return y
demo(1)
demo(2)
z = demo(3)
print(z)

______________________________________________________

a = {'a' : 1,'b' : 2,'c' : 3}
for key,value in a:
	print(key,value)
	
	
a = {'a' : 1,'b' : 2,'c' : 3}
for key,value in a.items():
	print(key,value)
_______________________________________________________

string = 'welCOME'
print(a.capitalize())

_______________________________________________________

a = ['welcome','santra','techspot']
a.insert(a.index('santra'),'to')
print(a)

_______________________________________________________

def func(list1):
	list1 += [1]
	
mylist = [1,2,3,4]
func(mylist)
print(len(mylist))

_______________________________________________________

list1 = ['welcome','to','santra','techspot']
list2 = list1
list3 = list1[:]
_______________________________________________________