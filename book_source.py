"""
参考自 qingyuedu 项目：
- book/model/BookSource.kt：定义了书源的所有核心字段和注释
- 仅保留服务端聚合必需字段，字段命名和功能均与原项目一一对应
"""

from typing import Optional, Dict

class BookSource:
    """
    书源规则结构体
    参考自 qingyuedu: book/model/BookSource.kt
    """

    def __init__(
        self,
        name: str,                        # 书源名称
        url: str,                         # 书源主页/根地址
        enabled: bool = True,             # 是否启用，参考 bookSource.enabled
        group: Optional[str] = None,      # 分组，参考 bookSource.bookSourceGroup
        type: int = 0,                    # 类型（0文本，1音频），参考 bookSource.bookSourceType

        # 搜索相关
        search_url: Optional[str] = None,     # 搜索接口URL，参考 bookSource.searchUrl
        rule_search: Optional[str] = None,    # 搜索结果解析规则，参考 bookSource.ruleSearch

        # 发现/推荐
        explore_url: Optional[str] = None,    # 发现页URL，参考 bookSource.exploreUrl
        rule_explore: Optional[str] = None,   # 发现页解析规则，参考 bookSource.ruleExplore

        # 详情页
        rule_book_info: Optional[str] = None, # 详情页解析规则，参考 bookSource.ruleBookInfo

        # 目录页
        rule_toc: Optional[str] = None,       # 目录页解析规则，参考 bookSource.ruleToc

        # 正文页
        rule_content: Optional[str] = None,   # 正文页解析规则，参考 bookSource.ruleContent

        # 其它可选
        login_url: Optional[str] = None,      # 登录地址，参考 bookSource.loginUrl
        login_check_js: Optional[str] = None, # 登录检测JS，参考 bookSource.loginCheckJs
        js_lib: Optional[str] = None,         # 全局自定义JS，参考 bookSource.jsLib
        cover_decode_js: Optional[str] = None,# 封面解密JS，参考 bookSource.coverDecodeJs
        header: Optional[Dict[str, str]] = None, # 自定义请求头，参考 bookSource.header
        enabled_cookie_jar: bool = False,     # 是否自动保存cookie，参考 bookSource.enabledCookieJar
        comment: Optional[str] = None         # 书源注释，参考 bookSource.bookSourceComment
    ):
        self.name = name
        self.url = url
        self.enabled = enabled
        self.group = group
        self.type = type

        self.search_url = search_url
        self.rule_search = rule_search

        self.explore_url = explore_url
        self.rule_explore = rule_explore

        self.rule_book_info = rule_book_info
        self.rule_toc = rule_toc
        self.rule_content = rule_content

        self.login_url = login_url
        self.login_check_js = login_check_js
        self.js_lib = js_lib
        self.cover_decode_js = cover_decode_js
        self.header = header or {}
        self.enabled_cookie_jar = enabled_cookie_jar
        self.comment = comment

    def to_dict(self):
        """
        导出为 JSON 字典结构
        """
        return {
            "name": self.name,
            "url": self.url,
            "enabled": self.enabled,
            "group": self.group,
            "type": self.type,
            "search_url": self.search_url,
            "rule_search": self.rule_search,
            "explore_url": self.explore_url,
            "rule_explore": self.rule_explore,
            "rule_book_info": self.rule_book_info,
            "rule_toc": self.rule_toc,
            "rule_content": self.rule_content,
            "login_url": self.login_url,
            "login_check_js": self.login_check_js,
            "js_lib": self.js_lib,
            "cover_decode_js": self.cover_decode_js,
            "header": self.header,
            "enabled_cookie_jar": self.enabled_cookie_jar,
            "comment": self.comment,
        }