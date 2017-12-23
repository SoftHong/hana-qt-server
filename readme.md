## 가상 서버 설정
```
# 실행
source myvenv/bin/activate

# 종료
deactivate
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
