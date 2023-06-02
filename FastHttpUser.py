from locust import task, FastHttpUser, between


# a supposedly more optimized user
class FasterUser(FastHttpUser):
    @task
    def hello_world(self):
        # This method will run an HTTP GET request on the path `/`
        self.client.get("/")

    wait_time = between(0.5, 1) # wait between 0.5 and 1 seconds between requests, randomly distributed