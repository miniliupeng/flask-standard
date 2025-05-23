# Flask应用项目

这是一个使用Flask框架构建的Web应用项目，采用规范的目录结构设计。

## 目录结构

```
flask-standard/
├── app/                    # 应用主目录
│   ├── config/             # 配置文件
│   ├── controllers/        # 控制层
│   ├── models/             # 数据模型层
│   ├── services/           # 业务逻辑层
│   ├── static/             # 静态文件（CSS, JS, 图片）
│   ├── templates/          # 模板文件
│   ├── utils/              # 工具包
│   ├── views/              # 视图层
│   └── __init__.py         # 应用初始化
├── docs/                   # 文档
├── instance/               # 实例配置（不进入版本控制）
├── migrations/             # 数据库迁移
├── .env.example            # 环境变量示例
├── tests/                  # 测试代码
├── requirements.txt        # 依赖清单
├── run.py                  # 运行脚本
└── README.md               # 项目说明
```

## 安装和运行

1. 创建虚拟环境：

```bash
conda create --name venv python=3.11
```

2. 激活虚拟环境：

```bash
source activate venv
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
flask db init   # 初始化迁移存储库
flask db migrate -m "初始化数据库"  # 生成初始迁移文件
flask db upgrade   # 同步模型表结构到数据库
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

## 基础知识

### 路由规则

  @app.route("/")
  @app.route("/user/list", methods=['GET', 'POST'])

### 接收参数

#### url参数/user/info?userId=1
  userId = request.args.get('userId')
#### 表单参数
  request.form.get("userName")
#### 请求正文参数
  request.get_data()
#### 路由参数
  @app.route("/user/get/<userId>", methods=['GET'])
  def user_get(userId):

  路由参数-int类型
  @app.route("/user/get/<int:userId>", methods=['GET'])

### 蓝图
  user = Blueprint('user', __name__, url_prefix="/sys/user")
### 全局请求拦截
  @app.before_request
### 统一异常处理
  @app.errorhandler(404)
  @app.errorhandler(Exception)

## 开发流程

### 环境配置

### 控制层

客户端发起请求->控制层拿到请求参数->控制层调用处理业务方法->控制层返回处理结果。

#### 规范化控制层的整个请求入参出参

#### 参数校验


### 数据模型层

#### 模型基类

#### 数据转化


### 业务逻辑层

#### 业务逻辑基类

#### SQLAlchemy默认开启事务，但需要显式提交
  事务-批量新增用户，有重复name，会全部失败
  不开启事务-批量新增用户，前两条记录插入成功，未回滚


### 权限拦截

#### 使用Flask自带的@app.before_request装饰器

#### 自定义装饰器

#### Token认证

Token存储策略:
  CacheTokenStrategy: 缓存存储策略,一般开发阶段常用的方案，服务重启后，token数据会丢失。
  MysqlTokenStrategy: Mysql存储策略，不想多安装一个redis中间件的的另一种token持久化方案
  RedisTokenStrategy: redis存储策略，建议使用的方案

### 日志处理

#### 日志处理
  控制台输出StreamHandler
  按照日志大小进行切分RotatingFileHandler
  按照日期进行切分TimedRotatingFileHandler

### 异常处理
@errorhandler

ExceptionConfig异常配置类
ErrorEnum 错误码枚举基类
GlobalErrorEnum 全局错误码，定义一些常用的错误码
BizException 自定义异常，方便全局捕获
AssetTool 异常断言工具类，用于抛出自定义异常的

### 单元测试

### 代码生成

#### Db First      将数据库表映射成ORM模型  关键的技术就是代码生成器——通过读取数据库元数据，然后定制模板，使用模板引擎输出自定义页面或文件的工具
即Database First是基于已存在的数据库，利用某些工具（如代码生成器）创建实体类，数据库对象与实体类的匹配关系等，你也可以手动修改这些自动生成的代码及匹配文件。也就是从一个数据库开始，然后生成实体框架和相应代码。 


#### Model First 
这里说的Model不是SQLAlchemy中的model，而是先利用某些工具（如UML设计工具）设计出可视化的实体数据模型及他们之间的关系，然后再根据这些实体、关系去生成数据库对象及相关代码文件。


#### Code First    根据ORM模型转成数据库表
Code First 这种方式需要先写一些代码，如实体对象，数据关系等，然后根据已有的代码描述，自动创建数据对象。但其实这种方法与Model First是非常类似的。我们自己写的代码，其实就是用代码表示实体模型，而Model First是用可视化的方式描述了实体模型。

Flask-Migrate