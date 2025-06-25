# readmy 后端“规则驱动解析”多书源聚合路线图

## 目标
- 在服务器端实现对多种书源的统一聚合与解析
- 支持多种解析规则（XPath/CSS/正则/JSONPath/JS）
- 输出统一格式，供阅读软件使用
- 不依赖前端，适用于“聚合书源服务”

---

## 路线图

### 1. 解析器能力完善与测试
- [ ] 为每种规则类型（XPath/CSS/正则/JSONPath/JS）完善 `extract` 方法和容错处理
- [ ] 补全或优化各类内容解析器的单元测试
- [ ] 增强异常捕获与日志记录

### 2. 书源配置管理
- [ ] 设计/完善 BookSource 结构，支持主流阅读软件书源字段
- [ ] 实现书源的批量导入、导出、校验与格式转换（支持青阅读、阅读3.x等常见格式）
- [ ] 支持书源分组、启用/禁用、注释等管理功能

### 3. 聚合解析流程
- [ ] 实现多书源聚合：根据用户请求，在多个 BookSource 上并发/串行发起内容解析
- [ ] 统一聚合各书源返回的章节、正文、元数据等信息，去重、排序、补全
- [ ] 支持失败书源的错误提示与回退机制

### 4. 标准化输出接口
- [ ] 设计统一的API接口，如 `/search` `/bookinfo` `/toc` `/content`
- [ ] 支持输出为 JSON、YAML 等格式，并兼容主流阅读软件的书源格式（如 bookSource.json）
- [ ] 提供聚合结果的统一格式定义（字段/结构标准）

### 5. 配套工具与自动化
- [ ] 开发书源格式转换工具
- [ ] 提供命令行工具/脚本，便于批量解析和测试

### 6. 规则调试与兼容性扩展
- [ ] 支持扩展新的规则类型、增强对复杂页面和反爬机制的兼容

### 7. 服务部署与性能优化
- [ ] 部署为后台服务，支持高并发请求和队列机制
- [ ] 优化网络请求、缓存机制，减少重复抓取和解析

### 8. 文档与开发体验
- [ ] 完善项目文档，详细说明书源结构、API用法、二次开发接口
- [ ] 提供典型书源、调用示例和常见问题排查指引

---

## 最终实现效果
- 支持多书源聚合、自动适配各种规则，后端一站式解析
- 输出统一的标准书源/阅读数据格式，直接对接阅读软件
- 可持续扩展、易于维护、便于调试和管理

---

analyzeRule/
├── __init__.py
├── analyze_rule.py         # 统一调度入口（AnalyzeRule.kt）
├── analyze_by_xpath.py     # XPath 分析器（AnalyzeByXPath.kt）
├── analyze_by_jsoup.py     # CSS Selector 分析器（AnalyzeByJSoup.kt）
├── analyze_by_regex.py     # 正则分析器（AnalyzeByRegex.kt）
├── analyze_by_jsonpath.py  # JSONPath 分析器（AnalyzeByJSonPath.kt）
├── analyze_by_js.py        # JS 分析器（AnalyzeByJs.kt）
├── analyze_by_base.py      # 分析器基类（AnalyzeByBase.kt）
└── analyze_rule_factory.py # 工厂类（AnalyzeRuleFactory.kt）
