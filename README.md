# autotest_for_transtelematika

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
python -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```sh
pip install -r requirements.txt
```

```
Запустить тесты:
```sh

pytest step_defs/main.py
```