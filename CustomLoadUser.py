from locust import HttpUser, task, constant
from locust import LoadTestShape


class CustomLoadUser(HttpUser):
    wait_time = constant(1)

    @task
    def hello_world(self):
        # This method will run an HTTP GET request on the path `/`
        self.client.get("/")


# the user doesn't change, just the LoadTestShape

class PeakLoad(LoadTestShape):
    steps = [
        {"start_time": 60, "users": 10, "spawn_rate": 2},
        {"start_time": 120, "users": 20, "spawn_rate": 2},
        {"start_time": 180, "users": 60, "spawn_rate": 2},
        {"start_time": 240, "users": 90, "spawn_rate": 2},
        {"start_time": 300, "users": 150, "spawn_rate": 2},
        {"start_time": 360, "users": 200, "spawn_rate": 2},
        {"start_time": 420, "users": 150, "spawn_rate": 2},
        {"start_time": 480, "users": 80, "spawn_rate": 2},
        {"start_time": 540, "users": 40, "spawn_rate": 2},
        {"start_time": 600, "users": 20, "spawn_rate": 2},
        {"start_time": 660, "users": 10, "spawn_rate": 2}
    ]

    def tick(self):
        run_time = self.get_run_time()

        for step in self.steps:
            if run_time < step["start_time"]:
                tick = (step["users"], step["spawn_rate"])
                return tick

        return None
