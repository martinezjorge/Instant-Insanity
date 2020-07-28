import math as math
from itertools import combinations


def cubes_generator(colors):
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


def solve_stack(cubes, visited, solution_num):
    i = 7
    multiplicity = [0 for i in range(30)]
    half_sol_flag = False
    half_sol_counter = 0
    while -1 < i < len(cubes):
        moving_forward = True
        next_half_solution = False
        for j in range(3):

            # this stops the dfs at the third thread
            if i == 0 and solution_num == 1 and j == 2:
                half_sol_flag = False
                moving_forward = False
                break

            if half_sol_flag == False and i == (len(cubes) - 1) and visited[i][j] == solution_num:
                if j < 2:
                    visited[i][j] = 0
                    multiplicity[cubes[i][j][0] - 1] -= 1
                    multiplicity[cubes[i][j][1] - 1] -= 1
                    j += 1
                else:
                    visited[i][j] = 0
                    multiplicity[cubes[i][j][0] - 1] -= 1
                    multiplicity[cubes[i][j][1] - 1] -= 1
                    next_half_solution = True

            if next_half_solution:
                break

            if visited[i][j] == 0 and multiplicity[cubes[i][j][0] - 1] + 1 < 3 and multiplicity[
                cubes[i][j][1] - 1] + 1 < 3:
                visited[i][j] = solution_num
                multiplicity[cubes[i][j][0] - 1] += 1
                multiplicity[cubes[i][j][1] - 1] += 1
                moving_forward = False
                i += 1
                break

        if moving_forward:
            i = i - 1
            done_backtracking = False
            while not done_backtracking and i >= 0:
                for k in range(3):
                    if visited[i][k] == solution_num:
                        visited[i][k] = 0
                        multiplicity[cubes[i][k][0] - 1] -= 1
                        multiplicity[cubes[i][k][1] - 1] -= 1
                        k = k + 1
                        while k < 3:
                            if visited[i][k] == 0 and (multiplicity[cubes[i][k][0] - 1] + 1) < 3 and (
                                    multiplicity[cubes[i][k][1] - 1] + 1) < 3:
                                visited[i][k] = solution_num
                                multiplicity[cubes[i][k][0] - 1] += 1
                                multiplicity[cubes[i][k][1] - 1] += 1
                                done_backtracking = True
                                i += 1
                                break
                            k = k + 1
                        break
                if not done_backtracking:
                    i = i - 1
        if i == len(cubes):
            half_sol_flag = True

        if i == len(cubes) and solution_num != 2:
            half_sol_counter += 1
            # print("First Half Solution")
            # for t in range(len(visited)):
            # print(visited[t])
            half_sol_flag = solve_stack(cubes, visited, 2)

            if not half_sol_flag:
                i -= 1

        if i == len(cubes) and solution_num == 2:
            for t in visited:
                print(t)

    if i == -1:
        half_sol_flag = False
        # print("Number of half solutions: ", half_sol_counter)
        # print("No Solution")

    # if half_sol_flag and solution_num == 1:
    # print("NUmber of half solutions: ", half_sol_counter)
    # print("Complete Solution")
    # for t in range(len(visited)):
    #    print(visited[t])

    # if half_sol_flag == False and solution_num == 1 and i == -1:
    # print("No Solution")
    # if half_sol_flag == True and solution_num == 2:
    # print("Solution Found")

    # have to think about exactly what data i want from the puzzles and
    # write out every half solution to a file
    # write out every solution to a file
    # write whether the stack had a solution, true or false
    return half_sol_flag


def find_min_obs(cubes):
    min_obs = len(cubes) + 1
    i = len(cubes)

    while i > 0:
        solution = False
        subsets = combinations(cubes, i)

        for subset in subsets:
            visited = [[0, 0, 0] for i in range(len(subset))]
            solution = solve_stack(subset, visited, 1)
            if not solution:
                print("A 'No Solution' was found in a stack of ", i, " cubes!")
                print("Minimum obstacle is now: ", min_obs - 1)
                min_obs -= 1
                for element in subset:
                    print(element)
                break
            else:
                print("A Solution Was Found")

        if solution:
            print("Every subset of ", i, " cubes had a solution")
            print("Minimum Obstacle: ", min_obs)
            if min_obs > len(cubes):
                print("No Minimal Obstacle")
            break
        i -= 1


# Puzzle 1
color1 = [1 + math.floor(n * math.pi) % 30 for n in range(1, 181)]
# Puzzle 2
color2 = [(1 + math.floor(i * math.e % 30)) for i in range(1, 181)]
# Puzzle 3
color3 = [(1 + math.floor(i * math.sqrt(3)) % 30) for i in range(1, 181)]
# Puzzle 4
color4 = [(1 + math.floor(i * math.sqrt(5)) % 30) for i in range(1, 181)]

# cubes = cubes_generator(color2)

cubes = [
    [[11, 13], [9, 19]],
    [[15, 26], [25, 30]],
    [[2, 15], [25, 30]],
    [[11, 23], [5, 10]],
    [[5, 27], [6, 24]],
    [[12, 15], [4, 10]],
    [[21, 28], [3, 21]],
    [[2, 7], [10, 12], [20, 29]],
    [[4, 13], [8, 19], [19, 24]],
    [[11, 19], [7, 24], [12, 25]],
    [[7, 14], [8, 20], [7, 30]],
    [[17, 23], [14, 22], [9, 24]],
    [[12, 22], [5, 21], [17, 30]],
    [[23, 24], [1, 3], [23, 27]],
    [[3, 8], [28, 30], [29, 30]],
    [[9, 18], [23, 14], [5, 8]],
    [[1, 14], [4, 29], [15, 28]],
    [[14, 16], [16, 18], [17, 28]],
    [[25, 29], [24, 27], [27, 28]],
    [[18, 30], [2, 13], [6, 22]],
    [[4, 22], [6, 26], [3, 6]],
    [[5, 9], [7, 17], [8, 16]],
    [[11, 12], [26, 29], [6, 11]],
    [[9, 22], [2, 20], [15, 25]],
    [[22, 23], [21, 26], [3, 25]],
    [[15, 27], [1, 16], [2, 21]],
    [[4, 20], [13, 20], [21, 25]],
    [[8, 12], [6, 7], [3, 13]],
    [[11, 27], [16, 26], [1, 10]],
    [[17, 17], [2, 20], [18, 18]]
]

visited = [[1, 0, 2],
           [0, 2, 1],
           [0, 1, 2],
           [2, 1, 0],
           [2, 0, 1],
           [1, 2, 0],
           [0, 2, 1],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]
           ]

solve_stack(cubes, visited, 1)
