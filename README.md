**Installation**

1. Install python 3.8
2. Install packages from requirements.txt
3. Install allure https://docs.qameta.io/allure/#_installing_a_commandline


**Running tests**

1. Run in default browser pytest -m ui
2. Run in custom browser pytest -m ui --browser=firefox
3. Run tests and generate allure report pytest --alluredir={directory}
4. View allure report allure serve {directory}
