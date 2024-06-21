inp = "hello:5438,car:214,book:8799,apple:2187"

def leng(x, y):
    xi = len(x)
    while xi not in map(int, str(y)):
        xi -= 1
        if xi < 1:
            return 0  
    return xi

s = ''
for i in inp.split(','):
    x, y = i.split(':')
    if str(len(x)) in str(y):
        s += x[len(x) - 1]
    else:
        length = leng(x, y)
        if length < 1:
            s += 'x'
        
        else:
            s += x[length - 1]

print(s)



'''def string_to_dict(inp):
    # Split the input string by commas to get key-value pairs
    pairs = inp.split(',')
    
    result_dict = {key: int(value) for key, value in (pair.split(':') for pair in pairs)}
    
    return result_dict'''


