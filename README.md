# test_project
M3 test project
Чтобы развернуть проект, необходимо выполнить следующие действия:
Развернуть виртуальное окружение, активировать его и выполнить команды:
  1. python setup.py sdist --formats=gztar --dist-dir  .
  2. pip install . --extra-index-url http://pypi.bars-open.ru/simple/ --trusted-host pypi.bars-open.ru
  3. python manage.py makemigrations app
  4. python manage.py migrate
  5. python manage.py runserver 
