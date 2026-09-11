""" 
Point           *args                       **kwargs
=====           =====                       ========
Collects        Positional arguments        Keyword arguments
Stored as       Tuple                       Dictionary
Symbol          Single star *               Double star **
Example call    func(10, 20, 30)            func(name="Aman", age=21)

"""
def show_data(*args, **kwargs):
    print(args)
    print(kwargs)
    
show_data(10, 20, name="Aman", age=21)
    
# (10, 20)
# {'name': 'Aman', 'age': 21}

