# Teacher Panel Service

One of the services of Software-Engineering-1402-02 microservice project.

## Functionalities provided by this service 

- Users can register as teachers create content for students.
- Teachers can create courses to represent the content they intend to provide.
- Courses contain English learning videos and exams.
- Exams contain subjects to inform students of exam's content.
- Each question of exam has 4 options and a category to represent question type.

## Implementation parts of service

1. An API written with ASP.NET Core and C# which is responsible for database interactions
and providing Django core server with data required to create views.
2. The logic to create forms and render views based on data retrieved by the API.

## How do these parts interact with each other ?
The Django core server sends HTTP requests to the API.