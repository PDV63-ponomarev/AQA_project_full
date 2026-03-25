## Тесты на TOOLS QA (demoqa.com)

В данном проекте представлены учебные автотесты.
Тесты написанный на **Selene Python**.  
Тесты запускаются через удаленный браузер **Selenoid autotest**.  
Сборка происходит с помощью **[Jenkins](https://jenkins.autotests.cloud/job/001-PDV63-project_full/)** на сайте для демонстраций.  
Отчет демонстрация сформирован в **[Allure](https://jenkins.autotests.cloud/job/001-PDV63-project_full/allure/)**

### Автотесты для сайта **[demoqa.com](https://demoqa.com)**:
<details><summary>1. Elements</summary>

- Text Box:
  - Заполнения формы
- Check box:
  - Раскрытие ветки
  - Отметка чекбоксов
- Radio Button
  - Выбор кнопок
- Web Tables
  - Заполнение формы нового человека
  - Добавление человека в таблицу
  - Проверка работы строки поиска
  - Проверка работы отображения 20 человек
- Buttons
  - Двойной клик
  - Клик правой кнопкой мыши
  - Клик по кнопке с динамическим ID
- Links
  - Открытие новой вкладки по ссылки
  - Открытие новой вкладки по ссылки с текстом
  - Получение статус кодов API
- Dynamic Properties
  - Кнопка становится активной через 5 сек
  - Кнопка меняет цвет через 5 сек
  - Появляется кнопка через 5 сек
  - Комплексная проверка в одном
</details> 

<details>
    <summary>2. Form</summary>

- Practice Form
  - Заполнение полной формы
</details>

<details>
    <summary>3. Alert, Frame & Windows</summary>

- Alerts
     - Уведомление
     - Уведомление через 5 сек
     - Диалог
     - Диалог с полем ввода
</details> 

### Пример allure отчета

<details>
    <summary>Overview</summary>
<img src ="allure/Overview.PNG">
</details> 

<details>
    <summary>Suites</summary>
<img src ="allure/Suites.PNG">
</details> 

<details>
    <summary>Видео выполнения</summary>
    <a href="allure/video.mp4">Скачать или открыть видео выполнения</a>
</details>