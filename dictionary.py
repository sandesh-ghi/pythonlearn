# unorder data type change value / add edit update
# key | value pair
# define with curly brackets {}

d={
    'name':'python',
    'fees':9000,
    'duration': '2 months'
}
# f=d['fees']
# print(f)
for n in d:
    print(d[n])


# for j, k in d.items():
#     print(f"{j}: {k}")      # f->string formate()   # Using old-style formatting (%)
                                                    # print("%s: %s" % (key, value))
                                                    # Using str.format()
                                                    # print("{}: {}".format(key, value))