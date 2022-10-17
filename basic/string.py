# 문자열에 작은따옴표 (') 포함시키기
from turtle import hideturtle


str1 = "Python's favorite food is perl"

print(str1)

# 문자열에 큰따옴표 (") 포함시키기
str2 = 'Python"s favorite food is perl'

print(str2)

# 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
str3 = "Python\"s f'avorite food is perl"

print(str3)

# 여러 줄인 문자열을 변수에 대입하고 싶을 때
str4 = "Life is too short\nYou need python"  # 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
# 위 예처럼 줄바꿈 문자 \n을 삽입하는 방법이 있지만 읽기에 불편하고 줄이 길어지는 단점이 있다.

print(str4)

str5 = """
Life is too short
You need python
"""

print(str5)


# 문자열 연산하기

# 문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
print(head + tail)

print(head * 2)

# 문자열 길이 구하기
print(len(head))

# 문자열 인덱싱
print(head[0])
print(head[-1])

# 문자열 슬라이싱
print(head[0:6])
print(head[1:6])
print(head[0:])
print(head[:])
print(head[1:-1])

# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)


# 문자열 포매팅 따라 하기 (문자열 포맷 코드 이용, format 함수 이용, f 문자열 포매팅)

# 숫자 바로 대입 (문자열 포맷 코드 %d)
str6 = "I eat %d apples." % 3

print(str6)

# 문자열 바로 대입 (문자열 포맷 코드 %s)
str7 = "I eat %s apples." % "five"

print(str7)

# 숫자 값을 나타내는 변수로 대입
number = 3
str8 = "I eat %d apples." % number

print(str8)

# 2개 이상의 값 넣기
number = 10
day = "three"
str9 = "I ate %d apples. so I was sick for %s days." % (number, day)

print(str9)

# 여기에서 재미있는 것은 %s 포맷 코드인데, 이 코드는 어떤 형태의 값이든 변환해 넣을 수 있다. 무슨 말인지 예를 통해 확인해 보자.

# >>> "I have %s apples" % 3
# 'I have 3 apples'
# >>> "rate is %s" % 3.234
# 'rate is 3.234'
# 3을 문자열 안에 삽입하려면 %d를 사용하고, 3.234를 삽입하려면 %f를 사용해야 한다. 하지만 %s를 사용하면 이런 것을 생각하지 않아도 된다. 왜냐하면 %s는 자동으로 % 뒤에 있는 값을 문자열로 바꾸기 때문이다.

# 포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다
str10 = "error is %d%%." % 98
print(str10)

# 포맷 코드와 숫자 함께 사용하기
str11 = (
    "%10s" % "hi"
)  # 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨 두라는 의미
print(str11)

str12 = "%-10sjane." % "hi"
print(str12)

# 소수점 표현하기
str13 = "%0.4f" % 3.141592
print(str13)

# 소수점 표현하기 2
str14 = "%10.4f" % (3.141592 + 3)
print(str14)


# format 함수를 사용한 포매팅 (문자열의 format 함수를 사용하면 좀 더 발전된 스타일로 문자열 포맷을 지정할 수 있다.)
str15 = "I eat {0} apples".format(3)
print(str15)

# 2개 이상의 값을 넣을 경우 문자열의 {0}, {1}과 같은 인덱스 항목이 format 함수의 입력값으로 순서에 맞게 바뀐다.
str16 = "I eat {0} apples{1}".format(3, 4)
print(str16)

# 이름으로 넣기
str17 = "I eat {number1} apples{number2}".format(number1=10, number2=15)
print(str17)

# 인덱스와 이름을 혼용해서 넣기
str18 = "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
print(str18)

# 왼쪽 정렬
str19 = "{number:<10}".format(number="hi")
print(str19)

# 오른쪽 정렬
str20 = "{number:>10}".format(number="hi")
print(str20)

# 가운데 정렬
str21 = "{0:^10}".format("hi")
print(str21)

# 공백 채우기
str22 = "{0:=^10}".format("hi")
print(str22)

str23 = "{0:=>10}".format("hi")
print(str23)

str24 = "{0:=<10}".format("hi")
print(str24)

# 소수점 표현하기
str25 = "{0:0.4f}안녕하세요".format(3.141592 + 3)
print(str25)

str26 = "{0:10.4f}".format(3.141592)
print(str26)

# format 함수를 사용해 문자열 포매팅을 할 경우 { }와 같은 중괄호(brace) 문자를 포매팅 문자가 아닌 문자 그대로 사용하고 싶은 경우에는 위 예의 {{ }}처럼 2개를 연속해서 사용하면 된다.
str27 = "{{ and }}".format()
print(str27)


