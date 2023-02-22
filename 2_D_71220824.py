platno = input("Masukan plat nomor: ").split()[1]
plat = (int(platno))
try:
  if plat <= 3000:
    print("Plat nomor ini untuk mobil masbro") 
  elif plat  >= 3001 and plat <=  4000:
    print("Plat nomor ini untuk motor masbro")
  elif plat  >= 4001 and plat <= 5000:
    print("Plat nomor ini untuk angkutan umum masbro")
  else:
    print("Plat nomor tidak terindikasi masbro")
    
except:
    print()
