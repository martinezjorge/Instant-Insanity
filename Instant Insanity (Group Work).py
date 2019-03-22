import math as math

def cubesGenerator(colors):
    cubes = []
    cube = []
    pair = []
    for i in range(180):
        pair.append(colors[i])
        if (i + 1) % 2 == 0:
            cube.append(pair)
            pair = []
        if (i + 1) % 6 == 0:
            cubes.append(cube)
            cube = []
    return cubes

def solve(cubes, solnNum):

    multiplicity = [0 for i in range(30)]

    halfSolFlag = False

    i = 0
    while -1 < i < len(cubes):
        movingForward = True
        flag = False

        for j in range(3):

            if halfSolFlag == False and i == (len(cubes) - 1) and visited[i][j] == solnNum:

                #print("This ran baby")
                if j == 0:

                    visited[i][j] = 0
                    multiplicity[cubes[i][j][0]-1] -= 1
                    multiplicity[cubes[i][j][1]-1] -= 1
                    j += 1

                elif j == 1:
                    visited[i][j] = 0
                    multiplicity[cubes[i][j][0]-1] -= 1
                    multiplicity[cubes[i][j][1]-1] -= 1
                    j += 1

                elif j == 2:
                    visited[i][j] = 0
                    multiplicity[cubes[i][j][0]-1] -= 1
                    multiplicity[cubes[i][j][1]-1] -= 1
                    flag = True

            if flag:
                break

            if visited[i][j] == 0 and multiplicity[cubes[i][j][0] - 1] + 1 < 3 and multiplicity[cubes[i][j][1] - 1] + 1 < 3:
                visited[i][j] = solnNum
                multiplicity[cubes[i][j][0] - 1] += 1
                multiplicity[cubes[i][j][1] - 1] += 1
                #  print(multiplicity[cubes[i][j][0]-1], " " , multiplicity[cubes[i][j][1]-1])

                i += 1

                movingForward = False

                break

        if movingForward == True:

            i = i - 1
            doneBacktracking = False
            while doneBacktracking != True and i >= 0:
                for k in range(3):
                    # locate the last cube face and cube we used
                    # print("f i:", i)
                    # print("f k:", k)
                    if visited[i][k] == solnNum:
                        visited[i][k] = 0
                        multiplicity[cubes[i][k][0] - 1] -= 1
                        multiplicity[cubes[i][k][1] - 1] -= 1

                        k = k + 1
                        while k < 3:
                            # go right until we find a cube face we can use or backtrack again
                            # print("s i:", i)
                            # print("s k:", k)
                            if visited[i][k] == 0 and (multiplicity[cubes[i][k][0] - 1] + 1) < 3 and (multiplicity[cubes[i][k][1] - 1] + 1) < 3:
                                visited[i][k] = solnNum
                                multiplicity[cubes[i][k][0] - 1] += 1
                                multiplicity[cubes[i][k][1] - 1] += 1
                                doneBacktracking = True
                                i += 1
                                break
                            k = k + 1
                        break
                if doneBacktracking != True:
                    i = i - 1

        if i == len(cubes):
            halfSolFlag = True

        if i == len(cubes) and solnNum != 2:
            #print(i)
            #print("First Run Finished")
            for l in range(len(cubes)):
                print(visited[l])
            halfSolFlag = solve(cubes, 2)
            #print("Second Run Finished")
            for l in range(len(cubes)):
                print(visited[l])
            if halfSolFlag == False :
                #print("Second Half Solution Not Found")
                i -= 1

    if i == -1 :
        #print("Finished Empty")
        halfSolFlag = False

    return halfSolFlag


# Puzzle 1
color1 = [1 + math.floor(n * math.pi) % 30 for n in range(1, 181)]
# Puzzle 2
color2 = [(1 + math.floor( i * math.e % 30)) for i in range(1,181)]
# Puzzle 3
color3 = [(1 + math.floor( i * math.sqrt(3) ) % 30) for i in range(1,181)]
# Puzzle 4
color4 = [(1 + math.floor( i * math.sqrt(5)) % 30) for i in range(1,181)]

# Generate Cubes
cubes1 = cubesGenerator(color1)

testCube = cubes1[0:3] + cubes1[3:30]

# Output the cube stack
for i in range(len(testCube)):
    print("Cube", i + 1, testCube[i])

# Generate visited array
visited = [[0, 0, 0] for i in range(len(testCube))]

# might try to create a function that will encapsulate findHalfSolution two times to search for a
# complete solution

# Searching for First Half Solution
#solution = solve(testCube,1)


#if solution:
    #print("Solution Found")
#else:
    #print("No Solution Found")

# Output visited array with half solutions
#for i in range(len(testCube)):
    #print("Cube", i + 1, visited[i])
'''
p = len(cubes1)
minObs = len(cubes1) + 1
while p>0:
    for y in range(p):
        testCube = cubes1[0:y] + cubes1[y:30]
        solution = solve(testCube,1)
        if not solution:
            p -= 1
            minObs -= 1
            break
        elif y == (p-1):
            print("Minimal Obstacle has been found")
            p = 0
print("Minimal obstacle is", minObs)
'''