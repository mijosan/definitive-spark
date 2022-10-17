s1 = set([1, 2, 3])
print(s1)


s2 = set("Hello")
print(s2)

# set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환한후 해야 한다.
l1 = list(s2)

print(l1)

# 중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용하기도 한다.


# set 자료형을 정말 유용하게 사용하는 경우는 교집합, 합집합, 차집합을 구할 때이다.
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)

s1.add(4)
print(s1)

s1.remove(2)
print(s1)
