# communication.md

## Issue
环境：Windows（版本待确认），sdt-greet 版本待确认。\
复现：`sdt-greet --name " "`\
期望：空白姓名不被接受，不输出 `Hello, !`，应报错并非 0 退出；错误文案待确认。\
实际：输出 `Hello, !`，退出码 0。

## 提交信息
标题：Reject blank name input\
正文：\
问题：`--name " "` 被当作有效姓名，输出 `Hello, !` 且退出码 0。
方案：trim 后校验空值，报错并返回非零；补充空白姓名测试。

## 评审意见
Blocking：当前实现把空白姓名当有效输入，输出 `Hello, !` 且退出码 0，会让调用方误判成功并传播空姓名。建议入口 trim 后校验空值，报错并返回非零，补回归测试。