import os
from app import create_app

app = create_app(os.getenv('ENV', 'dev'))  # 创建应用，从环境变量获取环境名称

# 在Python中，__name__是一个特殊的内置变量，它表示当前模块的名称。
# 当你直接运行一个Python文件时，Python会将__name__设置为字符串'__main__'。
# 但如果这个文件被作为模块导入到其他文件中，__name__的值就会是该模块的名称（通常是文件名，不含.py后缀）。

# 这段代码的作用是：只有当你直接运行run.py文件时（而不是作为模块导入时），才会执行app.run(debug=True)，启动Flask应用服务器。
# 这是一种常见的Python设计模式，用于区分直接执行和被导入的情况。
if __name__ == '__main__':  # 当直接运行此文件时
    app.run()  # 运行应用