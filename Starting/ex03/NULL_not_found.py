def NULL_not_found(object: any) -> int:
    if (type(object) == type(None)):
        print("Nothing: None <class 'NoneType'>");
        return 0
    elif (isinstance(object, float) and object != object):
        print("Cheese: nan <class 'float'>")
        return 0
    elif (isinstance(object, bool) and object == False):
        print("Fake: False <class 'bool'>")
        return 0
    elif (isinstance(object, int) and object == 0):
        print("Zero: 0 <class 'int'>")
        return 0
    elif (isinstance(object, str) and object == ""):
        print("Empty: <class 'str'>")
        return 0
    # elif (isinstance(object, str) and object == "Toto"):
    #     print("Toto is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
        return 1
    # return 42
    # Type not Found$
    # 1$
    #
    # print(type(object))
