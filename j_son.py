'''
    JSON support data types:
    string
    number
    boolean
    null
    object
    array

'''

import json
d={
    'course_name': 'python',
    'fees': 15000
}
f=json.dumps(d)
print(type(f))

print(f)

