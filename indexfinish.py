
import sys
import pygame
from ultis import *
from dfs import dfs
from bfs import bfs
from astar import AStarSearch

import time


def draw_map(screen, node: Node, state: State, resolution_width, resolution_height):
    map = state.getMap(node)

    startX = 100
    startY = 200
    x, y = 100, 200
    i1 = 1
    b_w = 160
    color = WHITE

    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i == node.data[1] and j == node.data[0]) or (i == node.data[3] and j == node.data[2]):
                b_w /= 2

    if not ((node.data[0] < node.data[2]) or ((node.data[0] == node.data[2]) and node.data[1] > node.data[3])):
        temp_data = (node.data[2], node.data[3], node.data[0], node.data[1])
        node.data = temp_data

    for i in range(len(map)):
        for j in range(len(map[i])):
            color = (199, 208, 207)
            if map[i][j] == 1:
                color = (199, 208, 207)
                w, h = 40, 30
                ang = 15
                pygame.draw.polygon(screen, color, [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)], 1)
                pygame.draw.line(screen, (45, 56, 65),
                                 (x+ang+w, y-10+h), (x+ang+w, y+h))
                pygame.draw.line(screen, (45, 56, 65),
                                 (x+ang, y+h), (x+ang, y+h+10))
                pygame.draw.polygon(screen, (45, 56, 65), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)], 1)
            if map[i][j] == 4:
                color = YELLOW
                w, h = 40, 30
                ang = 15
                pygame.draw.polygon(screen, color, [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)], 1)
                pygame.draw.line(screen, (45, 56, 65),
                                 (x+ang+w, y-10+h), (x+ang+w, y+h))
                pygame.draw.line(screen, (45, 56, 65),
                                 (x+ang, y+h), (x+ang, y+h+10))
                pygame.draw.polygon(screen, (45, 56, 65), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)], 1)
            elif map[i][j] == -2:
                color = RED
                w, h = 40, 30
                ang = 15
                pygame.draw.polygon(screen, color, [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)], 1)
                pygame.draw.line(screen, (45, 56, 65),
                                 (x+ang+w, y-10+h), (x+ang+w, y+h))
                pygame.draw.line(screen, (45, 56, 65),
                                 (x+ang, y+h), (x+ang, y+h+10))

                pygame.draw.polygon(screen, (45, 56, 65), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)], 1)
                pygame.draw.line(screen, BLACK, (x-10, y),
                                 (x+ang+w, y-10+h), 3)
                pygame.draw.line(
                    screen, BLACK, (x-10+w, y-10), (x+ang, y+h), 3)
            elif map[i][j] == 2:
                color = RED
                w, h = 40, 30
                ang = 15
                pygame.draw.polygon(screen, color, [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)], 1)
                pygame.draw.line(screen, (45, 56, 65),
                                 (x+ang+w, y-10+h), (x+ang+w, y+h))
                pygame.draw.line(screen, (45, 56, 65),
                                 (x+ang, y+h), (x+ang, y+h+10))
                pygame.draw.polygon(screen, (45, 56, 65), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)], 1)
                pygame.draw.line(screen, WHITE, (x-10, y),
                                 (x+ang+w, y-10+h), 3)
                pygame.draw.line(
                    screen, WHITE, (x-10+w, y-10), (x+ang, y+h), 3)
            elif map[i][j] == 5:
                color = WHITE
                w, h = 40, 30
                ang = 15
                pygame.draw.polygon(screen, color, [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)], 1)
                # pygame.draw.line(display,(45,56,65),(x-10,y),(x-10,y+10))
                pygame.draw.line(screen, (45, 56, 65),
                                 (x+ang+w, y-10+h), (x+ang+w, y+h))
                pygame.draw.line(screen, (45, 56, 65),
                                 (x+ang, y+h), (x+ang, y+h+10))
                pygame.draw.polygon(screen, (45, 56, 65), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)], 1)
            elif map[i][j] == 6:
                color = BLACK
                w, h = 40, 30
                ang = 15
                pygame.draw.polygon(screen, color, [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x-10+w, y-10), (x+ang+w, y-10+h), (x+ang, y+h)], 1)
                pygame.draw.line(screen, (45, 56, 65),
                                 (x+ang+w, y-10+h), (x+ang+w, y+h))
                pygame.draw.line(screen, (45, 56, 65),
                                 (x+ang, y+h), (x+ang, y+h+10))

                pygame.draw.polygon(screen, (45, 56, 65), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h+10), (x+ang+w, y+h)], 1)
            x += 40
            y -= 10
        x = startX+(i1*25)
        y = startY+(i1*30)
        i1 += 1
    startX = 100
    startY = 200
    x, y = 100, 200
    i1 = 1
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i == node.data[3] and j == node.data[2]):
                w, h = 40, 30
                ang = 15

                pygame.draw.polygon(
                    screen, BLUE, [(x-10+w, y-10), (x-10, y), (x-10, y-b_w), (x-10+w, y-10-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10+w, y-10), (x-10, y), (x-10, y-b_w), (x-10+w, y-10-b_w)], 1)

                pygame.draw.polygon(
                    screen, BLUE, [(x-10, y), (x+ang, y+h), (x+ang, y+h-b_w), (x-10, y-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x+ang, y+h), (x+ang, y+h-b_w), (x-10, y-b_w)], 1)

                pygame.draw.polygon(screen, BLUE, [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h-b_w), (x+ang+w, y-10+h-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h-b_w), (x+ang+w, y-10+h-b_w)], 1)

                pygame.draw.polygon(screen, BLUE, [
                                    (x-10, y-b_w), (x-10+w, y-10-b_w), (x+ang+w, y-10+h-b_w), (x+ang, y+h-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y-b_w), (x-10+w, y-10-b_w), (x+ang+w, y-10+h-b_w), (x+ang, y+h-b_w)], 1)

                pygame.draw.line(screen, BLACK, (x-10, y), (x-10, y-b_w))
                pygame.draw.line(screen, BLACK, (x+ang+w, y -
                                 10+h), (x+ang+w, y-10+h-b_w))
                pygame.draw.line(screen, BLACK, (x+ang, y+h), (x+ang, y+h-b_w))

            x += 40
            y -= 10
        x = startX+(i1*25)
        y = startY+(i1*30)
        i1 += 1
    startX = 100
    startY = 200
    x, y = 100, 200
    i1 = 1
    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i == node.data[1] and j == node.data[0]):
                w, h = 40, 30
                ang = 15

                pygame.draw.polygon(
                    screen, BLUE, [(x-10+w, y-10), (x-10, y), (x-10, y-b_w), (x-10+w, y-10-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10+w, y-10), (x-10, y), (x-10, y-b_w), (x-10+w, y-10-b_w)], 1)

                pygame.draw.polygon(
                    screen, BLUE, [(x-10, y), (x+ang, y+h), (x+ang, y+h-b_w), (x-10, y-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y), (x+ang, y+h), (x+ang, y+h-b_w), (x-10, y-b_w)], 1)

                pygame.draw.polygon(screen, BLUE, [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h-b_w), (x+ang+w, y-10+h-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x+ang+w, y-10+h), (x+ang, y+h), (x+ang, y+h-b_w), (x+ang+w, y-10+h-b_w)], 1)

                pygame.draw.polygon(screen, BLUE, [
                                    (x-10, y-b_w), (x-10+w, y-10-b_w), (x+ang+w, y-10+h-b_w), (x+ang, y+h-b_w)])
                pygame.draw.polygon(screen, (0, 0, 0), [
                                    (x-10, y-b_w), (x-10+w, y-10-b_w), (x+ang+w, y-10+h-b_w), (x+ang, y+h-b_w)], 1)

                pygame.draw.line(screen, BLACK, (x-10, y), (x-10, y-b_w))
                pygame.draw.line(screen, BLACK, (x+ang+w, y -
                                 10+h), (x+ang+w, y-10+h-b_w))
                pygame.draw.line(screen, BLACK, (x+ang, y+h), (x+ang, y+h-b_w))
            x += 40
            y -= 10
        x = startX+(i1*25)
        y = startY+(i1*30)
        i1 += 1

