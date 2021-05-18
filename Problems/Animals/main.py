file = open("animals.txt", "r", encoding="utf-8")
animals = file.readlines()

new_file = open("animals_new.txt", "w", encoding="utf-8")

new_animals = ""
for animal in animals:
    new_animals += animal.replace("\n", "") + " "
new_animals = new_animals[:-1]  # remove last whitespace

new_file.write(new_animals)

file.close()
new_file.close()
