import tkinter as tk
import time
import random

# ── Window Setup ─────────────────────────────────────────────────
root = tk.Tk()
root.title("DSA Visualizer — Dinesh Chell | NIT Rourkela")
root.geometry("1000x600")
root.configure(bg="#1e1e2e")
root.resizable(False, False)

# ── Title Label ──────────────────────────────────────────────────
title = tk.Label(root,
                 text="DSA ALGORITHM VISUALIZER",
                 bg="#1e1e2e", fg="#cdd6f4",
                 font=("Arial", 14, "bold"))
title.pack(pady=5)

# ── Canvas ───────────────────────────────────────────────────────
canvas = tk.Canvas(root, width=1000, height=380,
                   bg="#1e1e2e", highlightthickness=0)
canvas.pack()

# ── Status Label ─────────────────────────────────────────────────
status_var = tk.StringVar()
status_var.set("Click any algorithm to start!")
status_label = tk.Label(root, textvariable=status_var,
                        bg="#1e1e2e", fg="#a6e3a1",
                        font=("Arial", 11))
status_label.pack()

# ── Array ────────────────────────────────────────────────────────
arr = [random.randint(10, 100) for _ in range(15)]

# ── COLORS ───────────────────────────────────────────────────────
COLOR_DEFAULT  = "#89b4fa"   # blue
COLOR_COMPARE  = "#f38ba8"   # red
COLOR_SWAP     = "#fab387"   # orange
COLOR_SORTED   = "#a6e3a1"   # green
COLOR_PIVOT    = "#f9e2af"   # yellow
COLOR_FOUND    = "#a6e3a1"   # green
COLOR_SEARCH   = "#cba6f7"   # purple
COLOR_DISCARD  = "#45475a"   # dark gray

# ── Draw Function ────────────────────────────────────────────────

def draw(arr, color_map={}):

    try:
        # Prevent crash if window closed
        if not root.winfo_exists():
            return

        canvas.delete("all")

        n = len(arr)
        bar_width = 900 // n
        start_x = (1000 - bar_width * n) // 2

        for i, val in enumerate(arr):

            x1 = start_x + i * bar_width
            y1 = 370 - val * 3
            x2 = x1 + bar_width - 3
            y2 = 370

            color = color_map.get(i, COLOR_DEFAULT)

            # Draw bar
            canvas.create_rectangle(
                x1,
                y1,
                x2,
                y2,
                fill=color,
                outline="",
                width=0
            )

            # Draw value
            canvas.create_text(
                x1 + bar_width // 2,
                y2 + 14,
                text=str(val),
                fill="#cdd6f4",
                font=("Arial", 9)
            )

            # Draw index
            canvas.create_text(
                x1 + bar_width // 2,
                y1 - 10,
                text=str(i),
                fill="#6c7086",
                font=("Arial", 8)
            )

        root.update_idletasks()
        root.update()

    except tk.TclError:
        return



# ── Helper — mark all sorted ─────────────────────────────────────
def mark_all_sorted(arr):
    color_map = {i: COLOR_SORTED for i in range(len(arr))}
    draw(arr, color_map)
    status_var.set("✅ Sorting Complete!")

# ════════════════════════════════════════════════════════════════
# 1. BUBBLE SORT
# ════════════════════════════════════════════════════════════════
def bubble_sort():
    status_var.set("Running: Bubble Sort | O(n²) time | O(1) space")
    n = len(arr)
    color_map = {}

    for i in range(n):
        for j in range(n - i - 1):
            # Highlight comparing pair
            color_map = {j: COLOR_COMPARE,
                         j+1: COLOR_COMPARE}
            # Add already sorted
            for k in range(n - i, n):
                color_map[k] = COLOR_SORTED
            draw(arr, color_map)
            time.sleep(0.2)

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                color_map = {j: COLOR_SWAP,
                             j+1: COLOR_SWAP}
                for k in range(n - i, n):
                    color_map[k] = COLOR_SORTED
                draw(arr, color_map)
                time.sleep(0.2)

    mark_all_sorted(arr)

