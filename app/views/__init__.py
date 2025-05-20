from flask import Blueprint

main_bp = Blueprint("main", __name__)  # 创建主蓝图

# 导入路由模块
from . import main  # 导入主页面视图
from . import auth  # 导入认证视图
from . import user  # 导入用户视图

# 这种导入方式的目的是：
# 1. 先创建蓝图对象
# 2. 然后导入各视图模块，让它们使用已定义好的蓝图
# 3. 视图模块中的路由会自动注册到蓝图上
# 4. 避免循环导入问题

# 这是一个特殊的导入模式，其目的是：
# 执行main.py文件中的所有代码
# 不直接使用main.py中的任何对象
# 允许main.py文件中的代码使用__init__.py中预先定义的main_bp对象
# 执行顺序：
# __init__.py中创建main_bp蓝图对象
# 然后导入main.py
# main.py中的代码使用已创建好的main_bp定义路由
# 这种导入方式类似于"触发执行"，目的不是获取导入的内容，而是让被导入文件中的代码能够运行并使用当前环境中的对象。
