class Node:
    def __init__(self):
        self.d = {}
        self.flag = 0

class Tries:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        temp = self.root
        for i in s:
            if i not in temp.d:
                temp.d[i] = Node()
            temp = temp.d[i]
        temp.flag = 1

    def search(self, s):
        temp = self.root
        for i in s:
            if i not in temp.d:
                return False
            temp = temp.d[i]
        return temp.flag == 1

    def prefix(self, s):
        temp = self.root
        for i in s:
            if i not in temp.d:
                return False
            temp = temp.d[i]
        return True

    def all_prefix(self, s):
        def auto(t, s):
            if t.flag == 1:
                print(s)
            for i in t.d:
                auto(t.d[i], s + i)

        t = self.root
        for i in s:
            if i in t.d:
                t = t.d[i]
            else:
                return
        auto(t, s)

    def auto_gen(self, s):
        lst = []
        t = self.root
        for i in s:
            if i in t.d:
                t = t.d[i]
            else:
                return lst
        self.dfs(t, s, lst)
        return lst

    def dfs(self, t, pr, lst):
        if t.flag == 1:
            lst.append(pr)
        for i, val in t.d.items():
            self.dfs(val, pr + i, lst)

    def longest_word_with_prefix(self, l):
        longest_word = ""
        for prefix in l:
            words_with_prefix = self.auto_gen(prefix)
            for word in words_with_prefix:
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word

obj = Tries()
obj.insert("wood")
obj.insert("word")
obj.insert("wrap")
obj.insert("school")
print(obj.search("wood"))
print(obj.prefix("won"))
print(obj.auto_gen("wo")) 
obj.all_prefix('wo') 
print(obj.longest_word_with_prefix(['wo', 'sc']))
'''n=int(input())
for i in range(n):
    a,s=input().split(" ")
    if a=='1':
        obj.insert(s)
    elif a=='2':
        print(obj.search(s))
    elif a=='3':
        print(obj.prefix(s))'''
    
