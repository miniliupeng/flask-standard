from flask import Flask
from flask_migrate import Migrate

from app.config import config
from app.models import db

migrate = Migrate()  # 创建迁移实例


def create_app(env):  # 应用工厂函数
    app = Flask(__name__, instance_relative_config=True)  # 创建Flask应用实例,允许Flask应用从实例文件夹（instance folder）加载配置文件
    
    # 配置加载顺序：环境配置 > 实例配置 > 默认配置
    app.config.from_object(config[env])  # 默认配置：从对象加载配置
    app.config.from_pyfile("config.py", silent=True)  # 实例配置：从文件 instance/config.py 加载配置   silent=True参数表示如果文件不存在也不会报错

    db.init_app(app)  # 初始化数据库
    migrate.init_app(app, db)  # 初始化迁移

    # 导入模型以便Migrate能够检测到
    from app.models import User

    # 蓝图注册代码放在create_app函数内部而不是文件顶部的原因：
    # 1. 避免循环导入：这是最主要的原因。如果在文件顶部导入，可能会导致循环依赖问题，因为：
    #       蓝图(main_bp)可能依赖于app实例或其配置
    #       如果views模块中也导入了app包中的其他模块，就会形成循环导入
    # 2. 延迟导入：只在真正需要时才导入蓝图模块，遵循"按需导入"原则
    # 3. 应用工厂模式：符合Flask的应用工厂模式最佳实践，使应用实例创建和配置更加灵活
    # 4. 测试友好：使测试时可以轻松替换或模拟蓝图，方便单元测试

    # 注册蓝图
    from app.views import main_bp
    from app.controllers.auth_controller import auth_bp
    from app.controllers.user_controller import user_bp
    from app.controllers.mcp_controller import mcp_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(mcp_bp)

    return app  # 返回配置好的应用
