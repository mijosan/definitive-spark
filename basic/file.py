# a = input("입력")  # input은 입력되는 모든 것을 문자열로 취급하기 때문에 number는 숫자가 아닌 문자열임에 주의하자.
# print(a)

# ※ 한 줄 씩 읽어 출력할 때 줄 끝에 \n 문자가 있으므로 빈 줄도 같이 출력된다.
f = open("C:/Users/mobigen/Documents/hello.txt", "r")
print(f.read())  # f.read()는 파일의 내용 전체를 문자열로 돌려준다. 따라서 위 예의 data는 파일의 전체 내용이다.


# 지금까지 살펴본 예제를 보면 항상 다음과 같은 방식으로 파일을 열고 닫아 왔다.

f = open("foo.txt", "w")
f.write("Life is too short, you need python")
f.close()
# 파일을 열면 위와 같이 항상 close해 주는 것이 좋다. 하지만 이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까? 파이썬의 with문이 바로 이런 역할을 해준다. 다음 예는 with문을 사용해서 위 예제를 다시 작성한 모습이다.

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")


class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second


a = FourCal()
