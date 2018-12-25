if n % 2 == 1:
    flag = False
else:
    flag = True

for i in range(n):
    for j in range(n):
        Rect = (a * j, a * i, (a * (j + 1) - 1), (a * i + a))
        if flag:
            pygame.draw.rect(screen, (255, 255, 255), Rect)
            flag = False
        else:
            flag = True
