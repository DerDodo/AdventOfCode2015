from operator import attrgetter
from typing import List, Dict, Set, Tuple

from util.file_util import read_input_file


class Distance:
    a: str
    b: str
    dist: int

    def __init__(self, line: str):
        parts = line.split(" ")
        self.a = parts[0]
        self.b = parts[2]
        self.dist = int(parts[4])


def parse_input_file() -> Tuple[Dict[str, Dict[str, int]], Set[str]]:
    lines = read_input_file(9, 1)
    distances = list(map(Distance, lines))
    distance_map = {}
    location_set: Set[str] = set()
    for distance in distances:
        if distance.a not in distance_map:
            distance_map[distance.a] = {}
        distance_map[distance.a][distance.b] = distance.dist

        if distance.b not in distance_map:
            distance_map[distance.b] = {}
        distance_map[distance.b][distance.a] = distance.dist

        location_set.add(distance.a)
        location_set.add(distance.b)

    return distance_map, location_set


class Route:
    used_locations: Set[str]
    current_locations: str
    distance: int

    def __init__(self, current_location: str):
        self.used_locations = set()
        self.used_locations.add(current_location)
        self.current_locations = current_location
        self.distance = 0


def get_all_remaining_routes(route: Route, distances: Dict[str, Dict[str, int]], locations: Set[str]) -> List[Route]:
    all_routes: List[Route] = list()
    for new_location in locations:
        if new_location not in route.used_locations:
            new_route = Route(new_location)
            new_route.used_locations.update(route.used_locations)
            new_route.distance = route.distance + distances[route.current_locations][new_location]
            if len(route.used_locations) == len(locations) - 1:
                all_routes.append(new_route)
            else:
                all_routes.extend(get_all_remaining_routes(new_route, distances, locations))
    return all_routes


def find_all_routes(distances: Dict[str, Dict[str, int]], locations: Set[str]) -> List[Route]:
    all_routes: List[Route] = list()
    for location in locations:
        route = Route(location)
        all_routes.extend(get_all_remaining_routes(route, distances, locations))
    return all_routes


def find_shortest_route(distances: Dict[str, Dict[str, int]], locations: Set[str]) -> int:
    all_routes = find_all_routes(distances, locations)
    return min(all_routes, key=attrgetter('distance')).distance


if __name__ == '__main__':
    all_distances, all_locations = parse_input_file()
    routes = find_all_routes(all_distances, all_locations)
    shortest_route = min(routes, key=attrgetter('distance')).distance
    longest_route = max(routes, key=attrgetter('distance')).distance
    print(f"Shortest route: {shortest_route}")
    print(f"Longest route: {longest_route}")
