import os
import platform
import subprocess

print("Pornire regresie liniara...")


x_vals = []
y_vals = []

with open("src/main/java/org/example/dataset.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) != 2:
            continue  # ignoră linii goale sau greșite
        x_vals.append(float(parts[0]))
        y_vals.append(float(parts[1]))

n = len(x_vals)
if n == 0:
    raise Exception("Datasetul este gol sau formatat gresit!")



sum_x = sum(x_vals)
sum_y = sum(y_vals)
sum_xy = sum(x*y for x, y in zip(x_vals, y_vals))
sum_x2 = sum(x*x for x in x_vals)

a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
b = (sum_y - a * sum_x) / n

print(f"Ecuatia regresiei: y = {a} * x + {b}")



width = 500
height = 500

min_x, max_x = min(x_vals), max(x_vals)
min_y, max_y = min(y_vals), max(y_vals)

def scale_x(x):
    if max_x == min_x:
        return width // 2
    val = int((x - min_x) / (max_x - min_x) * (width - 1))
    return max(0, min(width - 1, val))

def scale_y(y):
    if max_y == min_y:
        return height // 2
    val = height - int((y - min_y) / (max_y - min_y) * (height - 1))
    return max(0, min(height - 1, val))

# fundal alb
image = [[(255,255,255) for _ in range(width)] for _ in range(height)]

# desenare puncte (rosu)
for x, y in zip(x_vals, y_vals):
    px = scale_x(x)
    py = scale_y(y)
    image[py][px] = (255,0,0)

# desenare linie regresie (albastru)
for i in range(width):
    real_x = min_x + (i / (width - 1)) * (max_x - min_x)
    real_y = a*real_x + b
    py = scale_y(real_y)
    if 0 <= py < height:
        image[py][i] = (0,0,255)


output_path = "src/main/java/org/example/Result.ppm"

with open(output_path, "w") as f:
    f.write("P3\n")
    f.write(f"{width} {height}\n255\n")
    for row in image:
        for r,g,b in row:
            f.write(f"{r} {g} {b} ")
        f.write("\n")

print("Imagine salvata la:", output_path)


full_path = os.path.abspath(output_path)
system = platform.system()

try:
    if system == "Windows":
        subprocess.run(["cmd", "/c", "start", "", full_path])
    elif system == "Darwin":
        subprocess.run(["open", full_path])
    else:  # Linux
        subprocess.run(["xdg-open", full_path])
except Exception as e:
    print("Nu s-a putut deschide automat imaginea:", e)
    print("Imaginea este salvata la:", full_path)