import unittest
from linkedlist import LinkedList

class SortedListTests(unittest.TestCase):

    def setUp(self) -> None:
        self.linked_list = LinkedList()

        self.linked_list_1 = LinkedList()
        self.linked_list_2 = LinkedList()
        self.linked_list_3 = LinkedList()

    def tearDown(self) -> None:
        del self.linked_list

        del self.linked_list_1
        del self.linked_list_2
        del self.linked_list_3

    def test_can_add_and_get_item(self):
        '''Test: the user can add and then get an item using the syntax: [<index_number>]'''
        self.linked_list.add(value='Andrew')

        item = self.linked_list[0]

        self.assertEqual(item.data, 'Andrew')

    def test_can_add_and_get_item_using_index(self):
        '''Test: the user can add an item by giving an index and then get an item by an index'''
        names = ['James', 'Maria', 'Leon', 'Jill']

        for name in names:
            self.linked_list.add(value=name)

        index = 2
        self.linked_list.add(value='Andrew', index=index)

        item = self.linked_list[index]

        self.assertEqual(item.data, 'Andrew')

    def test_can_remove_last_item(self):
        names = ['James', 'Maria', 'Leon', 'Jill']

        for name in names:
            self.linked_list.add(value=name)

        self.linked_list.remove()
        
        items = [i.data for i in self.linked_list]
        
        self.assertTrue('Jill' not in items)

    def test_can_remove_last_item_using_index(self):
        names = ['James', 'Maria', 'Andrew', 'Leon', 'Jill']

        for name in names:
            self.linked_list.add(value=name)

        self.linked_list.remove(index=2)
        items = [i.data for i in self.linked_list]

        self.assertTrue('Andrew' not in items)
        
        self.linked_list.remove(index=0)
        items = [i.data for i in self.linked_list]
        
        self.assertTrue('James' not in items and len(items) != 0)

    def test_empty_linked_list(self):
        self.assertEqual(len(self.linked_list), 0)

    def test_non_empty_linked_list(self):
        names = ['James', 'Maria', 'Leon', 'Jill']

        for name in names:
            self.linked_list.add(value=name)

        self.assertEqual(len(self.linked_list), 4)

    def test_generator_and_iterator(self):
        names = ['James', 'Maria', 'Leon', 'Jill']

        for name in names:
            self.linked_list.add(value=name)

        iterator = iter(self.linked_list)

        item_1 = next(iterator)
        item_2 = next(iterator)

        self.assertEqual(item_1.data, 'James')
        self.assertEqual(item_2.data, 'Maria')

    def test_greater_then(self):
        names_1 = ['James', 'Maria', 'Lora']
        names_2 = ['Leon', 'Jill']

        for name in names_1:
            self.linked_list_1.add(value=name)

        for name in names_2:
            self.linked_list_2.add(value=name)

        self.assertEqual(self.linked_list_1 > self.linked_list_2, True)

    def test_greater_or_equal(self):
        names_1 = ['James', 'Maria', 'Lora']
        names_2 = ['Leon', 'Jill']

        for name in names_1:
            self.linked_list_1.add(value=name)

        for name in names_2:
            self.linked_list_2.add(value=name)

        self.assertEqual(self.linked_list_2 >= self.linked_list_1, False)

    def test_linked_list_joining(self):
        names_1 = ['James', 'Maria', 'Lora']
        names_2 = ['Leon', 'Jill']

        for name in names_1:
            self.linked_list_1.add(value=name)

        for name in names_2:
            self.linked_list_2.add(value=name)

        linked_list_3 = self.linked_list_1 + self.linked_list_2

        items = [i.data for i in linked_list_3]

        self.assertEqual(items, ['James', 'Maria', 'Lora', 'Leon', 'Jill'])
    
    def test_empty_or_not(self):
        self.assertFalse(bool(self.linked_list))

        self.linked_list.add(value='Andrew')

        self.assertTrue(bool(self.linked_list))
   

if __name__ == '__main__':
    unittest.main()