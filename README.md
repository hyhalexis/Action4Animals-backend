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
### Get a specific user
`GET` `/users/{id}/`
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": <ID>,
            "first_name": <USER INPUT FOR FIRST_NAME>,
            "last_name": <USER INPUT FOR LAST_NAME>,
            "username": <USER INPUT FOR USERNAME>,
            "phone_number": <USER INPUT FOR PHONE_NUMBER>,
            "email": <USER INPUT FOR EMAIL>,
            "posts": [ <SERIALIZED POSTS WITH BASIC INFO>, ... ],
            "comments_posted": [ <SERIALIZED BASIC INFO OF COMMENTS>, ... ],
            "communities": [ <SERIALIZED BASIC INFO OF COMMUNITIES>, ... ],
            "chats": [ <SERIALIZED BASIC INFO OF CHATS>, ...],
            "messages_sent": [ <SERIALIZED BASIC INFO OF MESSAGES SENT BY THE USER>, ...],
            "messages_received": [ <SERIALIZED BASIC INFO OF MESSAGES RECEIVED BY THE USER>, ...]
        }
    ]
}
```
### Update a specific user
`/POST/` `/users/{id}/`
##### Request
```yaml
{
    "first_name": <USER INPUT FOR FIRST_NAME>,
    "last_name": <USER INPUT FOR LAST_NAME>,
    "phone_number": <USER INPUT FOR PHONE_NUMBER>,
    "email": <USER INPUT FOR EMAIL>,
    "password": <USER INPUT FOR PASSWORD>
}
```
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": <ID>,
            "first_name": <USER INPUT FOR FIRST_NAME>,
            "last_name": <USER INPUT FOR LAST_NAME>,
            "username": <USER INPUT FOR USERNAME>,
            "phone_number": <USER INPUT FOR PHONE_NUMBER>,
            "email": <USER INPUT FOR EMAIL>,
            "posts": [ <SERIALIZED POSTS WITH BASIC INFO>, ... ],
            "comments_posted": [ <SERIALIZED BASIC INFO OF COMMENTS>, ... ],
            "communities": [ <SERIALIZED BASIC INFO OF COMMUNITIES>, ... ],
            "chats": [ <SERIALIZED BASIC INFO OF CHATS>, ...],
            "messages_sent": [ <SERIALIZED BASIC INFO OF MESSAGES SENT BY THE USER>, ...],
            "messages_received": [ <SERIALIZED BASIC INFO OF MESSAGES RECEIVED BY THE USER>, ...]
        }
    ]
}
```
### Delete a specific user
`/DELETE/` `/users/{id}/`
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": <ID>,
            "first_name": <USER INPUT FOR FIRST_NAME>,
            "last_name": <USER INPUT FOR LAST_NAME>,
            "username": <USER INPUT FOR USERNAME>,
            "phone_number": <USER INPUT FOR PHONE_NUMBER>,
            "email": <USER INPUT FOR EMAIL>,
            "posts": [ <SERIALIZED POSTS WITH BASIC INFO>, ... ],
            "comments_posted": [ <SERIALIZED BASIC INFO OF COMMENTS>, ... ],
            "communities": [ <SERIALIZED BASIC INFO OF COMMUNITIES>, ... ],
            "chats": [ <SERIALIZED BASIC INFO OF CHATS>, ...],
            "messages_sent": [ <SERIALIZED BASIC INFO OF MESSAGES SENT BY THE USER>, ...],
            "messages_received": [ <SERIALIZED BASIC INFO OF MESSAGES RECEIVED BY THE USER>, ...]
        }
    ]
}
```
### Get all communities
`/GET/` `/communities/`
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": 1,
            "name": "NY corgi lovers",
            "users": [ <SERIALIZED BASIC INFO OF USER>, ...],
            "posts": [ <SERIALIZED BASIC INFO OF POSTS>, ...],
            "chats": [ <SERIALIZED BASIC INFO OF CHATS>, ...]
        }
        ...
    ]
}
```
### Create a community
`/POST/` `/communities/`
##### Request
```yaml
{
    "name": <USER INPUT FOR NAME>
}
```
##### Response
``` yaml
{
    "success": true,
    "data": {
        "id": <ID>,
        "name": <USER INPUT FOR NAME>,
        "users": [],
        "posts": [],
        "chats": []
    }
}
```
### Get a community by id
`/GET/` `/communities/{id}/`
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": <ID>,
            "name": <USER INPUT FOR NAME>,
            "users": [ <SERIALIZED BASIC INFO OF USER>, ...],
            "posts": [ <SERIALIZED BASIC INFO OF POSTS>, ...],
            "chats": [ <SERIALIZED BASIC INFO OF CHATS>, ...]
        }
    ]
}
```
### Update a specific community
`/POST/` `/communities/{id}/`
##### Request
```yaml
{
    "name": <USER INPUT FOR NAME>
}
```
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": <ID>,
            "name": <USER INPUT FOR NAME>,
            "users": [ <SERIALIZED BASIC INFO OF USER>, ...],
            "posts": [ <SERIALIZED BASIC INFO OF POSTS>, ...],
            "chats": [ <SERIALIZED BASIC INFO OF CHATS>, ...]
        }
    ]
}
```
### Delete a specific community
`/DELETE/` `/communities/{id}/`
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": <ID>,
            "name": <USER INPUT FOR NAME>,
            "users": [ <SERIALIZED BASIC INFO OF USER>, ...],
            "posts": [ <SERIALIZED BASIC INFO OF POSTS>, ...],
            "chats": [ <SERIALIZED BASIC INFO OF CHATS>, ...]
        }
    ]
}
```
### Add a user to a community
`/POST/` `/communities/{id}/add/`
##### Request
```yaml
{
    "user_id": <USER INPUT FOR USER_ID>
}
```
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": <ID>,
            "name": <USER INPUT FOR NAME>,
            "users": [ <SERIALIZED BASIC INFO OF USER>, ...],
            "posts": [ <SERIALIZED BASIC INFO OF POSTS>, ...],
            "chats": [ <SERIALIZED BASIC INFO OF CHATS>, ...]
        }
    ]
}
```
### Get all posts in a specific community
`/GET/` `/communities/{id}/posts/`
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": 1,
            "timestamp": "2021-02-19 14:29:59.373606",
            "content": "Anyone saw a corgi around 55th Ave?",
            "edited": false
        }
        ...
    ]
}
```
### Get all posts posted by a specific user
`/GET/` `/users/{id}/posts/`
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": 1,
            "timestamp": "2021-02-19 14:29:59.373606",
            "content": "Anyone saw a corgi around 55th Ave?",
            "edited": false
        }
    ]
}
```
### Create a post
`/POST/` `/users/{id}/communities/{id}/posts/`
##### Request
```yaml
{
    "content": <USER INPUT FOR CONTENT>
}
```
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": <ID>,
            "timestamp": <NOW>",
            "content": <USER INPUT FOR CONTENT>,
            "edited": false
        }
    ]
}
```
### Get a specific post
`/GET/` `/posts/{id}/`
##### Response
```yaml
{
    "success": true,
    "data": {
        "id": <ID>,
        "timestamp": <NOW>",
        "content": <USER INPUT FOR CONTENT>,
        "edited": <EDITED>
        "poster": {
            "id": <USER_ID>,
            "first_name": <USER INPUT FOR FIRST_NAME>,
            "last_name": <USER INPUT FOR LAST_NAME>,
            "username": <USER INPUT FOR USERNAME>
        },
        "community": {
            "id": <COMMUNITY_ID>,
            "name": <USER INPUT FOR NAME>
        },
        "comments": [ <SERIALIZED BASIC INFO OF COMMENT>, ...],
        "tags": [ <SERIALIZED BASIC INFO OF TAGS>, ...]
    }
}
```
### Update a specific post
`/POST/` `/posts/{id}/`
##### Request
```yaml
{
    "content": <USER INPUT FOR CONTENT>
}
```
##### Response 
```yaml
{
    "success": true,
    "data": {
        "id": <ID>,
        "timestamp": <NOW>",
        "content": <USER INPUT FOR CONTENT>,
        "edited": true
        "poster": {
            "id": <USER_ID>,
            "first_name": <USER INPUT FOR FIRST_NAME>,
            "last_name": <USER INPUT FOR LAST_NAME>,
            "username": <USER INPUT FOR USERNAME>
        },
        "community": {
            "id": <COMMUNITY_ID>,
            "name": <USER INPUT FOR NAME>
        },
        "comments": [ <SERIALIZED BASIC INFO OF COMMENT>, ...],
        "tags": [ <SERIALIZED BASIC INFO OF TAGS>, ...]
    }
}
```
### Delete a post
`/DELETE/` `/posts/{id}/`
##### Response
```yaml
{
    "success": true,
    "data": {
        "id": <ID>,
        "timestamp": <NOW>",
        "content": <USER INPUT FOR CONTENT>,
        "edited": true
        "poster": {
            "id": <USER_ID>,
            "first_name": <USER INPUT FOR FIRST_NAME>,
            "last_name": <USER INPUT FOR LAST_NAME>,
            "username": <USER INPUT FOR USERNAME>
        },
        "community": {
            "id": <COMMUNITY_ID>,
            "name": <USER INPUT FOR NAME>
        },
        "comments": [ <SERIALIZED BASIC INFO OF COMMENT>, ...],
        "tags": [ <SERIALIZED BASIC INFO OF TAGS>, ...]
    }
}
```
### Get all comments of a specific post
`/GET/` `/posts/{id}/comments/`
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": 1,
            "timestamp": "2021-02-19 15:16:12.700020",
            "content": "Congrats!",
            "edited": false
        }
        ...
    ]
}
```
### Get all comments posted by a specific user
`/GET/` `/users/{id}/comments/`
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": 1,
            "timestamp": "2021-02-19 15:16:12.700020",
            "content": "Congrats!",
            "edited": false
        }
        ...
    ]
}
```
### Create a comment
`/POST/` `/users/{user_id}/posts/{post_id}/comments/`
##### Request
```yaml
{
    "content": <USER INPUT FOR CONTENT>
}
```
##### Response
```yaml
{
    "success": true,
    "data": {
        "id": <ID>,
        "timestamp": <NOW>",
        "content": <USER INPUT FOR CONTENT>,
        "edited": true
        "commenter": {
            "id": <USER_ID>,
            "first_name": <USER INPUT FOR FIRST_NAME>,
            "last_name": <USER INPUT FOR LAST_NAME>,
            "username": <USER INPUT FOR USERNAME>
        },
        "post": {
            "id": <POST_ID>,
            "timestamp": <POSTED TIME>,
            "content": <USER INPUT FOR CONTENT>,
            "edited": <EDITED>
        }
    }
}
```
### Get a specific comment
`/GET/` `/comments/{id}/`
##### Response
```yaml
{
    "success": true,
    "data": {
        "id": <ID>,
        "timestamp": <NOW>",
        "content": <USER INPUT FOR CONTENT>,
        "edited": true
        "commenter": {
            "id": <USER_ID>,
            "first_name": <USER INPUT FOR FIRST_NAME>,
            "last_name": <USER INPUT FOR LAST_NAME>,
            "username": <USER INPUT FOR USERNAME>
        },
        "post": {
            "id": <POST_ID>,
            "timestamp": <POSTED TIME>,
            "content": <USER INPUT FOR CONTENT>,
            "edited": <EDITED>
        }
    }
}
```
### Update a specific comment
`/POST/` `/comments/{id}/`
##### Request
```yaml
{
    "content": <USER INPUT FOR CONTENT>
}
```
##### Response
```yaml
{
    "success": true,
    "data": {
        "id": <ID>,
        "timestamp": <NOW>",
        "content": <USER INPUT FOR CONTENT>,
        "edited": true
        "commenter": {
            "id": <USER_ID>,
            "first_name": <USER INPUT FOR FIRST_NAME>,
            "last_name": <USER INPUT FOR LAST_NAME>,
            "username": <USER INPUT FOR USERNAME>
        },
        "post": {
            "id": <POST_ID>,
            "timestamp": <POSTED TIME>,
            "content": <USER INPUT FOR CONTENT>,
            "edited": <EDITED>
        }
    }
}
```
### Delete a specific comment
`/DELETE/` `/comments/{id}/
```yaml
{
    "success": true,
    "data": {
        "id": <ID>,
        "timestamp": <NOW>",
        "content": <USER INPUT FOR CONTENT>,
        "edited": true
        "commenter": {
            "id": <USER_ID>,
            "first_name": <USER INPUT FOR FIRST_NAME>,
            "last_name": <USER INPUT FOR LAST_NAME>,
            "username": <USER INPUT FOR USERNAME>
        },
        "post": {
            "id": <POST_ID>,
            "timestamp": <POSTED TIME>,
            "content": <USER INPUT FOR CONTENT>,
            "edited": <EDITED>
        }
    }
}
```
### Get all tags
`/GET/` `/tags/`
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": 1,
            "description": "welcome home",
            "posts": [ <SERIALIZED BASIC INFO OF POST>, ...]
        }
        ...
    ]
}
```
### Create a tag
`/POST/` `/tags/`
##### Request
```yaml
{
    "description": <USER INPUT FOR DESCRIPTION>
}
```
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": <ID>,
            "description": <USER INPUT FOR DESCRIPTION>,
            "posts": [ <SERIALIZED BASIC INFO OF POST>, ...]
        }
    ]
}
```
### Get a specific tag
`/GET/` `/tags/{id}/`
##### Response
```yaml
{
    "success": true,
    "data": [
        {
            "id": <ID>,
            "description": <USER INPUT FOR DESCRIPTION>,
            "posts": [ <SERIALIZED BASIC INFO OF POST>, ...]
        }
    ]
}
```
### Update a specific tag
`/POST/` `/tags/{id}/`
##### Request
```yaml
{
    "description": <USER INPUT FOR DESCRIPTION>
}
```
##### Response
```yaml
{
    "success": true,
    "data": {
        "id": 1,
        "description": "sweet bean",
        "posts": [ <SERIALIZED BASIC INFO OF POST>, ...]
    }
}
```
### Delete a specific tag
`/DELETE/` `/tags/{id}/`
##### Response
```yaml
{
    "success": true,
    "data": {
        "id": 1,
        "description": "sweet bean",
        "posts": [ <SERIALIZED BASIC INFO OF POST>, ...]
    }
}
```
### Add a tag to a post
`/POST/` `/posts/{id}/add/`
##### Request
```yaml
{
    "tag_id": <USER INPUT FOR TAG_ID>
}
```
##### Response
```yaml
{
    "success": true,
    "data": {
        "id": <POST_ID>,
        "timestamp": <POSTED TIME>,
        "content": <USER INPUT FOR CONTENT>,
        "edited": <EDITED>,
        "poster": {
            "id": <USER_ID>,
            "first_name": <USER INPUT FOR FIRST_NAME>,
            "last_name": <USER INPUT FOR LAST_NAME>,
            "username": <USER INPUT FOR USERNAME>
        },
        "community": {
            "id": <COMMUNIRY_ID>,
            "name": <USER INPUT FOR NAME>
        },
        "comments": [ <SERIALIZED BASIC INFO OF COMMENT>, ...],
        "tags": [
            {
                "id": <TAG_ID>,
                "description": <USER INPUT FOR DESCRIPTION>
            }
        ]
    }
}
```






















