import math


def map_to_coords(pos):
    pos_x = math.floor(pos / 8)
    pos_y = pos % 8
    return [pos_x, pos_y]


def get_all_valid_moves(init_pos):
    pos_x = init_pos[0]
    pos_y = init_pos[1]
    deltas = [-2, 2, -1, 1]
    board_size_length = 7
    valid_coords_list = []
    for x in deltas:
        for y in deltas:
            if abs(x) != abs(y):
                if 0 <= pos_x + x <= board_size_length and 0 <= pos_y + y <= board_size_length:
                    valid_coords_list.append([pos_x + x, pos_y + y])

    return valid_coords_list


def find_paths(start_pos, end_pos):
    queue = []
    visited = {}
    start_coord = map_to_coords(start_pos)
    end_coord = map_to_coords(end_pos)
    queue.append(start_coord)
    visited[tuple(start_coord)] = None
    while queue:
        current_coordinate = queue.pop(0)
        if current_coordinate == end_coord:
            break
        moves_list = get_all_valid_moves(current_coordinate)
        for move in moves_list:
            if tuple(move) not in visited:
                queue.append(move)
                visited[tuple(move)] = current_coordinate
    # going through the path data we collected
    path = []
    pointer = end_coord
    while visited[tuple(pointer)]:
        path.append(pointer)
        pointer = visited[tuple(pointer)]

    return len(path)


print(find_paths(19, 36))
