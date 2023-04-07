### How to run the application:
- Docker:
    - open cmd and go to the project directory
    - execute "docker build --tag python-docker ." in command line
    - execute "docker run"
    - visit http://localhost:5000/

- Without Docker:
    - open cmd and go to the project directory
    - execute "./app.py"
    - visit http://localhost:5000/

### Routes:
- http://localhost:5000/api/v1/{chess-figure}/{current-field}
- http://localhost:5000/api/v1/{chess-figure}/{current-field}/{dest-field}