import dash
from dash import dcc, html
import requests
import pandas as pd

# URL API
API_URL = "http://127.0.0.1:8000/api/mytable/"

# Функция загрузки данных
def get_data():
    try:
        print(f"🔗 Запрашиваю данные из API: {API_URL}")
        response = requests.get(API_URL)
        print(f"📡 Статус-код ответа: {response.status_code}")

        if response.status_code == 200:
            try:
                data = response.json()
                if not data:
                    print("API вернул пустой список!")
                    return pd.DataFrame()

                # Проверяем структуру данных
                df = pd.DataFrame(data)
                print(f"Данные из API:\n{df.head()}")

                # Проверяем, есть ли нужные колонки
                if "name" not in df.columns or "age" not in df.columns:
                    print("Ошибка: Отсутствуют колонки 'name' или 'age'. API даёт:", df.columns)
                    return pd.DataFrame()

                return df
            except ValueError:
                print(" Ошибка: API вернул не JSON-ответ!")
                print(response.text)  # Выведет HTML-ошибку, если API сломан
                return pd.DataFrame()
        else:
            print(f" Ошибка {response.status_code}: {response.text}")
            return pd.DataFrame()
    except Exception as e:
        print(f" Ошибка при запросе API: {e}")
        return pd.DataFrame()

# Загружаем данные
df = get_data()
print(df)

# Проверка данных
if df.empty:
    print("данные не загружены!")

# Создаём Dash приложение
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1("График пользователей", style={'textAlign': 'center'}),
    dcc.Graph(
        id="user-age-graph",
        figure={
            "data": [
                {
                    "x": df["name"] if "name" in df else [],  
                    "y": df["age"] if "age" in df else [],
                    "type": "bar",
                    "marker": {"color": "blue"},
                }
            ],
            "layout": {"title": "Возраст пользователей"}
        }
    )
])

# Запускаем сервер Dash
if __name__ == "__main__":
    app.run_server(debug=True, port=8050)
