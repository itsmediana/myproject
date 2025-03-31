import dash
from dash import dcc, html
import requests
import pandas as pd
import os

# Получаем URL API из переменной окружения или по умолчанию
API_URL = os.getenv("API_URL", "http://localhost:8000/api/mytable/")

# Загрузка данных
def get_data():
    try:
        print(f"🔗 Запрашиваю данные из API: {API_URL}")
        response = requests.get(API_URL, verify=False)
        print(f"📡 Статус-код ответа: {response.status_code}")
        response.raise_for_status()

        try:
            data = response.json()
        except Exception as parse_err:
            print("❌ Ошибка парсинга JSON:", parse_err)
            print("🔴 Текст ответа:", response.text[:300])
            return pd.DataFrame()

        if not data:
            print("❌ API вернул пустой список!")
            return pd.DataFrame()

        df = pd.DataFrame(data)
        print(f"🟢 Загружено строк: {len(df)}")
        print(df.head())
        return df

    except Exception as e:
        print(f"⚠️ Ошибка при запросе API: {e}")
        return pd.DataFrame()

# Загружаем данные
df = get_data()

if df.empty:
    print("⚠️ Данные не загружены! Пустой график.")

# Инициализация Dash
app = dash.Dash(__name__)

# Макет
app.layout = html.Div(children=[
    html.H1("График пользователей", style={'textAlign': 'center'}),
    dcc.Graph(
        id="user-age-graph",
        figure={
            "data": [
                {
                    "x": df.get("name", pd.Series()),
                    "y": df.get("age", pd.Series()),
                    "type": "bar",
                    "marker": {"color": "blue"},
                }
            ],
            "layout": {"title": "Возраст пользователей"}
        }
    )
])

# Запуск
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=True)
