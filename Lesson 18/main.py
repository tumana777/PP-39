# class A:
#     def show(self):
#         print("A")
#
# class B(A):
#     def test(self):
#         print("B")

# from abc import ABC, abstractmethod
#
# class Payment(ABC):
#     def __init__(self, amount):
#         self.amount = amount
#
#     @abstractmethod
#     def pay(self):
#         pass
#
# class CashPayment(Payment):
#     def pay(self):
#         print(f"Paid with cash {self.amount}$")
#
#
# class CreditCardPayment(Payment):
#     def pays(self):
#         print(f"Paid with credit card {self.amount}$")
#
# payment = CashPayment(100)
# payment.pay()
#
# payment1 = CreditCardPayment(200)
# payment1.pay()


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.size = 0
#
#     def empty(self):
#         return self.size == 0
#
#     def peek(self):
#         if self.empty():
#             return "Stack is empty"
#         return self.top.data
#
#     def push(self, data):
#         new_node = Node(data)
#
#         new_node.next = self.top
#         self.top = new_node
#         self.size += 1
#
#     def pop(self):
#
#         if self.empty():
#             return "Stack is empty"
#
#         popped_element = self.top.data
#
#         self.top = self.top.next
#         self.size -= 1
#         return popped_element
#
#
# stack = Stack()
# print(stack.empty())
# print(stack.peek())

# stack.push(8)
# stack.push(6)
# stack.push(12)
# stack.push(7)
# stack.push(9)
# print(stack.peek())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.peek())


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def prepend(self, data):
#         new_node = Node(data)
#
#         new_node.next = self.head
#         self.head = new_node
#
#     def append(self, data):
#         new_node = Node(data)
#
#         if self.head is None:
#             self.head = new_node
#             return
#
#         current = self.head
#
#         while current.next:
#             current = current.next
#
#         current.next = new_node
#
#     def print_list(self):
#
#         current = self.head
#
#         while current:
#             print(current.data, end=" -> " if current.next else "\n")
#             current = current.next
#
#
# ll = LinkedList()

# print(ll.head)

# ll.append(5)
# ll.append(12)
# ll.append(15)
# ll.append(26)
# ll.append(20)
# ll.append(13)
# ll.prepend(10)
#
# ll.print_list()

# print(ll.head.data)


# from collections import deque
#
# deque_obj = deque(maxlen=12)
#
# deque_obj.append(7)
# deque_obj.append(3)
# deque_obj.append(5)
# deque_obj.append(9)
# deque_obj.appendleft(10)
# deque_obj.extend([11, 13, 15])
# deque_obj.appendleft(12)
# deque_obj.pop()
# deque_obj.popleft()
#
# print(list(deque_obj))


# from queue import Queue
#
# queue = Queue(maxsize=3)

# queue.put(8)
# queue.put(6)
# queue.put(12)
# queue.put(7)
# queue.put(9)
# print(queue.queue)
# queue.get()
# print(queue.queue)

# queue.put(10)
# queue.put(11)
# queue.put(12)
# queue.put(13)

# queue.put_nowait(12)
# queue.put_nowait(13)
# queue.put_nowait(14)
# queue.put_nowait(15)

# print(queue.queue)

# queue.get_nowait()