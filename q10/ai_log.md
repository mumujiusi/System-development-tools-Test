核心提示：--name 仅空白时以 SystemExit(2) 退出，只改 cli.py，运行 pytest。
智能体改动：cli.py 增加 if not a.name.strip(): p.error("name cannot be blank")。
人工验证：diff 仅 cli.py 变更，无无关修改；pytest 1 passed。
