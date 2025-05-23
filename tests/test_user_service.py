from app.models.user import User
from app.services.user_service import UserService
from app.utils.validators.id_validator import IdForm


class TestUserService:
    """
    用户业务逻辑测试
    """

    def test_login(self, m_db):
        """
        测试登录
        :param m_db:
        :return:
        """
        user_service = UserService(db=m_db, model=User)
        assert user_service.login("lp", "123")

    def test_get_user(self, m_db):
        """
        测试通过id查询用户信息
        :param m_db:
        :return:
        """
        user_service = UserService(db=m_db, model=User)
        form = IdForm(data={"id": 1})
        assert user_service.get(form)
