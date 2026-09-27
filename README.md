# Python 爬虫部分

个人学习 Python 爬虫的练习代码合集，内容从 `requests` 入门，逐步到 xpath/jsonpath 解析、自动化爬虫、多线程采集，再到 JS 逆向与登录逆向。代码以亲手实践为主，属练习性质。

- GitHub：<https://github.com/wangfuhong666/python-spider>
- Gitee：<https://gitee.com/wang_fuhong/python-spider>

## 环境与依赖

- Python 3（开发环境为 3.13）
- 主要第三方库：

```bash
pip install requests lxml jsonpath jsonpath-ng DrissionPage PyExecJS loguru openpyxl beautifulsoup4 moviepy
```

| 依赖 | 用途 |
| --- | --- |
| `requests` | 发送 HTTP 请求，本仓库用得最多的库 |
| `lxml` | xpath 解析 HTML |
| `jsonpath` / `jsonpath_ng` | 从 JSON 响应中按表达式提取数据 |
| `DrissionPage` | 浏览器自动化采集（替代 Selenium 的方案） |
| `PyExecJS` | 在 Python 里执行 JS 代码，JS 逆向的核心工具 |
| `loguru` | 日志输出 |
| `openpyxl` | 读写 Excel |
| `beautifulsoup4` | HTML 解析（少量案例使用） |
| `moviepy` | 音视频处理（音视频分离下载的案例） |

补充说明：

- `execjs` 需要本机已安装 **Node.js**，否则无法执行 JS。
- `DrissionPage` 需要本机有 **Chrome / Edge** 浏览器。
- 超级鹰打码平台的 SDK 已内置在 `09_过验证码\Chaojiying_Python`，无需额外安装。

## 目录结构

| 目录 | 文件数 | 内容 |
| --- | ---: | --- |
| `01基础复习` | 1 | 基础语法复习 |
| `03-requests请求参数` | 19 | `requests` 基础、请求头与 Cookie 设置、反爬情况下的音视频下载、爬虫练习 1~12 |
| `04-json模块与jsonpath语法规则` | 9 | `json` 模块、`jsonpath` 语法、正则复习 |
| `05-csv读写与案例实战` | 2 | `csv` 模块读写与实战案例 |
| `06 07-xpath解析&案例实战` | 4 | `lxml` + xpath 解析、多页数据采集实战 |
| `08自动化爬虫` | 6 | `DrissionPage` 自动化采集，含百度图片爬取练习 |
| `09_过验证码` | 4 | 打码平台（超级鹰）接口接入，含官方 SDK |
| `10爬虫案例实战` | 7 | 综合案例实战，含 AI 示范代码 |
| `10线程` | 1 | 线程入门 |
| `11线程` | 6 | 单线程 / 多线程 / 多进程 / 线程池的性能对比，以及音乐下载实战 |
| `11_初始js逆向` | 8 | base64 编码、MD5、AES、DES 等常见加密算法与 JS 调用 |
| `12js逆向入门案例` | 2 | `execjs` 执行 JS 的入门案例 |
| `13_酷狗音乐逆向案例` | 5 | 酷狗音乐搜索接口逆向 |
| `14_宁波大学案例` | 3 | 校园网站数据采集案例（含 AI 示范代码） |
| `15_杭州空气质量查询js逆向练习` | 4 | 请求参数加密/解密的 JS 逆向练习 |
| `16_逆向登录` | 4 | 登录流程逆向，含 RSA 加密与 eval 混淆处理 |
| `17_DP自动化` | 1 | `DrissionPage` 自动化 |
| `DP监听` | 2 | `DrissionPage` 网络请求监听 |
| `爬虫案例练习` | 17 | 综合练习：top500 数据、参考文献、外来物种入侵多网站、拾光 AI 画板、摸头表情包自动处理、IOI 2026 实时排行榜等 |

## 运行方式

```bash
python 文件名.py
```

多数脚本直接运行即可；`12js逆向入门案例`、`16_逆向登录` 等依赖同目录下的 `.js` 文件（由 `execjs` 读取执行），请保持目录结构完整。

