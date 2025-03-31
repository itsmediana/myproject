import requests
import pandas as pd
import plotly.express as px
import os

API_URL = "http://django-app:8000/api/mytable/"


def get_data():
    try:
        print(f"🔗 Запрашиваю данные из API: {API_URL}")
        response = requests.get(API_URL)
        print(f"📡 Статус-код ответа: {response.status_code}")
        response.raise_for_status()
        data = response.json()
        if not data:
            print("❌ API вернул пустой список!")
            return pd.DataFrame()
        df = pd.DataFrame(data)
        print(f"✅ Загружено строк: {len(df)}")
        return df
    except Exception as e:
        print(f"⚠️ Ошибка при запросе API: {e}")
        return pd.DataFrame()

# Получаем данные
df = get_data()

# Если не пусто — строим график
if not df.empty:
    fig = px.bar(df, x="name", y="age", title="Возраст пользователей")
    fig.write_html("report.html")
    print("✅ Отчёт сохранён в report.html")
else:
    print("⚠️ Нет данных для отчёта.")
