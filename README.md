# booking-system
테니스 레슨 예약시스템

## 1. 프로젝트 목표 및 범위
레슨 예약 시스템으로 관리자와 회원을 타겟 사용자로 하여 권한 및 역할을 설정하였습니다.
테니스 클럽을 중점에 두고 만들었으나 요가 스튜디오나 회의실 예약 등으로 변경 가능합니다.  

## 2. 기술 스택 및 개발 환경
Django, Html, CSS


## 3. 레포 및 배포
repo : https://github.com/helloghostt/booking-system<br>
url : 

    superuser
    username : admin-park
    password : park1234!

## 4. WBS 작성 - 업무 분류 체계

```mermaid
gantt
title booking-system
dateFormat YY-MM-DD

section 기획
리포지토리 생성 :2024-03-29, 1d
프로젝트 아이디어 기획 :2024-03-29, 2d
프로젝트 아이디어 수정 :2024-03-31, 2d

section 설계
와이어프레임 작성 :2024-04-01, 2d
ERD 작성 :2024-04-01, 2d
데이터베이스 설계 : 2024-04-01, 3d
UI/UX 설계 : 2024-04-04, 5d

section 개발
모델 구현 :2024-04-04, 5d
CRUD 구현 :2024-04-05, 5d
인증 구현 :2024-04-06, 5d
코드 개선 :2024-04-08, 7d
버그 수정 :2024-04-10, 6d

section 배포
테스트 :2024-04-15, 2d
문서 수정 :2024-04-16, 2d
배포 및 프로젝트 완료 :2024-04-17, 1d
```

## 5. 와이어프레임 작성





## 6. ERD 작성
 <img src="erd.png" alt="alt text" width="400">

## 7. 폴더구조
    django
    ├── tennisproject
    ├── accounts
    ├── courts
    ├── bookings
    ├── notices
    ├── templates
    │   ├── accounts
    │   ├── bookings
    │   └── notices
    ├── media
    └── static

## 8. URL 구조 및 페이지별 상세

|URL|페이지 설명|GET|POST|PUT|DELETE|로그인 권한|작성자 권한|
|------|---|:---:|:---:|:---:|:---:|:---:|:---:|
|/accounts/login|로그인| |✔️| | | | |
|/accounts/logout|로그아웃| |✔️| | |✔️| |
|/accounts/signup|회원가입| |✔️| | | | |
|/accounts/profile|프로필 조회<br>비밀번호 변경<br>회원 탈퇴|✔️<br><br><br>| |✔️|<br><br>✔️|✔️<br>✔️<br>✔️|<br>✔️<br>✔️|
|/bookings|예약 목록<br>예약 생성|✔️<br><br>|<br>✔️| | |✔️<br>✔️| |
|/bookings/{bookingId}|예약 상세|✔️| | | |✔️|✔️|
|/courts|코트 목록|✔️| | | | | |
|/courts/{courtId}|코트 상세|✔️| | | | | |
|/notices|공지사항 목록<br>공지사항 생성|✔️<br><br>|<br>✔️| | |<br>✔️|<br>✔️|
|/notices/{noticeId}|공지사항 상세<br>공지사항 수정<br>공지사항 삭제|✔️<br><br><br>| |✔️|<br><br>✔️|<br>✔️<br>✔️|<br>✔️<br>✔️|


    1. 메인 페이지 구현
        - url : `/`
        - 클럽 소개, 공지사항, 입장하기 버튼
    2. Django admin
        - url : `/admin`
        - 코트별 시간대 설정, 회원 관리
    3. 회원가입 페이지
        - url : `/accounts/signup`
        - 입력값은 id, password
    4. 로그인 페이지
        - url : `/accounts/login`
        - 입력값은 id, password
    5. 프로필 페이지
        - url : `/accounts/profile`
        - password 변경 기능, 예약 확인 기능
    6. 클럽 소개 페이지
        - url: `/intro`
        - 클럽에 대한 간단한 소개와 주소
        - 연락처에는 이메일 보내기 기능
    7. 예약 페이지
        - url : `/bookings/create`
        - 날짜 선택하고 시간에 따른 클래스 선택
    8. 공지사항 게시판
        - url : `/notices`
        - 관리자만 이벤트 등의 글을 작성, 수정, 삭제
        - 회원은 글을 읽기만 가능

## 9. 느낀 점

## 10. 트러블슈팅


