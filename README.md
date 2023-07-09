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
$ django-admin startproject jangoproject
$ python manage.py runserver
$ python manage.py migrate
$ python manage.py startapp home
$ python manage.py startapp file
$ python manage.py startapp user
```

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
|2023.05.18 | Djagno 설치 및 프로젝트, 앱(home, file) 생성 |
|2023.05.20 | 업로드 파일 정보 모델에 저장 후 결과 페이지 출력 |
|2023.05.25 | 로그인, 회원가입 UI 구현 / yunju+jiyun branch merge |
|2023.05.26 | DB Mysql과 연동 |
|2023.05.29 | 로그인 사용자 정보 및 업로드 파일 리스트 출력 |
|2023.06.01 | 페이징 기능 구현 |
|2023.06.06 | yunju+jiyun+seonyoung branch merge |

## 화면 구성 📺
| 로그인 페이지 | 회원가입 페이지 |
| ------------ | ---------------- |

| 메인 페이지 | 검사결과 페이지 |
| ------------ | ---------------- |
