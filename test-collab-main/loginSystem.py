print("============== LOGIN SYSTEM =============\n")

list_cmd = ["Buat Akun", "Login Akun"]
for no,list in enumerate(list_cmd, start=1):
  print(f"{no}. {list}")
  
cmd = input(">> ")
while True:
  if cmd == "1":
    username = input("Buat Username : ")
    password = input("Buat password : ")

    print("Akun berhasil dibuat, silahkan login")

  elif cmd == "2":
    user = input("Masukkan Username : ")
    psw = input("Masukkan password : ")

    if user == username and psw == password:
      print("Akses diterima")
      print(f"Selamat datang {user}")
    else:
      print("Password atau Username salah")
      
  elif cmd == "0":
    break

  else:
    print("Perintah tidak valid")
