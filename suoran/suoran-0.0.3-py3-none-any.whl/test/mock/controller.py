from suoran import route

class TestController:
    '''
    '''

    @route.get('/')
    def index(self):
        '''
        '''
        return 'index'