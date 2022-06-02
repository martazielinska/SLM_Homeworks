import matplotlib.pyplot as plt

two_standard = {}
for i in [1, 2, 3, 4, 5, 6]:
    for j in [1, 2, 3, 4, 5, 6]:
        s = i + j
        if s in two_standard:
            two_standard[s] += 1
        else:
            two_standard[s] = 1

print(two_standard)

#plt.scatter(two_standard.keys(), two_standard.values())
#plt.show()
all_dice = []
for x1 in range(2,12):
    for x2 in range(x1, 12):
        for x3 in range(x2, 12):
            for x4 in range(x3, 12):
                for x5 in range(x4, 12):
                    new_list=[1,x1,x2,x3,x4,x5]
                    all_dice.append(new_list)
print(all_dice)

for d1 in all_dice:
    for d2 in all_dice:
        test = {}
        #print(d1)
        for i in d1:
            for j in d2:
                #print(i)
                s = i + j
                if s in test:
                    test[s] += 1
                else:
                    test[s] = 1
            if test == two_standard:
                print(d1, " ", d2)