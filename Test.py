
#Extract in seperate packages 
    
import random

class LatticeNode:
    def __init__(self, provided_val):
        self.__val = provided_val
        self.__can_connect_to = [] #can connect to these lattices
        self.__connected_to = [] #connected to them

    def get_val(self):
        return self.__val

    def add_node_it_can_connect_to(self, node):
        self.__can_connect_to.append(node)

    def connect(self, node):
        self.__connected_to.append(node)
        node.__connected_to.append(self)

        self.__can_connect_to.remove(node) #can't connect to this anymore
        node.__can_connect_to.remove(self)

    # def disconnect(self, node):
    #     self.__can_connect_to.remove(node)

    def get_random_node_to_connect_to(self):
        if len(self.__can_connect_to) > 0:
            return random.choice(self.__can_connect_to)

    def is_connected_to(self, node):
        return node in self.__connected_to
    

class Lattice:
    def __init__(self, input_lattice_size):
        self.__no_of_nodes = input_lattice_size**input_lattice_size
        self.__side_len_end = input_lattice_size #pos no  
        self.__side_len_start_index = 0 #index
        self.__lattice_matrix = self.__create_lattice_matrix()

    def get_no_of_nodes(self):
        return self.__no_of_nodes   

    def get_random_path(self, starting_node_val, ending_node_val):
        starting_node = self.get_node_with_value(starting_node_val)
        ending_node = self.get_node_with_value(ending_node_val)

        return self.__get_random_path(starting_node, ending_node, [starting_node], [])
    
    def get_node_with_value(self, provided_val):
        for row in self.__lattice_matrix:
            for node in row:
                if node.get_val() == provided_val: return node

    def __get_random_path(self, node_current, node_destination, current_path, random_path):
        if len(random_path) == 0: #didn't find the path yet so it's empty
            if node_current == node_destination:
                for node in current_path: random_path.append(node) #updating if found
                return random_path
            
            random_next_node = node_current.get_random_node_to_connect_to()

            while random_next_node != None:
                if not node_current.is_connected_to(random_next_node): #proceeding iff not connected
                    node_current.connect(random_next_node)
                    current_path.append(random_next_node)
                    self.__get_random_path(random_next_node, node_destination, current_path, random_path)
                    current_path.pop()
                random_next_node = node_current.get_random_node_to_connect_to()

        return random_path

    def __create_lattice_matrix(self):
        lattice_matrix = []
        self.__initialize(lattice_matrix)
        self.__connect_nodes(lattice_matrix)
        return lattice_matrix
    
    def __initialize(self,lattice_matrix):
        lattice_node_val = 1
        for row_no in range(self.__side_len_end):
            row = []
            for col_no in range(self.__side_len_end):
                row.append(LatticeNode(lattice_node_val))
                lattice_node_val += 1
            lattice_matrix.append(row)
        
    def __connect_nodes(self, lattice_matrix):
        for row_no in range(self.__side_len_end):
            for col_no in range(self.__side_len_end):
                if row_no-1 >= self.__side_len_start_index:
                    lattice_matrix[row_no][col_no].add_node_it_can_connect_to(lattice_matrix[row_no - 1][col_no])
                if row_no+1 < self.__side_len_end:
                    lattice_matrix[row_no][col_no].add_node_it_can_connect_to(lattice_matrix[row_no+1][col_no])
                if col_no - 1 >= self.__side_len_start_index:
                    lattice_matrix[row_no][col_no].add_node_it_can_connect_to(lattice_matrix[row_no][col_no - 1])
                if col_no+1 < self.__side_len_end:
                    lattice_matrix[row_no][col_no].add_node_it_can_connect_to(lattice_matrix[row_no][col_no + 1])

#api should be seperate
def api():
    def get_node_val_along_path(path):
        node_val_path = [node.get_val() for node in path] if len(path) > 0 else None
        return node_val_path

    lattice = Lattice(int(input())) #makes a lattice a/c to given size
    starting_node_val = int(input())
    ending_node_val = int(input())
    random_path = lattice.get_random_path(starting_node_val, ending_node_val) #gets random path without repetations
    
    print(get_node_val_along_path(random_path))

if __name__ == "__main__":
    api()




