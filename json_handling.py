import json


'''http://stackabuse.com/reading-and-writing-json-to-a-file-in-python/
'''

print("Json file processing")
json_file =open("E:\\D_DRIVE\\Trainings\\Python\Json_file.json")
data = json.load( json_file) 


print( type(data))

''' 
for i in data["files"]:
#	print("Filetypes " + i["filetype"])
	print ( i.get("filetype"))

	for j in i.get("filetype").get():
		print( j.get("column"))

'''