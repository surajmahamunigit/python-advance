import json

def dump_load(employees):
    """
    Serialize and Deserialize the file
    """

    # Serialization using JSON
    with open("employees.json","w") as file:
        json.dump(employees,file)
        print("Serializing successful: employees.json")
        file.close()

    # Deserialization using JSON
    with open("employees.json","r") as file:
        dat= json.load(file)
        print("Deserializing successful: employees.json")


#
employees=[{"name":"raj","rank":"manager","age":23},
           {"name": "vishal","rank": "senior","age":25},
           {"name": "rahi","rank": "junior","age":18}
]

dump_load(employees)