import re

def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


#=============== Задание 1 (1, 2, 3) ===============

#1
# def find_sum_of_prime(n):
#     sum = 0
#     for i in range(2, n // 2 + 1):
#         if(n % i == 0 and is_prime(i)):
#             sum += i
#     return sum

#2
# def find_gr_3(n):
#     count = 0
#     while(n != 0):
#         digit = n % 10
#         if digit > 3 and digit % 2 != 0:
#             count += 1
#         n //= 10
#     return count

#3
# def find_sum_of_digits(n):
#     sum = 0
#     while(n != 0):
#         sum += (n % 10)
#         n //= 10
#     return sum

# def find_proiz(n):
#     proiz = 1
#     n_sum = find_sum_of_digits(n)
#     for i in range(2, n // 2 + 1):
#         if n % i == 0 and find_sum_of_digits(i) < n_sum:
#             proiz *= i
#     return proiz



#=============== Задания 2-4 (1, 9, 18) ===============

# 1
# def count_russian_chars_unicode(text):
#     count = 0
#     for char in text:
#         # Проверяем, что символ относится к кириллице по коду Unicode
#         if 'а' <= char <= 'я' or 'А' <= char <= 'Я' or char == 'ё' or char == 'Ё':
#             count += 1
    
#     return count

# print(count_russian_chars_unicode("Привет world"))

#9
# def isPol(str):
#     str_1 = ""
#     for i in range(len(str) - 1, -1, -1):
#         str_1 += str[i]
#     if str == str_1:
#         return True
#     return False

# print(isPol("madam"))
# print(isPol("radar"))
# print(isPol("sir"))

#18
# def findDate(text):
#     pattern = r'\b(0[1-9]|[12][0-9]|3[0-1])\.(0[1-9]|1[0-2])\.(\d{4})\b'

#     res = re.findall(pattern, text)
#     return res

# print(findDate("Даты: 05.06.2024, 31.12.2023, 00.13.2024, 32.01.2024, 15.00.2024"))


#=============== Задание 5 ===============

#5


#=============== Задания 6-8 (1, 9, 18) ===============

# #1
# def find_max_float(s):
#     max_num = None
#     i = 0
#     current_num = ""
#     while i < len(s):
#         if s[i].isdigit() or s[i] == '.' or s[i] == '-' and (i == 0 or not
#         s[i-1].isdigit()):
#             current_num += s[i]
#             i += 1

#             while i < len(s) and (s[i].isdigit() or s[i] == '.'):
#                 current_num += s[i]
#                 i += 1
            
#             try: 
#                 if current_num.count('.') <= 1:
#                     if current_num.count('-') <= 1 and (current_num.count('-') == 0 or current_num[0] == '-'):
#                         num = float(current_num)
#                         if max_num is None or num > max_num:
#                             max_num = num
#             except ValueError:
#                 pass
#             current_num = ""
#         else:
#             i += 1
#     return max_num

# s = "abc-3.14xyz5.67123-45.60.5"
# result = find_max_float(s)
# print(result)
# s = "abc -3.14 xyz 5.6 7123 -45.6 0.5"
# result = find_max_float(s)
# print(result)

# #9
# def find_min_rational(s):
#     min_num = None
#     current_num = ""
#     i = 0

#     def parse_fraction(frac_str):
#         if '/' in frac_str:
#             parts = frac_str.split('/')
#             if len(parts) == 2:
#                 try: 
#                     numerator = float(parts[0])
#                     denominator = float(parts[1])
#                     if(denominator != 0):
#                         return numerator / denominator
#                 except ValueError:
#                     pass
#         return None
    
#     def parse_decimal(dec_str):
#         try: 
#             if dec_str.count('.') <= 1 and dec_str.count('-') <= 1:
#                 if dec_str.count('-') == 0 or (dec_str.count('-') == 1 and dec_str[0] == '-'):
#                     return float(dec_str)
#         except ValueError:
#             pass
#         return None

#     while i < len(s):
#         if s[i].isdigit() or s[i] == '-' or s[i] == '/':
#             current_num += s[i]
#             i += 1
#             while i < len(s) and (s[i].isdigit() or s[i] == '.' 
#             or s[i] == '/' or (s[i] == '-' and current_num.count('-') == 0)):
#                 current_num += s[i]
#                 i += 1
#             value = parse_decimal(current_num)
            
#             # Если не десятичная, пробуем как обыкновенную дробь
#             if value is None:
#                 value = parse_fraction(current_num)
            
#             # Обновляем минимум
#             if value is not None:
#                 if min_num is None or value < min_num:
#                     min_num = value
            
#             current_num = ""
#         else:
#             i += 1
    
#     return min_num

# s = "abc -3.14 xyz 5/2 123 -45.6 1/3 0.5 -7/8"
# result = find_min_rational(s)
# print(result)

# #18
# def max_consecutive_digits(s):
#     max_count = 0
#     curr_count = 0

#     for char in s:
#         if char.isdigit():
#             curr_count += 1
#             if curr_count > max_count:
#                 max_count = curr_count
#         else:
#             curr_count = 0
#     return max_count


#=============== Задание 9 ===============
# def sort_strings():
#     strings = []
#     print("Enter strings:")
#     while True:
#         s = input()
#         if s == "":
#             break
#         strings.append(s)
    
#     strings.sort(key = len)
#     return strings

# result = sort_strings()
# print(result)


#=============== Задание 10 ===============
def count_words(s):
    words = s.split()
    return len(words)

def sort_by_word_num():
    strings = []
    while True:
        s = input()
        if s == "":
            break
        strings.append(s)
        
        

#=============== Задания 11-14 (1, 4, 7, 10) ===============

#1



#=============== Задания 15-19 (1, 13, 25, 37, 49) ===============