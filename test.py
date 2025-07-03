import win32gui
import win32api
import win32con


def get_window_rect(window_title):
    # 用于获取所有窗口信息并找到匹配窗口
    def enum_window(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):  # 确保是可见的窗口
            if win32gui.GetWindowText(hwnd) == window_title:  # 根据窗口标题查找
                left, top, right, bottom = win32gui.GetWindowRect(hwnd)  # 获取窗口坐标
                windows.append((left, top, right, bottom))

    windows = []
    win32gui.EnumWindows(enum_window, windows)  # 列出所有窗口并查找目标窗口

    if windows:
        return windows[0]  # 返回找到的第一个窗口坐标
    else:
        return None  # 如果没有找到，返回None


window_title = "你的游戏窗口标题"  # 填写你游戏的窗口标题
window_rect = get_window_rect(window_title)

if window_rect:
    print(f"窗口的位置和大小: {window_rect}")
else:
    print("未找到窗口")



# 假设你已经得到了窗口的坐标
window_left, window_top, window_right, window_bottom = window_rect

# 游戏内某个区域的相对坐标和大小
relative_x, relative_y = 50, 20  # 相对位置
relative_width, relative_height = 200, 50  # 区域的大小

# 计算该区域在屏幕上的坐标
x1 = window_left + relative_x
y1 = window_top + relative_y
x2 = window_left + relative_x + relative_width
y2 = window_top + relative_y + relative_height

print(f"区域的屏幕坐标: ({x1}, {y1}, {x2}, {y2})")