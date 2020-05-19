from fractions import Fraction

def Weyl_dimension_formula_SO10(a1,a2,a3,a4,a5):

	a = [0, a1, a2, a3, a4, a5]

	prod1 = 1
	prod2 = 1
	prod3 = 1

	for k in [1,2,3]:
		for i in range(1,k+1):
			sum1 = 0
			for j in range(i,k+1):
				sum1 = sum1 + a[j]
			prod1 = prod1*(Fraction(sum1,(k-i+1))+1)

	for k in [0,1,2,3]:
		for l in [4,5]:
			sum2 = 0
			for j in range(1,k+1):
				sum2 = sum2 + a[4-j]
			prod2 = prod2*(Fraction((sum2 + a[l]),(k+1)) + 1)

	for k in [0,1,2]:
		for i in range(k+1,4):
			sum3 = 0
			for j in range(k+1,i+1):
				sum3 = sum3 + a[4-j]
			sum4 = 0
			for j in range(1,k+1):
				sum4 = sum4 + 2*a[4-j]
			prod3 = prod3*(Fraction((sum3+sum4+a4+a5),(i+k+2)) + 1)

	result = prod1*prod2*prod3
	return result

# input Dynkin label [a1,a2,a3,a4,a5]
a1 = 0
a2 = 1
a3 = 0
a4 = 0
a5 = 1

# calculate the dimension by Weyl dimension formula
dimension = Weyl_dimension_formula_SO10(a1,a2,a3,a4,a5)
print(dimension)



