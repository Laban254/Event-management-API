# Quickstart Guide

This quickstart guide will walk you through the essential steps to get started with the Event Management API. It covers registration, authentication, obtaining access tokens, using refresh tokens, and basic usage of the API.

## Register a User

### Endpoint


    POST /api/auth/register/ HTTP/1.1
    Host: localhost:8000
    Content-Type: application/json
    
    {
      "username": "example_user",
      "email": "example@example.com",
      "password": "your_password"
    }

### Example Response



    HTTP/1.1 201 Created
    Content-Type: application/json
    
    {
      "id": 1,
      "username": "example_user",
      "email": "example@example.com"
    }

### Notes

-   Replace `localhost:8000` with the actual API host.
-   Adjust the request payload and response based on your API's implementation.

## Login and Obtain Access Token

### Endpoint


    POST /api/auth/login/ HTTP/1.1
    Host: localhost:8000
    Content-Type: application/json
    
    {
      "username": "example_user",
      "password": "your_password"
    }

### Example Response


    HTTP/1.1 200 OK
    Content-Type: application/json
    
    {
      "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "user": {
        "id": 1,
        "username": "example_user",
        "email": "example@example.com"
      }
    }

### Notes

-   The access token and refresh token will be used for authentication and refreshing tokens.
-   Store these tokens securely for subsequent API requests.

## Use Refresh Token API

### Endpoint


    POST /api/auth/token/refresh/ HTTP/1.1
    Host: localhost:8000
    Content-Type: application/json
    
    {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }

### Example Response


    HTTP/1.1 200 OK
    Content-Type: application/json
    
    {
      "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
      "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
    }

### Notes

-   Use the refresh token to obtain a new access token when the current one expires.
-   The new access token will allow continued access to protected API endpoints.



## Interacting with API Using Spectacular Swagger UI

After obtaining your access token, you can interact with the Event Management API using Spectacular Swagger UI.

1.  **Access Spectacular Swagger UI**: Navigate to `http://localhost:8000/api/schema/swagger-ui/` in your browser.
    
2.  **Authorize Swagger UI**:
    
    -   Click on the "Authorize" button in the top-right corner of the Swagger UI interface.
    -   Enter your access token in the format `Bearer <your_access_token>`.
    -   Click "Authorize" to apply the token.
3.  **Making Authenticated Requests**:
    
    -   Explore endpoints and use the provided fields to enter parameters.
    -   Execute requests directly from Swagger UI, with the access token automatically included in requests.

### Notes:

-   Ensure your access token remains secure and is used appropriately.
-   Customize the endpoint URLs and paths based on your specific API implementation.