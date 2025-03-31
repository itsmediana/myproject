from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def load_api_data(self):
        self.client.get("https://shiny-tribble-7vpx7w6qv4942gvg-8000.app.github.dev/api/mytable/")
