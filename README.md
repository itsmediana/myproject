# myproject

Playwright — это инструмент для автоматического тестирования пользовательского интерфейса (веб-страниц). Мы используем его, чтобы протестировать, что Dash-график действительно отобразился на странице.

Locust — это инструмент для симуляции большого количества пользователей, которые одновременно взаимодействуют с вашим приложением. Это нужно, чтобы проверить, как ваше API выдерживает нагрузку.


Формирование отчета:
- запускаем оба контейнера в фоне docker compose up -d
- docker compose ps проверяем чтобы были в статусе UP
- сохраняем репорт: docker compose exec dash-app python myproject/plotly_report.py

открыть отчет: 
- убедиться что находишься в той папке, где файл : cd /workspaces/myproject
- docker cp myproject-dash-app-1:/app/report.html ./report.html
- python3 -m http.server 8080

коммит: 
- git add report.html myproject/plotly_report.py
- git commit -m "Добавлен статический отчёт Plotly"
- git push

удалить порты:
- удаляем все порты: docker compose down
- запускаем все порты в контейнере докер: docker compose up -d
- смотрим какие порты активны lsof -i :8050
- убиваем порты: kill -9 (номер)

запуск автотеста playwrite: 
- python myproject/test_dash_app.py


почистить память и проверить: 
- docker system prune -a
- df -h проверка сколько осталось

запуск проекта с самого начала после открытия нового codespace: 
- docker compose up -d запуск портов
- docker compose ps проверка что все контейнеры работают UP
- проверить есть ли порты во вкладке ПОРТЫ, если нет, то добавить + порт 8000 и 8050. Всё должно открываться на веб страницах.

перезапуск lowcost:
- docker compose down
- docker compose up --build -d
- docker compose logs locust