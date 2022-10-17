# Key와 Value의 쌍 여러 개가 { }로 둘러싸여 있다. 각각의 요소는 Key : Value 형태로 이루어져 있고 쉼표(,)로 구분되어 있다.
# Key에는 변하지 않는 값을 사용하고, Value에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다.

dic = {
    "name": "pey",
    "phone": "0119993323",
    "birth": "1118",
    "birth": "1119",
    (1, 2): "hello",
}

print(dic[1, 2])
print(dic)

dic["test"] = "value"

print(dic)

dic["test"] = "value2"

print(dic)


# 또 한 가지 주의해야 할 사항은 Key에 리스트는 쓸 수 없다는 것이다.
# 하지만 튜플은 Key로 쓸 수 있다. 딕셔너리의 Key로 쓸 수 있느냐 없느냐는
# Key가 변하는(mutable) 값인지 변하지 않는(immutable) 값인지에 달려 있다.
# 리스트는 그 값이 변할 수 있기 때문에 Key로 쓸 수 없다.

dic[(1, 2)] = "good"
print(dic)

print(dic[(1, 2)])
print(dic.keys())

list = tuple(dic.keys())
list2 = dic.keys()

print(list)

if list == list2:
    print("같다")
else:
    print("다르다")

for i in list2:
    print(i)

tuple = dic.items()
print(tuple)

dic.clear()
print(dic)

# 다만 다음 예제에서 볼 수 있듯이 a['nokey']처럼 존재하지 않는 키(nokey)로 값을 가져오려고
# 할 경우 a['nokey']는 Key 오류를 발생시키고 a.get('nokey')는 None을 돌려준다는 차이가 있다.
# 어떤것을 사용할지는 여러분의 선택이다.

# print(dic["name", "default"])
print(dic.get("hello", "default"))

"name" in dic
