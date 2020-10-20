import re
import copy

class ReParse():
    """
    注意：&#&是''的意思，只是一个占位符，但其存在有莫大的意义！
    """
    def __init__(self, arr):
        self.pattern = arr
        self.pattern_tree = []

    def split(self, pattern):
        """
        作用：
            切分形如这样的pattern：'(求其|是但|是旦|隨便)(哼|亨|唱|將){{一}首|{一}隻}歌{仔}{嚟}{比我|俾我}(聽|停)'
                        result=['(', '求其', '|', '是但', '|', '是旦', '|', '隨便', ')', '(', '哼', '|', '亨', '|', '唱', '|', '將', ')', '{', '{', '一', '}', '首', '|', '{', '一', '}', '隻', '}', '歌', '{', '仔', '}', '{', '嚟', '}', '{', '比我', '|', '俾我', '}', '(', '聽', '|', '停', ')']
        核心思想：
            转化成树结构（list实现）
        :param pattern:
        :return:
        """
        pattern=re.sub(r'\|','|&#&',pattern)
        pt = re.compile(r'([\{\}\|\(\)])')
        arr = re.split(pt, pattern)
        arr = list(filter(lambda item: item != '', arr))
        return arr

    def findNext(self, str):
        """
        作用：
        把同等级的括号（'{'或者'(')找出来并切分,用于get_pattern_tree函数
        :param str:
        :return:
        """
        str = list(str)
        if str[0] == '{':
            nextsign = '}'
        else:
            nextsign = ')'
        tempt = [str[0]]
        endPoint = -1
        for i in range(1, len(str)):
            if str[i] == str[0]:
                tempt.append(str[i])
            elif str[i] in nextsign:
                tempt.pop(-1)
            else:
                pass
            if len(tempt) == 0:
                endPoint = i
                break
        return str[:endPoint + 1], str[endPoint + 1:]

    def get_pattern_tree(self, left, present):
        """
        作用：
            递归切分为树结构，以供parse_tree函数使用
            例如：[['&#&', '|', '求其', '|', '&#&是但', '|', '&#&是旦', '|', '&#&隨便'], ['唱', '|', '&#&將'], ['&#&', '|', '隻', '|', '&#&這', '|', '&#&', ['&#&', '|', '一'], '首'], ['&#&', '|', '飲'], '歌']
        :param left:
        :param present:
        :return:
        """
        if len(left) == 0:
            self.pattern_tree = present
            return

        if left[0] == '{':
            lleft, rleft = self.findNext(left)
            present.append(['&#&', '|'])
            lleft.pop(0)
            self.get_pattern_tree(lleft, present[-1])
            self.get_pattern_tree(rleft, present)
        elif left[0] == '(':
            lleft, rleft = self.findNext(left)
            present.append([])
            lleft.pop(0)
            self.get_pattern_tree(lleft, present[-1])
            self.get_pattern_tree(rleft, present)
        elif left[0] == ')':
            pass
        elif left[0] == '}':
            pass
        elif left[0] == '|':
            present.append('|')
            self.get_pattern_tree(left[1:], present)
        else:
            present.append(left[0])
            self.get_pattern_tree(left[1:], present)

    def parse_tree(self, left, pre_arr):
        """
        作用：
        递归实现
        :param left:
        :param pre_arr:
        :return:
        """
        # 每次处理列表的一个元素
        # 可能是嵌套列表:返回该列表所有组合的集合(pre_arr),再与上一个函数的pre_arr结合，pop出med的当前项
        # 可能是字符串：pre_arr的每一项都添加该字符串
        if len(left) == 0:
            return pre_arr
        if type(left[0]) == type([]):
            pre_arr_next = []
            # 把"|"分隔的都抽出来各自处理
            division = []
            division_index = [-1]
            for i in range(len(left[0])):
                if left[0][i] == '|':
                    division_index.append(i)
            division_index.append(len(left[0]))
            for i in range(len(division_index) - 1):
                if division_index[i + 1] - division_index[i] > 2:
                    division.append(list(left[0][division_index[i] + 1:division_index[i + 1]]))
                else:
                    division.append(left[0][division_index[i] + 1])
            # 每个分隔符之间的内容分别递归，获得各自的值
            for divi in division:
                pre_arr_nexti = self.parse_tree(divi, [])
                pre_arr_next.extend(pre_arr_nexti)
            # 把合并后的nextarr再和pre_arr的合并
            if len(pre_arr) == 0:
                for item in pre_arr_next:
                    pre_arr.append(item)
            else:
                pre_arrCopy = copy.deepcopy(pre_arr)
                pre_arr.clear()
                for itemi in pre_arrCopy:
                    for itemj in pre_arr_next:
                        pre_arr.append(itemi + itemj)
            left.pop(0)
            # 再继续处理后面的
            if type(left) == type([]) and len(left) != 0:
                pre_arr = self.parse_tree(left, pre_arr)
            return pre_arr
        else:
            if len(pre_arr) == 0:
                if type(left) == type([]):
                    pre_arr.append(left[0])
                else:
                    pre_arr.append(left)
            else:
                pre_arrCopy = copy.deepcopy(pre_arr)
                pre_arr.clear()
                for item in pre_arrCopy:
                    pre_arr.append(item + left[0])
            if type(left) == type([]) and len(left) != 0:
                left.pop(0)
                pre_arr = self.parse_tree(left, pre_arr)
            return pre_arr

    def Parse(self):
        splited_pattern = self.split(self.pattern)
        self.get_pattern_tree(splited_pattern, [])
        result = self.parse_tree(self.pattern_tree, [])
        result = list(map(lambda a: re.sub(r'&#&', '', a), result))
        return result


