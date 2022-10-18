def add(a, b):  # a, b는 매개변수
    return a + b


print(add(3, 4))  # 3, 4는 인수


# *args처럼 매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어 주기 때문이다.
def add_many(*args):
    result = 0
    for i in args:
        result = result + i

    return result


# 키워드 파라미터 kwargs
# 입력값 a=1 또는 name='foo', age=3이 모두 딕셔너리로 만들어져서 출력된다는 것을 확인할 수 있다.
# 즉 **kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고
# 모든 key=value 형태의 결괏값이 그 딕셔너리에 저장된다.
def print_kwargs(**kwargs):
    print(kwargs)


test = {"age": 3, "name": "foo"}

# print_kwargs(test) not working
print_kwargs(a="test")


def add_and_mul(a, b):
    return a + b, a * b


print(add_and_mul(3, 4))


# 위 오류 메시지는 초깃값을 설정해 놓은 매개변수 뒤에 초깃값을 설정해 놓지 않은
# 매개변수는 사용할 수 없다는 뜻이다. 즉 매개변수로 (name, old, man=True)는 되지만
# (name, man=True, old)는 안 된다는 것이다. 초기화시키고 싶은 매개변수를 항상 뒤쪽에 놓는 것을 잊지 말자.
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


a = 1


def vartest():
    global a
    a = a + 1


vartest()
print(a)
