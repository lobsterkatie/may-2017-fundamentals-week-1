animals = ["aardvark", "bear", "cow", "deer", "elephant", "frog", "gorilla",
           "hamster", "ibex", "jaguar", "kangaroo", "llama", "mongoose"]

#random comment for me to take out next time!!

#for loop version
capital_four_letter_animals = []

for animal in animals:
	if len(animal) == 4:
		capital_animal = animal.title()
		capital_four_letter_animals.append(capital_animal)

print "for-loop version:", capital_four_letter_animals

#list comprehesion version