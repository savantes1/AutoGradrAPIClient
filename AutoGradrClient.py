import requests

class HTTP_NotOK(Exception):
    def __init__(self, httpStatusCode, message):
        super().__init__(message)
        self.HttpStatusCode = httpStatusCode



class AutoGradrClient:
    def __init__(self, email, password):
        self.__baseUrl = "https://autogradr.app/api"
        
        self.__session = requests.Session()

        # Login to AutoGradr
        loginResponse = self.__session.post(f"{self.__baseUrl}/auth/email/login", json={"email":email, "password": password})

        # Check if there was a problem logging in
        if loginResponse.status_code != 200:
            raise HTTP_NotOK(loginResponse.status_code, f'Error trying to login to AutoGradr as "{email}"')

        # Store the auth for subsequent http calls
        self.__session.auth = (loginResponse.json()['user_uuid'], loginResponse.json()['session_token'])


    def __get(self, relativeUrl):

        response = self.__session.get(f"{self.__baseUrl}/{relativeUrl}")

        # Check if there was a problem performing the GET request
        if response.status_code != 200:
            raise HTTP_NotOK(response.status_code, f'Problem trying to do http GET on "{relativeUrl}"')

        return response.json()



    def GetCourseRoster(self, courseId):
        return self.__get(f"courses/{courseId}/roster")
        

    def GetAssignment(self, assignmentId):
        return self.__get(f"assignments/{assignmentId}")


    def GetExerciseSet(self, exerciseSetId):
        return self.__get(f"exercise-sets/{exerciseSetId}")


    def GetExercises(self, exerciseSetId):
        return self.__get(f"exercise-sets/{exerciseSetId}/exercises")


    def GetTestCases(self, testCaseSetId):
        return self.__get(f"test-case-sets/{testCaseSetId}/test-cases")

    def GetAssignmentAttempts(self, assignmentId):
        return self.__get(f"assignments/{assignmentId}/attempts")

    def GetAttemptResultSets(self, attemptId):
        return self.__get(f"attempts/{attemptId}/result-sets")


    def __del__(self):

        # Logout of AutoGradr
        self.__session.post(f"{self.__baseUrl}/logout", data={})

