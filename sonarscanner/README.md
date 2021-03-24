Scanning source code
===

### Setup sonarqube 

Run a sonarqube server

```sh
docker run -itd --name sonarqube -p 9001:9000 sonarqube:lts
```

Access to http://localhost:9001 using browser

- User: admin
- password: admin

Create a project
- Add a project key which random characters up to 400
  - test-myproject-key-12345
- Add display name up to 255 chars
  - test-myproject

Generate a token
- Add a random characters
  - test-myproject-token-12345
- Copy a token in display

Choice main language. In that case of python, Choice `Other`  
Choice your OS

### Execute scanner

How to scan

```sh
sudo docker run --rm -e SONAR_HOST_URL="http://sonarqube:9000" -e SONAR_LOGIN="Past a token" --link sonarqube -v "${PWD}/src:/usr/src" sonarsource/sonar-scanner-cli -Dsonar.projectKey=test-myproject-key-12345
```
