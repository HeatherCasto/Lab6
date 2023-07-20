a=True
def encoder(password):
  b=[]
  for i in password:
    #int(i)
    c=(int(i)+3)%9
    str(c)
    b.append(c)
  for j in b:
    print(j,end="")
while a is True:
  print(" ")
  print("choose you opition ")
  print(" ")
  inp=int(input("choose 1 for encoder and 2 for decoder"))
  password=str(input("enter the password"))
  if inp==1:
             encoder(password)
