def linearSearch(niz, zeljeniBroj):
	for index in range(len(niz)):
	    if niz[index] == zeljeniBroj:
 		    return index
	
print(linearSearch([1, 4, 1, 6, 3, 7, 4, 2], 7))
    
def binarySearch(niz, zeljeniBroj):
    duzinaNiza = len(niz)
    donjaGranica = 0
    gornjaGranica = duzinaNiza - 1
    sredina = 0

    while donjaGranica <= gornjaGranica:
        sredina = (donjaGranica + gornjaGranica) // 2
        if niz[sredina] < zeljeniBroj:
            donjaGranica = sredina + 1
        elif niz[sredina] > zeljeniBroj :
            gornjaGranica = sredina - 1
        else:
            return sredina
    return -1

print(linearSearch([1, 2, 3, 6, 8, 232, 312 ,456, 564], 312))