class Node:
    def __init__(self, name):
        self.name = name
        self.next = None  # Clockwise
        self.prev = None  # Counter-clockwise ("behind")

class MusicalChairs:
    def __init__(self, students):
        # Build circular doubly linked list
        self.head = Node(students[0])
        current = self.head
        
        for name in students[1:]:
            new_node = Node(name)
            current.next = new_node
            new_node.prev = current
            current = new_node
            
        current.next = self.head
        self.head.prev = current

    def find_node(self, name):
        current = self.head
        start = current
        while True:
            if current.name == name:
                return current
            current = current.next
            if current == start:
                break
        return None

    def remove_behind(self, ref_name, steps):
        ref_node = self.find_node(ref_name)
        if not ref_node:
            return

        # Move counter-clockwise 'steps' times
        target = ref_node
        for _ in range(steps):
            target = target.prev

        print(f"Eliminating '{target.name}' ({steps}-th behind '{ref_name}')")

        # Update pointers to remove target
        target.prev.next = target.next
        target.next.prev = target.prev

        if target == self.head:
            self.head = target.next

    def get_remaining(self):
        remaining = []
        current = self.head
        start = current
        while True:
            remaining.append(current.name)
            current = current.next
            if current == start:
                break
        return remaining

# Initial order in clockwise direction
initial_order = ['P', 'R', 'T', 'Q', 'S', 'V', 'U', 'W']
game = MusicalChairs(initial_order)

# Round 1: 4th student behind P leaves (S)
game.remove_behind('P', 4)

# Round 2: 5th student behind Q leaves (U)
game.remove_behind('Q', 5)

# Round 3: 3rd student behind V leaves (R)
game.remove_behind('V', 3)

# Round 4: 4th student behind U leaves (W)
game.remove_behind('U', 4)

# Output results
print("\nStudents left after 4th round:")
print(game.get_remaining())
