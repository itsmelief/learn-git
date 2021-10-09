print('''
			  Program Tebak Usia  
		[ Saya akan menebak umur Anda ]
	[ Silahkan Anda masukkan tahun kelahiran Anda ]
	''')

tahun_kelahiran = input('  Masukkan tahun kelahiran : ')
tahun_sekarang = 2021 - int(tahun_kelahiran)
print('  Umur Anda ' + str(tahun_sekarang) + ' tahun')