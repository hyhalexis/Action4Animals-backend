import json
from db import db, User, Community, Post, Comment, Tag, Chat, Message
from flask import Flask, request
import dao
import users_dao
import os

app = Flask(__name__)
db_filename = "animal.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

def extract_token(request):
    auth_header = request.headers.get("Authorization")
    if auth_header is None: 
        return False, json.dumps({"error": "Missing authorization header."})
    
    bearer_token = auth_header.replace("Bearer ", "").strip()
    if bearer_token is None or not bearer_token:
        return False, json.dumps(({"error": "Invalid authorization header"}))
    return True, bearer_token

def success_response(data, code=200):
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

@app.route("/")
def header():
    return ("An app developed to facilitate animal adoption.")

@app.route("/users/")
def get_all_users():
    return success_response(dao.get_all_users())

@app.route("/users/", methods=["POST"])
def create_user():
    body = json.loads(request.data)
    user = dao.create_user(body)
    return success_response(user)

@app.route("/users/<int:user_id>/")
def get_user_by_id(user_id):
    user = dao.get_user_by_id(user_id)
    if user is None:
        return failure_response("User not found.")
    return success_response(user)

@app.route("/users/<int:user_id>/", methods=["POST"])
def update_user(user_id):
    body = json.loads(request.data)
    user = dao.update_user(user_id, body)
    if user is None:
        return failure_response("User not found.")
    return success_response(user)

@app.route("/users/<int:user_id>/", methods=["DELETE"])
def delete_user(user_id):
    user = dao.delete_user(user_id)
    if user is None:
        return failure_response("User not found.")
    return success_response(user)

@app.route("/communities/")
def get_all_communities():
    return success_response(dao.get_all_communities())

@app.route("/communities/", methods=["POST"])
def create_community():
    body = json.loads(request.data)
    community = dao.create_community(body)
    return success_response(community)

@app.route("/communities/<int:community_id>/")
def get_community_by_id(community_id):
    community = dao.get_community_by_id(community_id)
    if community is None:
        return failure_response("Community not found.")
    return success_response(community)

@app.route("/communities/<int:community_id>/", methods=["POST"])
def update_community(community_id):
    body = json.loads(request.data)
    community = dao.update_community(community_id, body)
    if community is None:
        return failure_response("Community not found.")
    return success_response(community)

@app.route("/communities/<int:community_id>/", methods=["DELETE"])
def delete_community(community_id):
    community = dao.delete_community(community_id)
    if community is None:
        return failure_response("Community not found.")
    return success_response(community)

@app.route("/communities/<int:community_id>/add/", methods=["POST"])
def add_user_to_community(community_id):
    body = json.loads(request.data)
    community = dao.add_user_to_community(community_id, body)
    if community is None:
        return failure_response("Community or user not found.")
    return success_response(community)

@app.route("/communities/<int:community_id>/posts/")
def get_all_posts_in_community(community_id):
    posts = dao.get_all_posts_in_community(community_id)
    if posts is None:
        return failure_response("Community not found.")
    return success_response(posts)

@app.route("/users/<int:user_id>/posts/")
def get_all_posts_by_user(user_id):
    posts = dao.get_all_posts_by_user(user_id)
    if posts is None:
        return failure_response("User not found.")
    return success_response(posts)

@app.route("/users/<int:user_id>/communities/<int:community_id>/posts/", methods=["POST"])
def create_post(user_id, community_id):
    body = json.loads(request.data)
    post = dao.create_post(user_id, community_id, body)
    return success_response(post)

@app.route("/posts/<int:post_id>/")
def get_post_by_id(post_id):
    post = dao.get_post_by_id(post_id)
    if post is None:
        return failure_response("Post not found.")
    return success_response(post)

@app.route("/posts/<int:post_id>/", methods=["POST"])
def update_post(post_id):
    body = json.loads(request.data)
    post = dao.update_post(post_id, body)
    if post is None:
        return failure_response("Post not found")
    return success_response(post)

@app.route("/posts/<int:post_id>/", methods=["DELETE"])
def delete_post(post_id):
    post = dao.delete_post(post_id)
    if post is None:
        return failure_response("Post not found")
    return success_response(post)

