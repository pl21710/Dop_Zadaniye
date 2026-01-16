import numpy as np
import matplotlib.pyplot as plt

# ====== Ввод функции ======
print("Выберите функцию для построения графика:")
print("Варианты: sin, cos, tan, exp, log, x3, poly, radial")
func = input("Введите название функции: ").lower()

# ====== Настройка диапазона ======
# По умолчанию x от 0 до 2π
x = np.arange(0, 2 * np.pi, 0.01)

# ====== Вычисление y ======
if func == "sin":
    y = np.sin(x)
    label = "sin(x)"
elif func == "cos":
    y = np.cos(x)
    label = "cos(x)"
elif func == "tan":
    x = np.linspace(0, 2 * np.pi, 1000)
    y = np.tan(x)
    label = "tan(x)"
elif func == "exp":
    x = np.linspace(0, 5, 500)
    y = np.exp(x)
    label = "exp(x)"
elif func == "log":
    x = np.linspace(0.01, 10, 500)
    y = np.log(x)
    label = "log(x)"
elif func == "x3":
    y = x**3 + 2
    label = "x^3 + 2"
elif func == "poly":
    y = x**3 - 3*x**2 + 2*x + 1
    label = "x^3 - 3x^2 + 2x + 1"
elif func == "radial":
    x = np.linspace(-1, 1, 500)
    y = np.sqrt(1 - x**2)
    label = "sqrt(1 - x^2)"
else:
    print("Функция не поддерживается. Построим sin(x).")
    y = np.sin(x)
    label = "sin(x)"

# ====== Построение графика ======
plt.figure(figsize=(8,5))
plt.plot(x, y, label=label, color='blue', linewidth=2)
plt.title(f"График функции: {label}")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()

# ====== Отображение и сохранение ======
plt.show()
plt.savefig("graph.png", dpi=300)
print("График сохранён как graph.png")
