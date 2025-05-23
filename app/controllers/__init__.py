# 控制层
from flask import jsonify


#规范化控制层的整个请求入参出参
class R:
    @staticmethod
    def success(msg="成功"):
        mDict = {"code": 0, "msg": msg}
        return jsonify(mDict)

    @staticmethod
    def fail(msg, code=9999):
        mDict = {"code": code, "msg": msg}
        return jsonify(mDict)

    @staticmethod
    def data(data):
        mDict = {"code": 0, "msg": "成功", "data": data}
        return jsonify(mDict)
