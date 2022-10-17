autotest_for_transtelematika
# Тестирование Яндекс.Маркета с помощью Selenuim и Pytest-bdd

#Технологии:
- Python 3.8
- pytest
- pytest-bdd
- selenium

## _Как запустить проект:_
Клонировать репозиторий и перейти в него в командной строке:
```sh
git clone https://github.com/redbull7214/autotest_for_transtelematika.git
cd autotest_for_transtelematika

```
Cоздать и активировать виртуальное окружение:
```sh
python -m venv venv
source venv/Scripts/activate 
```
Установить зависимости из файла requirements.txt и обновить pip:
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```


Запустить тесты:
```sh

pytest step_defs/main.py
```
