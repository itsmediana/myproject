import requests
import pandas as pd
import plotly.express as px

API_URL = "http://127.0.0.1:8000/api/mytable/"  # Локальный адрес API

def get_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except Exception as e:
        print("❌ Ошибка при загрузке данных:", e)
        return pd.DataFrame()

# Загружаем данные
df = get_data()

if df.empty:
    print("⚠️ Нет данных — отчёт не будет создан.")
else:
    print("✅ Данные загружены. Строим график...")

    fig = px.bar(df, x="name", y="age", title="Возраст пользователей")
    fig.write_html("report.html")

    print("📊 Отчёт сохранён: report.html")