## 关于仓库内容

- **仓库只保存代码与小型数据**（`.py`、`.js`、`.html`、`.csv`、`.json`、`.txt`、`.xlsx` 等）。爬虫练习过程中下载的**音频、图片、压缩包**已被 `.gitignore` 排除——它们占了近 290 MB，且涉及版权，不适合放进公开仓库。
- 采集结果类的 `csv` / `xlsx` 文件保留在仓库里，作为练习产物留档。
- 部分脚本中的 **Cookie 与登录态**是调试时从浏览器复制粘贴的，仅供本机学习使用，多数已过期；如果你要复用这些脚本，请替换成自己的。
- 本仓库代码**仅供学习与个人练习**。抓取任何网站前请阅读该网站的 `robots.txt` 与服务条款，控制请求频率，不要用于商业用途或对目标站点造成压力。

## 自动同步（GitHub ↔ Gitee）

本仓库在 GitHub 和 Gitee 各有一份，靠 GitHub Actions 双向保持一致，**所有分支和标签都会同步**：

| 方向 | 工作流 | 触发时机 | 生效速度 |
| --- | --- | --- | --- |
| GitHub → Gitee | `.github/workflows/sync-to-gitee.yml` | 任意分支的 push（也可手动触发） | 约 1 分钟内 |
| Gitee → GitHub | `.github/workflows/sync-from-gitee.yml` | 每 15 分钟检查一次（也可手动触发） | 最长约 15 分钟 |

所以**只往一端提交就够了**，另一端会自动跟上；往 Gitee 提交时，GitHub 侧最长慢 15 分钟。

设计要点：

- **只做快进（fast-forward）同步，从不 `force push`。** 某个分支如果在两端已经分叉，工作流会失败并点名是哪个分支，而不是悄悄覆盖掉另一边的代码；此时需要手动对齐。
- **分支删除不会自动传播**：在一边删掉的分支，另一边会保留，需要两边都手动删（刻意为之，避免误删）。
- GitHub → Gitee 依赖仓库 secret `GITEE_TOKEN`（Gitee 私人令牌，需 `projects` 权限）。令牌被撤销或过期后，同步会在日志里明确报错。
- 日常本地提交时，`git push` 会通过一个 remote 上的两个 push 地址**同时**推到两端（瞬时，不依赖 Actions）；Actions 主要负责兜底「在网页上直接改代码」的情况。
- 定时工作流在仓库连续 60 天无活动后会被 GitHub 自动暂停，需要去 Actions 页面手动重新启用。

排查同步问题：

```bash
gh run list --workflow sync-to-gitee.yml
gh run view <run-id> --log
```

## 许可证

除下方「第三方内容声明」列出的内容外，本仓库代码基于 [MIT 许可证](LICENSE) 开源，可自由使用、修改、分发和商用，只需保留版权声明。

```
Copyright (c) 2026 王福洪
```

### 第三方内容声明

以下内容**不属于**上述 MIT 许可证的授权范围，版权归各自所有者，收录在此仅作为学习过程中的接入示例或抓取产物：

| 路径 | 来源 | 说明 |
| --- | --- | --- |
| `09_过验证码/Chaojiying_Python` | [超级鹰](https://www.chaojiying.com) 官网 | 官方提供的 Python 接入示例代码，官方未附带许可证声明 |
| `爬虫案例练习/拾光AI画板/main.html`、`elements.html` | 拾光视界（SHIGUANG VISION） | 网页抓取产物 |
| `10爬虫案例实战/test.html` | 百度首页 | 网页抓取产物 |
| `10爬虫案例实战/error.html` | 某站点错误页 | 网页抓取产物 |

除上述内容外，仓库中的其余代码均为本人编写。

如果你要复用本仓库的代码，请注意：**抓取到的第三方内容受其自身服务条款与著作权保护**，请遵守目标站点的 `robots.txt` 与相关法律，不要直接转载抓取到的第三方内容，也不要将本项目用于未经授权的用途。
