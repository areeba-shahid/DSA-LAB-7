class Tower:
    def __init__(self):
        self.terminate = 1
    
    def print_move(self, source, destination):
        print("{} -> {}".format(source, destination))
    
    def move(self, disc, source, destination, auxiliary):
        if disc == self.terminate:
            self.print_move(source, destination)
        else:
            # Move `disc - 1` discs from source to auxiliary
            self.move(disc - 1, source, auxiliary, destination)
            # Move the `disc` from source to destination
            self.print_move(source, destination)
            # Move `disc - 1` discs from auxiliary to destination
            self.move(disc - 1, auxiliary, destination, source)

# Instantiate and call the move function
t = Tower()
t.move(3, 'A', 'B', 'C')
