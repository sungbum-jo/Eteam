po = float(input('po :'))
ne = float(input('ne :'))
mid = float(input('mid :'))

all = po + ne + mid

po1 = po/all
ne1 = ne/all
mid1 = mid/all

all1 = (po1 * 10) + ne1 + (mid1 * 5)

sum_pone = po+ne
po2=po/sum_pone
ne2=ne/sum_pone

pone = po2*10+ne2

print(all1)
print(pone)
print((all1+pone)/2)

