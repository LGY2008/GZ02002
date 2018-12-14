import allure
import pytest

"""
    目标：allure报告添加测试步骤
    方法：@allure.step("内容")
    注意：此方法只能修饰函数
    
    目标2：allure添加描述
    方法：allure.attach("描述：","内容")
    修饰对象：只能修饰函数体内容
"""

class Test01():
    @allure.step("新增方法操作")
    def test001(self):
        # 添加 描述
        allure.attach("描述：","test01被添加")
        print("test001被执行")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step("修改方法操作")
    def test002(self):
        allure.attach("test02被修改", "")
        print("test002被执行")

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step("查询所有方法操作")
    def test003(self):
        allure.attach("描述：", "test03被查询")
        print("test003被执行")

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step("查询指定方法操作")
    def test004(self):
        allure.attach("描述：", "test04被查询")
        print("test004被执行")
        assert 0

    @allure.step("删除方法操作")
    def test005(self):
        allure.attach("描述：", "test05被删除")
        print("test005被执行")