# ════════════════════════════════════════════════════════════════
# 2. SELECTION SORT
# ════════════════════════════════════════════════════════════════
def selection_sort():
    status_var.set("Running: Selection Sort | O(n²) time | O(1) space")
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            color_map = {j: COLOR_COMPARE,
                         min_idx: COLOR_PIVOT}
            for k in range(i):
                color_map[k] = COLOR_SORTED
            draw(arr, color_map)
            time.sleep(0.15)
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        color_map = {i: COLOR_SWAP, min_idx: COLOR_SWAP}
        for k in range(i):
            color_map[k] = COLOR_SORTED
        draw(arr, color_map)
        time.sleep(0.25)

    mark_all_sorted(arr)

# ════════════════════════════════════════════════════════════════
# 3. INSERTION SORT
# ════════════════════════════════════════════════════════════════
def insertion_sort():
    status_var.set("Running: Insertion Sort | O(n²) time | O(1) space")
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        color_map = {i: COLOR_PIVOT}
        draw(arr, color_map)
        time.sleep(0.2)

        while j >= 0 and arr[j] > key:
            color_map = {j: COLOR_COMPARE,
                         j+1: COLOR_COMPARE}
            draw(arr, color_map)
            time.sleep(0.15)
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        color_map = {j+1: COLOR_SORTED}
        draw(arr, color_map)
        time.sleep(0.2)

    mark_all_sorted(arr)

# ════════════════════════════════════════════════════════════════
# 4. QUICK SORT
# ════════════════════════════════════════════════════════════════
def quick_sort_helper(arr, low, high, sorted_set):
    if low < high:
        pi = partition(arr, low, high, sorted_set)
        sorted_set.add(pi)
        quick_sort_helper(arr, low, pi - 1, sorted_set)
        quick_sort_helper(arr, pi + 1, high, sorted_set)

def partition(arr, low, high, sorted_set):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        color_map = {high: COLOR_PIVOT,
                     j: COLOR_COMPARE}
        for s in sorted_set:
            color_map[s] = COLOR_SORTED
        draw(arr, color_map)
        time.sleep(0.15)

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            color_map = {i: COLOR_SWAP,
                         j: COLOR_SWAP,
                         high: COLOR_PIVOT}
            for s in sorted_set:
                color_map[s] = COLOR_SORTED
            draw(arr, color_map)
            time.sleep(0.15)

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort():
    status_var.set("Running: Quick Sort | O(n log n) avg | O(log n) space | Yellow = Pivot")
    sorted_set = set()
    quick_sort_helper(arr, 0, len(arr) - 1, sorted_set)
    mark_all_sorted(arr)

# ════════════════════════════════════════════════════════════════
# 5. HEAP SORT
# ════════════════════════════════════════════════════════════════
def heapify(arr, n, i, heap_size):
    largest = i
    left    = 2 * i + 1
    right   = 2 * i + 2

    color_map = {i: COLOR_PIVOT}
    if left < n:
        color_map[left] = COLOR_COMPARE
    if right < n:
        color_map[right] = COLOR_COMPARE
    for k in range(heap_size, n):
        color_map[k] = COLOR_SORTED
    draw(arr, color_map)
    time.sleep(0.15)

    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        color_map = {i: COLOR_SWAP, largest: COLOR_SWAP}
        for k in range(heap_size, n):
            color_map[k] = COLOR_SORTED
        draw(arr, color_map)
        time.sleep(0.15)
        heapify(arr, n, largest, heap_size)

def heap_sort():
    status_var.set("Running: Heap Sort | O(n log n) time | O(1) space | Yellow = Root")
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, n)

    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        color_map = {0: COLOR_SWAP, i: COLOR_SORTED}
        for k in range(i, n):
            color_map[k] = COLOR_SORTED
        draw(arr, color_map)
        time.sleep(0.2)
        heapify(arr, n, 0, i)

    mark_all_sorted(arr)

