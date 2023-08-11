class Graph:
    def __init__(self):
        self.users = {}  # dictionary to represent the users
        self.num_nodes = 0  # a counter to count the number of users
        self.adj_matrix = []  # adj matrix representation

    def add_node(self, node):
        if node not in self.users.values():  # check if the username is already taken
            self.users[self.num_nodes + 1] = node  # adds the user to the dictionary
            self.num_nodes += 1  # increment the counter
            for row in self.adj_matrix:
                row.append(0)  # add a zero to each row
            self.adj_matrix.append(
                [0 for i in range(self.num_nodes)]
            )  # adds a new row of zeroes

    def add_edge(self, node1, node2):
        if (
            node1 in self.users.values() and node2 in self.users.values()
        ):  # check if both users exists
            index1 = list(self.users.values()).index(
                node1
            )  # find the index of user1 and user2
            index2 = list(self.users.values()).index(node2)
            self.adj_matrix[index1][index2] = 1
            self.adj_matrix[index2][
                index1
            ] = 1  # set an edge in the adj matrix so we change it to 1

    def remove_node_and_connections(self, node):
        if node in self.users.values():  # check if the user exists
            index = list(self.users.values()).index(node)  # get the index of the user
            self.adj_matrix.pop(index)  # remove the corresponding row from the matrix
            for row in self.adj_matrix:
                row.pop(index)  # remove the element at each row to dissconnect the user
            self.users = {
                k: v for k, v in self.users.items() if v != node
            }  # removes the node from the dic
            self.num_nodes -= 1  # decrement the counter

    def remove_edge(self, node1, node2):
        if (
            node1 in self.users.values() and node2 in self.users.values()
        ):  # check if both users exists
            index1 = list(self.users.values()).index(node1)
            index2 = list(self.users.values()).index(node2)  # finds the index
            self.adj_matrix[index1][index2] = 0
            self.adj_matrix[index2][
                index1
            ] = 0  # initialize the value to 0 so no more connections between them

    def get_neighbors(self, node):
        if node in self.users.values():
            index = list(self.users.values()).index(node)
            # find all the indices where x = 1 so theres a connection and save them into i
            neighbors = [i for i, x in enumerate(self.adj_matrix[index]) if x == 1]
            # returns the list of neighbors of a specific user
            return [list(self.users.values())[i] for i in neighbors]
        else:
            return []

    def __str__(self):
        return str(self.adj_matrix)  # string representation of the adj matrix


def display_menu():
    print(
        "1. Add a user to the platform.\n"
        + "2. Remove a user from the platform.\n"
        + "3. Send a friend request to another user.\n"
        + "4. Remove a friend from your list.\n"
        + "5. View your list of friends.\n"
        + "6. View the list of users on the platform.\n"
        + "7. Exit.\n"
        + "- - - - - - - - - - - - - - -\n"
    )


def get_choice():
    while True:
        choice = int(input("Please enter your choice here: "))
        if choice < 1 or choice > 7:
            print("Invalid input. Please enter a number between 1 and 7.")
        else:
            return choice


def add_user(graph):
    new_user = input("Please enter the username: ")
    while True:
        if new_user in graph.users.values():
            print("Username already taken.\n")
            new_user = input("Please enter the username: ")
        else:
            print("User added successfully.\n")
            graph.add_node(new_user)
            return graph


def remove_user(graph):
    username = input("Please enter the user you want to remove: ")
    while True:
        if username in graph.users.values():
            graph.remove_node_and_connections(username)
            return graph
        else:
            print("Please make sure of the username.")
            username = input("Please enter the user you want to remove: ")


def friend_request(graph):
    user1 = input("Please enter the name of the first user: ")
    user2 = input("Please enter the name of the second user: ")
    if user1 in graph.users.values() and user2 in graph.users.values():
        graph.add_edge(user1, user2)
        print("\nFriend request sent successfully.\n")
    else:
        print("One or both users do not exist.")


def remove_friend(graph):
    user1 = input("Please enter the name of the first user: ")
    user2 = input("Please enter the name of the second user: ")
    if user1 in graph.users.values() and user2 in graph.users.values():
        graph.remove_edge(user1, user2)
        print("\nFriendship removed successfully.\n")
        print(graph)
    else:
        print("One or both users do not exist.")


def view_friend_list(graph):
    user = input("Please enter a user: ")
    if user in graph.users.values():
        friends = graph.get_neighbors(user)
        print(friends)
    else:
        print("User does not exist.")


def main():
    graph = Graph()
    while True:
        display_menu()
        choice = get_choice()
        if choice == 1:
            add_user(graph)
        elif choice == 2:
            remove_user(graph)
        elif choice == 3:
            friend_request(graph)
        elif choice == 4:
            remove_friend(graph)
        elif choice == 5:
            view_friend_list(graph)
        elif choice == 6:
            print(graph.users)
        elif choice == 7:
            print("Exiting the Program.")
            break


main()
