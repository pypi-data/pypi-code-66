from unittest import TestCase, skip
from test.mock import controller

class RouteTest(TestCase):
    '''
    路由测试。
    '''

    def test_controller(self):
        '''
        测试控制器。
        '''

        tc = controller.TestController()
        r = tc.index()
        self.assertEqual(r, 'index')
        