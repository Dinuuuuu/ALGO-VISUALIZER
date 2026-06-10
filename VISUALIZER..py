import tkinter as tk
import time
import random

root = tk.Tk()
root.title("DSA Visualizer — Dinesh Chell")
root.geometry("900x520")
root.configure(bg="#1e1e2e")

canvas = tk.Canvas(root, width=900, height=400,
                   bg="#1e1e2e", highlightthickness=0)
canvas.pack(pady=10)

arr = [random.randint(10, 100) for _ in range(12)]

def draw(arr, c1=-1, c2=-1, sorted_till=-1):
    canvas.delete("all")
    n = len(arr)
    w = 800 // n
    for i, val in enumerate(arr):
        x1 = 50 + i * w
        y1 = 380 - val * 3
        x2 = x1 + w - 4
        y2 = 380
        # Color logic
        if i == c1 or i == c2:
            color = "#f38ba8"   # red = comparing
        elif i <= sorted_till:
            color = "#a6e3a1"   # green = sorted!
        else:
            color = "#89b4fa"   # blue = normal
        canvas.create_rectangle(x1, y1, x2, y2,
                                fill=color, outline="")
        canvas.create_text(x1+w//2, y2+15,
                          text=str(val),
                          fill="white",
                          font=("Arial", 10))
    root.update()

# ── Bubble Sort ──────────────────────────────────────
def bubble_sort():
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            draw(arr, j, j+1)
            time.sleep(0.25)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw(arr, j, j+1)
                time.sleep(0.25)
    draw(arr, sorted_till=n-1)

# ── Selection Sort ───────────────────────────────────
def selection_sort():
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            draw(arr, j, min_idx, sorted_till=i-1)
            time.sleep(0.2)
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        draw(arr, i, min_idx, sorted_till=i)
        time.sleep(0.3)
    draw(arr, sorted_till=n-1)

# ── Insertion Sort ───────────────────────────────────
def insertion_sort():
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            draw(arr, j, j+1)
            time.sleep(0.2)
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        draw(arr, sorted_till=i)
        time.sleep(0.2)
    draw(arr, sorted_till=n-1)

# ── New Array ────────────────────────────────────────
def new_array():
    global arr
    arr = [random.randint(10, 100) for _ in range(12)]
    draw(arr)

# ── Buttons ──────────────────────────────────────────
frame = tk.Frame(root, bg="#1e1e2e")
frame.pack()

tk.Button(frame, text="🔀 New Array",
          command=new_array,
          bg="#313244", fg="white",
          font=("Arial", 11),
          padx=12, pady=6,
          relief="flat").pack(side="left", padx=5)

tk.Button(frame, text="▶ Bubble Sort",
          command=bubble_sort,
          bg="#89b4fa", fg="#1e1e2e",
          font=("Arial", 11, "bold"),
          padx=12, pady=6,
          relief="flat").pack(side="left", padx=5)

tk.Button(frame, text="▶ Selection Sort",
          command=selection_sort,
          bg="#a6e3a1", fg="#1e1e2e",
          font=("Arial", 11, "bold"),
          padx=12, pady=6,
          relief="flat").pack(side="left", padx=5)

tk.Button(frame, text="▶ Insertion Sort",
          command=insertion_sort,
          bg="#fab387", fg="#1e1e2e",
          font=("Arial", 11, "bold"),
          padx=12, pady=6,
          relief="flat").pack(side="left", padx=5)

# ── Start ────────────────────────────────────────────
draw(arr)
root.mainloop()