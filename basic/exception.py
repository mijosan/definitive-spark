try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)
finally:
    print("finally")


# try문에 else절 사용하기
# 오류가 없으면 else절이 수행된다.
try:
    age = int(input("나이를 입력하세요: "))
except:
    print("입력이 정확하지 않습니다.")
else:
    if age <= 18:
        print("미성년자는 출입금지입니다.")
    else:
        print("환영합니다.")


# 오류 회피하기
try:
    f = open("나없는파일", "r")
except FileNotFoundError:
    pass

# 오류 일부러 발생시키기
# NotImplementedError는 파이썬 내장 오류로, 꼭 작성해야 하는 부분이 구현되지 않았을 경우 일부러 오류를 일으키기 위해 사용한다.
class Bird:
    def fly(self):
        raise NotImplementedError


class Eagle(Bird):
    def fly(self):
        print("very fast")


eagle = Eagle()
eagle.fly()

# 예외 만들기
# 프로그램 수행 도중 특수한 경우에만 예외 처리를 하기 위해서 종종 예외를 만들어서 사용한다.
# 직접 예외를 만들어 보자. 예외는 다음과 같이 파이썬 내장 클래스인 Exception 클래스를 상속하여 만들 수 있다.
# 오류 메시지를 출력했을 때 오류 메시지가 보이게 하려면 오류 클래스에 다음과 같은 __str__ 메서드를
# 구현해야 한다. __str__ 메서드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메서드이다.
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."


def say_nick(nick):
    if nick == "바보":
        raise MyError()
    print(nick)


try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")


try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
