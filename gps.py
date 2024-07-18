"""Create routes between cities on a map."""
import sys
import argparse

# Your implementation of City, Map, bfs, and main go here.


class City():
    ''' The City class holds information representing a city (such as the names and neighbors
    as well as the distance between cities and the interstates that connect them)'''
    def __init__(self, name):
        ''' create an instance of the City class'''
        self.name = name
        self.neighbors = {}
    
    def __repr__(self):
        ''' return the attribute of the instance '''
        return self.name
    
    def add_neighbor(self, neighbor, distance, interstate):
        ''' '''
        if neighbor.name not in self.neighbors:
            self.neighbors[neighbor] = (distance, interstate)
        if self.name not in neighbor.neighbors:
            neighbor.neighbors[self.name] = (distance, interstate)
              
class Map():
    ''' the Map class stores information as a form of Graph and relationships between cities'''
    def __init__(self, relationships):
        ''' create an instance of the Map class and it relationship to the cities surrounding it '''
        self.cities = []

        for key in relationships:
            city = None
            for cit in self.cities:
                if cit.name == key:
                    city = cit

            if not city:
                city = City(key)
                self.cities.append(city)

            for neighbor_city, distance, interstate in relationships[key]:
                neighbor = None
                for cit in self.cities:
                    if cit.name == neighbor_city:
                        neighbor = cit

                if not neighbor:
                    neighbor = City(neighbor_city)
                    self.cities.append(neighbor)

                city.add_neighbor(neighbor, distance, interstate)
                                   
    def __repr__(self):
        ''' return the cities attribute '''
        return str(self.cities)
    
def bfs(graph, start, goal):
    explored = []
    queue = [[start]]
    
    if start == goal:
        return [start]
    
    while queue: 
        path = queue.pop(0)
        last_node = path[-1]

        if last_node not in explored:
            id = [city.name for city in graph.cities]
            neighbors = graph.cities[id.index(str(last_node))].neighbors
            
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            if str(neighbor) == goal:
                return [str(city) for city in new_path]
                
        explored.append(last_node)
        
    print(f"No path found from {start} to {goal}")
    
    return None


def main(start, destination, graph):
    ''' create a map object and find a path between two cities as well as tell someone how far they must drive '''
    new_map = Map(graph)
    instructions = bfs(new_map, start, destination)
    
    emp_string = ""
    
    if not instructions:
        return "No path found"
    
    for i, city in enumerate(instructions):
        if i == 0:
            print(f"Starting city {start}")
            emp_string += (f"Starting city {start}")
            
        if i < len(instructions) - 1:
            next_city = instructions [i + 1]
            id = [city.name for city in map.cities].index(city)
            dict = map.cities[id].neighbors
            
            neighbor = ()
            for key, value in dict.items():
                new_key = str(key)
                neighbor[new_key] = value
                distance, interstate = neighbor[next_city]
                
            print(f"Drive {distance} miles on {interstate} towards {next_city} then")
            emp_string += (f"Drive {distance} miles on {interstate} towards {next_city} then")
            
        if i == len(instructions) - 1:
            print(f"You will arrive at your destination")
            emp_string += (f"You will arrive at your destination")
            
    return emp_string


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--starting_city', type = str, help = 'The starting city in a route.')
    parser.add_argument('--destination_city', type = str, help = 'The destination city in a route.')
    
    args = parser.parse_args(args_list)
    
    return args

