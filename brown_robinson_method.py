import prettytable  # модуль для форматированного (красивого) вывода таблиц

# Игра в n пальцев: игроки A и B одновременно показывают от 1 до n пальцев каждый, сумма показанных пальцев = k
# если k - чётное, A выигрывает k рублей, иначе - B выигрывает k рублей => выигрыш A равен (-1) ** k * k рублей
n = int(input("Введите количество пальцев для игры в n пальцев: "))
a = [[0] * n for i in range(n)]  # платёжная матрица игры
for i in range(n):
    for j in range(n):
        k = (i + 1) + (j + 1)
        a[i][j] = (-1) ** k * k
# форматированный вывод платёжной матрицы
a_pretty_table = prettytable.PrettyTable()
a_pretty_table.field_names = ["Ai \\ Bj"] + [f"B{j}" for j in range(1, n + 1)]
for i in range(n): a_pretty_table.add_row([f"A{i + 1}"] + a[i])
print("Платёжная матрица игры:", a_pretty_table, sep="\n")
print()

# Метод Брауна-Робинсона - численный метод решения игр
iters = int(input("Введите количество итераций для метода Брауна-Робинсона: "))
i, j = 1, None  # игрок A может начать со случайной стратегии, пусть это будет 1 стратегия => i = 1
lower_game_price = upper_game_price = game_price = None  # game_price - цена игры => lower - нижняя, upper - верхняя
total_gain_b, total_gain_a = [0] * n, [0] * n
cnt_a, cnt_b = [1] + [0] * (n - 1), [0] * n  # учтено, что взяли в начале i = 1
for k in range(1, iters + 1):
    current_gain_b = [a[i - 1][x] for x in range(n)]
    total_gain_b = [total_gain_b[x] + current_gain_b[x] for x in range(n)]
    j = total_gain_b.index(min(total_gain_b)) + 1
    cnt_b[j - 1] += 1
    current_gain_a = [a[x][j - 1] for x in range(n)]
    total_gain_a = [total_gain_a[x] + current_gain_a[x] for x in range(n)]
    i = total_gain_a.index(max(total_gain_a)) + 1
    cnt_a[i - 1] += 1
    lower_game_price, upper_game_price = min(total_gain_b) / k, max(total_gain_a) / k
    game_price = (lower_game_price + upper_game_price) / 2
# ответы: выигрышные стратегии Sa(p1, p2, ..., pn) и Sb(q1, q2, ..., qn), цена игры = значение game_price на посл. итер.
p, q = [cnt_a[x] / iters for x in range(n)], [cnt_b[x] / iters for x in range(n)]

# форматированный вывод ответов
print("Выигрышная стратегия Sa(p1, p2, ..., pn) для A:", *[f"p{x + 1} = {p[x]:.10f}" for x in range(n)], sep="\n")
print("Выигрышная стратегия Sb(q1, q2, ..., qn) для B:", *[f"q{x + 1} = {q[x]:.10f}" for x in range(n)], sep="\n")
print(f"Цена игры = {game_price:.10f}")
