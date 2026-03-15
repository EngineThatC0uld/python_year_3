import re

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
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
def find_dates_simple(text):
    # Регулярное выражение для поиска потенциальных дат
    pattern = r'(\d{1,2})\s+(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s+(\d{4})'
    
    months = {
        'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4,
        'мая': 5, 'июня': 6, 'июля': 7, 'августа': 8,
        'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12
    }
    
    # Максимальное количество дней в месяцах (для невисокосного года)
    month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    def is_leap_year(year):
        """Проверка на високосный год"""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    def get_max_days(month, year):
        """Получение максимального количества дней в месяце"""
        if month == 2 and is_leap_year(year):
            return 29
        return month_days[month]
    
    found_dates = []
    
    for match in re.finditer(pattern, text, re.IGNORECASE):
        day = int(match.group(1))
        month_name = match.group(2).lower()
        year = int(match.group(3))
        month = months[month_name]
        
        max_days = get_max_days(month, year)
        
        if 1 <= day <= max_days:
            found_dates.append(match.group(0))
        else:
            print(f"Некорректная дата: {match.group(0)}")
    
    return found_dates

# Пример использования
text = "31 февраля 2007, 15 мая 2023, 29 февраля 2020, 31 ноября 2023"
valid_dates = find_dates_simple(text)
print("Корректные даты:", valid_dates)

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
# def count_words(s):
#     words = s.split()
#     return len(words)

# def sort_by_word_num():
#     strings = []
#     while True:
#         s = input()
#         if s == "":
#             break
#         strings.append(s)
#     strings.sort(key = count_words)
#     return strings

# result = sort_by_word_num()
# print(result)

#=============== Задания 11-14 (1, 4, 7, 10) ===============

# #1
# def number_vowel(s):
#     count = 0
#     vowels = ['a', 'e', 'u', 'i', 'o', 'y']
#     for char in s.lower():
#         if char in vowels:
#             count += 1
#     return count

# def number_consonant(s):
#     count = 0
#     consonants = ['q', 'z', 'w', 's', 'x', 'd', 'c', 'r', 'f', 'v', 't', 'g', 'b', 'h', 'n', 'j', 'm', 'k', 'm', 'l', 'p']
#     for char in s.lower():
#         if char in consonants:
#             count += 1
#     return count

# def sr_vowel_cons(s):
#     vowels = number_vowel(s)
#     consonants = number_consonant(s)
#     number_of_chars = vowels + consonants
#     if number_of_chars == 0:
#         return 0
#     avg_vowels = vowels / number_of_chars
#     avg_consonants = consonants / number_of_chars
#     return abs(avg_consonants - avg_vowels)

# def sort_vowel_consonant():
#     strings = []
#     while True:
#         s = input()
#         if s == "":
#             break
#         strings.append(s)
#     strings.sort(key = sr_vowel_cons)
#     return strings

# strings = sort_vowel_consonant()
# print(strings)

# #4
# def solve(strings):
#     if not strings: 
#         return strings
#     first_avg = sum(ord(ch) for ch in strings[0]) / len(strings[0])
#     deviations = []
#     for s in strings:
#         avg = sum(ord(ch) for ch in s) / len(s)
#         #квадратичное отклонение
#         deviation = (avg - first_avg) ** 2
#         deviations.append((deviation, s))
#     return [s for _, s in sorted(deviations)]

# strings = [
#     "aaa",      # 97, маленькое отклонение
#     "zzz",      # 122, большое отклонение  
#     "hello",    # первая строка
#     "b",        # 98, маленькое отклонение
#     "ZZZ"       # 90, ещё меньше
# ]

# result = solve(strings)
# print(result)

# #7
# def sort_vowel_cons(string):
#     vowels = set('aeuio')

#     vc = 0 #гласная + согласная
#     cv = 0 #согласная + гласная

#     for i in range(len(string) - 1):
#         current = string[i]
#         next_char = string[i + 1]

#         if current.isalpha() and next_char.isalpha():
#             if current in vowels and next_char not in vowels:
#                 vc += 1
#             elif current not in vowels and next_char in vowels:
#                 cv += 1
#     return vc - cv

# def solve(strings):
#     if not strings:
#         return strings
#     return sorted(strings, key = sort_vowel_cons)

