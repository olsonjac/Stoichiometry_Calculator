#constant varibale used for converting atoms to moles
avogadro = float(6.02 * 10**23)

#gram to gram conversion that asked for the necessary variable inputs
def gram_gram():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in grams of the given reactant: "))
  r1m = float(input("enter the atomic mass for the given reactant: ")) 
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  r2m = float(input("Enter the atomic mass of the desired product: "))
  answer = (float(r1a)/r1m)*(r2c/r1c)*(r2m)
  print(f"{answer} grams of {r2} will be made.") 
  
def gram_atom():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in grams of the given reactant(use \"^\" for exponents and including NO labels): "))
  r1m = float(input("enter the atomic mass for the given reactant: ")) 
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (float(r1a)/r1m)*(r2c/r1c)*(avogadro)
  print(f"{r2} will end up with {answer} atoms") 

def gram_mol():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in grams of the given reactant(use \"^\" for exponents): "))
  r1m = float(input("enter the atomic mass for the given reactant: ")) 
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a/r1m)*(r2c/r1c)
  print(f"there are {answer} moles of {r1}")

def gram_Liter():  
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in grams of the given reactant(use \"^\" for exponents): "))
  r1m = float(input("enter the atomic mass for the given reactant: ")) 
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a/r1m)*(r2c/r1c)*(22.4)
  print(f"{answer} Liters of {r2} will be made.")

#the "eval" expression is used to convert a written expression in scientific notation to a useable variable
def atom_atom():
  r1 = input("enter the given reactant symbol: ")
  r1a = input("enter the amount of the given reactant in atoms(use \"^\" for exponents): ")
  r1a = r1a.replace("^","**")
  r1a = r1a.replace(" ","")
  r1a = eval(r1a)
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (float(r1a)/avogadro)*(r2c/r1c)*(avogadro)
  print(f"{r1} will make {answer} atoms of {r2}") 

#atoms to mole conversion function.
def atom_mol():
  r1 = input("enter the given reactant symbol: ")
  r1a = input("enter the amount of atoms of the given reactant (use \"^\" for exponents): ")
  r1a = r1a.replace("^","**")
  r1a = eval(r1a)
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the disred product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a/avogadro)*(r2c/r1c)
  print(f"there are {answer} moles of {r2}")

#moles to atom conversion
def mol_atom():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the moles of the given reactant(use \"^\" for exponents): "))
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbl of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a)*(r2c/r1c)*(avogadro)
  print(f"there are {answer} atoms of {r2}")
#moles to Liter conversion
def mol_L():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the moles of the given reactant(use \"^\" for exponents): "))
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a)*(r2c/r1c)*(22.4)
  print(f"there are {answer} Liters of {r1}")

#Atom to liter conversion    
def atom_L():
  r1 = input("enter the given reactant symbol: ")
  r1a = input("enter the amount of atoms of the given reactant (use \"^\" for exponents): ")
  r1a = eval(r1a)
  r1a = r1a.replace("^","**")
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (float(r1a)/avogadro)*(r2c/r1c)*(22.4)
  print(f"there are {answer} Liters of {r2}")

#moles to moles conversion
def mol_mol():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the moles of the given reactant: "))
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a)*(r2c/r1c)
  print(f"there are {answer} moles of {r2}")

#Liters to moles conversion
def Liter_mol():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in Liters of the given reactant: "))
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a/22.4)*(r2c/r1c)
  print(f"there are {answer} moles of {r2}")

#Liters to atoms conversion
def Liter_atom():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in Liters of the given reactant: "))
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a/22.4)*(r2c/r1c)*(avogadro)
  print(f"there are {answer} atoms of {r2}")
  
#Liters to liters conversion
def Liter_Liter():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in Liters of the given reactant: "))
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a/22.4)*(r2c/r1c)*(22.4)
  print(f"there are {answer} Liters of {r2}")

#initializes user input for the while loop below
initial = ""
final = ""

#while loop that controls the main body of the code
while True:
  
  initial = input("enter what units you START with(grams(g),moles(m),Liters(L),atoms(a)):")
  final = input("enter what units you need at the END (grams(g),moles(m),Liters(L),atoms(a)): ") 

#if statements that check for which function to implement based on the initial and final variables.

  if final == "a" and initial == "a":
    atom_atom()
    break
  elif initial == "a" and final == "m":
    atom_mol()
    break
  elif initial == "m" and final == "L":
    mol_L()
    break
  elif  initial == "a" and final == "L":
    atom_L()
    break
  elif  initial == "m" and final == "m":
    mol_mol()
    break
  elif initial == "m" and final == "a":
    mol_atom()
    break
  elif initial == "g" and final == "m":
    gram_mol()
    break
  elif initial == "g" and final == "a":
    gram_atom()
    break
  elif initial == "g" and final == "L":
    gram_Liter()
    break
  elif initial == "L" and final == "a":
    Liter_atom()
    break
  elif initial == "L" and final == "m":
    Liter_mol()
    break
  elif initial == "L" and final == "L":
    Liter_Liter()
    break
  elif initial == "g" and final == "g":
    gram_gram()
    break
  #informs user they did not enter the correct option
  else:
    print("make sure you choose from the available options(g,a,L,m)")
    print("")
    continue
    