@app.route("/posts/<int:post_id>/comments/")
def get_all_comments_for_post(post_id):
    comments = dao.get_all_comments_for_post(post_id)
    if comments is None:
        return failure_response("Post not found.")
    return success_response(comments)

@app.route("/users/<int:user_id>/comments/")
def get_all_comments_by_user(user_id):
    comments = dao.get_all_comments_by_user(user_id)
    if comments is None:
        return failure_response("User not found.")
    return success_response(comments)

@app.route("/users/<int:user_id>/posts/<int:post_id>/comments/", methods=["POST"])
def create_comment(user_id, post_id):
    body = json.loads(request.data)
    comment = dao.create_comment(user_id, post_id, body)
    return success_response(comment)

@app.route("/comments/<int:comment_id>/")
def get_comment_by_id(comment_id):
    comment = dao.get_comment_by_id(comment_id)
    if comment is None:
        return failure_response("Comment not found.")
    return success_response(comment)

@app.route("/comments/<int:comment_id>/", methods=["POST"])
def update_comment(comment_id):
    body = json.loads(request.data)
    comment = dao.update_comment(comment_id, body)
    if comment is None:
        return failure_response("Comment not found.")
    return success_response(comment)

@app.route("/comments/<int:comment_id>/", methods=["DELETE"])
def delete_comment(comment_id):
    comment = dao.delete_comment(comment_id)
    if comment is None:
        return failure_response("Comment not found.")
    return success_response(comment)

@app.route("/tags/")
def get_all_tags():
    return success_response(dao.get_all_tags())

@app.route("/tags/", methods=["POST"])
def create_tag():
    body = json.loads(request.data)
    tag = dao.create_tag(body)
    return success_response(tag)

@app.route("/tags/<int:tag_id>/")
def get_tag_by_id(tag_id):
    tag = dao.get_tag_by_id(tag_id)
    if tag is None:
        return failure_response("Tag not found.")
    return success_response(tag)

@app.route("/tags/<int:tag_id>/", methods=["POST"])
def update_tag(tag_id):
    body = json.loads(request.data)
    tag = dao.update_tag(tag_id, body)
    if tag is None:
        return failure_response("Tag not found.")
    return success_response(tag)

@app.route("/tags/<int:tag_id>/", methods=["DELETE"])
def delete_tag(tag_id):
    tag = dao.delete_tag(tag_id)
    if tag is None:
        return failure_response("Tag not found.")
    return success_response(tag)

@app.route("/posts/<int:post_id>/add/", methods=["POST"])
def add_tag_to_post(post_id):
    body = json.loads(request.data)
    post = dao.add_tag_to_post(post_id, body)
    if post is None:
        return failure_response("Tag or post not found.")
    return success_response(post)

@app.route("/communities/<int:community_id>/chats/")
def get_all_chats_in_community(community_id):
    chats = dao.get_all_chats_in_community(community_id)
    if chats is None:
        return failure_response("Community not found.")
    return success_response(chats)

@app.route("/users/<int:user_id>/chats/")
def get_all_chats_of_user(user_id):
    chats = dao.get_all_chats_of_user(user_id)
    if chats is None:
        return failure_response("User not found.")
    return success_response(chats)

@app.route("/chats/", methods=["POST"])
def create_chat():
    body = json.loads(request.data)
    chat = dao.create_chat(body)
    return success_response(chat)

@app.route("/chats/<int:chat_id>/")
def get_chat_by_id(chat_id):
    chat = dao.get_chat_by_id(chat_id)
    if chat is None:
        return failure_response("Chat not found.")
    return success_response(chat)

@app.route("/chats/<int:chat_id>/", methods=["DELETE"])
def delete_chat(chat_id):
    chat = dao.delete_chat(chat_id)
    if chat is None:
        return failure_response("Chat not found.")
    return success_response(chat)

@app.route("/chats/<int:chat_id>/add/", methods=["POST"])
def add_user_to_chat(chat_id):
    body = json.loads(request.data)
    chat = dao.add_user_to_chat(chat_id, body)
    if chat is None:
        return failure_response("Chat or user not found.")
    return success_response(chat)

