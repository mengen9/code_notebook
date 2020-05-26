def plm_modules(licenses, *args):
    print("\n欣达集团licenses:{}".format(licenses))
    for i in args:
        print(i, end=" ")
    print()
def caxa_plm_modules(*args):
    print(type(args))
    for i in args:
        print(i, end=" ")
    print()
def print_modles(unprint_modles, completed_prints):
    while unprint_modles:
        current_modles = unprint_modles.pop()
        print("printing modle : {}".format(current_modles))
        completed_prints.append(current_modles)
def show_completed_modles(comleted_prints):
    print("The follwing models have been printed")
    for i in comleted_prints:
        print(i)