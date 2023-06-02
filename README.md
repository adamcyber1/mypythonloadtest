# mypythonloadtest

## Setup

Initialize environment:
```commandline
git clone 
cd mypythonloadtest
pip install .
```

## instructions

### Basic Local Test
1. Run the flask server:
```commandline
flask run --port 8080
```

To run with a more performance web server, run: 

```commandline
 waitress-serve --port=8080 --threads 24 app:app
```

2. Run the BasicUser load test:
```commandline
 locust --autostart --host http://127.0.0.1:8080 -f BasicUser.py --users 1 --spawn-rate 1 --run-time 30s 
```
This will run a load test with 1 user for 30 seconds. 

3. Locust will run a basic server on `http://localhost:8089/` which can be used to observe the load test results

## Other Load Test Scenarios

- RampUpLoadUser - a performance test that ramps up load indefinitely: 
```commandline
 locust --autostart --host http://127.0.0.1:8080 -f RampUpLoadUser.py
```

- CustomLoadUser - runs a fully custom load profile - in this case to generate a peak
```commandline
 locust --autostart --host http://127.0.0.1:8080 -f CustomLoadUser.py
```

### Distributed load test 
TBC