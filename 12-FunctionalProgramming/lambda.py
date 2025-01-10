'''import statistics
x = input("first number")
y = input("second number")

mean = lambda x,y: statistics.mean(x+y)

print(f"Mean is equal to : {mean(x,y)}")
'''
'''
n1 = int(input("1 : "))
n2 = int(input("2 : "))

mean = lambda n1,n2 : (n1+n2)/2

result = mean(n1,n2)
print(f"mean is {result}")
'''
'''
def ms_to_kmh(ms):
    return int(ms*3.6)
ms = int(input("jak szybko jedzie samochodzik? : "))
print(f"jedzie {ms_to_kmh(ms)} kmh")
'''
'''
ms = int(input("jak szybko jedzie samochodzik? : "))
ms_to_kmh = lambda ms : ms*3.6
print(f"jedzie {ms_to_kmh(ms)} kmh")
'''
'''
def a_s(dis,hour,min):
    av = dis/(hour+(min/60))
    return round(av,1)

dis = int(input(" podaj odleglość : "))
hour = int(input(" podaj godizny : "))
min = int(input(" podaj minuty : "))
print(f"srednia predkosc : {a_s(dis,hour,min)} km/h")
'''
'''
a_s = lambda dis,hour,min : round(dis/(hour+(min/60)),1)
dis = int(input(" podaj odleglość : "))
hour = int(input(" podaj godizny : "))
min = int(input(" podaj minuty : "))
print(f"srednia predkosc : {a_s(dis,hour,min)} km/h")
'''
'''
number = 4
number = int(number)
is_even = lambda number: number % 2

if is_even(number) == 0:
    print("even")
else:
    print("odd")
'''
'''
name = "Janek"
surname = "DSAD"
ini = lambda name,surname : name[0] + surname [0]
print(f"twoje inicjały to {ini(name,surname)}")
'''
'''
names = [
      'James',
      'Emily',
      'William',
      'Olivia',
      'Benjamin',
      'Sophia',
      'Henry']

sort_names = lambda names : sorted(names, key = len)
print(f"posortowane iminona : {sort_names(names)}")
'''
'''
sen = "I completely agree with you"
result = list(map(lambda sen : len(sen), sen.split))
print(result)
'''
'''
Products = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
value = list(map(lambda Products: Products[0] * Products[1], Products))
print(sum(value))
'''
employees = ["SMITH Lucy","JONES Janet","LEE Jerry","JACKSON Peter","JOHNSON Rick","LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e:e[0]=="J", employees))
print(emp_J)