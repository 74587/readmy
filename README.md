# readmy

analyzeRule/
├── __init__.py
├── analyze_rule.py        # 统一调度入口（AnalyzeRule.kt）
├── analyze_by_xpath.py    # XPath 分析器（AnalyzeByXPath.kt）
├── analyze_by_jsoup.py    # CSS Selector 分析器（AnalyzeByJSoup.kt）
├── analyze_by_regex.py    # 正则分析器（AnalyzeByRegex.kt）
├── analyze_by_jsonpath.py # JSONPath 分析器（AnalyzeByJSonPath.kt）
├── analyze_by_js.py       # JS 分析器（AnalyzeByJs.kt）
├── analyze_by_base.py     # 分析器基类（AnalyzeByBase.kt）
└── analyze_rule_factory.py# 工厂类（AnalyzeRuleFactory.kt）