# f 문자열 포매팅 (파이썬 3.6 버전부터는 f 문자열 포매팅 기능을 사용할 수 있다)
# 다음과 같이 문자열 앞에 f 접두사를 붙이면 f 문자열 포매팅 기능을 사용할 수 있다.
name = "홍길동"
age = 3.1416

# f 문자열 포매팅은 위와 같이 name, age와 같은 변수 값을 생성한 후에 그 값을 참조할 수 있다. 또한 f 문자열 포매팅은 표현식을 지원하기 때문에 다음과 같은 것도 가능하다.
# ※ 표현식이란 문자열 안에서 변수와 +, -와 같은 수식을 함께 사용하는 것을 말한다.
str28 = f"나의 이름은 {name:=^10}입니다.{{ and }} 나이는 {age + 1:0.3f} 입니다."  # name, age와 같은 변수 값을 생성한 후에 그 값을 참조할 수 있다.
print(str28)

# 문자열 관련 함수들
# 문자열 자료형은 자체적으로 함수를 가지고 있다. 이들 함수를 다른 말로 문자열 내장 함수라 한다. 이 내장 함수를 사용하려면 문자열 변수 이름 뒤에 ‘.’를 붙인 다음에 함수 이름을 써주면 된다. 이제 문자열의 내장 함수에 대해서 알아보자

# 문자 개수 세기(count)
a = "hobby"
print(a.count("b"))

# 위치 알려주기1(find)
# 처음으로 나온 위치를 반환한다. 만약 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다.
print(a.find("o"))
print(a.find("j"))

# 문자열 중 문자 t가 맨 처음으로 나온 위치를 반환한다. 만약 찾는 문자나 문자열이 존재하지 않는다면 오류를 발생시킨다. 앞의 find 함수와 다른 점은 문자열 안에 존재하지 않는 문자를 찾으면 오류가 발생한다는 점이다.
print(a.index("o"))
# print(a.index("j"))

# 문자열 삽입(join)
print(",".join(a))

# join 함수는 문자열뿐만 아니라 앞으로 배울 리스트나 튜플도 입력으로 사용할 수 있다(리스트와 튜플은 곧 배울 내용이니 여기에서는 잠시 눈으로만 살펴보자). join 함수의 입력으로 리스트를 사용하는 예는 다음과 같다.
print(",".join(["a", "b", "c"]))

# 소문자를 대문자로 바꾸기(upper)
# >>> a = "hi"
# >>> a.upper()
# 'HI'
# upper 함수는 소문자를 대문자로 바꾸어 준다. 만약 문자열이 이미 대문자라면 아무 변화도 일어나지 않을 것이다.

# 대문자를 소문자로 바꾸기(lower)
# >>> a = "HI"
# >>> a.lower()
# 'hi'
# lower 함수는 대문자를 소문자로 바꾸어 준다.

# 왼쪽 공백 지우기(lstrip)
# >>> a = " hi "
# >>> a.lstrip()
# 'hi '
# 문자열 중 가장 왼쪽에 있는 한 칸 이상의 연속된 공백들을 모두 지운다. lstrip에서 l은 left를 의미한다.

# 오른쪽 공백 지우기(rstrip)
# >>> a= " hi "
# >>> a.rstrip()
# ' hi'
# 문자열 중 가장 오른쪽에 있는 한 칸 이상의 연속된 공백을 모두 지운다. rstrip에서 r는 right를 의미한다.

# 양쪽 공백 지우기(strip)
# >>> a = " hi "
# >>> a.strip()
# 'hi'
# 문자열 양쪽에 있는 한 칸 이상의 연속된 공백을 모두 지운다.

# 문자열 바꾸기(replace)
# >>> a = "Life is too short"
# >>> a.replace("Life", "Your leg")
# 'Your leg is too short'
# replace(바뀌게 될 문자열, 바꿀 문자열)처럼 사용해서 문자열 안의 특정한 값을 다른 값으로 치환해 준다.

# 문자열 나누기(split)
# >>> a = "Life is too short"
# >>> a.split()
# ['Life', 'is', 'too', 'short']
# >>> b = "a:b:c:d"
# >>> b.split(':')
# ['a', 'b', 'c', 'd']
# split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다. 만약 b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다. 이렇게 나눈 값은 리스트에 하나씩 들어가게 된다. ['Life', 'is', 'too', 'short']나 ['a', 'b', 'c', 'd']가 리스트인데 02-3에서 자세히 알아볼 것이니 여기에서는 너무 신경 쓰지 않아도 된다.

# 위에서 소개한 문자열 관련 함수는 문자열 처리에서 사용 빈도가 매우 높고 유용하다. 이 외에도 몇 가지가 더 있지만 자주 사용되지는 않는다.
