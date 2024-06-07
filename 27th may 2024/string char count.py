def string(s):
    x=[]
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            x.append(s[i - 1] + str(count))
            count = 1
        
    x.append(s[-1] + str(count))

    return ''.join(x)

input_str = "aaabbaaaaddd"
output_str = string(input_str)
print(" ",output_str)

'''def string(s):
    x= []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        x.append(s[i] + str(count))
        i += 1
    return ''.join(x)

input_str = "aaabbaaaaddd"
output_str = string(input_str)
print(" ", output_str)'''
