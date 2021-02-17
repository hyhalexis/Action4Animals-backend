from flask_sqlalchemy import SQLAlchemy
import datetime
import hashlib
import os
import bcrypt

db = SQLAlchemy()

association_users_communities = db.Table(
    "association_users_communities",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("community_id", db.Integer, db.ForeignKey("community.id"))
)

association_users_chats = db.Table(
    "association_users_chats",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("chat_id", db.Integer, db.ForeignKey("chat.id"))
)

association_users_messages_received = db.Table(
    "association_users_messages_received",
    db.Model.metadata,
    db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
    db.Column("message_id", db.Integer, db.ForeignKey("message.id"))
)

association_posts_tags = db.Table(
    "association_posts_tags",
    db.Model.metadata,
    db.Column("post_id", db.Integer, db.ForeignKey("post.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id"))
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False, unique=True)
    phone_number = db.Column(db.Integer, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password_digest = db.Column(db.String, nullable=False)
    posts = db.relationship("Post")
    comments_posted = db.relationship("Comment")
    communities = db.relationship("Community", secondary=association_users_communities, back_populates="users")
    chats = db.relationship("Chat", secondary=association_users_chats, back_populates="users")
    messages_sent = db.relationship("Message")
    messages_received = db.relationship("Message", secondary=association_users_messages_received, back_populates="receivers")

    session_token = db.Column(db.String, nullable=False, unique=True)
    session_expiration = db.Column(db.DateTime, nullable=False)
    update_token = db.Column(db.String, nullable=False, unique=True)

    def __init__(self, **kwargs):
        self.first_name = kwargs.get("first_name", "")
        self.last_name = kwargs.get("last_name", "")
        self.username = kwargs.get("username", "")
        self.phone_number = kwargs.get("phone_number")
        self.email = kwargs.get("email")
        self.password_digest = bcrypt.hashpw(kwargs.get("password").encode("utf8"), bcrypt.gensalt(rounds=13))
        self.renew_session()

    
    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "phone_number": self.phone_number,
            "email": self.email,
            "posts": [p.serialize_basic() for p in self.posts],
            "comments_posted": [c.serialize_basic() for c in self.comments_posted],
            "communities": [c.serialize_basic() for c in self.communities],
            "chats": [c.serialize_basic() for c in self.chats],
            "messages_sent": [ms.serialize_basic() for ms in self.messages_sent],
            "messages_received": [mr.serialize_basic() for mr in self.messages_received]
        }

    def serialize_basic(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "phone_number": self.phone_number,
            "email": self.email
        }

    def _urlsafe_base_64(self):
        return hashlib.sha1(os.urandom(64)).hexdigest()

    # Generates new tokens, and resets expiration time
    def renew_session(self):
        self.session_token = self._urlsafe_base_64()
        self.session_expiration = datetime.datetime.now() + datetime.timedelta(days=1)
        self.update_token = self._urlsafe_base_64()

    def verify_password(self, password):
        return bcrypt.checkpw(password.encode("utf8"), self.password_digest)

    # Checks if session token is valid and hasn't expired
    def verify_session_token(self, session_token):
        return session_token == self.session_token and datetime.datetime.now() < self.session_expiration

    def verify_update_token(self, update_token):
        return update_token == self.update_token

