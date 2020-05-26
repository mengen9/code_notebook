# 导入整个模块
import day5_module
# 导入特定的函数
from day5_module import caxa_plm_modules, print_modles, show_completed_modles
# 调用函数1
day5_module.plm_modules(20,"图文档", "工作流","编码工具")
# 调用函数2
caxa_plm_modules("BOM版本管理", "配置管理")
# 调用函数3和4
unprint_modules = ["飞机", "自行车", "电脑"]
completed_print = []
print_modles(unprint_modules, completed_print)
show_completed_modles(completed_print)
# 使用as给函数指定别名
# from module_name import function_name as fn
# 使用as给模块指定别名
# import module_name as mn
# 导入模块中所有的函数
# from module_name import *
