import json

json_str = '{"nombre":"Oscar","Edad":21,"pais":"Colombia"}'
print(json_str)
print(type(json_str))

python_dict=json.loads(json_str)
print(python_dict)
print(type(python_dict))
print(python_dict['Edad'])
print(python_dict['pais'])


data = {
    "Boxeador":"Keiner",
    "nombre":"keinxz",
    "edad":20,
    "cursos":["jabs", "recto", "cruzado", "upper", "Juego de pies"]
}

json_data = json.dumps(data)
print(json_data)
print(type(json_data))

"""
Python l  JSON
dict ==> Object
list ==> Array
tuple ==> Array
str ==> String
int ==> Number
float ==> Number
True ==> true
False ==> false
None ==> null
"""