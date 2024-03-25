import LinkedList as ll

my_linked_list = ll.LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

print("LL before reverse():")
my_linked_list.print_list()

my_linked_list.reverse()

print("\nLL after reverse():")
my_linked_list.print_list()