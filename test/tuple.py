t1 = (1, 2, "a", "b")
t2 = (3, 4, "a", "b")
# del t1[0] not working
# t1[0] = 3 not working

print(t1[0])
print(t1[1:])
t2 = t1 + t2  # 요소값을 지우거나 변경만 못하지 더하기는 가능

print(t1 * 3)
print(len(t2))
