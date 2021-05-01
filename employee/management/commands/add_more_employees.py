from django.core.management.base import BaseCommand
from employee.models import Employee
from employee.forms import EmployeeForm
import random
from django.core.files import File


class Command(BaseCommand):
    help = 'Добавление 1009 пользователей указанное подразделение'

    def add_arguments(self, parser):
        parser.add_argument('subdivision', type=str, help=u'В какое подразделение добавить 1009 пользователей')

    def handle(self, *args, **kwargs):
        current_subdivision = kwargs['subdivision']

        f = open("support_files/russian_surnames.txt", "r", encoding="utf-8")
        surname_lst = []
        for surname in f:
            t = surname[0] + surname.strip()[1:].lower()
            surname_lst.append(t)
        f.close()

        alphabet = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯ'

        Salary_level_1 = "150000", "140000", "170000"
        Salary_level_2 = "100000", "110000", "105000", "95000", "97000", "92000"
        Salary_level_3 = "75000", "65000", "67000", "69000", "68500", "72500", "74500", "73500", "71500", "68000"
        Salary_level_4 = "40000", "50000", "42000", "43000", "44500", "45500", "42500", "41500", "46000", "47000"
        Salary_level_5 = "20000", "30000", "22000", "23000", "24500", "25500", "22500", "21500", "26000", "27000"

        Day = "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"
        Month = "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"

        Year = "2018", "2019", "2020"

        def data_create(subdivision, employment_position, employee_salary):
            First = random.choice(surname_lst)
            Last = f'{random.choice(alphabet)}. {random.choice(alphabet)}.'
            Employee_Year = random.choice(Year)
            Employee_Month = random.choice(Month)
            Employee_Day = random.choice(Day)
            dict_with_data = {'name': First + ' ' + Last,
                              'subdivision': subdivision,
                              'employment_position': employment_position,
                              'employment_start_date': Employee_Year + '-' + Employee_Month + '-' + Employee_Day,
                              'salary': employee_salary}
            return dict_with_data

        count_one = 1
        self.stdout.write(f'count_1_lvl -  {count_one}')
        try:
            data_level_1 = data_create(current_subdivision, "Руководитель направления",
                                       random.choice(Salary_level_1))
            form = EmployeeForm(data=data_level_1)
            form.save()
            current_child_len = Employee.objects.order_by('date_added')
            current_child_id = current_child_len[(len(current_child_len) - 1)]
            boss_level_1_id = current_child_id.id
            boss_level_1 = Employee.objects.get(id=current_child_id.id)
            boss_level_1.move_to(None, 'left')
            boss_level_1.save()
            self.stdout.write(f'boss 1 -  {boss_level_1}')
            self.stdout.write(f'boss_id - {boss_level_1_id}')
        except:
            self.stdout.write(f'some bad here 1 {data_level_1}')

        # 1 + 3 + 3*5 + 3*5*6 + 3*5*6*10 = 1009
        for i_two in range(3):
            count_one += 1
            try:
                data_level_2 = data_create(current_subdivision, "Руководитель среднего звена",
                                           random.choice(Salary_level_2))
                form = EmployeeForm(data=data_level_2)
                form.save()
                current_child_len = Employee.objects.order_by('date_added')
                current_child_id = current_child_len[(len(current_child_len) - 1)]
                boss_level_2_id = current_child_id.id
                boss_level_2 = Employee.objects.get(id=current_child_id.id)
                boss_level_1 = Employee.objects.get(id=boss_level_1_id)
                boss_level_2.move_to(boss_level_1, 'first-child')
                boss_level_2.save()
                self.stdout.write(f'lvl2 empolyee: {data_level_2}')
            except:
                self.stdout.write(f'some bad here 2 {data_level_2}')

            for i_three in range(5):
                count_one += 1
                self.stdout.write(f'count_3_lvl - {count_one}')
                try:
                    data_level_3 = data_create(current_subdivision, "Опытный специалист",
                                               random.choice(Salary_level_3))
                    form = EmployeeForm(data=data_level_3)
                    form.save()
                    current_child_len = Employee.objects.order_by('date_added')
                    current_child_id = current_child_len[(len(current_child_len) - 1)]
                    boss_level_3_id = current_child_id.id
                    boss_level_3 = Employee.objects.get(id=current_child_id.id)
                    boss_level_2 = Employee.objects.get(id=boss_level_2_id)
                    boss_level_3.move_to(boss_level_2, 'first-child')
                    boss_level_3.save()
                except:
                    self.stdout.write(f'some bad here 3 {data_level_3}')

                for i_four in range(6):
                    count_one += 1
                    try:
                        data_level_4 = data_create(current_subdivision, "Рядовой сотрудник",
                                                   random.choice(Salary_level_4))
                        form = EmployeeForm(data=data_level_4)
                        form.save()
                        current_child_len = Employee.objects.order_by('date_added')
                        current_child_id = current_child_len[(len(current_child_len) - 1)]
                        boss_level_4_id = current_child_id.id
                        boss_level_4 = Employee.objects.get(id=current_child_id.id)
                        boss_level_3 = Employee.objects.get(id=boss_level_3_id)
                        boss_level_4.move_to(boss_level_3, 'first-child')
                        boss_level_4.save()
                    except:
                        self.stdout.write(f'some bad here 4 {data_level_4}')

                    for i_five in range(10):
                        count_one += 1
                        try:
                            data_level_5 = data_create(current_subdivision, "Стажер",
                                                       random.choice(Salary_level_5))
                            form = EmployeeForm(data=data_level_5)
                            form.save()
                            current_child_len = Employee.objects.order_by('date_added')
                            current_child_id = current_child_len[(len(current_child_len) - 1)]
                            boss_level_5 = Employee.objects.get(id=current_child_id.id)
                            boss_level_4 = Employee.objects.get(id=boss_level_4_id)
                            boss_level_5.move_to(boss_level_4, 'first-child')
                            boss_level_5.save()
                        except:
                            self.stdout.write(f'some bad here 5 {data_level_5}')

        self.stdout.write(f'Finish - added {count_one} employees')