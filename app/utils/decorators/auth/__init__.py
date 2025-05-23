from functools import wraps

# from flask import abort

from app.utils.token import TokenStrategyFactory
from app.config.exception import AssertTool, GlobalErrorEnum


class HasPerm(object):
    """
    权限装饰器类
    """

    def __init__(self, access=None, name=None):
        self.access = access
        self.name = name

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            # 这里处理权限拦截的逻辑
            if not TokenStrategyFactory.check_token(self.access):
                # abort(403)
                AssertTool.raise_biz(GlobalErrorEnum.GL99990403)
            else:
                return func(*args, **kwargs)

        return wrapped_function
