# 파이썬 확장자 .py로 만든 파이썬 파일은 모두 모듈이다.
# import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다.
# 파이썬 라이브러리는 파이썬을 설치할 때 자동으로 설치되는 파이썬 모듈을 말한다.
# 때로는 mod1.add, mod1.sub처럼 쓰지 않고 add, sub처럼 모듈 이름 없이 함수 이름만 쓰고 싶은 경우
# 도 있을 것이다. 이럴 때는 "from 모듈 이름 import 모듈 함수"를 사용하면 된다.
# 위 형식을 사용하면 위와 같이 모듈 이름을 붙이지 않고 바로 해당 모듈의 함수를 쓸 수 있다.from mod1 import add, sub
# from mod1 import *
# mod1.py
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# if __name__ == "__main__"을 사용하면 C:\doit>python mod1.py처럼 직접 이 파일을 실행했을 때는
# __name__ == "__main__"이 참이 되어 if문 다음 문장이 수행된다. 반대로 대화형 인터프리터나
# 다른 파일에서 이 모듈을 불러서 사용할 때는 __name__ == "__main__"이 거짓이 되어
# if문 다음 문장이 수행되지 않는다.


# mod1.py
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


if (
    __name__ == "__main__"
):  # mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장된다.
    print(add(1, 4))
    print(sub(4, 2))

# 도트 연산자(.)를 사용해서 import a.b.c처럼 import할 때 가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야만 한다.
