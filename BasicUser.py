# Imports classes from Locust
from locust import HttpUser, task, between

class BasicUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/")

    wait_time = between(0.5, 1)  # wait between 0.5 and 1 seconds between requests, randomly distributed
