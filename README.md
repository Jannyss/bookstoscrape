### Проект, парсящий сайт http://books.toscrape.com/ и печатающий названия всех книг, находящихся на сайте.

#### Инструкция по запуску:

Для корректного запуска программы необходимо скачать все файлы с репозитория и сохранить на локальный диск. Открыть командную строку(терминал) и перейти в каталог с файлами. Все зависимости, необходимые проекту, можно установить командой:

`pip install -r requirements.txt`

Затем необходимо запустить самого бота командой:

`scrapy crawl bookspider `

После её выполнения в корне каталога появится файл books.txt, строки которого являются названиями книг.

Или же можно выполнить команду:

`scrapy crawl bookspider -о books.json -t json`

В этом случае помимо создания файла books.txt, в корне каталога появится также файл books.json с аналогичной информацией.
books.json имеет формат:

```
[
{'name': Название_книги1},
{'name': Название_книги2},
...
]
```
