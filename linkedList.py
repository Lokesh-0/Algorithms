class Node:
    '''
    constructor
    Node:
    {
    Value: 5
    Next: none
    }
    '''
    def __init__(self, value):
        self.value = value
        self.next = None


class linkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length+=1
        return True


    def set_value(self, index, value):
        '''
        checks if the index is out of the current list
        '''
        if index < 0 or index >= self.length:
            return False
        '''
        if not then temp will start checking from the head value and run over the
        range present and once the temp is equal to the index provided it will replace the
        value with the given value as of the below code
        '''

        temp = self.head
        for i in range(index):
            temp = temp.next

        temp.value = value
        return True



    def pop_start(self):
        '''
        Popping out head in the list and making Head+1 as Main Head 
        '''
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp


    def pop_end(self):
        '''
        Dropping the tail and pointing the tail-1 as the main tail
        '''
        if self.length == 0:
            return None 
        temp = self.head 
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def get(self, index):
        '''
        get the value at a desired index
        '''
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def insert(self, value, index):
        '''
        Edge Case  1 if the index is out of bounce
        '''
        if index < 0 or index > self.length:
            return False
        '''
        Edge Case 2: if the insert should be at the start of the list
        '''
        if index == 0:
            return self.prepend(value)
        '''
        Edge Case 3  if the insert should be at the End of the list
        '''
        if index == self.length:
            return self.append(value)
        '''
        Edge Case 4: if the insertion will be in the middle of the list
        '''
        new_node = Node(value)
        '''
        get the new value
        '''
        temp = self.get(index - 1)
        '''
        set the temp to index where the element needs to be inserted 
        '''
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    def remove(self, index):
        '''
        remove the element at the index needed
        '''
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_end()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return temp
        
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before  = temp
            temp = after
   

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

my_linked_list = linkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.print_list()
#print(my_linked_list.insert(97,2))

#print(my_linked_list.remove(2))
my_linked_list.reverse()

#my_linked_list.prepend(29)

#print(my_linked_list.pop_start())

#print(my_linked_list.pop_end())
#my_linked_list.set_value(4,99)
#print(my_linked_list.insert(97,2))
my_linked_list.print_list()

#print(my_linked_list.get(4))





