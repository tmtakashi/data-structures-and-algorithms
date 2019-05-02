import ctypes


class DynamicArray(object):

    def __init__(self):
        self.n = 0  # actual content size
        self.capacity = 1  # capacity of the array
        self.A = self.make_array(self.capacity)

    def __len__(self):
        '''
        Returns length of the actual sequence.
        '''
        return self.n

    def __getitem__(self, k):
        '''
        Returns element at index k.
        '''
        if not 0 <= k < self.n:
            return IndexError('Index is out of bounds!')

        return self.A[k]

    def append(self, elem):
        '''
        Add element to the end of the array.
        '''
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = elem
        self.n += 1

    def _resize(self, new_cap):
        '''
        Resize internal array to new capacity.
        '''
        B = self.make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        '''
        Returns new array with new_cap
        '''
        return (new_cap * ctypes.py_object)()


if __name__ == "__main__":
    arr = DynamicArray()

    print('Appending 1')
    arr.append(1)
    print('Length: ', len(arr))

    print('Appending 2')
    arr.append(2)
    print('Length: ', len(arr))

    print('Index 0: ', arr[0])
    print('Index 1: ', arr[1])
