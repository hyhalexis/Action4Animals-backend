# Action4Animals-backend
An application built to facilitate adoption of homeless animals and help pet owners find their lost pets.
https://alexishaoanimal.herokuapp.com/
### Register an account
`POST `/register/`
##### Request
```yaml
{
    "first_name": <USER INPUT FOR FIRST_NAME>,
    "last_name": <USER INPUT FOR LAST_NAME>,
    "username": <USER INPUT FOR USERNAME>,
    "phone_number": <USER INPUT FOR PHONE_NUMBER>,
    "email": <USER INPUT FOR EMAIL>,
    "password": <USER INPUT FOR PASSWORD>
}
```
##### Response
```yaml
{
    "session_token": <SESSION_TOKEN>,
    "session_expiration": <SESSION_EXPIRATION>,
    "update_token": <UPDATE_TOKEN>
}
```
### Login
`POST` `/login/`
##### Request
```yaml
{
    "username": <USER INPUT FOR USERNAME>,
    "password": <USER INPUT FOR PASSWORD>
}
```
##### Response
```yaml
{
    "session_token": <SESSION TOKEN>,
    "session_expiration": <SESSION EXPIRATION>,
    "update_token": <UPDATE TOKEN>
}
```
### Update session
`/POST/` `/session/`
##### Request
```yaml
update_token
```
##### Response
```yaml
{
    "session_token": <SESSION_TOKEN>,
    "session_expiration": <SESSION_EXPIRATION>,
    "update_token": <UPDATE_TOKEN>
}
```
### Verify session implementation
`/GET/` `/secret/`
##### Response
```yaml
{
    "session_token": <SESSION_TOKEN>,
    "session_expiration": <SESSION_EXPIRATION>,
    "update_token": <UPDATE_TOKEN>
}
```
### Get all users
`GET` `/users/`
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": 1,
            "first_name": "Thomas",
            "last_name": "Black",
            "username": "tmz123",
            "phone_number": 1231451678,
            "email": "tmz123@cornell.edu",
            "posts": [ <SERIALIZED POSTS WITH BASIC INFO>, ... ],
            "comments_posted": [ <SERIALIZED BASIC INFO OF COMMENTS>, ... ],
            "communities": [ <SERIALIZED BASIC INFO OF COMMUNITIES>, ... ],
            "chats": [ <SERIALIZED BASIC INFO OF CHATS>, ...],
            "messages_sent": [ <SERIALIZED BASIC INFO OF MESSAGES SENT BY THE USER>, ...],
            "messages_received": [ <SERIALIZED BASIC INFO OF MESSAGES RECEIVED BY THE USER>, ...]
        }
        ...
    ]
}
```
### Get user by id
`GET` `/users/{id}/`
##### Response
```yaml




