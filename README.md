# welcome fanatics
Краткое введение во все инструменты, что будут использоваться при работе над проектом

## venv
Обязательно используйте виртуальное окружение при работе над проектом
```bash
python3 -m venv .venv #если окружение еще не создано
source .venv/bin/activate #Unix
.venv/Scripts/activate.bat #Windows
```

## [requirements.txt](requirements.txt)
Файл, в котором  хранится информация о **всех** используемых *сторонних* библиотеках

Установка:
```bash
pip install -r requirements.txt
```
Пожалуйста, **не забывайте** поддерживать файл актуальным, если добавляете новые библиотеки

## .gitignore
Файл с указанием файлов, которые не стоит коммитить

Наличие [.gitignore](.gitignore) в коммите **ОБЯЗАТЕЛЬНО**
## pyray 3d
Примеры использование находятся в: [basic3d.py](3d-examples/basic3d.py);  **внимательно** изучите, если какая то часть кода непонятна, спрашивайте
## pre-commit
### ОБЯЗАТЕЛЬНЫЙ ИНСТРУМЕНТ В РАБОТЕ
Утилита, запускаяющая определенные хуки, такие как линтер и форматтер кода, перед совершением коммита

Устанавливается посредством [requirements.txt](requirements.txt) и команды:
```bash
pre-commit install
```

### [.pre-commit-config.yaml](.pre-commit-config.yaml)
Файл с настройками pre-commit. Все уже настроено, его наличие **ОБЯЗАТЕЛЬНО** в коммите(в таком же виде, какой прикреилен здесь)
#### ruff
Линтер и форматер кода
```bash
ruff check #проверка кода
ruff --fix #проверка и исправление
```
#### black
Продвинутый форматтер кода
```bash
black .
```
#### pyupgrade
Автоматическая проверка синтаксиса

#### Все вышеуказанные хуки запускаются автоматически *перед совершением коммита*, необходимо только убедиться в правильной установке pre-commit
