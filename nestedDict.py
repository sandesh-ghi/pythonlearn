# nested dictionary :-> meand putting a dictionary inside another dictionary.
# collection of dictionaries into one single dictionary.

course={
    'php':{'duration': '2 Months','fees':'13000'},
    'python': {'duration': '2 Months', 'fees': '12000'},
    'java': {'duration': '2 Months' , 'fees': '12000'}
}
# print(course)
# print(course['php']['fees'])


course['java']['fees'] = 14000      #update

for k,v in course.items():
    print(k,v['duration'],v['fees'])
   