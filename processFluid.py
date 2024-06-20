def process(*parameter):
    if len(parameter) > 2:
        print(parameter)
        return True
    else:
        print("not enough to process")
        return True #this is a mistake and should not be merged

def results():
    print("working")