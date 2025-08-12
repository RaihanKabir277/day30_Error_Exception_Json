
height = float(input("Height(M) : "))
weight = int(input("Weight(Kg) : "))

# bmi = weight / height ** 2
# print(bmi)

#even if we give the unreal height and weight it will work

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)