def test(levels_array, method_choice):
    i = 0
    for level in levels_array:
        if level is None:
            continue

        path = []
        nNode = 0
        mem = 0

        start = time.time()
        if method_choice == 1:
            path, nNode, mem = dfs(level.state)
                # memory = memory_usage(level.state)
                # print("Memory usage:", memory, "B")
        elif method_choice == 0:
                path, nNode, mem = bfs(level.state)
                # memory = memory_usage(level.state)
                # print("Memory usage:", memory, "B")
        elif method_choice == 2:
                path, nNode, mem = AStarSearch(level.state)
                # memory = memory_usage(level.state)
                # print("Memory usage:", memory, "B")
        end = time.time()

        data = path[len(path) - 1].data

        str_level = str(levels_array.index(level) + 1)
        success = str(level.state.board[data[1]][data[0]]
                          == 4 and level.state.board[data[3]][data[2]] == 4)
        if success == "True":
            i += 1

        print("Level " + str_level + ": " + success + ", path length: ", len(path),
                  ", So node da tim kiem: ", nNode, ", Time: ", round(end - start, 4), "s, Memory Usage: ", mem, "B")
    print("So level success: " + str(i))
    print("Tong so level: " + str(len(levels_array)))
    input("Press enter to exit.")
    return

def memory_usage(state):
    memory = 0
    for node in state.states:
        # Tính kích thước của một đối tượng Node
        size = sys.getsizeof(node)
        # Cộng dồn kích thước vào biến memory
        memory += size
    return memory


