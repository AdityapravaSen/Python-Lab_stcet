from python_package import fish, mamals, birds, amphibians, reptiles

i = int(input("Enter 1 for fish 2 for mammals 3 for birds 4 for amphibians and 5 for reptiles"))

if(i == 1):
    fish.fishchar()
    fish.fishex()
if(i == 2):
    mamals.mchar()
    mamals.mex()
if(i == 3):
    birds.bchar()
    birds.bex()

if(i == 4):
    amphibians.achar()
    amphibians.aex()

if(i == 5):
    reptiles.rchar()
    reptiles.rex()
