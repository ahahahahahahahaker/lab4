import csv
# вариант 2 с доп заданием
bag = []
place = 9  # для решения доп задания надо поменять на '7'
points = 10
totalpt = 205
diff = totalpt - points
place -= 1
diff -= 5  # очки за ингалятор
inf = []
with open('innf//inf.csv', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    i = 0
    next(reader)
    for row in reader:
        inf.append(row)
        inf[i][1] = inf[i][1][0]
        inf[i][0] = inf[i][0][0]
        if inf[i][0] == 'и':
            ingalate = i
        i += 1
inf.remove(inf[ingalate])
i -= 1
for j in range(i):
    for k in range(j + 1, i):
        for l in range(k + 1, i):
            pt1, pt2, pt3 = map(int, [inf[j][2], inf[k][2], inf[l][2]])
            pl1, pl2, pl3 = map(int, [inf[j][1], inf[k][1], inf[l][1]])
            letter1, letter2, letter3 = inf[j][0], inf[k][0], inf[l][0]
            if pl1 + pl2 + pl3 <= place:
                survival_points = 2 * (pt1 + pt2 + pt3)
                if survival_points > diff:
                    bag.append(['и'])
                    print('Очков выживания:', survival_points - diff)
                    items = [pl1 * letter1, pl2 * letter2, pl3 * letter3]
                    for g in range(len(items)):
                        bag.append([items[g]])
                    for q in range(0, 9, 3):
                        print(bag[q], bag[q + 1], bag[q + 2])
                    bag = [['и']]
                else:
                    for n in range(l + 1, i):
                        pt4, pl4 = map(int, [inf[n][2], inf[n][1]])
                        letter4 = inf[n][0]
                        if pl1 + pl2 + pl3 + pl4 <= place:
                            survival_points = 2 * (pt1 + pt2 + pt3 + pt4)
                            if survival_points > diff:
                                bag.append(['и'])
                                print('Очков выживания:', survival_points - diff)
                                items = [pl1 * letter1, pl2 * letter2, pl3 * letter3, pl4 * letter4]
                                for g in range(len(items)):
                                    bag.append([items[g]])
                                for q in range(0, 9, 3):
                                    print(bag[q], bag[q + 1], bag[q + 2])
                                bag = [['и']]
                            else:
                                for m in range(n+1, i):
                                    pt5, pl5 = map(int, [inf[m][2], inf[m][1]])
                                    letter5 = inf[m][0]
                                    if pl1 + pl2 + pl3 + pl4 + pl5 <= place:
                                        survival_points = 2 * (pt1 + pt2 + pt3 + pt4 + pt5)
                                        if survival_points > diff:
                                            bag.append(['и'])
                                            print('Очков выживания:', survival_points - diff)
                                            items = pl1*letter1+pl2*letter2+pl3*letter3+pl4*letter4+pl5*letter5
                                            for g in range(len(items)):
                                                bag.append([items[g]])
                                            print(bag[0], bag[1], bag[2])
                                            print(bag[3], bag[4], bag[5])
                                            print(bag[6], bag[7], bag[8])
                                            bag = [['и']]
                                        else:
                                            for v in range(m + 1, i):
                                                pt6, pl6 = map(int, [inf[v][2], inf[v][1]])
                                                letter6 = inf[v][0]
                                                if pl1 + pl2 + pl3 + pl4 + pl5 + pt6 <= place:
                                                    survival_points = 2 * (pt1 + pt2 + pt3 + pt4 + pt5)
                                                    if survival_points > diff:
                                                        bag.append(['и'])
                                                        print('Очков выживания:', survival_points - diff)
                                                        items = (pl1*letter1 + pl2*letter2 + pl3*letter3 + pl4*letter4
                                                                 + pl5*letter5 + pl6*letter6)
                                                        for g in range(len(items)):
                                                            bag.append([items[g]])
                                                        for q in range(0, 9, 3):
                                                            print(bag[q], bag[q + 1], bag[q + 2])
                                                        bag = [['и']]
if bag == []:
    print('Нет решений :(')
