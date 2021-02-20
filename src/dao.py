from db import db, User, Community, Post, Comment, Tag, Chat, Message
import datetime

def get_all_users():
    return [u.serialize() for u in User.query.all()]
    
def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return user.serialize()

def update_user(user_id, body):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    user.first_name = body.get("first_name", user.first_name)
    user.last_name = body.get("last_name", user.last_name) 
    user.phone_number = body.get("phone_number", user.phone_number)
    user.email = body.get("email", user.email)
    user.password_digest = body.get("password_digest", user.password_digest)
    db.session.commit()
    return user.serialize()

def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    db.session.delete(user)
    db.session.commit()
    return user.serialize()

def get_all_communities():
    return [c.serialize() for c in Community.query.all()]

def create_community(body):
    community = Community(
        name = body.get("name")
    )
    db.session.add(community)
    db.session.commit()
    return community.serialize()
    
def get_community_by_id(community_id):
    community = Community.query.filter_by(id=community_id).first()
    if community is None:
        return None
    return community.serialize()

def update_community(community_id, body):
    community = Community.query.filter_by(id=community_id).first()
    if community is None:
        return None
    community.name = body.get("name", community.name)
    db.session.commit()
    return community.serialize()

def delete_community(community_id):
    community = Community.query.filter_by(id=community_id).first()
    if community is None:
        return None
    db.session.delete(community)
    db.session.commit()
    return community.serialize()

def add_user_to_community(community_id, body):
    community = Community.query.filter_by(id=community_id).first()
    if community is None:
        return None
    user_id = body.get("user_id")
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    community.users.append(user)
    db.session.commit()
    return community.serialize()

def get_all_posts_in_community(community_id):
    community = Community.query.filter_by(id=community_id).first()
    if community is None:
        return None
    return [p.serialize_basic() for p in community.posts]

def get_all_posts_by_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return [p.serialize_basic() for p in user.posts]

def create_post(user_id, community_id, body):
    post = Post(
        timestamp = datetime.datetime.now(),
        content = body.get("content"),
        edited = False,
        user_id = user_id,
        community_id = community_id
    )
    db.session.add(post)
    db.session.commit()
    return post.serialize()

def get_post_by_id(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return None
    return post.serialize()

def update_post(post_id, body):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return None
    post.content = body.get("content", post.content)
    post.edited = True
    db.session.commit()
    return post.serialize()

def delete_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return None
    db.session.delete(post)
    db.session.commit()
    return post.serialize()

def get_all_comments_of_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return None
    return [c.serialize_basic() for c in post.comments]

def get_all_comments_by_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return [c.serialize_basic() for c in user.comments_posted]

def create_comment(user_id, post_id, body):
    comment = Comment(
        timestamp = datetime.datetime.now(),
        content = body.get("content"),
        edited = False,
        user_id = user_id,
        post_id = post_id
    )
    db.session.add(comment)
    db.session.commit()
    return comment.serialize()

def get_comment_by_id(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    if comment is None:
        return None
    return comment.serialize()

def update_comment(comment_id, body):
    comment = Comment.query.filter_by(id=comment_id).first()
    if comment is None:
        return None
    comment.content = body.get("content", comment.content)
    comment.edited = True
    db.session.commit()
    return comment.serialize()

def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()
    if comment is None:
        return None
    db.session.delete(comment)
    db.session.commit()
    return comment.serialize()

def get_all_tags():
    return [t.serialize() for t in Tag.query.all()]

def create_tag(body):
    tag = Tag(
        description = body.get("description")
    )
    db.session.add(tag)
    db.session.commit()
    return tag.serialize()

def get_tag_by_id(tag_id):
    tag = Tag.query.filter_by(id=tag_id).first()
    if tag is None:
        return None
    return tag.serialize()

def update_tag(tag_id, body):
    tag = Tag.query.filter_by(id=tag_id).first()
    if tag is None:
        return None
    tag.description = body.get("description", tag.description)
    db.session.commit()
    return tag.serialize()

def delete_tag(tag_id):
    tag = Tag.query.filter_by(id=tag_id).first()
    if tag is None:
        return None
    db.session.delete(tag)
    db.session.commit()
    return tag.serialize()

def add_tag_to_post(post_id, body):
    post = Post.query.filter_by(id=post_id).first()
    if post is None:
        return None
    tag_id = body.get("tag_id")
    tag = Tag.query.filter_by(id=tag_id).first()
    if tag is None:
        return None
    post.tags.append(tag)
    db.session.commit()
    return post.serialize()

def get_all_chats_in_community(community_id):
    community = Community.query.filter_by(id=community_id).first()
    if community is None:
        return None
    return [c.serialize_basic() for c in community.chats]

def get_all_chats_of_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return [c.serialize_basic() for c in user.chats]

def create_chat(body):
    community_id = body.get("community_id")
    chat = Chat(
        community_id = body.get("community_id")
    )
    db.session.add(chat)
    db.session.commit()
    return chat.serialize()

def get_chat_by_id(chat_id):
    chat = Chat.query.filter_by(id=chat_id).first()
    if chat is None:
        return None
    return chat.serialize()

def delete_chat(chat_id):
    chat = Chat.query.filter_by(id=chat_id).first()
    if chat is None:
        return None
    db.session.delete(chat)
    db.session.commit()
    return chat.serialize()

def add_user_to_chat(chat_id, body):
    chat = Chat.query.filter_by(id=chat_id).first()
    if chat is None:
        return None
    user_id = body.get("user_id")
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    chat.users.append(user)
    db.session.commit()
    return chat.serialize()

def remove_user_from_chat(chat_id, body):
    chat = Chat.query.filter_by(id=chat_id).first()
    if chat is None:
        return None
    user_id = body.get("user_id")
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    if user not in chat.users:
        return "not in chat"
    chat.users.remove(user)
    db.session.commit()
    return chat.serialize()

def get_all_messages_of_chat(chat_id):
    chat = Chat.query.filter_by(id=chat_id).first()
    if chat is None:
        return None
    return [m.serialize_basic() for m in chat.messages]

def get_all_messages_sent_by_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return [m.serialize_basic() for m in user.messages_sent]

def get_all_messages_received_by_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return [m.serialize_basic() for m in user.messages_received]

def create_message(chat_id, body):
    message = Message(
        timestamp = datetime.datetime.now(),
        content = body.get("content"),
        sender_id = body.get("sender_id"),
        chat_id = chat_id
    )
    chat = Chat.query.filter_by(id=chat_id).first()
    sender = User.query.filter_by(id=body.get("sender_id")).first()
    for user in chat.users:
        if user is not sender:
            user.messages_received.append(message)
    db.session.add(message)
    db.session.commit()
    return message.serialize()

def get_message_by_id(message_id):
    message = Message.query.filter_by(id=message_id).first()
    if message is None:
        return None
    return message.serialize()

def recall_message(message_id):
    message = Message.query.filter_by(id=message_id).first()
    if message is None:
        return None
    datetime_str = message.timestamp
    datetime_dt = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S.%f")
    if datetime_dt + datetime.timedelta(minutes=2) < datetime.datetime.now():
        return "time limit" 
    db.session.delete(message)
    db.session.commit()
    return message.serialize()

