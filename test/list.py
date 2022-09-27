a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[1])
print(a[-1])

a = [1, 2, 3, ["a", "b", "c"]]

print(a[0])
print(a[-1][0])
print(a[0:2])

b = a[0]

a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

print(a * 3)
print(len(a * 3))

print(str(a[2]) + "hi")

# 문자열은 안되지만 리스트는 값을 수정 할 수 있다
a[2] = 4
print(a)

# del 객체
# 객체란 파이썬에서 사용되는 모든 자료형을 말한다.
del a[2]
print(a)


# 리스트 관련 함수들
a.append(99)
print(a)

# 리스트 안에는 어떤 자료형도 추가할 수 있다.
# a.append([5, 6])
# print(a)

a.sort()
print(a)

a.sort(reverse=True)
print(a)

a.reverse()
print(a)

# index(x) 함수는 리스트에 x 값이 있으면 x의 위치 값을 돌려준다.
print(a.index(99))

a.append([1, 2, 3])
print(a)
print(a.index([1, 2, 3]))

# insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수이다. 파이썬에서는 숫자를 0부터 센다는 것을 반드시 기억하자.
a.insert(1, 70)
print(a)

# remove(x)는 리스트에서 첫 번째로 나오는 x를 삭제하는 함수이다.
a.remove(70)
print(a)

# pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.
print(a.pop())
print(a)

# count(x)는 리스트 안에 x가 몇 개 있는지 조사하여 그 개수를 돌려주는 함수이다.
print(a.count(99))

# extend(x)에서 x에는 리스트만 올 수 있으며 "원래의 a 리스트에 x 리스트를 더하게 된다".
a.extend([1, 4, 5])  # a = a + [1, 4, 5]
print(a)

a.append([1, 5, 7])  #
print(a)
