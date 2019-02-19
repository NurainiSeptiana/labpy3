print ('Program untuk menentukan bilangan terbesar')

def pengulangan():
	print ('Masukkan 3 bilangan yang diinginkan!')
	a=int(input('bilangan1 = '))
	b=int(input('bilangan2 = '))
	c=int(input('bilangan3 = '))

	if a>b and a>c:
		if b>c:
			print (a, 'adalah bilangan terbesar dari', b, 'dan', c,)
		else:
			print (a, 'adalah bilangan terbesar dari', c, 'dan', b,)
	elif b>a and b>c:
		if a>c:
			print (b, 'adalah bilangan terbesar dari', c, 'dan', a,)
		else:
			print (b, 'adalah bilangan terbesar dari', a, 'dan', c,)
	else:
		if a>b:
			print (c, 'adalah bilangan terbesar dari', b, 'dan', a,)
		else: 
			print (c, 'adalah bilangan terbesar dari', a, 'dan', b,)
	print ('')
	print ('Ingin coba lagi? (ya/tidak)')
	x=input()
	if x=='ya':
		return pengulangan()
	if x=='tidak':
		print('terimakasi telah menggunakan program ini. Nuraini Septiana TI.18.A3')
pengulangan()