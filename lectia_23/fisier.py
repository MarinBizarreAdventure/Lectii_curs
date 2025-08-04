import json

# Date Python
persoana = {
    "nume": "Ion Marinescu",
    "varsta": 35,
    "casatorit": True,
    "copii": ["Ana", "Mihai"],
    "adresa": {
        "oras": "Cluj-Napoca",
        "cod_postal": "400000"
    }
}

# Convertim la JSON string
json_string = json.dumps(persoana)
print("JSON string:")
print(json_string)


with open('file.json','w') as f:
    json.dump(persoana,f, indent=4, sort_keys=True,separators=(',',':'))