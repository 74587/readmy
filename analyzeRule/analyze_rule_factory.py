"""
参考 qingyuedu: book/webBook/analyzeRule/AnalyzeRuleFactory.kt
根据规则字符串自动实例化对应分析器（如有需要可进一步细化）
"""
from .analyze_by_xpath import AnalyzeByXPath
from .analyze_by_jsoup import AnalyzeByJSoup
from .analyze_by_regex import AnalyzeByRegex
from .analyze_by_jsonpath import AnalyzeByJSonPath
from .analyze_by_js import AnalyzeByJS

class AnalyzeRuleFactory:
    @staticmethod
    def get_analyzer(rule: str, content_type: str = "html"):
        if rule.startswith("$.") or rule.startswith("$["):
            return AnalyzeByJSonPath()
        elif rule.startswith("//"):
            return AnalyzeByXPath()
        elif rule.startswith(".") or rule.startswith("#"):
            return AnalyzeByJSoup()
        elif rule.startswith("regex:"):
            return AnalyzeByRegex()
        elif rule.startswith("js:"):
            return AnalyzeByJS()
        return AnalyzeByXPath() if content_type == "html" else AnalyzeByJSonPath()