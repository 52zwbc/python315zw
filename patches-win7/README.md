# Win7/Vista 兼容补丁（取自 PythonVista v3.15.0）

来源：https://github.com/adang1345/PythonVista （tag `v3.15.0`，`patches/` 目录）。
该仓库发布的是补丁包而非改完的完整源码：从 python.org 官方 sdist 出发，
按 `Notes.md` 中 Python 3.15 一节打补丁，再跑 `Tools/msi/buildrelease.bat`。

## 补丁清单（3.15.0 用这 5 个官方补丁 + 1 个自制）

| 补丁 | 作用 |
|---|---|
| `add-dll-8.patch` | 随包安装 `api-ms-win-core-path-l1-1-0.dll`（Vista/Win7 运行必需） |
| `restore-vista-handling-13.patch` | 恢复 Vista/SP2 兼容 |
| `build-full-installer-9.patch` | 切到 `full.wixproj` 打完整离线包（含调试符号/二进制、UCRT、自由线程版、x64 tail-call 解释器、JIT） |
| `fix-launcher-2.patch` | py 启动器 Win7 兼容 + 随包带 dll |
| `fix-tcltk-3.patch` | 用支持 Vista 的 Tcl/Tk 依赖（见 python/cpython#124111） |
| `zh-bundle-win7.patch` | 自制：将上面两个补丁对 `Default.wxl` 的改动汉化后合入本仓库版本 |

3.15 原生支持 VS2026（v145 工具集），无需 `support-vs-*` 补丁。
未采用其余补丁（3.15 一节未要求）。

## 应用顺序（workflow 中执行，勿调换）

```
add-dll-8 → fix-tcltk-3 → fix-launcher-2 → build-full-installer-9 → restore-vista-13 → zh-bundle-win7
```

`add-dll-8` 须在 `fix-tcltk-3` 之前（同改 `get_externals.bat`）。
`build-full-installer-9` 与 `restore-vista-13` 对 `Tools/msi/bundle/Default.wxl`
的 hunks 用 `--exclude` 跳过，改由 `zh-bundle-win7.patch` 以汉化形式加入：
`FailureOldOS`（Win10 门槛）拆为 6 条 Win7/Vista/Server 中文提示（bootstrapper cpp
引用了这些新 ID，缺失会导致构建失败）；3 条 `Include_*` 由“下载”改为“安装”、
VS 2017→VS 2026（full 离线包语义；自由线程版 3.15 已去“实验性”）。
`restore-vista-13` 对 `Default.thm` 的 hunk（去 Deprecation 横幅）与本仓库成功页
双图正交，直接应用。

## 与中文汉化的合并说明

- 其余补丁文件与中文改动（`Parser/pegen.c`、`Python/bltinmodule.c`、`Objects/*`、
  `Modules/_io/*`、`Lib/_zh_builtins.py`）无重叠，直接应用。
- 本版按 python313zw 方式暂不汉化标准库（无 `_zh_stdlib.py`），无运行横幅（`Modules/main.c` 未动）。
- 3.15 新增汉化：软关键字 `惰性~lazy`（`Parser/pegen.c`）、`哨兵~sentinel`、
  `不可变字典~frozendict`（`Lib/_zh_builtins.py` + `frozendict_methods` 中文方法）。
