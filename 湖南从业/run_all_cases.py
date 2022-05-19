# encoding: utf-8
# @file: run_all_cases.py
# @desc:
import os
import pytest

# 当前路径(使用 abspath 方法可通过dos窗口执行)
current_path = os.path.dirname(os.path.abspath(__file__))
# json报告路径
json_report_path = os.path.join(current_path, 'report\\json')
# html报告路径
html_report_path = os.path.join(current_path, 'report\\html')

# 指定案例目录
specify_testcase_path = os.path.join(current_path, 'testcases')
# 执行pytest下的用例并生成json文件
# pytest.main(['-s', '-v', '--alluredir=%s' % json_report_path, '--clean-alluredir'])  # 运行所有用例
pytest.main(['-s', '-v', specify_testcase_path, '--alluredir=%s' % json_report_path, '--clean-alluredir'])  # 运行指定用例
# 把json文件转成html报告
os.system('allure generate %s -o %s --clean' % (json_report_path, html_report_path))
os.system('allure open %s' % html_report_path)
