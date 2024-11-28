def new_func(x):
    spisok = []
    for i in range(1, x):
        for j in range(1, x):
            post_spisok = []
            if x % (i + j) == 0 and i != j:
                post_spisok.append(i)
                post_spisok.append(j)
            else:
                continue
            post_spisok.sort()
            if post_spisok not in spisok:
                spisok.append(post_spisok)
            else:
                continue
    for i in spisok:
        for j in i:
            print(j, end="")


new_func(9)