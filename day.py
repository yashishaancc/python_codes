d = int(input("Enter date(1-31): "))
m = int(input("Enter month(1-12): "))
y = int(input("Enter year(>=1): "))
f = 0
a = (y-1)%400
o = 1 if (y%4 == 0 and y%100 != 0 or y%400 == 0) else 0
if a//100 == 1:
	f = 5 + a-100 + (a-100)//4 + d
if a//100 == 2:
	f = 3 + a-200 + (a-200)//4 + d
if a//100 == 3:
	f = 1 + a-300 + (a-300)//4 + d
if a//100 == 0:
	f = 0 + a-000 + (a-000)//4 + d
if m == 1:
	f += 0
if m == 2:
	f += 3
if m == 3:
	f += 3+o
if m == 4:
	f += 3+o+3
if m == 5:
	f += 3+o+3+2
if m == 6:
	f += 3+o+3+2+3
if m == 7:
	f += 3+o+3+2+3+2
if m == 8:
	f += 3+o+3+2+3+2+3
if m == 9:
	f += 3+o+3+2+3+2+3+3
if m == 10:
	f += 3+o+3+2+3+2+3+3+2
if m == 11:
	f += 3+o+3+2+3+2+3+3+2+3
if m == 12:
	f += 3+o+3+2+3+2+3+3+2+3+2
f = f%7
if f == 0:
	print("Sunday")
if f == 1:
	print("Monday")
if f == 2:
	print("Tuesday")
if f == 3:
	print("Wednesday")
if f == 4:
	print("Thursday")
if f == 5:
	print("Friday")
if f == 6:
	print("Saturday")