# strings = [
#     "hello",
#     "world",
#     "python",
#     "abc",
#     "aei",     # только гласные
#     "bcdf",    # только согласные
#     "abacaba"
# ]

# result = solve(strings)
# print("Исходный порядок:", strings)
# print("Отсортировано:    ", result)

# #10
# def avg_mirrored(string):
#     #ffghhvada
#     count = 0
#     for i in range(len(string) - 2):
#         if string[i] == string[i + 2] and string[i] != string[i + 1]:
#             count += 1
#     return count / len(string)

# def solve(strings):
#     if not strings:
#         return strings
#     return sorted(strings, key = avg_mirrored)

# test_strings = [
#         "ada",           # 1 тройка (ada), длина 3 → 1/3 ≈ 0.333
#         "abacaba",       # Тройки: aba(0-2), aca(2-4), aba(4-6) → 3/7 ≈ 0.429
#         "hello",         # нет троек → 0/5 = 0
#         "aaa",           # нет (все символы равны) → 0/3 = 0
#         "abcabc",        # нет → 0/6 = 0
#         "abac",          # aba(0-2) → 1/4 = 0.25
#         "xoxox",         # xox(0-2), oxo(1-3), xox(2-4) → 3/5 = 0.6
#         "aba ba cab",    # с пробелами: aba(0-2), aba(6-8?) проверим
#         "a",             # длина < 3 → 0/1 = 0
#         "ab",            # длина < 3 → 0/2 = 0
#     ]

# print(solve(test_strings))

#=============== Задания 15-19 (1, 13, 25, 37, 49) ===============

# #1 
# def find_after_last_maxi(arr):
#     if not arr:
#         return arr
#     max_val = max(arr)
#     last_max_index = len(arr) - 1 - arr[::-1].index(max_val) #очень сложно...
#     return len(arr) - last_max_index - 1

# test = [1, 2, 3, 2, 1]
# test = [5, 1, 5, 2, 5, 3]
# print(find_after_last_maxi(test))

# #13
# def rearrange_before_min(arr):
#     if not arr:
#         return arr
    
#     min_val = min(arr)
#     min_val_index = arr.index(min_val)
#     if min_val_index == 0:
#         return arr

#     result = arr[min_val_index:] + arr[:min_val_index]
#     return result

# arr = [3, 5, 1, 7, 2, 8]
# print(rearrange_before_min(arr))

# #25
# def find_max_on_interval(arr, a, b):
#     if not arr:
#         return None
#     if a < 0 or a >= len(arr) or b < a:
#         return None 
#     end = min(b, len(arr) - 1)
#     max_on_interval = max(arr[a:end+1])
#     return max_on_interval

# arr = [3, 7, 1, 9, 4, 2, 8, 5]
# a = 1
# b = 4
# print(find_max_on_interval(arr, a, b))

# #37
# def find_less_left(arr):
#     indexes = []
#     count = 0
#     for i in range(1, len(arr)):
#         if arr[i] < arr[i - 1]:
#             indexes.append(i)
#             count += 1
#     return indexes, count

# def find_less_left_v2(arr):
#     indexes = [i for i in range(1, len(arr)) if arr[i] < arr[i - 1]]
#     return indexes, len(indexes)

# arr = [5, 3, 7, 2, 8, 1]
# print(find_less_left(arr))
# print(find_less_left_v2(arr))

#49

# def prime_div(num):
#     divs = []
#     if is_prime(num):
#         divs.append(num)
#     else:
#         for i in range(2, num // 2 + 1):
#             if is_prime(i) and num % i == 0:
#                 divs.append(i)
#     return divs

# def find_all_prime_div():
#     arr = []
#     while True:
#         s = input()
#         if s == "":
#             break
#         try:
#             num = int(s)
#             if num <= 0:
#                 print("Enter positive numbers")
#                 continue
#             arr.append(num)
#         except ValueError:
#             print("Enter Integers only")
#     if not arr:
#         print("Array is empty")
#         return set()

#     divisors = set()
#     for i in range(len(arr)):
#         divisors.update(prime_div(arr[i]))
#     return divisors

# #14 21 35
# #6 10 15
# #12 30 18
# a = find_all_prime_div()
# print(a)
