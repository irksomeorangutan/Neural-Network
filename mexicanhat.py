import matplotlib.pyplot as plt

def corrections(i, r1, r2, m):
	k = i-r1
	h = i-r2
	j = i+r1+1
	l = i+r2+1
	if k<0:
		k = 0
	if h<0:
		h = 0
	if l>m:
		l = m
	if j>m:
		j = m
	return k, h, j, l

def activation_fn(x):
	if x<0:
		return 0
	elif x>2:
		return 2
	else:
		return x

# step1 - initialize parameteres and weights

n=int(input("Enter no. of neurons:"))
signal=[0.0]*n
print("\nEnter initial values of activations:")
for i in range(n):
    signal[i]=float(input(":"))
r1 = int(input("R1:"))
r2 = int(input("R2:"))
c1 = float(input("C1:"))
c2 = float(input("C1:"))
t_max = int(input("t_max:"))

x = signal.copy() # step 2


for t in range(0, t_max): #step 3 step 7 & 8
	x_old = x.copy() #step 6
	plt.plot(x_old)
	print ('t = {}'.format(t+1))
	for i in range(0, n):
		k, h, j, l = corrections(i, r1, r2, n)
		sum1 = sum((x_old[k:j]))
		left = sum(x_old[h:k])
		right = sum((x_old[j:l]))
		sum2 = left + right
		x[i] = activation_fn((c1*sum1 - c2*sum2)) # step 4 & 5
		print ('	x{} = {}'.format(i, x[i]))
plt.show()
