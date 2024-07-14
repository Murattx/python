# Step 1: Create a personel dictionary
personnel = {
    "Michael": { "age": 20, 
                 "children": [] },

    "Linda": {"age": 30, 
              "children": []}
}

# Step 2: Update the child informations
personnel["Michael"]["children"] = [
    {"name": "Karen", "age": 12, "gender": "female"},
    {"name": "Greg", "age": 7, "gender": "male"}
]

personnel["Linda"]["children"] = [
    {"name": "Susan", "age": 6, "gender": "female"}
]

# Step 3: Print michale childer names

print(personnel["Michael"]["children"][0]["name"], "and", personnel["Michael"]["children"][1]["name"])

