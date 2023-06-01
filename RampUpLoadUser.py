
# https://docs.locust.io/en/stable/custom-load-shape.html

import math
from locust import HttpUser,  task, constant
from locust import LoadTestShape

class RampUpLoadUser(HttpUser):
    wait_time = constant(0.5)

    @task
    def hello_world(self):
        # This method will run an HTTP GET request on the path `/`
        self.client.get("/")


class RampUp(LoadTestShape):
    step_duration_seconds = 30
    step_size_users = 10
    user_spawn_rate = 10

    def tick(self):
        run_time = self.get_run_time()

        current_step = math.floor(run_time / self.step_duration_seconds) + 1
        return (current_step * self.step_size_users, self.user_spawn_rate)