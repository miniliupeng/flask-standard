"""
配置包 - 按环境分类的应用配置
"""

from .dev import Development
from .test import Test
from .pro import Production

# 配置映射字典，用于根据环境名称选择对应配置
config = {
    "dev": Development,
    "test": Test,
    "pro": Production,
}
