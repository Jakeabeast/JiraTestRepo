def process(*parameter):
    if len(parameter) > 2:
        print(parameter)
        return True
    else:
        print("not enough to process")
        return False #corrected mistake for successful merge

def results():
    print("working")