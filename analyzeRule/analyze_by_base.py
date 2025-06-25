"""
参考 qingyuedu: book/webBook/analyzeRule/AnalyzeByBase.kt
定义所有分析器的基类和接口规范
"""
from abc import ABC, abstractmethod
from typing import Any, List

class AnalyzeByBase(ABC):
    @abstractmethod
    def extract(self, content: str, rule: str, **kwargs) -> List[Any]:
        """
        解析内容，返回匹配结果列表
        """
        pass