# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для этого использовать шаблон template и подставить в него значения из строки
ospf_route. Значения из строки ospf_route надо получить с помощью Python.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
parts = ospf_route.split()
prefix = parts[0]
ad_metric = parts[1].strip('[]')
next_hop = parts[3].rstrip(',')
last_update = parts[-2].strip(',')
out_int = parts[-1]
# template = """
# Prefix                {prefix}
# AD/Metric             {ad_metric}
# Next-Hop              {next_hop}
# Last update           {last_update}
# Outbound Interface    {out_int}
# """
print(f'''
Prefix                {prefix}
AD/Metric             {ad_metric}
Next-Hop              {next_hop}
Last update           {last_update}
Outbound Interface    {out_int}
''')
