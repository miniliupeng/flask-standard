# Flask应用项目

这是一个使用Flask框架构建的Web应用项目，采用规范的目录结构设计。

## 目录结构

```
flask-mcp/
├── app/                    # 应用主目录
│   ├── config/             # 配置文件
│   ├── models/             # 数据模型
│   ├── static/             # 静态文件（CSS, JS, 图片）
│   ├── templates/          # 模板文件
│   ├── utils/              # 工具函数
│   ├── views/              # 视图函数和路由
│   └── __init__.py         # 应用初始化
├── instance/               # 实例配置（不进入版本控制）
├── tests/                  # 测试代码
├── docs/                   # 文档
├── .env.example            # 环境变量示例
├── requirements.txt        # 依赖清单
├── run.py                  # 运行脚本
└── README.md               # 项目说明
```

## 安装和运行

1. 创建虚拟环境：

```bash
python -m venv venv
```

2. 激活虚拟环境：

- Windows:
```bash
venv\Scripts\activate
```

- Linux/Mac:
```bash
source venv/bin/activate
```

3. 安装依赖：

```bash
pip install -r requirements.txt
```

4. 设置环境变量：

```bash
# Windows
copy .env.example .env

# Linux/Mac
cp .env.example .env
```

5. 初始化数据库：

```bash
flask db init
flask db migrate -m "初始化数据库"
flask db upgrade
```

6. 运行应用：

```bash
python run.py
```

应用将在 http://127.0.0.1:5000/ 运行。

## 测试

运行测试：

```bash
python -m pytest
```

## 功能特点

- 模块化的应用结构
- 基于蓝图的路由管理
- SQLAlchemy ORM数据库支持
- 用户认证系统
- 响应式前端设计
- 单元测试支持

## 许可证

MIT 