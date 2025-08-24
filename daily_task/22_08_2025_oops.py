# 📌 Day 2 Topic: Data Structures in Python
# Inside the Topic:
# 1. Lists, Tuples, Sets, Dictionaries – built-in Python data structures.
# 2. Stack (LIFO – Last In, First Out).
# 3. Queue (FIFO – First In, First Out).
# 4. Basic operations: push, pop, enqueue, dequeue, is_empty.
# 5. When to use Stack vs Queue in real life.


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0

# Example
s = Stack()
s.push(10)
s.push(20)
print("Popped:", s.pop())
print("Is empty?", s.is_empty())


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty!"

    def is_empty(self):
        return len(self.queue) == 0

# Example
q = Queue()
q.enqueue(1)
q.enqueue(2)
print("Dequeued:", q.dequeue())
print("Is empty?", q.is_empty())
