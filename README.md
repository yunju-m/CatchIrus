# CatchIrus 🐈
**강원대학교 컴퓨터공학과 캡스톤 프로젝트** <br/>
**개발기간: 2023.06 ~ 2023.**

## 프로젝트 소개

CatchIrus는 Catch + Virus의 축약어로 바이러스를 잡는 사이트를 의미합니다. 
어떠한 임의의 파일을 업로드하면 해당 파일에 대해 바이러스가 존재하는지 판단하여 사용자에게 알려줍니다. 

## 개발자 소개
| 마윤주 | 장선영 | 설지윤 |
| :----: | :----: | :----: |
| 강원대학교 컴퓨터공학과 4학년 | 강원대학교 컴퓨터공학과 4학년 | 강원대학교 컴퓨터공학과 4학년 |

## 시작 가이드

### Requirements

For building and running the application you need:

- [python 3.9.13](https://www.python.org/downloads/)
- [Django 4.2.2](https://docs.djangoproject.com/ko/4.2/intro/install/)
- [Pycharm](https://www.jetbrains.com/ko-kr/pycharm/download/#section=windows)
- [VisualStudioCode](https://code.visualstudio.com/download)

### git connection

```bash
$ git clone https://github.com/yunju-m/CatchIrus.git
$ cd .
```

### venv 가상환경

#### 가상환경 설치 및 시작

```
$ python -m venv venv
$ venv\Scripts\activate.bat
```

#### 가상환경 종료

```
$ deactivate
```

### django 개발환경

```
$ pip install django
$ pip list
$ django-admin startproject djangoproject
$ python manage.py runserver
$ python manage.py migrate
$ python manage.py startapp home
$ python manage.py startapp file
$ python manage.py startapp user
```
### model 변경 시 makemigrations, migrate

1. django에게 변경사항을 알려주는 작업

```bash
$ python manage.py makemigrations
```

2. 변경사항을 데이터베이스에 적용

```bash
$ python manage.py migrate
```

 ### maraidb 테이블 생성 후 저장
 - 기존 db 오류 발생 시 : **초기화 작업** 필요
```shell
$ python manage.py migrate --fake home(app이름) zero
$ python manage.py migrate home(app이름)
```
- mariaDB의 table 삭제 시 makemigraions, migrate을 통해 재생성⭕
- 조건1: 기존 table 모두 삭제한 후 전체 생성해야함.
- 조건2: migrations 파일의 내역 존재❌

### 새로운 앱 프로젝트 setting

```
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "home",
    "file",
    "user",
]
```

### django super사용자 생성
```shell
$ python manage.py createsuperuser
$ username: yunju
$ Email address: yunju@django.com
$ Password:
$ Password (again): 
Superuser created successfully
``` 

### Beautifulsoup4 설치
```shell
$ pip install beautifulsoup4
```


## Stacks ⭐

### Environment

![Visual Studio Code](https://img.shields.io/badge/VisualStudioCode-007ACC?style=for-the-badge&logo=VisualStudioCode&logoColor=white)
![Pycharm](https://img.shields.io/badge/Pycharm-000000?style=for-the-badge&logo=Pycharm&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)

### Development

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)
![Html](https://img.shields.io/badge/Html-E34F26?style=for-the-badge&logo=Html5&logoColor=white)
![Css](https://img.shields.io/badge/Css-1572B6?style=for-the-badge&logo=Css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=Javascript&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=Bootstrap&logoColor=white)
![JQuery](https://img.shields.io/badge/JQuery-0769AD?style=for-the-badge&logo=jQuery&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=MariaDB&logoColor=white)

## 프로젝트 진행 상황

| 날짜 |                            내용                             |
| --------- | ----------------------------------------------------------- |
|2023.05.16 | 메인, 결과 페이지 UI 구현 |
|2023.05.18 | Djagno 설치 및 프로젝트, 앱(home, common) 생성 |
|2023.05.20 | 업로드 파일 정보 모델에 저장 후 결과 페이지 출력 |
|2023.05.25 | 로그인, 회원가입 UI 구현 / yunju+jiyun branch merge |
|2023.05.26 | DB MariaDB와 연동 |
|2023.05.29 | 로그인 사용자 정보 및 업로드 파일 리스트 출력 |
|2023.06.01 | 페이징 기능 구현 |
|2023.06.06 | yunju+jiyun+seonyoung branch merge |
|2023.07.09 | djangoproject 전체 구조 수정 및 .gitignore 추가 |
|2023.07.09 | 가상환경 venv 변경 |
|2023.07.09 | 회원가입 후 자동 로그인 문제 해결 |
|2023.07.09 | 업로드 파일 저장 경로 변경 |
|2023.07.15 | CatchIrus API 명세서 작성 - notion |
|2023.07.20 | 파일별 업로드 회원 정보 출력 |

## 화면 구성 📺
| 로그인 페이지 | 회원가입 페이지 |
| ------------ | ---------------- |

| 메인 페이지 | 검사결과 페이지 |
| ------------ | ---------------- |

## Data API Document 
<div align="center">
<img alt="dataApi" src="/static/img/DataApi.png">