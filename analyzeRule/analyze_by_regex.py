"""
参考自 qingyuedu: book/webBook/analyzeRule/AnalyzeByRegex.kt
实现正则表达式规则的内容提取
"""

from .analyze_by_base import AnalyzeByBase
import re
from typing import List, Any, Optional

class AnalyzeByRegex(AnalyzeByBase):
    def extract(
        self,
        content: str,
        rule: str,
        return_type: str = "auto",  # "auto", "group", "all"
        flags: Optional[int] = None,
        **kwargs
    ) -> List[Any]:
        """
        用正则表达式提取内容

        :param content: 原始文本
        :param rule: 正则表达式
        :param return_type: 返回类型 ("auto", "group", "all")
        :param flags: 可选，re.IGNORECASE 等
        :return: 匹配结果列表
        """
        try:
            # 处理正则标志
            re_flags = flags if flags is not None else 0

            pattern = re.compile(rule, re_flags)
            matches = pattern.findall(content)

            # 匹配对象为元组时（有分组），自动只返回第一个分组（仿照 qingyuedu 的常用用法）
            if matches and isinstance(matches[0], tuple):
                if return_type == "all":
                    return [match for match in matches]
                # 默认返回第一个分组
                return [match[0] for match in matches]
            return matches
        except Exception as e:
            # 可根据需要记录日志
            return []