input_lines = open('day_03_input.txt').read().split('\n')
line_1, line_2 = [x.split(',') for x in input_lines][:2]

direction_map_x = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
direction_map_y = {'U': 1, 'D': -1, 'L': 0, 'R': 0}


def parse_segment(direction):
    return {
        'direction': direction[0],
        'distance': int(direction[1:])
    }


def find_all_points(segments):
    x, y, length = 0, 0, 0
    coordinate_to_length = {}
    coordinates = set()
    for segment in segments:
        parsed_segment = parse_segment(segment)
        for _ in range(parsed_segment['distance']):
            x += direction_map_x[parsed_segment['direction']]
            y += direction_map_y[parsed_segment['direction']]
            length += 1
            coordinates.add((x, y))
            if (x, y) not in coordinate_to_length:
                coordinate_to_length[(x, y)] = length
    return coordinates, coordinate_to_length


def find_minimum_distance(all_intersections):
    distances = []
    for intersection in intersections:
        line_1_distance = line_1_distances[intersection]
        line_2_distance = line_2_distances[intersection]
        distances.append(line_1_distance + line_2_distance)
    print(min(distances))


line_1_coordinates, line_1_distances = find_all_points(line_1)
line_2_coordinates, line_2_distances = find_all_points(line_2)

intersections = line_1_coordinates.intersection(line_2_coordinates)

print(min([abs(x_coordinate) + abs(y_coordinate) for (x_coordinate, y_coordinate) in intersections]))

find_minimum_distance(intersections)
