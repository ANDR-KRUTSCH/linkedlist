from typing import Any

class LinkedList:
    '''Linked-list is the custom data-type in the format: data:link -> data:link -> data.link'''

    class _Node:

        def __init__(self, data: Any) -> None:
            self.data = data
            self._link = None

    
    def __init__(self) -> None:
        self._head = None
        self._length = 0

    def clear(self) -> None:
        '''Remove all contained nodes.'''

        self._head = None

    def add(self, value: Any, index: int = None) -> None:
        '''A method for adding a node to the linked-list. If an index was given, a node will be added at index-position else it will be added to the end of the linked-list.'''

        if index is not None and not isinstance(index, int):
            raise TypeError('index type must be an integer')
        elif index is not None and index < 0:
            raise ValueError('index value must be >= 0')
        
        # if there is no an index than pass the new node to the end of the LinkedList
        if index is None:
            # if there are no any nodes than pass the new node to the begin of the LinkedList
            if self._head is None:
                self._head = self._Node(data=value)
            # if there are some nodes than pass the new node to the end by giving the last node and creating the link to the new node for it
            else:
                node = self._head
                while True:
                    if node._link is None:
                        node._link = self._Node(data=value)
                        break
                    else:
                        node = node._link
        # if there is an index than pass the new node by index-position in the LinkedList 
        else:
            # if there are no any nodes and the index is 0
            if self._head is None and index == 0:
                self.add(value=value)
            # if there are no any nodes and the index is more than 0
            elif self._head is None and index > 0:
                raise IndexError('list assignment index out of range')
            # if there are some nodes and the index is 0
            elif self._head and index == 0:
                _head = self._head
                node = self._Node(data=value)
                node._link = _head
                self._head = node
            # if there are some nodes and the index is more than 0
            elif self._head and index > 0:
                node = self._head
                for i in range(index + 1):
                    if i == index - 1:
                        previous_node = node
                    elif i == index:
                        next_node = node
                        node = self._Node(data=value)
                        previous_node._link = node
                        node._link = next_node
                    node = node._link

        self._length += 1
        
    def remove(self, index: int = None) -> None:
        '''A method for removing a node from the linked-list. If an index was given, a node at given index-position will be removed else the last node will be removed.'''

        if index is not None and not isinstance(index, int):
            raise TypeError('index type must be an integer')
        elif index is not None and index < 0:
            raise ValueError('index value must be >= 0')
        
        # if there is no an index than remove the last node from the LinkedList
        if index is None:
            # if there are no nodes
            if self._head is None:
                pass
            # if there are some nodes
            else:
                previous_node = None
                node = self._head
                while True:
                    if node._link is None:
                        if previous_node is None:
                            self._head = None
                            break
                        else:
                            previous_node._link = None
                            break
                    else:
                        previous_node = node
                        node = node._link
        # if there an index than remove the node by an index from the LinkedList
        else:
            # if there are no nodes
            if self._head is None:
                raise IndexError('remove index out of range')
            # if there are nodes and index is 0
            elif self._head and index == 0:
                node = self._head
                if node._link is None:
                    self._head = None
                else:
                    self._head = node._link
            # if there are some nodes and index is more than 0
            elif self._head and index > 0:
                node = self._head
                for i in range(index + 1):
                    if i == index - 1:
                        previous_node = node
                    elif i == index:
                        next_node = node._link
                        previous_node._link = next_node
                    node = node._link

        self._length -= 1

    @property
    def length(self) -> int:
        '''returns the length of the LinkedList instance.'''

        return self._length
        
    def __len__(self) -> int:
        '''returns the length of the LinkedList instance.'''

        return self._length

    def __iter__(self):
        '''provides the opportunity to iterate the LinkedList instance.'''

        if self._head is None:
            pass
        else:
            node = self._head
            while True:
                if node._link is None:
                    yield node.data
                    break
                else:
                    yield node.data
                    node = node._link

    def __getitem__(self, index: int) -> _Node:
        '''provides getting nodes using the following syntax: LinkedList()[2] - where 2 is an index of the node.'''

        if not isinstance(index, int):
            raise TypeError('index type must be an integer')

        if self.length <= index or index < 0:
            raise IndexError('list index out of range')
        else:
            if index == 0:
                return self._head
            else:
                node = self._head._link

                i = 1
                while True:
                    if i == index:
                        return node
                    else:
                        node = node._link
                        i += 1

    def __gt__(self, item) -> bool:
        '''returns True if the first LinkedList instance length greater then the second LinkedList instance length else returns False when using ">" or "<" between them.'''

        if isinstance(item, self.__class__):
            return self.length > item.length
        else:
            raise TypeError('LinkedList can be compared using ">" and "<" only between the LinkedList instances')
        
    def __ge__(self, item) -> bool:
        '''returns True if the first LinkedList instance length greater or equal to the second LinkedList instance length else returns False when using ">=" or "<=" between them.'''

        if isinstance(item, self.__class__):
            return self.length >= item.length
        else:
            raise TypeError('LinkedList can be compared using ">=" and "<=" only between the LinkedList instances')
        
    def __add__(self, item) -> None:
        '''provides joining different LinkedList instances to one using "+" between instances.'''

        if isinstance(item, self.__class__):
            last_node = self[self.length - 1]
            last_node._link = item._head
            return self
        else:
            raise TypeError('LinkedList can be joined using "+" only with another LinkedList instance')
        
    def __delattr__(self, name: str) -> None:
        '''raises an error when trying to delete some attribute from the LinkedList.'''

        raise AttributeError('permission denied: attribute deleting')

    def __bool__(self) -> bool:
        '''returns True if there are one or more nodes in the LinkedList instance else returns False'''

        if self._head is None:
            return False
        else:
            return True