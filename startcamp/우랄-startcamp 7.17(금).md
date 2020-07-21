# 파이썬

> 금일 수업내용
>
> 파이썬에서 . 의 의미는 파일 밑에 파일을 얘기해준다.
>
> ex) start.camp는 start안에 있는 camp파일을 지정하는 것임.

## 1. 파이썬 설명 및 코드

### 1.1 파이썬 터미널에서 실행방법

- 터미널 키는법 : `ctrl` + `~` 누르면 나옴 
- 혹은 위의 탭에서 veiw -> terminal클릭 
- python `파일명` + tab 하면 자동완성 + `enter` 하면 만들어논 코드 실행



### 1.2 코딩문제

#### 1) problem 1

> 치구 두 명과 영화를 보러 갔는데, 영화관에서 셋 중 한명에게 무료 티켓을 증정하는 이벤트가 열렸습니다. 친구와 나 세명 중 랜덤으로 한 명을 뽑고, 만약 걸린 사람이 나 이면 개이득! 이라고 출력하는 프로그램을 만드세요.

#### 2) problem 2

> 로또 번호를 추첨하였을 때, 추첨된 숫자 중에 7이 포함되어 있다면 럭키!를 출력하는 프로그램을 만드세요.

#### 3) 제출방법

- DM으로 코드블락을 통해 코드 제출
- 프로그래밍 경험
- 스타트캠프에서 어려웠던 점(있다면)

#### 4) problem 1 정답

```python
import random #random 불러오기

friends = ['현우','봉현','병훈']
choice = random.choice(friends) #friends리스트중 랜덤으로 하나 뽑아서 choice에 넣기
print(choice)

if choice == '현우' :
    print('개이득')
```



#### 4) problem 2 정답

```python
import random
#numbers = range(1,46)
#lucky = random.sample(numbers,6)
numbers = random.sample(range(1,46),6)
print(numbers)

for number in numbers:
    if number == 7:
        print('럭키!')
```



### 1.3 코스피 코딩

> 브라우저는 요청과 응답이다.

#### 1) 파이썬에서 브라우저 정보 요청하는 법

- 필요한 모듈 불러오기(requests, bs4)
- 필요한 브라우저 정보가 나와있는 url 복사
- url에 담기
- 모듈로 요청을 보내기
- 응답을 받기
- text로 나와있는 정보들을 bs4모듈로 데이터를 정리하여 가져오기
- 필요한 정보에서 마우스 우클릭 -> 검사 -> 정보를 우클릭 -> copy -> copy selector
  - select에 데이터 할당하기
- 출력하기

```python
import requests #필요한 모듈 불러오기
import bs4 #필요한 모듈 불러오기 (정보를 정리해주는 역할을 하게 될 예정)

url = 'https://finance.naver.com/sise/'
requests.get(url) #모듈로 요청 보내기
response = requests.get(url).text #응답을 받기, 텍스트로 해당 브라우저의 모든 정보를 받게 됨.

data = bs4.BeautifulSoup(response, 'html.parser') # bs4안에 있는 뷰티풀숩은 html의 문법에 기반하여 분석을 해주고 난 뒤 data에 할당하겠다.
select = data.select_one('#KOSPI_now') 
print(select.text) #.text는 필요한 내용의 text를 출력해줌
```



### 1.4 날씨 코딩

> https://openweathermap.org/current#name
>
> API : 인터페이스 중 하나

- 필요한 모듈 불러오기
- 요청 url 만들기
- API이기 때문에 로그인하고 발급받은 api KEY가 필요함!
- 필요한 데이터 꺼내기
- 꺼낸 데이터 값을 기준으로 상태 정보를 출력하기

```python
import requests # 요청 모듈
#url = 'https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}'
key = 'asdasdasd'
url = 'https://api.openweathermap.org/data/2.5/weather?q=Daejeon&appid='
                 #오픈웨더에서 준 데이터를 바탕으로 우리는 대전의 데이터를 쓰겠다.
#url = f'https://api.openweathermap.org/data/2.5/weather?q=Daejeon&appid={key}' 원래 url = url + key형태이지만 f스트링으로 한번에 쓸수 있음.
response = requests.get(url).json() #json파일 형태로 응답을 받기
print(response['base'])# base에 해당하는 값을 출력해라! 딕셔너리에 있는 값을 출력할 때는 대[]로 묶어주기
weather = response['weather'][0]['main']
temp = round(response['main']['temp']-273.15)# round : 소수점 버리기
temp_max = round(response['main']['temp_max']-273.15)
temp_min = round(response['main']['temp_min']-273.15)
print(f'대전의 오늘 날씨는 {weather}이며, 기온은 {temp}도 입니다.')
print(f'대전의 최고기온은 {temp_max}도 이며, 최저기온은{temp_min}도 입니다.')
```



### 1.5 에러코드

- AttributeError : 속성오류
  - ex) [AttributeError] 'Response' object has no attribute 'jason'
  - response 안에 jason이란 애가 없다. 즉 선언(저장)을 안했거나, 오타일 가능성이 다분하다.