avogadro = float(6.02 * 10**23)

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
  print("")
  print(f"{r1a}g {r1}      {r2c} mol {r2}    {r2m} g {r2}")
  print(f"-------   x  -------- x --------- =     {answer} grams {r2}")
  print(f"{r1m}g/mol {r1}  {r1c} mol {r1}     1 mol {r2}")
  
def gram_atom():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in grams of the given reactant: "))
  r1m = float(input("enter the atomic mass for the given reactant: ")) 
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (float(r1a)/r1m)*(r2c/r1c)*(avogadro)
  print(f"{r2} will end up with {answer} atoms")
  print("")
  print(f"{r1a}g {r1}      {r2c} mol {r2}    {avogadro} atoms {r2}")
  print(f"-------   x  -------- x --------- =     {answer} atoms {r2}")
  print(f"{r1m}g/mol {r1}  {r1c} mol {r1}     1 mol {r2}")

def gram_mol():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in grams of the given reactant(use \"^\" for exponents): "))
  r1m = float(input("enter the atomic mass for the given reactant: ")) 
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  print("")
  answer = (r1a/r1m)*(r2c/r1c)
  print(f"there are {answer} moles of {r1}")
  print("")
  print(f"{r1a}g {r1}      {r2c} mol {r2}")
  print(f"-------   x  -------- = {answer} moles {r2}")
  print(f"{r1m}g/mol {r1}  {r1c} mol {r1}")
  
def gram_Liter():  
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in grams of the given reactant(use \"^\" for exponents): "))
  r1m = float(input("enter the atomic mass for the given reactant: ")) 
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a/r1m)*(r2c/r1c)*(22.4)
  print("")
  print(f"{answer} Liters of {r2} will be made.")
  print(f"{r1a}g {r1}        {r2c} mol         22.4 L")
  print(f"---------  x ----------x --------- = {answer} Liters {r2}")
  print(f"{r1m}g/mol {r1}    {r1c} mol        1 mol {r2}")

def atom_atom():
  r1 = input("enter the given reactant symbol: ")
  r1a = input("enter the amount of the given reactant in atoms(use \"^\" for exponents): ")
  r1a = r1a.replace("^","**")
  r1a = eval(r1a)
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (float(r1a)/avogadro)*(r2c/r1c)*(avogadro)
  print(f"{r1} will make {answer} atoms of {r2}") 
  print("")
  print(f"{round(r1a,3)}g {r1}        {r2c} mol    {round(avogadro,3)} atoms     ")
  print(f"---------  x ----------x --------- = {answer} atoms {r2}")
  print(f"{round(avogadro,3)} {r1}    {r1c} mol       1 mol {r2}")

def atom_mol():
  r1 = input("enter the given reactant symbol: ")
  r1a = input("enter the amount of atoms of the given reactant (use \"^\" for exponents): ")
  r1a = r1a.replace("^","**")
  r1a = eval(r1a)
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a/avogadro)*(r2c/r1c)
  print(f"there are {answer} moles of {r2}")
  print("")
  print(f"{round(r1a,3)}atoms {r1}    {r2c} mol")
  print(f"---------  x  --------- = {answer} moles {r2}")
  print(f"{round(avogadro,3)} {r1}    {r1c} mol")

def mol_atom():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the moles of the given reactant \n(use \"^\" for exponents):"))
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a)*(r2c/r1c)*(avogadro)
  print(f"there are {answer} atoms of {r2}")
  print("")
  print(f"{r1a}mol {r1}      {r2c} mol    {avogadro} atoms ")
  print(f"---------  x ----------x --------- = {answer} atoms {r2}")
  print(f"    1          {r1c} mol         1")

def mol_L():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the moles of the given reactant(use \"^\" for exponents): "))
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a)*(r2c/r1c)*(22.4)
  print(f"there are {answer} Liters of {r1}")
  print("")
  print(f"{r1a}mol {r1}      {r2c} mol    22.4 L ")
  print(f"---------  x ----------x --------- = {answer} Liters {r2}")
  print(f"    1          {r1c} mol         1 mol")
    
def atom_L():
  r1 = input("enter the given reactant symbol: ")
  r1a = input("enter the amount of atoms of the given reactant (use \"^\" for exponents): ")
  r1a = r1a.replace("^","**")
  r1a = eval(r1a)
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (float(r1a)/avogadro)*(r2c/r1c)*(22.4)
  print(f"there are {answer} Liters of {r2}")
  print("")
  print(f"{r1a}atoms {r1}      {r2c} mol    22.4 L ")
  print(f"--------- x                   ---------- x --------- = {answer} Liters {r2}")
  print(f"{avogadro}atoms       {r1c} mol       1 mol")

def mol_mol():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the moles of the given reactant: "))
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a)*(r2c/r1c)
  print(f"there are {answer} moles of {r2}")
  print("")
  print(f"{r1a}mol {r1}       {r2c} mol {r2}")
  print(f"--------- x    ---------- = {answer} moles {r2}")
  print(f"    1          {r1c} mol {r1}")

def Liter_mol():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in Liters of the given reactant: "))
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a/22.4)*(r2c/r1c)
  print(f"there are {answer} moles of {r2}")
  print("")
  print(f"{r1a}mol {r1}        22.4 L         {r2c} mol {r2}")
  print(f"--------- x    ---------- x ---------- = {answer} moles {r2}")
  print(f"  1              1 mol {r1}       {r1c} mol {r1}")

def Liter_atom():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in Liters of the given reactant: "))
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a/22.4)*(r2c/r1c)*(avogadro)
  print(f"there are {answer} atoms of {r2}")
  print("")
  print(f"{r1a} L {r1}        1 mol {r1}        {r2c} mol {r2}   {avogadro} atoms {r2} ")
  print(f"--------- x    ---------- x ---------- x ----------- = {answer} atoms {r2}")
  print(f"  1              22.4 L       {r1c} mol {r1}     1 mol {r2}")
  
def Liter_Liter():
  r1 = input("enter the given reactant symbol: ")
  r1a = float(input("enter the amount in Liters of the given reactant: "))
  r1c = int(input("enter the coefficient in front of the given reactant: "))
  r2 = input("enter the symbol of the desired product: ")
  r2c = int(input("enter the coefficient in front of the desired product: "))
  answer = (r1a/22.4)*(r2c/r1c)*(22.4)
  print("")
  print(f"there are {answer} Liters of {r2}")
  print("")
  print(f"{r1a} L {r1}       1 mol {r1}     {r2c} mol {r2}")
  print(f"--------- x    ---------- x -----------    = {answer} Liters {r2}")
  print(f"    1          22.4 L     {r1c} mol {r1}")

#initialzed the user input variables
initial = ""
final = ""
while True:
  
  initial = input("enter what units you START with(grams(g),moles(m),Liters(L),atoms(a)):")
  final = input("enter what units you need at the END (grams(g),moles(m),Liters(L),atoms(a)): ") 
  
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
  else:
    print("make sure you choose from the available options(g,a,L,m)")
    print("")
    continue
    
