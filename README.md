# AutoGradr API Client
A client for interacting with the AutoGradr web API in Python

#### Usage

```
from AutoGradrClient import AutoGradrClient

email = '[AutoGradr Email]'
password = '[AutoGradr Password]'

# Instantiate client
client = AutoGradrClient(email, password)

courseId = "[AutoGradr Course Id]"

# Get the roster of the specified course
roster = client.GetCourseRoster(courseId)

print(roster)
```
