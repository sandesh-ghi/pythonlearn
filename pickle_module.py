'''
    the pickle module implements a fundamental. but powerful algorithm for serialization (store) and deserialization (read)
    a python object structure.

   # Storing data types with pickle:
    Booleans,
    Integers,
    Floats,
    Complex numbers,
    (normal and Unicode) strings,
    Tuples,
    Lists,
    Sets and
    Dictionaries

    # Pickling files
    -> To use pickle, start by importing it in python.
    -> pickle has two main methods. The first one is dump, which dumps an object to a file object and the
                                    second one is load, which load an object from a file object.
    # pickle functions:
    -> dump() - this function is called to serialize and object hierarchy.
                pickling data is done via the dump() function. it accepts data and a file object.
                the dump() function then serializes the data and writes it to the file. the syntax of dump is as follows:
                Syntax: dump(obj,file)

    -> load() - this function is called to deserialize and  data stream.
        the load() function takes a file object, reconstruct the objects from the pickled representation, and returns it.
        syntax of load() is as follows:
        Syntax: load(obj,file)


'''


