"""
参考自 qingyuedu: book/webBook/analyzeRule/AnalyzeByXPath.kt
实现 XPath 规则的内容提取
"""

from .analyze_by_base import AnalyzeByBase
from lxml import etree
from typing import List, Any, Optional, Union

class AnalyzeByXPath(AnalyzeByBase):
    def extract(
        self,
        content: str,
        rule: str,
        return_type: str = "auto",  # "auto", "text", "html", "attr"
        attr: Optional[str] = None,
        **kwargs
    ) -> List[Any]:
        """
        用 XPath 表达式提取内容

        :param content: HTML/XML 文本
        :param rule: XPath 规则
        :param return_type: 返回类型 ("auto", "text", "html", "attr")
        :param attr: 若想直接提取属性，可指定属性名
        :return: 匹配结果列表
        """
        try:
            tree = etree.HTML(content)
            elements = tree.xpath(rule)
            results = []

            for el in elements:
                # 如果直接是属性/文本，不是Element对象
                if not hasattr(el, "tag"):
                    results.append(el)
                else:
                    if attr:
                        results.append(el.attrib.get(attr, ""))
                    elif return_type == "text":
                        results.append("".join(el.itertext()))
                    elif return_type == "html":
                        results.append(etree.tostring(el, encoding="unicode", with_tail=False))
                    else:  # auto
                        # 如果结果是Element，且XPath表达式以/text()结尾，返回纯文本，否则返回html
                        if rule.strip().endswith("text()"):
                            results.append("".join(el.itertext()))
                        else:
                            results.append(etree.tostring(el, encoding="unicode", with_tail=False))
            return results
        except Exception as e:
            # 可根据需要记录日志
            return []