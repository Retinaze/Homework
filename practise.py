number = "56577"
result = 0 

## цей кусок функції перебирає кожен символ в стрічці number
for item in number:
    for i in range(10):
        if str(i) == item:
            result *= 10
            result += i
            

print(result)
print(type(result))