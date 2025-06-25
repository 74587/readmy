"""
参考 qingyuedu: book/webBook/analyzeRule/AnalyzeRule.kt
负责统一调度、规则类型识别、分发到具体分析器
"""
from typing import Any, List, Optional
from .analyze_by_xpath import AnalyzeByXPath
from .analyze_by_jsoup import AnalyzeByJSoup
from .analyze_by_regex import AnalyzeByRegex
from .analyze_by_jsonpath import AnalyzeByJSonPath
from .analyze_by_js import AnalyzeByJS

class AnalyzeRule:
    @staticmethod
    def detect_rule_type(rule: str, content_type: str = "html") -> str:
        if rule.startswith("$.") or rule.startswith("$["):
            return "jsonpath"
        elif rule.startswith("//"):
            return "xpath"
        elif rule.startswith(".") or rule.startswith("#"):
            return "css"
        elif rule.startswith("regex:"):
            return "regex"
        elif rule.startswith("js:"):
            return "js"
        return "xpath" if content_type == "html" else "jsonpath"

    @classmethod
    def extract(cls, content: str, rule: str, content_type: str = "html", **kwargs) -> List[Any]:
        rule_type = cls.detect_rule_type(rule, content_type)
        if rule_type == "xpath":
            return AnalyzeByXPath().extract(content, rule, **kwargs)
        elif rule_type == "css":
            return AnalyzeByJSoup().extract(content, rule, **kwargs)
        elif rule_type == "regex":
            pattern = rule[6:] if rule.startswith("regex:") else rule
            return AnalyzeByRegex().extract(content, pattern, **kwargs)
        elif rule_type == "jsonpath":
            return AnalyzeByJSonPath().extract(content, rule, **kwargs)
        elif rule_type == "js":
            js_code = rule[3:] if rule.startswith("js:") else rule
            return AnalyzeByJS().extract(content, js_code, **kwargs)
        else:
            raise ValueError(f"Unknown rule type: {rule_type}")

    @classmethod
    def extract_first(cls, content: str, rule: str, content_type: str = "html", **kwargs) -> Optional[Any]:
        results = cls.extract(content, rule, content_type, **kwargs)
        return results[0] if results else None