n=7263
hours=n//60
'''if hours>3600:
    hours=n//60
print(hours)'''
h=n//3600
print(str(h)+"hr")
mini=hours%60
print(str(mini)+"min")
sec=n-hours*60
print(str(sec)+"sec")

