import pytest
from app import create_app
from app.models import db
from app.utils.token import TokenStrategyFactory

app = create_app("test")


# fixture的scope参数
# scope参数有四种，分别是'function','module','class','session'，默认为function。
#     function：每个test都运行，默认是function的scope
#     class：每个class的所有test只运行一次
#     module：每个module的所有test只运行一次
#     session：每个session只运行一次


@pytest.fixture
def client():
    # 装备一个客户端给test_控制层方法使用
    with app.test_client() as client:
        ctx = app.app_context()
        ctx.push()
        yield client  # this is where the testing happens!
        ctx.pop()


@pytest.fixture
def auth_client():
    """
    装备一个已授权的客户端给test_控制层方法使用
    :return:
    """
    with app.test_client() as client:
        ctx = app.app_context()
        ctx.push()
        token_strategy = TokenStrategyFactory.get_instance()
        data = token_strategy.set({"userId": 1, "userName": "admin"})
        # HTTP_KEY的方式存入全局请求头
        client.environ_base["HTTP_TOKEN"] = data.get("token")
        yield client  # this is where the testing happens!
        ctx.pop()


@pytest.fixture
def m_db():
    """
    装配db对象给test_模型层和服务逻辑层方法使用
    :return:
    """
    with app.app_context():
        yield db


# @pytest.fixture(scope="class")
# def m_table():
#     """
#     装配m_table对象给test_模型层和服务逻辑层方法使用
#     :return:
#     """
#     with app.app_context():
#         code_generator = CodeGenerator(app)
#         table = code_generator.build_table("t_role")
#         yield table
