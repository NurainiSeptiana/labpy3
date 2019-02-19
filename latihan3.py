def perulangan():

	print(" ")

	import random
	a = 0
	jumlah = int(input("Masukkan Jumlah N"))

	print(" ")

	for x in range(0,jumlah):
		i=random.uniform(0.0,0.5)
		a+=1S
		print("data ke-"=>,a,"=>",i) 

	print(" ")
	print("Terimakasi Sudah Menggunakan Program Ini ")
	print(" ")
	print("DILARANG MENG COPPY PROGRAM TANPA IZIN")
	print(" ")

	jawab = "ya"
	hitung = 0
	while jawab == "ya":
		hitung += 1
		jawab = input("Ingin Mengulang Program Ini ? (ya/tidak) ")
		if menjawab == "ya" :
			return pengulangan()
		elif jawab == "tidak" :
			break
	print("Total perulangan : ",hitung)

perulangan()
