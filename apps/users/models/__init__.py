from apps.shared.base import UUIDBaseModel, CreateBaseModel, SlugBaseModel
from apps.users.models.blogs import Blog, Step, Comment
from apps.users.models.courses import Category, Course, Lesson, Review
from apps.users.models.orders import Order
from apps.users.models.settings import Settings, FAQ
from apps.users.models.tags import Tag
from apps.users.models.users import User

__all__ = [
    'Course', 'Category', 'Settings', 'Blog', 'User', 'Order', 'Lesson' , 'Review', 'Step', 'Comment', 'FAQ'

]
