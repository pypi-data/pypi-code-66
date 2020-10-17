import time

class Pipeline():
    def __init__(self, sink):
        self.__sink = sink

    def pipe(self, element):
        c = type(self).__name__
        if 'step' not in element:
            element['step'] = list()
        element['step'].append(c)
        element = self.sink(element)

        if element == None:
            # done
            return

        if 'stamp' not in element:
            element['stamp'] = dict()
        element['stamp'][c] = time.perf_counter()

        if (self.__sink):
            self.__sink.pipe(element)

    def run(self):
        count = 0
        for elem in self.source():
            if elem == None:
                break
            count += 1
            self.pipe(elem)
        return count

    def sink(self, element):
        ''' default sink just returns element unchanged'''
        return element

    def source(self):
        ''' default source returns one element '''
        yield None

