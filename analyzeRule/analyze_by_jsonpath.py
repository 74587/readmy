"""
参考自 qingyuedu: book/webBook/analyzeRule/AnalyzeByJSonPath.kt
实现 JSONPath 规则的内容提取
"""

from .analyze_by_base import AnalyzeByBase
from typing import List, Any
import json

try:
    from jsonpath_ng import parse as jsonpath_parse
except ImportError:
    jsonpath_parse = None

class AnalyzeByJSonPath(AnalyzeByBase):
    def extract(
        self,
        content: str,
        rule: str,
        **kwargs
    ) -> List[Any]:
        """
        用 JSONPath 表达式提取内容

        :param content: JSON 字符串
        :param rule: JSONPath 规则（如 $.data[*].name）
        :return: 匹配结果列表
        """
        if not jsonpath_parse:
            raise ImportError("jsonpath-ng is not installed. Please install with 'pip install jsonpath-ng'.")
        try:
            data = json.loads(content)
            expr = jsonpath_parse(rule)
            return [match.value for match in expr.find(data)]
        except Exception as e:
            # 可根据需要记录日志
            return []