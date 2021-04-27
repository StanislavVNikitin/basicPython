class Date:

    def __init__(self, var_date):
        self.var_date = var_date

    @classmethod
    def split_date(cls, param):
        tmp = cls(param).var_date
        tmp_list = tmp.split("-")
        if cls.digit_date(tmp_list):
            print("Дата переданна в правильном формате")
        else:
            print("Дата должна быть в формате DD-MM-YYYY")

    @staticmethod
    def digit_date(my_list):
        print(my_list)
        i = 1
        if len(my_list) == 3:
            for en in my_list:
                if str.isdigit(en):
                    if i == 1:
                        if int(en) <= 0 or int(en) > 31:
                            print("День может быть от 1 до 31")
                            return False
                    elif i == 2:
                        if int(en) <= 0 or int(en) > 12:
                            print("Месяц может быть от 1 до 12")

                            return False
                    elif i == 3:
                        if int(en) <= 1900 or int(en) > 2100:
                            print("Год может быть от 1900 до 2100")
                            return False
                else:
                    return False
                i += 1
        else:
            return False

        return True


new_date1 = Date("d3-M2-2f21")
new_date1.split_date(new_date1.var_date)
print()
new_date2 = Date("23-12")
new_date2.split_date(new_date2.var_date)
print()
new_date3 = Date("23-12-2021")
new_date3.split_date(new_date3.var_date)
print()
new_date4 = Date("53-23-021")
new_date4.split_date(new_date4.var_date)
print()
new_date5 = Date("13-13-2021")
new_date5.split_date(new_date5.var_date)
print()
new_date6 = Date("32-10-2021")
new_date6.split_date(new_date6.var_date)
print()
new_date7 = Date("30-10-21")
new_date7.split_date(new_date7.var_date)
