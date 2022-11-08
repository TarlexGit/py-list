class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class NodesConstructor:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def add(self, data):
        self.length+=1
        if self.first == None:
            self.last = self.first = Node(data, None)
        else:
            self.last.next = self.last = Node(data, None)

    def set_to_pos(self, i, data):
        if i == 0:
            self.first = Node(data, self.first)
            return

        if self.first == None:
            self.last = self.first = Node(data, None)
            return

        point=self.first
        count = 0

        while point != None:
            count+=1
            if count == i:
                point.next = Node(data, point.next)
                if point.next.next == None:
                    self.last = point.next
                break
            point = point.next


    def add_to_pos(self, pos, data):
        if pos == 0:
            self.first = Node(data, self.first)
            return

        if self.first == None:
            self.last = self.first = Node(data, None)
            return

        point=self.first
        count = 0
        
        while point != None:
            count+=1
            if count == pos:
                point.next = Node(data, point.next)
                if point.next.next == None:
                    self.last = point.next
                break
            point = point.next


NC = NodesConstructor()
NC.add(1)
NC.add(2)
NC.add(3)
NC.add(4)
NC.add(5)

NC.set_to_pos(2, 6)

point = NC.first
count = 0
stack = []

while True:
    stack.append(point.value)
    point = point.next
    count +=1
    try:
        if point.next == None: 
            stack.append(point.value)
            break
    except AttributeError:
        print('breack with AttributeError')
        break

print(stack)
