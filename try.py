x = "word"

def func(x):
    try:
     
        return "hello " + x
    except Exception as e:
        
        return "An error occurred:", e

try:
    result = func(x) 
    print(result) 
except Exception as e:
    print("An unexpected error occurred:",e)
