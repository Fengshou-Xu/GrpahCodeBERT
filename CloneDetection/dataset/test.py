import json

data_by_index = {}
with open("data.jsonl", 'r') as f:
    for line in f:
        json_obj = json.loads(line)
        index = json_obj.get("idx")
        data_by_index[index] = json_obj


line1 = [13988825, 8660836]
line2 = [80378, 18548122]

print("index 13988825: ", data_by_index.get("13988825").get("func"))
print("index 8660836: ", data_by_index.get("8660836").get("func"))

print("-----------------\n")

print("index 80378: ", data_by_index.get("80378").get("func"))
print("index 18548122: ", data_by_index.get("18548122").get("func"))

# with open("data.jsonl", 'r') as f:
#     for line in f:
#         json_obj = json.loads(line)
#         index = json_obj.get("idx")
#         if index == "14377058":
#             print(json_obj.get("func"))
#             print(line)
#             exit(-1)