@app.route("/chats/<int:chat_id>/remove/", methods=["POST"])
def remove_user_from_chat(chat_id):
    body = json.loads(request.data)
    chat = dao.remove_user_from_chat(chat_id, body)
    if chat is None:
        return failure_response("Unable to remove user.")
    if chat == "not in chat":
        return failure_response("User is not in chat.")
    return success_response(chat)

@app.route("/chats/<int:chat_id>/messages/")
def get_all_messages_of_chat(chat_id):
    messages = dao.get_all_messages_of_chat(chat_id)
    if messages is None:
        return failure_response("Chat not found.")
    return success_response(messages)

@app.route("/users/<int:user_id>/messages/sent/")
def get_all_messages_sent_by_user(user_id):
    messages = dao.get_all_messages_sent_by_user(user_id)
    if messages is None:
        return failure_response("User not found.")
    return success_response(messages)

@app.route("/users/<int:user_id>/messages/received/")
def get_all_messages_received_by_user(user_id):
    messages = dao.get_all_messages_received_by_user(user_id)
    if messages is None:
        return failure_response("User not found.")
    return success_response(messages)

@app.route("/chats/<int:chat_id>/messages/", methods=["POST"])
def create_message(chat_id):
    body = json.loads(request.data)
    message = dao.create_message(chat_id, body)
    return success_response(message)

@app.route("/messages/<int:message_id>/")
def get_message_by_id(message_id):
    message = dao.get_message_by_id(message_id)
    if message is None:
        return failure_response("Message not found.")
    return success_response(message)

@app.route("/messages/<int:message_id>/", methods=["DELETE"])
def recall_message(message_id):
    message = dao.recall_message(message_id)
    if message is None:
        return failure_response("Message not found.")
    if message == "time limit":
        return failure_response("Message cannot be recalled.")
    return success_response(message)

@app.route("/messages/<int:message_id>/add/", methods=["POST"])
def add_user_to_message_receiver(message_id):
    body = json.loads(request.data)
    message = dao.add_user_to_message_receiver(message_id, body)
    if message is None:
        return failure_response("User or message not found.")
    if message == "sender error":
        return failure_response("Cannot add sender as receiver")
    return success_response(message)

@app.route("/register/", methods=["POST"])
def register_account():
    body = json.loads(request.data)
    first_name = body.get("first_name")
    last_name = body.get("last_name")
    username = body.get("username")
    phone_number = body.get("phone_number")
    email = body.get("email")
    password = body.get("password")

    if first_name is None or last_name is None or username is None or phone_number is None or email is None or password is None:
        return json.dumps({"error": "Invalid input."})
    created, user = users_dao.create_user(first_name, last_name, username, phone_number, email, password)
    if not created:
        return json.dumps({"error": "User already exists."})
    return json.dumps({
        "session_token": user.session_token,
        "session_expiration": str(user.session_expiration),
        "update_token": user.update_token,
    })

@app.route("/login/", methods=["POST"])
def login():
    body = json.loads(request.data)
    username = body.get("username")
    password = body.get("password")

    if username is None or password is None:
        return json.dumps({"error": "Invalid username or password."})
    successful, user = users_dao.verify_credentials(username, password)
    if not successful:
        return json.dumps({"error": "Incorrect username or password."})
    return json.dumps(
        {
            "session_token": user.session_token,
            "session_expiration": str(user.session_expiration),
            "update_token": user.update_token,
        }
    )

@app.route("/session/", methods=["POST"])
def update_session():
    successful, update_token = extract_token(request)
    if not successful:
        return update_token
    try:
        user = users_dao.renew_session(update_token)
    except Exception as e:
        return json.dumps({"error": f"Invalid update token: {str(e)}"})
    return json.dumps(
        {
            "session_token": user.session_token,
            "session_expiration": str(user.session_expiration),
            "update_token": user.update_token,
        }
    )

@app.route("/secret/", methods=["GET"])
def secret_message():
    successful, session_token = extract_token(request)
    if not successful:
        return session_token
    user = users_dao.get_user_by_session_token(session_token)
    if not user or not user.verify_session_token(session_token):
        return json.dumps({"error": "Invalid session token."})
    return json.dumps({
        "message": "You have successfully implemented sessions"}
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)