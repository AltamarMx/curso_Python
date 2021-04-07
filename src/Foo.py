class Foo:
    """
    This is a docstring of class Foo
    """
    class_variable = 3
    """This is a docstring for class_variable"""

    def __init__(self):
        self.instance_var_1 = 1
        """This is a docstring for instance_var_1"""
        self.instance_var_2 = 2

    def foo_method(self):
        """
        This is a docstring for foo_method.
        :param self:
        :return:
        """

    def bar_method(self):
        """
        This is a docstring for bar_method.
        :return:
        """

    def _private_method(self):
        """
        This is a docstring for _private_method
        :return:
        """

    def __name_mangled_method(self):
        """
        This is a docstring for __name_mangled_method
        :return:
        """