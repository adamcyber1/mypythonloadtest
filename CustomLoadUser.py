from locust import HttpUser, task, constant
from locust import LoadTestShape


class CustomLoadUser(HttpUser):
    wait_time = constant(1)

    @task
    def hello_world(self):
        # This method will run an HTTP GET request on the path `/`
        self.client.get("/")


class PeakLoad(LoadTestShape):
    steps = [
        {"duration": 60, "users": 10, "spawn_rate": 1},
        {"duration": 120, "users": 20, "spawn_rate": 1},
        {"duration": 180, "users": 40, "spawn_rate": 1},
        {"duration": 240, "users": 80, "spawn_rate": 1},
        {"duration": 300, "users": 120, "spawn_rate": 1},
        {"duration": 360, "users": 80, "spawn_rate": 1},
        {"duration": 420, "users": 40, "spawn_rate": 1},
        {"duration": 480, "users": 20, "spawn_rate": 1},
        {"duration": 540, "users": 10, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for step in self.steps:
            if run_time < step["duration"]:
                tick = (step["users"], step["spawn_rate"])
                return tick

        return None
