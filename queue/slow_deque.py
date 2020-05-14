class SlowDeque:
    """
    Slow implementation of a double ended queue (deque) using two stacks
    """

    def __init__(self):
        self.input = []
        self.output = []

    def enqueue_front(self, value):
        self.input.append(value)

    def dequeue_back(self):
        if len(self.output) == 0:
            while len(self.output) > 0:
                e = self.input.pop()
                self.output.append(e)
        return self.output.pop()

    def enqueue_back(self, value):
        self.output.append(value)

    def dequeue_front(self):
        if len(self.input) == 0:
            while len(self.input) > 0:
                e = self.output.pop()
                self.input.append(e)
        return self.input.pop()
