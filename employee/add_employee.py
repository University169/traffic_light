from .models import Employee
from .forms import EmployeeForm
import random

FirstName = "Иван", "Юрий", "Анна", "Юлия", "Андрей", "Дмитрий", "Алиса", "Оксана", "Сергей", "Антон", "Мария",\
            "Инокентий", "Ваган", "Екатерина", "Татьяна", "Михаил", "Ирина", "Светлана", "Максим", "Вадим"

LastName = "Черниченко", "Петросян", "Вазовски", "Дудь", "Махно", "Фуксман", "Лошкевич", "Фоменко", "Абоян",\
            "Кац", "Пак", "Кличко", "Гринько", "Чан", "Хан", "Любимых"

Salary_level_1 = "150000", "140000", "170000"
Salary_level_2 = "100000", "110000", "105000", "95000", "97000", "92000"
Salary_level_3 = "75000", "65000", "67000", "69000", "68500", "72500", "74500", "73500", "71500", "68000"
Salary_level_4 = "40000", "50000", "42000", "43000", "44500", "45500", "42500", "41500", "46000", "47000"
Salary_level_5 = "20000", "30000", "22000", "23000", "24500", "25500", "22500", "21500", "26000", "27000"

Day = "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",\

Month = "01", "02", "03", "04", "05", "06", "07", "08",\
        "09", "10", "11", "12"

Year = "2018", "2019", "2020"


def data_create(employment_position, subdivision, employee_salary):
    First = random.choice(FirstName)
    Last = random.choice(LastName)
    Employee_Year = random.choice(Year)
    Employee_Month = random.choice(Month)
    Employee_Day = random.choice(Day)
    dict_with_data = {'name': First + ' ' + Last,
                      'subdivision': subdivision,
                      'employment_position': employment_position,
                      'employment_start_date': Employee_Year + '-' + Employee_Month + '-' + Employee_Day,
                      'salary': employee_salary}
    return dict_with_data


def run_random():
    count_one = 0
    for i_one in range(1, 25):
        count_one = count_one + 1
        print('count_one - ', count_one)
        current_subdivision = "Подразделение" + str(i_one)
        try:
            form = EmployeeForm(data=data_create(current_subdivision, "Руководитель направления",
                                                 random.choice(Salary_level_1)))
            form.save()
            current_child_len = Employee.objects.order_by('date_added')
            current_child_id = current_child_len[(len(current_child_len) - 1)]
            boss_level_1_id = current_child_id.id
            boss_level_1 = Employee.objects.get(id=current_child_id.id)
            boss_level_1.move_to(None, 'left')
            boss_level_1.save()
        except:
            print('some bad here 1')

        for i_two in range(3):
            try:
                form = EmployeeForm(data=data_create(current_subdivision, "Руководитель среднего звена", random.choice(Salary_level_2)))
                form.save()
                current_child_len = Employee.objects.order_by('date_added')
                current_child_id = current_child_len[(len(current_child_len) - 1)]
                boss_level_2_id = current_child_id.id
                boss_level_2 = Employee.objects.get(id=current_child_id.id)
                boss_level_1 = Employee.objects.get(id=boss_level_1_id)
                boss_level_2.move_to(boss_level_1, 'first-child')
                boss_level_2.save()
                #print('boss - ', boss_level_1)
                #print('child - ', boss_level_2)
            except:
                print('some bad here 2')

            for i_three in range(3):
                try:
                    form = EmployeeForm(data=data_create(current_subdivision, "Опытный специалист", random.choice(Salary_level_3)))
                    form.save()
                    current_child_len = Employee.objects.order_by('date_added')
                    current_child_id = current_child_len[(len(current_child_len) - 1)]
                    boss_level_3_id = current_child_id.id
                    boss_level_3 = Employee.objects.get(id=current_child_id.id)
                    boss_level_2 = Employee.objects.get(id=boss_level_2_id)
                    boss_level_3.move_to(boss_level_2, 'first-child')
                    boss_level_3.save()
                    #print('boss - ', boss_level_2)
                    #print('child - ', boss_level_3)
                except:
                    print('some bad here 3')

                for i_four in range(4):
                    try:
                        form = EmployeeForm(data=data_create(current_subdivision, "Рядовой сотрудник", random.choice(Salary_level_4)))
                        form.save()
                        current_child_len = Employee.objects.order_by('date_added')
                        current_child_id = current_child_len[(len(current_child_len) - 1)]
                        boss_level_4_id = current_child_id.id
                        boss_level_4 = Employee.objects.get(id=current_child_id.id)
                        boss_level_3 = Employee.objects.get(id=boss_level_3_id)
                        boss_level_4.move_to(boss_level_3, 'first-child')
                        boss_level_4.save()
                        #print('boss - ', boss_level_3)
                        #print('child - ', boss_level_4)
                    except:
                        print('some bad here 4')

                    for i_five in range(5):
                        try:
                            form = EmployeeForm(data=data_create(current_subdivision, "Стажер", random.choice(Salary_level_5)))
                            form.save()
                            current_child_len = Employee.objects.order_by('date_added')
                            current_child_id = current_child_len[(len(current_child_len) - 1)]
                            boss_level_5 = Employee.objects.get(id=current_child_id.id)
                            boss_level_4 = Employee.objects.get(id=boss_level_4_id)
                            boss_level_5.move_to(boss_level_4, 'first-child')
                            boss_level_5.save()
                            #print('boss - ', boss_level_4)
                            #print('child - ', boss_level_5)
                        except:
                            print('some bad here 5')


run_random()