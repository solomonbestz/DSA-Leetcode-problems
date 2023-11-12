
class Node:
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
    
    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        
        current_node = self.head
        while True:
            if current_node.next_node is None:
                current_node.next_node = node
                break
            current_node = current_node.next_node
        
    def print_linked_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, "-->", end=" ")
            current_node = current_node.next_node
        print("None")



if __name__=='__main__':
    linked_list = LinkedList()

    linked_list.print_linked_list()
    linked_list.insert('Hello')
    linked_list.print_linked_list()
    linked_list.insert(234)
    linked_list.print_linked_list()
    linked_list.insert(34)
    linked_list.print_linked_list()
    # linked_list.inserting_at_begining([12, 34, 'Hello'])
