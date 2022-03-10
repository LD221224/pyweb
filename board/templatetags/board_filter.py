# 빼기 필터 만들기
from django import template
register = template.Library()


@register.filter
def sub(value, arg):
    # 기존값 - arg
    # 사용 ex) value|sub:3 (= value - 3)
    return value - arg