def main():
    levels_array = init_levels()
    method_choice = int(
        input("Nhap method: 0:BFS " " 1:DFS " " 2:A* " " : "))
    is_test = int(input("Test hay xem UI?: (Xem UI: 0, Test: 1): "))
    if is_test:
        test(levels_array, method_choice)
        return
    level_choice = int(input("Nhap level: "))
    done = False

    start = time.time()

    if method_choice == 0:
        path, nNode, mem = bfs(levels_array[level_choice - 1].state)
        algorithm = "Breadth-First Search"
    elif method_choice == 1:
        path, nNode, mem = dfs(levels_array[level_choice - 1].state)
        algorithm = "Depth-First Search"
    elif method_choice == 2:
        path, nNode, mem = AStarSearch(levels_array[level_choice - 1].state)
        algorithm = "A* Search"

    end = time.time()

    data = path[len(path) - 1].data

    str_level = str(level_choice)
    success = str(levels_array[level_choice - 1].state.board[data[1]][data[0]]
                    == 4 and levels_array[level_choice - 1].state.board[data[3]][data[2]] == 4)

    print("Level " + str_level + ": " + success + ", path length: ", len(path),
            ", So node da tim kiem: ", nNode, ", Time: ", round(end - start, 4), "s, Memory Usage: ", mem, "B")
        

    pygame.init()
    pygame.display.set_caption("Bloxorz")

    resolution_height = pygame.display.Info().current_h/1.1
    resolution_width = pygame.display.Info().current_w/1.1

    screen = pygame.display.set_mode((resolution_width, resolution_height))
    i = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if i < len(path) - 1:
                        i += 1
                elif event.key == pygame.K_LEFT:
                    if i > 0:
                        i -= 1
        screen.fill(GREEN)
        pygame.font.init()
        my_font = pygame.font.SysFont('Comic Sans MS', 30)

        text_surface = my_font.render(algorithm + " - level " +  str(level_choice), False, (0, 0, 0))
        screen.blit(text_surface, (10, 0))

        text_surface = my_font.render(
            'Solution: ' + str(len(path)) + " steps, Nodes searched: " + str(nNode) + " nodes, Memory Usage: " + str(mem) + " B", False, (0, 0, 0))
        screen.blit(text_surface, (10, resolution_height - 150))

        if i != 0:
            text_surface = my_font.render(
                str(path[i-1].data), False, (128, 128, 128))
            screen.blit(text_surface, (100 , resolution_height - 100))

            text_surface = my_font.render('->', False, (0, 0, 0))
            screen.blit(text_surface, (310, resolution_height - 100))

        text_surface = my_font.render(
            str(path[i].data), False, (255, 255, 255))
        screen.blit(text_surface, (370, resolution_height - 100))

        if i != len(path) - 1:
            text_surface = my_font.render('->', False, (0, 0, 0))
            screen.blit(text_surface, (580, resolution_height - 100))

            text_surface = my_font.render(
                str(path[i+1].data), False, (128, 128, 128))
            screen.blit(text_surface, (640, resolution_height - 100))

        draw_map(screen, path[i], levels_array[level_choice -
                 1].state, resolution_width, resolution_height)
        pygame.display.flip()


main()