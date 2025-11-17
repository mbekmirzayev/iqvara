from users.models.blogs import Blog, Comment, Step
from users.models.courses import Category, Course, Section, Enrollment, Lesson, Review
from users.models.payment import Payment, Promocode
from users.models.setting import FAQ, Setting , Device
from users.models.tags import Tag
from users.models.users import User

__all__ = [
    'Course', 'Category', 'Setting', 'Blog', 'Enrollment', 'User', 'Payment',
    'Lesson', 'Section', 'Review', 'Step', 'Comment',  'FAQ',
    'Tag', 'Promocode', 'Device'
]