# Imports classes from Locust
from locust import HttpUser, task, between

class BasicUser(HttpUser):
    @task
    def hello_world(self):
        # This method will run an HTTP GET request on the path `/`
        self.client.get("/")

    # to rate control a user, introduce wait times - https://docs.locust.io/en/stable/writing-a-locustfile.html#wait-time-attribute
    wait_time = between(0.5, 1) # wait between 0.5 and 1 seconds between requests, randomly distributed