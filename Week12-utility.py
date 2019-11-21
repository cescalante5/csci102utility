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
