"""Недавно маленький Антон научился читать некоторые буквы! Точнее, он научился читать буквы R, S и M. Кроме того, набор из трех букв R, S, M ему кажется правильным, если в нем символ R находится раньше, чем символ M.
Определите, является ли строка  правильной по мнению Антона.

Формат входных данных:
Дана строка S из трех символов, содержащая один символ R, один символ S и один символ M.

Формат выходных данных:
Выведите "Yes", если символ R находится в строке S раньше, чем символ M. В противном случае выведите "No".

"""# Читаем строку
s = input()

# Находим позиции букв R и M
r_pos = s.index('R')
m_pos = s.index('M')

# Проверяем, стоит ли R раньше M
if r_pos < m_pos:
    print("Yes")
else:
    print("No")