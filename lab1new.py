from math import *
import sys
sys.setrecursionlimit(5000)

lambd = 1
omega = 1/2
eps = 10**(-8)
delt = 0.06
x0 = [2,6]

def pause():
    programPause = input("\nPress the <ENTER> key to continue...\n")

def f(x,y):
	return float((2*(x**2)) + (3*x*y) + (6*(y**2)) - (6*x) - (2*y))

def derivata_x(x,y):
	return float((4*x)+(3*y)-6)

def derivata_y(x,y):
	return float((3*x)+(12*y)-2)

def gradientul(x,y):
	gradient = [derivata_x(x,y),derivata_y(x,y)]
	return gradient

def magnitudinea(x,y):
	grad = gradientul(x,y)
	grad[0] = float(grad[0])
	grad[1] = float(grad[1])
	mag = sqrt(grad[0]*grad[0] + grad[1]*grad[1])
	return mag

def pretendent(x,y,lambd):
	val1 = [x,y]
	grad = gradientul(x,y)
	val2 = [grad[0]*lambd,grad[1]*lambd]
	z = [val1[0]-val2[0], val1[1]-val2[1]]
	return z

def rezolv(x,y,lambd,limit):
	limit+=1
	z = pretendent(x,y,lambd)
	f0 = f(x,y)
	fz = f(z[0],z[1])
	gradz = gradientul(z[0],z[1])
	magnit0 = magnitudinea(x,y)
	magnitz = magnitudinea(z[0],z[1])
	if magnitz < eps or limit == 4000: 
		print("\n<Conditia de stopare a fost atinsa!> Nr:", str(limit))
		print("\nz = ", str(z))
		print("F(z) = ", str(fz))
		print("Gradientul = ", str(gradz))
		print("Magnitudinea = ", str(magnitz))
	else:
		if fz-f0 <= -delt*lambd*(magnit0*magnit0):
			print("\nSATISFACE Nr:", str(limit))
			print("---------------------------------------------------------")
			rezolv(z[0],z[1],lambd,limit)
		else:
			lambd = lambd*omega
			rezolv(x,y,lambd,limit)

def main():
	rezolv(x0[0],x0[1],lambd,limit=0)
	pause()

if __name__ == '__main__':
	main()