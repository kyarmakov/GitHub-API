Автоматический тест для проверки работы GitHub API на языке Python. Тест умеет создавать, проверять наличие и удалять репозиторий на GitHub.

Для запуска теста на Вашем компьютере должен быть установлен git, Python версии не ниже 3.4 и менеджер пакетов pip.
Чтобы убедиться, что Python установлен на Вашем компьютере, Вы можете выполнить команду ```python --version``` для Windows и ```python3 --version``` для Linux и Mac.

Также Вам нужно сгенерировать API token на [Github](https://github.com/settings/tokens/new). В Select scopes проставьте все галочки.

Порядок запуска:
1) Открыть консоль (командную строку на Windows) и клонировать проект ```git clone https://github.com/kyarmakov/GithubAPI.git```
2) Перейти в папку проекта ```cd GithubAPI```
3) Создать виртуальное окружение для избежания конфликтов версий ```python -m venv myvenv``` для Windows и ```python3 -m venv myvenv``` для Linux и Mac.
   Python 3 обычно уже включает модуль `venv`, который позволяет создавать виртуальные окружения. Если по какой-то причине он не установлен, Вы можете установить Python, содержащий `venv`, через пакетный менеджер:
   ```sudo apt-get update``` и ```sudo apt install python3-venv``` для Ubuntu/Debian.

4) Активировать виртуальное окружение. Для Windows ```myvenv\Scripts\activate``` . Для Linux/Mac ```source myvenv/bin/activate```
5) В файле .env заполнить переменные окружения USER_NAME (имя пользователя GitHub), REPO_NAME (имя репозитория) и API_TOKEN (сгенерированный ранее токен API)
6) Выполнить команду ```pip install -r requirements.txt``` для установки зависимостей.
7) Выполнить команду ```pytest```
