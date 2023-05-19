from os import system
from art import logo
print(logo)
skr=True 
def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def mul(n1,n2):
  return n1*n2
def div(n1,n2):
  return n1/n2
operations={
  '+' : add,
  '-' : sub,
  '*' : mul,
  '/' : div
}

def recalcu(ans):
  op1=input("Pick an operation")
  m3=int(input("What's the next number?: "))
  function=operations[op1](ans,m3)
  print(f"{ans} {op1} {m3} = {function}")
  cont=input(f"Type 'y' to continue calulating with {function},or type 'n' to start a new calculation: ").lower()
  if(cont=='n'):
    system('cls')
    print(logo)
    calcu()
  else:
    recalcu(function)
    
def calcu():
  m1=int(input("What's the first number?: "))
  op=input("+\n-\n*\n/\npick an operation: ")
  m2=int(input("What's the next number?: "))
  function=operations[op](m1,m2)
  print(f"{m1} {op} {m2} = {function}")
  cont=input(f"Type 'y' to continue calulating with {function},or type 'n' to start a new calculation: ").lower()
  if(cont=='n'):
    system('cls')
    print(logo)
    calcu()
  else:
    recalcu(function)
calcu()


