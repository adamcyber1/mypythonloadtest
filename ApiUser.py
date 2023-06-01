import time # Importing time from Python system library
from locust import HttpUser, task

class ApiUser(HttpUser):

    # This task will run when the user is instanciated
    def on_start(self):
        # run any initialization code that is needed for the user here - i.e. logging in.
        pass

    # This task will fail because there is no endpoint at https://petstore.swagger.io/v2/
    @task
    def hello_world(self):
        self.client.get("/")

    # The (3) after the task decorator tells Locust to run this task 3 times as often
    @task(3)
    def update_pets(self):
        # Using a for loop, count from 0-4 and use in HTTP request below
        for pet_id in range(5):
            # Run HTTP POST request and pass a JSON Body
            self.client.post(f"/pet?petId={pet_id}", json={"name":"Mittens"})
            time.sleep(1) # Wait for 1 second before continuing