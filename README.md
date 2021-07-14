![Detect Secrets](https://github.com/rokwire/rokwire-building-blocks-api/workflows/Detect%20Secrets/badge.svg)

# Rokwire Platform Building Blocks API Documentation
API definitions of the Rokwire Platform building blocks

## Install commit hooks

```
$ pip install -r requirements-dev.txt
$ pre-commit install
```

## Setup and Run 

- Create the Rokwire Platform API Doc Docker image and run the Docker container:
        
      docker build -t rokwire/api-doc .
      docker run -p 80:8080 rokwire/api-doc 

  Now you can view the API documentation at http://localhost/docs/

## Docker / AWS ECR

Create Docker image for Rokwire Platform API and push to AWS ECR for deployment using Fargate from within AWS CLI:

```
docker build -t rokwire/api-doc .
docker tag rokwire/api-doc:latest 779619664536.dkr.ecr.us-east-2.amazonaws.com/rokwire/api-doc:latest
docker push 779619664536.dkr.ecr.us-east-2.amazonaws.com/rokwire/api-doc:latest
```

# Other Modules in this Repository

- [App Config Building Block](https://github.com/rokwire/rokwire-building-blocks-api/tree/develop/appconfigservice)
  - Python Connexion-based RESTful web services for managing client application configurations.
- [Authentication Building Block](https://github.com/rokwire/rokwire-building-blocks-api/tree/develop/authservice)
  - Python Connexion-based RESTful web services for managing user authentication. Currently, this module provides API endpoints for phone-based user verification.
- [Auth Middleware Library](https://github.com/rokwire/rokwire-building-blocks-api/tree/develop/lib/auth-middleware)
  - Python Library that provides methods for managing authentication and authorization of incoming requests.
- [Events Building Block](https://github.com/rokwire/rokwire-building-blocks-api/tree/develop/eventservice)
  - Python Connexion-based RESTful web services for managing events.
- [Example Building Block](https://github.com/rokwire/rokwire-building-blocks-api/tree/develop/auth-middleware-test-svc)
  - An example building block that uses the Auth Middleware Library.
- [Logging Building Block](https://github.com/rokwire/rokwire-building-blocks-api/tree/develop/loggingservice)
  - Python Connexion-based RESTful web services for managing logs.
- [Profile Building Block](https://github.com/rokwire/rokwire-building-blocks-api/tree/develop/profileservice)
  - Python Connexion-based RESTful web services for managing user profiles.
  