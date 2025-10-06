from collections.abc import Hashable
listRandom = ['54', 'test', '$@LA', '&2', 'A', '101', '-21', '+21', [1, 2], {'x': 10}]
resultSet = set()
for item in listRandom:
    if isinstance(item, Hashable):
        resultSet.add(item)
print(resultSet)