if __name__ == "__main__":
    
    connections = {  
        "Baltimore": [("Washington", 39, "95"), ("Philadelphia", 106, "95")],
        "Washington": [("Baltimore", 39, "95"), ("Fredericksburg", 53, "95"), ("Bedford", 137, "70")], 
        "Fredericksburg": [("Washington", 53, "95"), ("Richmond", 60, "95")],
        "Richmond": [("Charlottesville", 71, "64"), ("Williamsburg", 51, "64"), ("Durham", 151, "85")],
        "Durham": [("Richmond", 151, "85"), ("Raleigh", 29, "40"), ("Greensboro", 54, "40")],
        "Raleigh": [("Durham", 29, "40"), ("Wilmington", 129, "40"), ("Richmond", 171, "95")],
        "Greensboro": [("Charlotte", 92, "85"), ("Durham", 54, "40"), ("Ashville", 173, "40")],
        "Ashville": [("Greensboro", 173, "40"), ("Charlotte", 130, "40"), ("Knoxville", 116, "40"), ("Atlanta", 208, "85")],
        "Charlotte": [("Atlanta", 245, "85"), ("Ashville", 130, "40"), ("Greensboro", 92, "85")],
        "Jacksonville": [("Atlanta", 346, "75"), ("Tallahassee", 164, "10"), ("Daytona Beach", 86, "95")],
        "Daytona Beach": [("Orlando", 56, "4"), ("Miami", 95, "268")],
        "Orlando": [("Tampa", 94, "4"), ("Daytona Beach", 56, "4")],
        "Tampa": [("Miami", 281, "75"), ("Orlando", 94, "4"), ("Atlanta", 456, "75"), ("Tallahassee", 243, "98")],
        "Atlanta": [("Charlotte", 245, "85"), ("Ashville", 208, "85"), ("Chattanooga", 118, "75"), ("Macon", 83, "75"), ("Tampa", 456, "75"), ("Jacksonville", 346, "75"), ("Tallahassee", 273, "27") ],
        "Chattanooga": [("Atlanta", 118, "75"), ("Knoxville", 112, "75"), ("Nashville", 134, "24"), ("Birmingham", 148, "59")],
        "Knoxville": [("Chattanooga", 112,"75"), ("Lexington", 172, "75"), ("Nashville", 180, "40"), ("Ashville", 116, "40")],
        "Nashville": [("Knoxville", 180, "40"), ("Chattanooga", 134, "24"), ("Birmingam", 191, "65"), ("Memphis", 212, "40"), ("Louisville", 176, "65")],
        "Louisville": [("Nashville", 176, "65"), ("Cincinnati", 100, "71"), ("Indianapolis", 114, "65"), ("St. Louis", 260, "64"), ("Lexington", 78, "64") ],
        "Cincinnati": [("Louisville", 100, "71"), ("Indianapolis,", 112, "74"), ("Columbus", 107, "71"), ("Lexington", 83, "75"), ("Detroit", 263, "75")],
        "Columbus": [("Cincinnati", 107, "71"), ("Indianapolis", 176, "70"), ("Cleveland", 143, "71"), ("Pittsburgh", 185, "70")],
        "Detroit": [("Cincinnati", 263, "75"), ("Chicago", 283, "94"), ("Mississauga", 218, "401")],
        "Cleveland":[("Chicago", 344, "80"), ("Columbus", 143, "71"), ("Youngstown", 75, "80"), ("Buffalo", 194, "90")],
        "Youngstown":[("Pittsburgh", 67, "76")],
        "Indianapolis": [("Columbus", 175, "70"), ("Cincinnati", 112, "74"), ("St. Louis", 242, "70"), ("Chicago", 183, "65"), ("Louisville", 114, "65"), ("Mississauga", 498, "401")],
        "Pittsburg": [("Columbus", 185, "70"), ("Youngstown", 67, "76"), ("Philadelphia", 304, "76"), ("New York", 391, "76"), ("Bedford", 107, "76")],
        "Bedford": [("Pittsburg", 107, "76")], #COMEBACK
        "Chicago": [("Indianapolis", 182, "65"), ("St. Louis", 297, "55"), ("Milwaukee", 92, "94"), ("Detroit", 282, "94"), ("Cleveland", 344, "90")],
        "New York": [("Philadelphia", 95, "95"), ("Albany", 156, "87"), ("Scranton", 121, "80"), ("Providence,", 95, "181"), ("Pittsburgh", 389, "76")],
        "Scranton": [("Syracuse", 130, "81")],
        "Philadelphia": [("Washington", 139, "95"), ("Pittsburgh", 305, "76"), ("Baltimore", 101, "95"), ("New York", 95, "95")]
    }
    
    args = parse_args(sys.argv[1:])
    main(args.starting_city, args.destination_city, connections)
    
        