import re
import random

class Equation(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        self.result = self.calc(self.num1, self.op, self.num2)

    def calc(self, num1, op, num2):  
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            return num1 / num2

    def output_question(self):
        return str(self.num1) + " " + self.op + " " + str(self.num2) + " = ?"
    

class Calc(object):
    def __init__(self, nb_num=5, value_range=[0, 9], nb_split=1, 
                has_multiply=False, has_negative=False, has_float=False):
        self.nb_num = nb_num
        self.value_range = value_range
        self.nb_split = nb_split
        self.has_multiply = has_multiply
        self.has_negative = has_negative
        self.has_float = has_float

        self.eq_list = []
        self.count = 0

    def generate(self):
        eq_list = []
        for _ in range(self.nb_num):
            eq_list.append(self.__generate_one())
        self.eq_list = eq_list
        return eq_list

    def generate_output(self):
        self.generate()

        output = ""
        for item in self.eq_list:
            output += item.output_question() + "\n"
            for _ in range(self.nb_split):
                output += "\n"
        return output

    def input_answer(self, an_list):
        if len(an_list) != self.nb_num:
            return -1
        
        count = 0
        for i in range(len(an_list)):
            correct = self.__is_right(an_list[i], self.eq_list[i].result)
            if correct is True:
                count += 1
        self.count = count
        return count

    def calc_score(self):
        return "您的成绩为%.2f分" % (100.0 * (self.count / len(self.eq_list)))

    def __generate_one(self):
        num1 = random.randint(self.value_range[0], self.value_range[1])
        num2 = random.randint(self.value_range[0], self.value_range[1])
        op_list = ["+", "-", "*", "/"]
        op = op_list[random.randint(0, 3)]
        return Equation(num1, op, num2)

    def __is_right(self, pred, real):
        return float(pred) == float(real)