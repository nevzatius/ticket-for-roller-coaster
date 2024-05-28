print("Hız trenine hoş geldiniz!")
height = int(input("Boyunuz kaç cm?"))
bill = 0

if height > 120:
  print("Hız trenine binebilirsiniz!")
  age = int(input("Kaç yaşındasınız?"))
  if age < 12:
    bill = 5
    print("Çocuk için hız Treni bileti 5₺")
  elif age <=18:
    bill = 10
    print("Genç için hız Treni bileti 10₺")
  elif age >=45 and <=55:
    bill = 0
    print("Sizlere ücretsiz.")
  else:
    bill = 15
    print("Yetişkin için hız Treni bileti 15₺")

  
  foto = input("Fotoğraf çekilmek ister misiniz? Evet veya Hayır.")
  if foto == "Evet":
    bill += 5
    print(f"Ödemeniz gereken tutar{bill}₺.")
  else:
    print(f"Ödemeniz gereken tutar{bill}₺.")
else:
  print("Maalesef hız trenine binemezsiniz.")