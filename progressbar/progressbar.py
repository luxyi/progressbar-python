
import sys


class ProgressBar(object):

    def __init__(self, max_num, length=50):
        self.__length = length
        self.__max_num = max_num
        self.__total_length = self.__calculate_total_length()
        self.__cur_num = 0

    def __calculate_total_length(self):
        return self.__max_num + len(str(self.__max_num)) * 2 + 11

    def update(self):
        self.__cur_num += 1
        percentage = self.__cur_num * 100 / self.__max_num
        arrows = self.__cur_num * self.__length / self.__max_num
        spaces = self.__length - arrows

        line = '{}'.format('\b'*(self.__length+self.__total_length))
        sys.stdout.write(line)
        line = '[{}{}] {:3}% ({}/{})'.format(
            '>'*arrows, ' '*spaces, percentage, self.__cur_num, self.__max_num)
        sys.stdout.write(line)
        sys.stdout.flush()
