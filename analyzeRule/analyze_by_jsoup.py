"""
参考自 qingyuedu: book/webBook/analyzeRule/AnalyzeByJSoup.kt
实现 CSS Selector 规则的内容提取

Python 实现采用 BeautifulSoup（功能与 JSoup 类似）
"""

from .analyze_by_base import AnalyzeByBase
from bs4 import BeautifulSoup
from typing import List, Any, Optional

class AnalyzeByJSoup(AnalyzeByBase):
    def extract(
        self,
        content: str,
        rule: str,
        return_type: str = "auto",  # "auto", "text", "html", "attr"
        attr: Optional[str] = None,
        **kwargs
    ) -> List[Any]:
        """
        用 CSS Selector 提取内容

        :param content: HTML 文本
        :param rule: CSS Selector 规则
        :param return_type: 返回类型 ("auto", "text", "html", "attr")
        :param attr: 若想直接提取属性，可指定属性名
        :return: 匹配结果列表
        """
        try:
            soup = BeautifulSoup(content, "lxml")
            elements = soup.select(rule)
            results = []

            for el in elements:
                if attr:
                    results.append(el.get(attr, ""))
                elif return_type == "text":
                    results.append(el.get_text())
                elif return_type == "html":
                    results.append(str(el))
                else:  # auto
                    # 如果rule以::text结尾或元素无嵌套，则返回文本，否则返回html
                    # 这里简单处理，实际可根据需求细化
                    results.append(el.get_text() if len(el.contents) == 1 and isinstance(el.contents[0], str) else str(el))
            return results
        except Exception as e:
            # 可根据需要记录日志
            return []