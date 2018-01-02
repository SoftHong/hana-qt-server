## 가상 서버 설정
```
# 실행
source myvenv/bin/activate

# 종료
deactivate
```

## 설치
```
pip install django
pip install django-rest-framework
pip install django-rest-swagger
```

## 서버 실행
```
python manage.py runserver
```

## Model 수정 후
```
python manage.py makemigrations
python manage.py migrate
```

## https
https://blog.elpo.net/get-free-ssl-certificate/
```
cd /root
git clone https://github.com/letsencrypt/letsencrypt
cd letsencrypt
./letsencrypt-auto certonly
```

## Custom profile model
https://simpleisbetterthancomplex.com/tutorial/2016/11/23/how-to-add-user-profile-to-django-admin.html
http://deathofagremmie.com/2014/05/24/retiring-get-profile-and-auth-profile-module/

## 관리자 페이지 세팅
https://wayhome25.github.io/django/2017/03/22/django-ep8-django-admin/

## 서버 시간 설정
```
$ tzselect
```
