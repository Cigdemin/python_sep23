animal_list = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'hippopotamus', 'monkey', 'crocodile', 'bear', 'panda', 'penguin', 'kangaroo', 'lion', 'gazelle', 'parrot', 'toucan', 'giraffe', 'elephant', 'kangaroo', 'monkey']
output_dict = {}

for animal in animal_list:
    count_num = animal_list.count(animal)
    output_dict[animal]=[count_num]
print(output_dict)