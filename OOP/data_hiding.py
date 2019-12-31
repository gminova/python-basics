class Queue:
    def __init__(self, contents):
        # _underscore marks a method as private
        # but does not prevent outside access
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        self._hiddenlist.pop(-1)

    def __repr__(self):
        return 'Queue({})'.format(self._hiddenlist)


q = Queue([1, 2, 3])
print(q)
q.push(0)
print(q)
q.pop()
print(q)
print(q._hiddenlist)
