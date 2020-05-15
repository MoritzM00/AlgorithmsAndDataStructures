class SlowDeque:
    """
    Slow implementation of a double ended queue (deque) using two stacks

    | in |
    |    |       dequeueBack         _________
    -- input stack ---> output stack        out
                                     _________

    When only dequeue_back and enqueue_front is in Use (FIFO one sided queue)
    then dequeue_back has an amortized Time Complexity of O(1).

    If you make use of enqueue_back and dequeue_front (double-ended queue) then this amortized
    runtime gets destroyed because out and in change their roles.
    Therefore, this is a really slow implementation of a deque and should not be used.
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
