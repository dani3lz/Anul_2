import time

def pause():
    programPause = input("\nPress the <ENTER> key to continue...\n")

def merge_sort(lista):
	global iteratii1
	if len(lista) > 1:
		iteratii1+= 1
		mid = len(lista)//2
		L = lista[:mid]
		R = lista[mid:]
		merge_sort(L)
		merge_sort(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			iteratii1+= 1 
			if L[i] < R[j]: 
				lista[k] = L[i] 
				i+= 1
				iteratii1+= 1
			else: 
				lista[k] = R[j] 
				j+= 1
				iteratii1+=1
			k+= 1
		while i < len(L): 
			lista[k] = L[i] 
			i+= 1
			k+= 1
			iteratii1+= 1
		while j < len(R): 
			lista[k] = R[j] 
			j+= 1
			k+= 1
			iteratii1+= 1
	return lista

def quick_sort(lista):
	global iteratii2
	elements = len(lista)
	if elements < 2:
		iteratii2+= 1
		return lista
	pozitia_curenta = 0
	for i in range(1, elements):
		iteratii2+= 1
		if lista[i] <= lista[0]:
			iteratii2+= 1
			pozitia_curenta+= 1
			temp = lista[i]
			lista[i] = lista[pozitia_curenta]
			lista[pozitia_curenta] = temp
	temp = lista[0]
	lista[0] = lista[pozitia_curenta] 
	lista[pozitia_curenta] = temp
	left = quick_sort(lista[0:pozitia_curenta])
	right = quick_sort(lista[pozitia_curenta+1:elements])
	lista = left + [lista[pozitia_curenta]] + right
	return lista

def bubble_sort(lista):
	global iteratii3
	n = len(lista) 
	for i in range(n): 
		for j in range(0, n-i-1):
			iteratii3+= 1
			if lista[j] > lista[j+1]:
				lista[j], lista[j+1] = lista[j+1], lista[j]
				iteratii3+= 1
	return lista

def printList(n): 
    for i in range(len(n)):         
        print(n[i], end =" ") 
    print() 

def main():
	global iteratii1,iteratii2,iteratii3
	g = 1
	while(g == 1):
		print("\n1. Cazul cel mai bun.")
		print("2. Cazul mediu")
		print("3. Cazul cel mai rau")
		print("4. Exit")
		t = input("Numarul:\t")
		t = int(t)
		if t == 1:
			iteratii1=iteratii2=iteratii3=0
			n = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
			counter1 = time.perf_counter()
			sort1 = merge_sort(n)
			counter2 = time.perf_counter()
			counter = counter2 - counter1
			print("\n---------- MergeSort:")
			printList(sort1)
			print("Timp: {:.8f} secunde, Iteratii: {}".format(counter,iteratii1))
			n = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
			counter1 = time.perf_counter()
			sort2 = quick_sort(n)
			counter2 = time.perf_counter()
			counter = counter2 - counter1
			print("\n---------- QuickSort:")
			printList(sort2)
			print("Timp: {:.8f} secunde, Iteratii: {}".format(counter,iteratii2))
			n = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
			counter1 = time.perf_counter()
			sort3 = bubble_sort(n)
			counter2 = time.perf_counter()
			counter = counter2 - counter1
			print("\n---------- BubbleSort:")
			printList(sort3)
			print("Timp: {:.8f} secunde, Iteratii: {}".format(counter,iteratii3))
			pause()
		elif t == 2:
			iteratii1=iteratii2=iteratii3=0
			n = [8,6,7,1,3,4,5,0,2,10,9,18,16,17,11,13,14,15,12,20,19]
			counter1 = time.perf_counter()
			sort1 = merge_sort(n)
			counter2 = time.perf_counter()
			counter = counter2 - counter1
			print("\n---------- MergeSort:")
			printList(sort1)
			print("Timp: {:.8f} secunde, Iteratii: {}".format(counter,iteratii1))
			n = [8,6,7,1,3,4,5,0,2,10,9,18,16,17,11,13,14,15,12,20,19]
			counter1 = time.perf_counter()
			sort2 = quick_sort(n)
			counter2 = time.perf_counter()
			counter = counter2 - counter1
			print("\n---------- QuickSort:")
			printList(sort2)
			print("Timp: {:.8f} secunde, Iteratii: {}".format(counter,iteratii2))
			n = [8,6,7,1,3,4,5,0,2,10,9,18,16,17,11,13,14,15,12,20,19]
			counter1 = time.perf_counter()
			sort3 = bubble_sort(n)
			counter2 = time.perf_counter()
			counter = counter2 - counter1
			print("\n---------- BubbleSort:")
			printList(sort3)
			print("Timp: {:.8f} secunde, Iteratii: {}".format(counter,iteratii3))
			pause()
		elif t == 3:
			iteratii1=iteratii2=iteratii3=0
			n = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
			counter1 = time.perf_counter()
			sort1 = merge_sort(n)
			counter2 = time.perf_counter()
			counter = counter2 - counter1
			print("\n---------- MergeSort:")
			printList(sort1)
			print("Timp: {:.8f} secunde, Iteratii: {}".format(counter,iteratii1))
			n = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
			counter1 = time.perf_counter()
			sort2 = quick_sort(n)
			counter2 = time.perf_counter()
			counter = counter2 - counter1
			print("\n---------- QuickSort:")
			printList(sort2)
			print("Timp: {:.8f} secunde, Iteratii: {}".format(counter,iteratii2))
			n = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
			counter1 = time.perf_counter()
			sort3 = bubble_sort(n)
			counter2 = time.perf_counter()
			counter = counter2 - counter1
			print("\n---------- BubbleSort:")
			printList(sort3)
			print("Timp: {:.8f} secunde, Iteratii: {}".format(counter,iteratii3))
			pause()
		elif t == 4:
			g = 0

		else:
			print("\nNu exista asa optiune!\n")


if __name__ == '__main__':
	main()