# ════════════════════════════════════════════════════════════════
# 6. BINARY SEARCH
# ════════════════════════════════════════════════════════════════
def binary_search():
    # First sort the array
    arr.sort()
    draw(arr)
    time.sleep(0.5)

    target = random.choice(arr)  # pick random target
    status_var.set(f"Binary Search: Looking for {target} | O(log n) time")

    lo, hi = 0, len(arr) - 1
    found = False

    while lo <= hi:
        mid = (lo + hi) // 2

        # Color map
        color_map = {}

        # Discarded regions
        for k in range(0, lo):
            color_map[k] = COLOR_DISCARD
        for k in range(hi + 1, len(arr)):
            color_map[k] = COLOR_DISCARD

        # Active search space
        for k in range(lo, hi + 1):
            color_map[k] = COLOR_DEFAULT

        # Mid pointer
        color_map[mid] = COLOR_SEARCH

        draw(arr, color_map)
        status_var.set(
            f"Searching {target} | lo={lo} mid={mid} hi={hi} | arr[mid]={arr[mid]}"
        )
        time.sleep(0.6)

        if arr[mid] == target:
            color_map[mid] = COLOR_FOUND
            draw(arr, color_map)
            status_var.set(
                f"✅ Found {target} at index {mid}! Took {abs(mid - lo) + 1} comparisons"
            )
            found = True
            break
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    if not found:
        status_var.set(f"❌ {target} not found!")

# ── New Array ────────────────────────────────────────────────────
def new_array():
    global arr
    arr = [random.randint(10, 100) for _ in range(15)]
    draw(arr)
    status_var.set("New array generated! Click any algorithm.")

# ════════════════════════════════════════════════════════════════
# BUTTONS
# ════════════════════════════════════════════════════════════════
btn_frame1 = tk.Frame(root, bg="#1e1e2e")
btn_frame1.pack(pady=3)

btn_frame2 = tk.Frame(root, bg="#1e1e2e")
btn_frame2.pack(pady=3)

# Row 1 — Control + Sorting
buttons_row1 = [
    ("🔀 New Array",      new_array,      "#313244", "#cdd6f4"),
    ("▶ Bubble Sort",     bubble_sort,    "#89b4fa", "#1e1e2e"),
    ("▶ Selection Sort",  selection_sort, "#a6e3a1", "#1e1e2e"),
    ("▶ Insertion Sort",  insertion_sort, "#fab387", "#1e1e2e"),
]

for text, cmd, bg, fg in buttons_row1:
    tk.Button(btn_frame1, text=text,
              command=cmd,
              bg=bg, fg=fg,
              font=("Arial", 10, "bold"),
              padx=12, pady=5,
              relief="flat",
              cursor="hand2").pack(side="left", padx=5)

# Row 2 — Advanced algorithms
buttons_row2 = [
    ("▶ Quick Sort",      quick_sort,     "#f9e2af", "#1e1e2e"),
    ("▶ Heap Sort",       heap_sort,      "#cba6f7", "#1e1e2e"),
    ("🔍 Binary Search",  binary_search,  "#f38ba8", "#1e1e2e"),
]

for text, cmd, bg, fg in buttons_row2:
    tk.Button(btn_frame2, text=text,
              command=cmd,
              bg=bg, fg=fg,
              font=("Arial", 10, "bold"),
              padx=12, pady=5,
              relief="flat",
              cursor="hand2").pack(side="left", padx=5)

# ── Legend ───────────────────────────────────────────────────────
legend_frame = tk.Frame(root, bg="#1e1e2e")
legend_frame.pack(pady=3)

legends = [
    ("■ Default",  COLOR_DEFAULT),
    ("■ Compare",  COLOR_COMPARE),
    ("■ Swap",     COLOR_SWAP),
    ("■ Sorted",   COLOR_SORTED),
    ("■ Pivot",    COLOR_PIVOT),
    ("■ Searching",COLOR_SEARCH),
    ("■ Discarded",COLOR_DISCARD),
]

for text, color in legends:
    tk.Label(legend_frame, text=text,
             bg="#1e1e2e", fg=color,
             font=("Arial", 9)).pack(side="left", padx=8)

# ── Initial Draw ─────────────────────────────────────────────────
draw(arr)
root.mainloop()