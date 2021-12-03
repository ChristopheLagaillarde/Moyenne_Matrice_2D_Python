try:
    n = int(input("Saisir la taille des matrices"))
    M1 = [[int(input("Matrice 1 :")) for i in range(n)] for j in range(n)]
    M2 = [[int(input("Matrice 2 :")) for i in range(n)] for j in range(n)]
    M3 = [[int(0) for i in range(n)] for j in range(n)]
    moyenne = int(0)

    for i in range(len(M1)):
        for j in range(len(M1)):
            moyenne += (M1[i][j] + M2[i][j])
            M3[i][j] = (M1[i][j] + M2[i][j]) // 2

    print(moyenne/2)
    print(M1)
    print(M2)
    print(M3)

except ValueError:
    print("Saisie non valide")