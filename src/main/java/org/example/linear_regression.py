import os
import platform
import subprocess


DATASET_PATH = "src/main/java/org/example/dataset.txt"
OUTPUT_PATH = "src/main/java/org/example/Result.ppm"

IMAGE_WIDTH = 500
IMAGE_HEIGHT = 500

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def load_dataset(path):
    x_values = []
    y_values = []

    with open(path, "r") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) != 2:
                continue

            x_values.append(float(parts[0]))
            y_values.append(float(parts[1]))

    if not x_values:
        raise Exception("Datasetul este gol sau formatat gresit!")

    return x_values, y_values


def compute_linear_regression(x_values, y_values):
    n = len(x_values)

    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xy = sum(x * y for x, y in zip(x_values, y_values))
    sum_x2 = sum(x * x for x in x_values)

    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    b = (sum_y - a * sum_x) / n

    return a, b


def create_blank_image(width, height, color):
    return [[color for _ in range(width)] for _ in range(height)]


def save_ppm_image(path, image, width, height):
    with open(path, "w") as file:
        file.write("P3\n")
        file.write(f"{width} {height}\n")
        file.write("255\n")

        for row in image:
            for r, g, b in row:
                file.write(f"{r} {g} {b} ")
            file.write("\n")


def open_image(path):
    full_path = os.path.abspath(path)
    system_name = platform.system()

    try:
        if system_name == "Windows":
            subprocess.run(["cmd", "/c", "start", "", full_path])
        elif system_name == "Darwin":
            subprocess.run(["open", full_path])
        else:
            subprocess.run(["xdg-open", full_path])
    except Exception as error:
        print("Nu s-a putut deschide automat imaginea:", error)
        print("Imaginea este salvata la:", full_path)


def main():
    print("Pornire regresie liniara...")

    x_values, y_values = load_dataset(DATASET_PATH)

    a, b = compute_linear_regression(x_values, y_values)
    print(f"Ecuatia regresiei: y = {a} * x + {b}")

    min_x = min(x_values)
    max_x = max(x_values)
    min_y = min(y_values)
    max_y = max(y_values)

    def scale_x(x):
        if max_x == min_x:
            return IMAGE_WIDTH // 2

        scaled = int((x - min_x) / (max_x - min_x) * (IMAGE_WIDTH - 1))
        return max(0, min(IMAGE_WIDTH - 1, scaled))

    def scale_y(y):
        if max_y == min_y:
            return IMAGE_HEIGHT // 2

        scaled = IMAGE_HEIGHT - int((y - min_y) / (max_y - min_y) * (IMAGE_HEIGHT - 1))
        return max(0, min(IMAGE_HEIGHT - 1, scaled))

    image = create_blank_image(IMAGE_WIDTH, IMAGE_HEIGHT, WHITE)

    for x, y in zip(x_values, y_values):
        pixel_x = scale_x(x)
        pixel_y = scale_y(y)
        image[pixel_y][pixel_x] = RED

    for i in range(IMAGE_WIDTH):
        real_x = min_x + (i / (IMAGE_WIDTH - 1)) * (max_x - min_x)
        real_y = a * real_x + b
        pixel_y = scale_y(real_y)

        if 0 <= pixel_y < IMAGE_HEIGHT:
            image[pixel_y][i] = BLUE

    save_ppm_image(OUTPUT_PATH, image, IMAGE_WIDTH, IMAGE_HEIGHT)
    print("Imagine salvata la:", OUTPUT_PATH)

    open_image(OUTPUT_PATH)


if __name__ == "__main__":
    main()