"""
配置包 - 按环境分类的应用配置
"""

from .development import DevelopmentConfig
from .testing import TestingConfig
from .production import ProductionConfig

# 配置映射字典，用于根据环境名称选择对应配置
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
