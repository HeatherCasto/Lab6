a=True
def encoder(password):
  b=[]
  for i in password:
    #int(i)
    c=(int(i)+3)%10
    str(c)
    b.append(c)
  for j in b:
    print(j,end="")
 b=[]
  for i in password:
    c=(int(i)-3)%10
    str(c)
    b.append(c)
  for j in b:
    print(j,end="")
  # for j in b:
  #   print(b)
  # b=str(b)[1:-1]
  # ' '.join(b)
  # for j in b:
  #   print(b)
def decode(password_encoded):
    password = ""
    for i in password_encoded:
        decoded_num = str((int(i) - 3) % 10)
        password += decoded_num
    return password
#original decode function
#def decoder(password):

 # b=[]
 # for i in password:
    # c=(int(i)-3)%10
  #   str(c)
  #   b.append(c)
  # for j in b:
  #   print(j,end="")
while a is True:
  print(" ")
  print("choose you opition ")
  print(" ")
  inp=int(input("choose 1 for encoder and 2 for decoder"))
  password=str(input("enter the password"))
  if inp==1:
             encoder(password)
  elif inp==2:
    decoder(password)
