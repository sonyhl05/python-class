mydict={
"name": "sony",
"id": 111,
"domain": ["devops", "cloud engineer", "SRE"],
"tool": { "os": ["linux", "windows"], "cloud": "AWS"}
}
print(mydict)
print(mydict["id"])
print(mydict["name"])
print(mydict["domain"])
print(mydict["domain"][1])
print(mydict["tool"])
print(mydict["tool"]["os"])
print(mydict["tool"]["os"][0])

mydict["place"]=["Bangalore", "poone"]
print(mydict)
mydict1={
"name1": "teja"
}

mydict.update(mydict1)
print(mydict)
