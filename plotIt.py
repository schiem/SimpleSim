import matplotlib.pyplot as plt

def parse_data(file_name):
    f = open(file_name, "r")
    obj_dict = {"objects" : [], "plants" : [], "animals" : []}
    objects = []
    plants = []
    animals = []
    for line in file:
        if line[0] == "C":
            obj_dict["objects"].append(objects)
            obj_dict["plants"].append(plants)
            obj_dict["animals"].append(animals)
            objects = []
            plants = []
            animals = []
        if line[0] == "O":
            objects.append(int(line.split(" ")[-1]))
        elif line[0] == "P":
            plants.append(int(line.split(" ")[-1]))
        elif line[0] == "A":
            animals.append(int(line.split(" ")[-1]))
    return obj_dict

def plot_data(data_dict, instance):
    pass 

