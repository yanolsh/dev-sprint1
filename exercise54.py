# This is where Exercise 5.4 goes
# Name:Yan Olshevskyy

def is_triangle(first, second ,third):
	
	if (first>second+third) or (second>first+third) or (third>first+second):
		print "No"
	else:
		print "Yes"

def get_user_input():
	first=int(raw_input('Please enter the first side of the triangle:\n'))
	
	second=int(raw_input('Please enter the second side of the triangle:\n'))
	third=int(raw_input('Please enter the thid side of the triangle:\n'))
	is_triangle(first, second, third)

def main():
	get_user_input()

if __name__ =='__main__':
	main()
