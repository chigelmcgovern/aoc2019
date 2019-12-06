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
    x, y = 0, 0
    coordinates = set()
    for segment in segments:
        parsed_segment = parse_segment(segment)
        for plumbus in range(parsed_segment['distance']):
            x += direction_map_x[parsed_segment['direction']]
            y += direction_map_y[parsed_segment['direction']]
            coordinates.add((x, y))
    return coordinates


line_one_points, line_two_points = find_all_points(line_1), find_all_points(line_2)
intersections = line_one_points.intersection(line_two_points)

print(min([abs(x_coordinate) + abs(y_coordinate) for (x_coordinate, y_coordinate) in intersections]))
