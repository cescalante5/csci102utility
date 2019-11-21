# Carlos Escalante
# CSCI 102 - Section C
# Week 12 - Part A

def PrintOutput(string):
    print('OUTPUT %s' % (string))

def LoadFile(file):
    with open(file, 'r+') as x:
        y = x.readlines()
    return y

def UpdateString(x, y, num):
    l = []
    for w in x:
        l.append(w)
    l[3] = y
    out = ''
    for j in l:
        out += w
    print('OUTPUT %s' % out)

def FindWordCount(l, s):
    count = 0
    for x in l:
        t = 0
        f = 0
        count -= 1
        while f != -1:
            f = x.find(s, t)
            t = x.find(s, t) + 1
            count += 1
    return count

def ScoreFinder(list1, list2, s):
    index = -1
    name = -1
    for x in list1:
        index += 1
        if x.lower() == s.lower():
            name = index
    if name != -1:
        print('OUTPUT %s got a score of %d' % (list1[name], list2[name]))
    else:
        print('OUTPUT player not found')            

def Union(list1, list2):
    for x in list1:
        index = -1
        for y in list2:
            index += 1
            if x == y:
                list2.remove(list2[index])
    out = list1 + list2
    return out

def Intersection(list1, list2):
    out = []
    for k in list1:
        for p in list2:
            if k == p:
                out.append(k)
    return out
