## Оглавление
1. Сборка проекта и локальный запуск
    * Клонируем репозиторий
    * Настройка
    * Запуск
    * Открытие OpenApi(swager)
    * Пример запуска
2. Запуск тестов


___

## Сборка проекта и локальный запуск:
### Клонируем репозиторий
Выполните в консоли

`git clone https://github.com/Madixxx22/statics_counter.git`

### Настройка
Создайте .env файл в том же каталоге что и docker-compose.yaml, и добавьте следующие параметры
```
DB_USER
DB_HOST
DB_PASSWORD
DB_NAME

POSTGRES_USER
POSTGRES_DB
POSTGRES_PASSWORD

PGADMIN_DEFAULT_EMAIL
PGADMIN_DEFAULT_PASSWORD
PGADMIN_CONFIG_SERVER_MODE
```
### Запуск
Установите docker desktop с оффициального сайта и запустите(если на windows или macos)
https://eternalhost.net/base/vps-vds/ustanovka-docker-linux (Воспользуйтесь инструкцией для Linux)

В консоле находясь в каталоге с файлом docker-compose.yaml запускаем команду
`docker-compose up` 
Если все было установлено и настроено корректно приложения запустится, кроме back end(http://127.0.0.1:8008) развернется postgresql и pgadmin(http://127.0.0.1:5050)

### Открытие OpenApi(swager)
Перейдя по ссылке http://127.0.0.1:8008/docs мы откроем автоматически сгенерированную документацию openapi swager
____
### Пример запуска
### Метод сохранения статистики.

Post запрос принимающий на вход дату в формате YYYY-MM-DD, неотрицательные views, clicks, cost. Сохраняет в БД запись и высчитывая cpm, cpc
![](https://github.com/Madixxx22/statics_counter/blob/master/img/photo_2022-05-16_16-52-55.jpg)
 ____
 
### Метод просмотра статистики.

Get запрос принимает на вход даты просмотра от и до. named_column_sorted поле перечисления полей, для вторичной сортировки по столбцу выходных данных кроме даты.
Чтобы сортировки по доп столбцу не происходило выберите пустой пункт. sorting_from_last bool поле если true то сортировка оп дате производится в порядке от самой новой записи к старой, если false то от самой старой к самой новой в выбранном диапозоне.

 ![](https://github.com/Madixxx22/statics_counter/blob/master/img/photo_2022-05-16_16-53-09.jpg)
 ![](https://github.com/Madixxx22/statics_counter/blob/master/img/photo_2022-05-16_16-53-15.jpg)
 
 ____
 ### Метод очистки статистики
 Delete метод удаляющий всю статистику из БД
 ![](https://github.com/Madixxx22/statics_counter/blob/master/img/photo_2022-05-16_16-53-18.jpg)
 ![](https://github.com/Madixxx22/statics_counter/blob/master/img/photo_2022-05-16_16-54-25.jpg)

## Запуск тестов
Тесты можно запустить и проверить работоспособность программы при запущенных docker контейнерах. Т.к нет тестовой БД тесты выполняются в основной. и 3 тест Очищает всю БД.
`docker-compose exec app python -m pytest app/tests`

Если обновляете БД проведите миграции с помощью *alembic* при запущенном контейнере. Обновление миграции произведите или перезапустив контейнер или вручную `alembic upgrade head` 