if __name__ == "__main__":
    patterns = ['{你|(我|{gm|gk})}好',
                '{求其|是但|是旦|隨便}(唱|將){隻|這|{一}首}{飲}歌',
                '(求其|是但|是旦|隨便)唱(隻|這|{一}首){啦}',
                '{你}{識唔識|會唔會}(唱|將){一}{首}(歌|卡拉ok|k)',
                '{你}(識|會)(唱|將)(歌|卡拉ok|k)',
                '高歌一曲',
                '好歌獻給{你|我}',
                '{我想|我要}{聽|請}你(唱|將){首|一首}歌',
                '{求其|是但|是旦|隨便}(哼|亨|唱|將){{一}首|{一}隻}歌{仔}{嚟}{比我|俾我}(聽|停)',
                '(要|想)聽你(唱|將){一}{首|隻}歌',
                '(將){一}首歌比我聽',
                '將首歌{比|俾}(你|我)聽',
                '將{首|這|隻}個{仔}{比|俾}(嚟|你|我)聽{吓}',
                '將你聽{吓}',
                '將修改聽{吓}',
                '槍手過嚟聽吓',
                '唔緊要啦將嚟聽吓啦',
                '{你}唱比我聽{好唔好}',
                '一齊唱{啦}',
                '你仲識{得}唱{其他|啲}(咩|乜){嘢}歌{曲}',
                '(將|唱){一}首{歌}好聽嘅歌{聽{吓}}',
                '{你}識唱(咩|乜){嘢}歌',
                '{(快啲|求其|是但|隨便){啦}}唱{{{就}得{㗎}}啦|呀}',
                '{唱}有隻雀仔跌落水',
                '唱吓歌啦',
                '唱{首國歌}((來|嚟|黎)聽(下|吓)|俾我聽){啦}',
                '我(要|想)聽你唱{歌仔|英文歌}{呀|啊|阿|吖}',
                '{我要聽}三隻小豬',
                '{我}叫你唱{歌}{啊}',
                '{咁}你{快啲}唱{啦|啊}',
                '唱歌仔',
                '(你|Siri)可唔可以唱歌{啊|㗎}',
                '(我想|我要)聽你唱',
                '一定要唱歌',
                'Siri出嚟唱歌',
                '(點解你|你點解)唔{識}唱{歌}',
                '你識唔識{得}唱{歌{仔}}',
                '{唔得}你一定要唱',
                '開始唱',
                '唱首(開心嘅|情)歌{俾我聽}',
                '{呢首聽過啦}唱(第二|下一)首{啦}',
                ]
    for i in range(len(patterns)):
        print("第{}个:\t{}".format(i, patterns[i]))
        result = ReParse(patterns[i]).Parse()  # 丢进去形如 '唱首(開心嘅|情)歌{俾我聽}'的string就出来一个list
        print(result)
