class Dequeue:
    """
    Slow implementation of a double ended queue (deque) using two stacks

    | in |
    |    |       dequeueBack         _________
    -- input stack ---> output stack        out
                                     _________

    Dequeue_back has an amortized time complexity of O(1)
    The other operations are O(1)
    """

    def __init__(self):
        self.input = []
        self.output = []

    def enqueue_front(self, value):
        self.input.append(value)

    def dequeue_back(self):
        if len(self.output) == 0:
            while len(self.input) > 0:
                e = self.input.pop()
                self.output.append(e)
        return self.output.pop()

    def enqueue_back(self, value):
        self.output.append(value)

    def dequeue_front(self):
        if len(self.input) == 0:
            return self.output.pop(0)
        else:
            return self.input.pop()
