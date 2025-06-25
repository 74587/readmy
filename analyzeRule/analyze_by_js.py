"""
参考自 qingyuedu: book/webBook/analyzeRule/AnalyzeByJs.kt
实现 JS 规则的内容提取

本实现基于 PyMiniRacer，支持执行 JS 片段。你也可以用 PyExecJS 或 Node.js 子进程等替代。
"""

from .analyze_by_base import AnalyzeByBase
from typing import List, Any, Optional

try:
    from py_mini_racer import py_mini_racer
except ImportError:
    py_mini_racer = None

class AnalyzeByJS(AnalyzeByBase):
    def extract(
        self,
        content: str,
        rule: str,
        context_vars: Optional[dict] = None,
        **kwargs
    ) -> List[Any]:
        """
        用 JavaScript 代码处理内容

        :param content: 可作为 JS 上下文变量传入
        :param rule: JS 代码（如 'function main(content) { ...; return result; }; main(content)'）
        :param context_vars: 额外的上下文变量字典
        :return: 结果（列表形式）
        """
        if not py_mini_racer:
            raise ImportError("py_mini_racer is not installed. Please install with 'pip install py-mini-racer'.")

        try:
            ctx = py_mini_racer.MiniRacer()
            # 注入 context_vars 和 content
            js_globals = context_vars.copy() if context_vars else {}
            js_globals['content'] = content
            # 将变量定义注入到 JS 上下文
            for k, v in js_globals.items():
                # 只支持基础类型，复杂结构需自行序列化
                if isinstance(v, str):
                    ctx.eval(f"var {k} = `{v.replace('`', '\\`')}`;")
                elif isinstance(v, (int, float)):
                    ctx.eval(f"var {k} = {v};")
                elif isinstance(v, (dict, list)):
                    import json
                    ctx.eval(f"var {k} = {json.dumps(v)};")
                else:
                    continue
            # 执行 rule（建议 rule 里是 return 一个值的 JS 表达式）
            result = ctx.eval(rule)
            # 返回列表形式以统一结构
            return [result] if not isinstance(result, list) else result
        except Exception as e:
            # 可根据需要记录日志
            return []