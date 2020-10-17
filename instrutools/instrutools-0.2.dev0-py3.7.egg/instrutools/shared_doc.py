
process_return = """res : a dictionary containing keywords:
         "status": (int) 0 if no error append >0 if errors
         "cmd" : (str) the command applied 
         "rtime": (float) os time when execution started
         "time" : (float) os time when execution finished
     
     if status ==0 (no error)
         "return" : any type it will depend on the command applied
     
     if status >0 the additional keyword must be present:
         "rtype": short string representing the error type
         "message": the error message description
"""

def redoc(f):
    f.__doc__ = f.__doc__.format(
       **globals()    
    )
    return f
    
    