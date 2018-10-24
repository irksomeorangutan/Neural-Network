from random import uniform
def activation_fn(x):
	if x>0:
		return x
	return 0

n=int(input("Enter no. of neurons:"))
activations=[0.0]*n
print("\nEnter initial values of activations:")
for i in range(n):
    activations[i]=float(input(":"))

k=float(input("\nEnter inhibitory weight : "))
 
print ("\nInitial values of activations:", activations )


a_old = activations.copy()
a_new = []
count = 0
while True: 
	temp = sum(a_old)
	for i in range(0, n): 
		value = a_old[i] - k * temp + k * a_old[i]
		a_new.append(activation_fn(value))
	a_old = a_new.copy() 
	count += 1
	if sum(a_new) == max(a_new): 
		break
	print('Iteration {} - activations = {}'.format(count, a_old))
	a_new = []
	
print('Iteration {} - activations = {}'.format(count, a_new))


i=0
while a_new[i]==0:
    i=i+1
print ("Winning neuron : ",i+1)
