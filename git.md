# Git

> Git은 분산버전관리시스템이다.

## 준비하기

윈도우에서 git을 활용하기 위해서 [git bash](https://gitforwindows.org/)를 설치합니다.

초기 설치를 완료한 이후에, 계정설정을 진행합니다.

```sh
$ git config --global user.email {이메일주소}
$ git config --global user.name {유저네임}

```



## 로컬 저장소 활용하기

### 1. 저장소 초기화

> 이제부터 이 디렉토리를 git으로 관리하겠다.(변경 이력을 감시하겠다.)

```sh
$ git init
```

- `.git` 디렉토리가 생성되며, 여기에 git과 관련된 모든 정보가 저장됩니다.
- 초기화를 하고나면 git bash에 `(master)` 라고 표시가 되는데, 이는 이 디렉토리는 이미 git이 관리하고 있다는 뜻으로 생각할 수 있습니다.
- 이미 초기화한 repo에서는 다시 `git init`을 하지 않습니다.

### 2.add

> working directory 작업공간에서 변경된 사항을 이력으로 관리하기 위해서는 반드시 staging area를 거쳐야 한다.

```sh
$ git add {staging 할 파일}
$ git add . 은 디렉토리에 있는 모든파일 올리기gi
```

### 3.Commit

> 이력을 확정짓는, 즉 기록을 남기는 명령어이다.

```sh
$ git commit -m '커밋 메세지'
```

커밋 기록을 확인하고 싶다면 아래의 명령어를 참고하세요.

```sh
$ git log
```

### 4.Status

> git을 쓰면서 가장 많이 사용해야 하는 명령어. 현재 상황을 확인할 수 있다.

```sh
$ git status
```

- 빨간색 스테이지에 아직 올라가지않은 녀석들

- 초록색 스테이지에 올라간 녀석들

## 원격 저장소 활용하기

여러 서비스중, github을 기준으로 설명합니다.

### 1. 준비사항

- github에 회원가입 후, 빈 reep를 만들어 준다.

### 2. 원격 저장소 등록

- 로컬저장소와 원격 저장소를 연결하는 일입니다.

```sh
$ git remote add origin {github repo url}
```

- 원격 저장소(remote)를 등록할건데, `origin` 라는 이름으로 원격 저장소를 등록하겠다라는 의미입니다.
- 원격 저장소 등록 현황을 확인하려면 아래의 명령어를 참고하세요.
- 깃프로그램아 원격 저장소기능 추가기능 별명은 origin 실제주소는 ~~~야

```sh
$ git remote -V
```

- 등록된 원격 저장소를 삭제하려면 아래의 명령어를 참고하세요

```sh
$ git remote rm { 삭제하고자 하는 remote name }
```





```sh
$ git push origin master
```

- master는 우리가 올린 commit들의 기록들

```sh
$ git pull origin master
```

- 를통해 집과 강의장에서 최신화를 하여 순서가 헤깔리지 않게한다.





# 0724 새로운 교수님

## Git

- working dir
  - 실제 작업공간
- staging area
  - add 명령어를 입력했을 때 임시로 저장이 되는 공간
- local repo(.git)
  - commit 명령어를 입력했을때 버전이 기록되는 공간

## 명령어

- `git init` 
  - `.git` 폴더를 만들어 주는 명령어
  - 최초 한번만 실행한다.
- `git add` 
  - 뒤에 staging area로 올리고 싶은 파일을 적어준다.
  - `.` 을 입력하면 전체 파일이 추가된다.
- `git commit` 
  - 버전을 생성
  - `-m` 옵션을 일반적으로 추가해준다.



- `git remote add` 
  - 원격 저장소의 주소를 등록
  - origin 이라는 이름을 기본값으로 사용.
  - `최초 한번` 만 실행한다.
- git push
  - 등록된 원격 저장소로 커밋 기록을 업로드
- git diff
  - 머가 바뀐지 나옴
  - 삭제가 된줄은 빨간색 추가가된줄은 초록색
- git commit --amend
  - 오타같은거 했을때 마지막 commit수정

### 0731

- 버전관리
  - add
  - commit
  - push
  - 
- 상태확인
  - status
  - log
  - diff
- 되돌리기
  - restore
  - --amend

### gitignore.io

- git은결국 우리 파일, 버전을 관리하고 확인하는 것
- 이거는 git으로 관리안해도 될꺼같다 에 사용
- 

### 0928

1. venv/ add commit

-> .git 폴더 기록

컴퓨터에서는 삭제안하고 

git한테는 삭제한척

git rm --cached <해당파일>

git commit

-> git 한테는 venv는 없는 파일(.gitignore에도 포함되어 있고, 지금 내가 갖고있는 애도 삭제했으니까)

venv 무슨 업데이트? -> git X .gitignore 포함되어있으니까

2. 위에꺼 시르면 git 폴더를 삭제한다음에 다시 gitinit하면된다.

