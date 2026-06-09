import os

replacements = {
    "从剪贴板读取 Cookie (抖音)": "写入 Cookie (抖音)",
    "从剪贴板读取 Cookie (TikTok)": "写入 Cookie (TikTok)",
    "当前剪贴板的内容不是有效的 Cookie 内容！": "当前提供的 Cookie 内容不是有效的 Cookie 内容！",
    "The current clipboard content is not valid Cookie data!": "The provided Cookie content is not valid Cookie data!",
    'msgid ""\n"复制 Cookie 内容至剪贴板后，按回车键确认继续；若输入任意内容并按回车，则取消"\n"操作："': 'msgid ""\n"复制 Cookie 内容至剪贴板后，按回车键确认继续；或直接在此粘贴输入 Cookie 并按回车；若输入 Q/q 并按回车，则取消"\n"操作："',
    'msgstr ""\n"After pasting the cookie into the clipboard, press Enter to proceed. Enter "\n"any content and press Enter to cancel: "': 'msgstr ""\n"After copying the cookie to the clipboard, press Enter to proceed; or directly paste the Cookie here and press Enter; enter Q/q and press Enter to cancel: "'
}

files = [
    "locale/tk.pot",
    "locale/en_US/LC_MESSAGES/tk.po",
    "locale/zh_CN/LC_MESSAGES/tk.po",
]

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    for old, new in replacements.items():
        content = content.replace(old, new)
        
    with open(f, "w", encoding="utf-8") as file:
        file.write(content)
print("done")
