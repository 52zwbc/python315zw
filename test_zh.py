# -*- coding: utf-8 -*-
"""中文别名冒烟测试: 打印 ~ print, 如果 ~ if, 惰性 ~ lazy, 哨兵 ~ sentinel, 不可变字典 ~ frozendict"""
打印("你好，中文Python!")

如果 True:
    打印("如果 True 分支 OK")
else:
    打印("不应该到这里")

x = 5
如果 x == 1:
    打印("一")
elif x == 5:
    打印("五-OK")
else:
    打印("其他")

# 打印参数透传
打印("a", "b", sep="-", end="!\n")

# 三元表达式也可用 如果 (与 if 同 token)
y = 10 如果 True else 20
assert y == 10, y

# 中文库管理别名: import 库 走 ku.py(ASCII 名, 避 WiX codepage 限制)
import 库 as _ku_test
assert _ku_test.构建pip参数("安装", ["requests"])[0:2] == ["install", "requests"]
assert "tuna.tsinghua" in _ku_test.构建pip参数("安装", ["requests"])[-1]
assert _ku_test.构建pip参数("卸载", ["requests"]) == ["uninstall", "requests", "-y"]
assert _ku_test.构建pip参数("帮助", []) is None

# 3.15 新增: 惰性 ~ lazy (软关键字, 仅模块级可用; 中文词之间须空格分词, 与 如果 等一致)
惰性 导入 json 命名为 _jl
assert _jl.loads('{"a": 1}')["a"] == 1
惰性 从 json 导入 loads 命名为 _loads
assert _loads('{"b": 2}')["b"] == 2
# 惰性不可用于函数内 (与 lazy 同限制)
try:
    compile("def f():\n    惰性 导入 json\n", "<test>", "exec")
    raise SystemExit("惰性在函数内应报 SyntaxError")
except SyntaxError:
    pass

# 3.15 新增: 哨兵 ~ sentinel
缺失 = 哨兵("缺失")
assert 缺失.__name__ == "缺失"
assert 缺失 is 缺失
assert isinstance(缺失, 哨兵)
assert repr(缺失) == "缺失"
assert isinstance(int | 缺失, object)

# 3.15 新增: 不可变字典 ~ frozendict
配置 = 不可变字典(主机="db", 端口=5432)
assert 配置["主机"] == "db"
assert 配置.取值("端口") == 5432
assert 配置.复制() == 配置
assert len(配置.所有键()) == 2
assert len(配置.键值对()) == 2
assert len(配置.所有值()) == 2
hash(配置)
try:
    配置["新"] = 1
    raise SystemExit("不可变字典应拒绝修改")
except TypeError:
    pass

打印("全部通过!")
