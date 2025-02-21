def function(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        return "Error: Incompatible data types"

result = function(10, 20)
print(result)
result = function(10, '20')
print(result)
result = function('10','20')
print(result)