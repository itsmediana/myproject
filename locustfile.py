from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def load_api_data(self):
        # Используем внутренний адрес Django-приложения
        self.client.get("/api/mytable/")
        
        # ИЛИ если нужны разные эндпоинты:
        # self.client.get("/api/other_endpoint/")