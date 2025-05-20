from flask import Blueprint, request, jsonify
from app.services.mcp_service import MCPService
from . import R

# 创建MCP蓝图
mcp_bp = Blueprint("mcp", __name__, url_prefix="/mcp")


@mcp_bp.route("/", methods=["GET"])
def index():
    """MCP主页"""
    system_info = MCPService.get_system_info()
    return R.data(system_info)


@mcp_bp.route("/status", methods=["GET"])
def status():
    """MCP状态"""
    system_status = MCPService.check_system_status()
    return R.data(system_status)


@mcp_bp.route("/info", methods=["GET"])
def info():
    """获取MCP信息"""
    return R.data(
        {
            "status": "success",
            "message": "MCP信息",
            "data": {
                "api_version": "1.0",
                "endpoints": [
                    {"path": "/mcp/", "method": "GET", "description": "MCP主页"},
                    {"path": "/mcp/status", "method": "GET", "description": "系统状态"},
                    {"path": "/mcp/info", "method": "GET", "description": "API信息"},
                ],
            },
        }
    )