class Community(db.Model):
    __tablename__ = "community"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    users = db.relationship("User", secondary=association_users_communities, back_populates="communities")
    posts = db.relationship("Post", cascade="delete")
    chats = db.relationship("Chat")

    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "users": [u.serialize_basic() for u in self.users],
            "posts": [p.serialize_basic() for p in self.posts],
            "chats": [c.serialize_basic() for c in self.chats]
        }
    
    def serialize_basic(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String, nullable=False)
    edited = db.Column(db.Boolean, nullable=False)
    comments = db.relationship("Comment")
    tags = db.relationship("Tag", secondary=association_posts_tags, back_populates="posts")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    community_id = db.Column(db.Integer, db.ForeignKey("community.id"), nullable=False)

    def __init__(self, **kwargs):
        self.timestamp = kwargs.get("timestamp")
        self.content = kwargs.get("content", "")
        self.edited = kwargs.get("edited")
        self.user_id = kwargs.get("user_id")
        self.community_id = kwargs.get("community_id")

    def serialize(self):
        poster = User.query.filter_by(id=self.user_id).first()
        community = Community.query.filter_by(id=self.community_id).first()
        if poster is None or community is None:
            return None
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "content": self.content,
            "edited": self.edited,
            "poster": poster.serialize_basic(),
            "community": community.serialize_basic(),
            "comments": [c.serialize_basic() for c in self.comments],
            "tags": [t.serialize_basic() for t in self.tags]
        }
    
    def serialize_basic(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "content": self.content,
            "edited": self.edited
        }

class Comment(db.Model):
    __tablename__ = "comment"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String, nullable=False)
    edited = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)

    def __init__(self, **kwargs):
        self.timestamp = kwargs.get("timestamp")
        self.content = kwargs.get("content", "")
        self.edited = kwargs.get("edited")
        self.user_id = kwargs.get("user_id")
        self.post_id = kwargs.get("post_id")

    def serialize(self):
        commenter = User.query.filter_by(id=self.user_id).first()
        post = Post.query.filter_by(id=self.post_id).first()
        if commenter is None or post is None:
            return None
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "content": self.content,
            "edited": self.edited,
            "commenter": commenter.serialize_basic(),
            "post": post.serialize_basic()
        }
    
    def serialize_basic(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "content": self.content,
            "edited": self.edited
        }

class Tag(db.Model):
    __tablename__ = "tag"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    posts = db.relationship("Post", secondary=association_posts_tags, back_populates="tags")

    def __init__(self, **kwargs):
        self.description = kwargs.get("description", "")

    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
            "posts": [p.serialize_basic() for p in self.posts]
        }
    
    def serialize_basic(self):
        return {
            "id": self.id,
            "description": self.description
        }
    
class Chat(db.Model):
    __tablename__ = "chat"
    id = db.Column(db.Integer, primary_key=True)
    community_id = db.Column(db.Integer, db.ForeignKey("community.id"), nullable=False)
    users = db.relationship("User", secondary=association_users_chats, back_populates="chats")
    messages = db.relationship("Message", cascade="delete")

    def __init__(self, **kwargs):
        self.community_id = kwargs.get("community_id")
    
    def serialize(self):
        community = Community.query.filter_by(id=self.community_id).first()
        if community is None:
            return None
        return {
            "id": self.id,
            "community": community.serialize_basic(),
            "users": [u.serialize_basic() for u in self.users],
            "messages": [m.serialize_basic() for m in self.messages]
        }

    def serialize_basic(self):
        community = Community.query.filter_by(id=self.community_id).first()
        if community is None:
            return None
        return {
            "id": self.id,
            "community": community.serialize_basic(),
            "users": [u.serialize_basic() for u in self.users]
        }

class Message(db.Model):
    __tablename__ = "message"
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String, nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    receivers = db.relationship("User", secondary=association_users_messages_received, back_populates="messages_received")
    chat_id = db.Column(db.Integer, db.ForeignKey("chat.id"), nullable=False)

    def __init__(self, **kwargs):
        self.timestamp = kwargs.get("timestamp")
        self.content = kwargs.get("content")
        self.sender_id = kwargs.get("sender_id")
        self.chat_id = kwargs.get("chat_id")
    
    def serialize(self):
        sender = User.query.filter_by(id=self.sender_id).first()
        chat = Chat.query.filter_by(id=self.chat_id).first()
        if sender is None or chat is None:
            return None
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "content": self.content,
            "sender": sender.serialize_basic(),
            "receivers": [r.serialize_basic() for r in self.receivers],
            "chat": chat.serialize_basic()
        }

    def serialize_basic(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "content": self.content
        }
