
make install:
	pip install -r requirements.txt

make run:
	python manage.py runserver

make test:
	python manage.py test