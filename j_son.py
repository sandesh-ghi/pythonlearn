# '''
#     JSON support data types:
#     string
#     number
#     boolean
#     null
#     object
#     array
#
# '''

# import json
# d={
#     'course_name': 'python',
#     'fees': 15000
# }
# f=json.dumps(d)
# print(type(f))
#
# print(f)


# '''
#     # Converting JSON Data to python object
#     -> if you have a JSON string , you can parse it by using the json.loads() method
#
#
# '''

# import json
# d='{"cname":"python", "fees":1200, "duration": "2 Months"}'
#
# x=json.loads(d)
# print(type(x))
# print(x)
# for a in x:
    # print(a,x[a])


import json
file = open("posts.json","r")
x = file.read()
finaldata = json.loads(x)
# print(finaldata)

for a in finaldata:
    print(a['country'],a['postalCode'])
