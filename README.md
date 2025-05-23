## Установка
```bash
python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

## Запуск программы
```bash
python main.py 
```

## Запуск тестов
После установки зависимостей (и активации виртуального окружения, если вы его создавали):
```bash
pip install -r requirements.txt

pytest -q

python3 -m pytest -q
```

## Статический анализ кода
После установки зависимостей:
```bash
flake8 src tests