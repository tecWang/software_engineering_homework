from calc import Calc

c = Calc()
print(c.generate_output())

an_list = input()
c.input_answer(an_list.split(" "))

print(c.calc_score())