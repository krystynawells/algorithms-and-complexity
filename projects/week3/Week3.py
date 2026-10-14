import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    return mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 1:
    Implement the Linear Search Algorithm for an arbitrary input array
    """)
    return


@app.cell
def _(np):
    def linSearch(arr, val):
        for i in range(len(arr)):
            if arr[i] == val:
                return i
        return -1

    arr_t1 = np.array([1, 2, 8, 4, 6, 3, 0, 7, 5, 9])
    target_t1 = 5

    idx_t1 = linSearch(arr_t1, target_t1)
    return arr_t1, idx_t1, linSearch, target_t1


@app.cell
def _(arr_t1, idx_t1, mo, target_t1):
    mo.md(f"""
    ## Result

    arbitrary input array: {arr_t1}

    number {target_t1} is in index {idx_t1}
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2
    Create an array of 500 elements, where the array is not sorted and has elements from 0 to 499 with no repetitions (Hint: use ```np.arange()``` and then ```np.random.shuffle()```).
    Then, call the ```search()``` function to find number 10 in the array. Calculate the time it takes to find the number.
    """)
    return


@app.cell
def _(linSearch, mo, np, time):
    # create array of 0–499 and shuffle
    arr_500 = np.arange(500)
    np.random.shuffle(arr_500)

    target = 10

    # time the search
    start_time = time.time()
    idx_500 = linSearch(arr_500, target)
    end_time = time.time()

    elapsed = end_time - start_time

    # display result 
    mo.md(
    f"""
    ## Result

    array of 500 elements: {arr_500}

    number {target} is in index {idx_500}

    time took: {elapsed:.6f}
    """
    )

    return


@app.cell
def _(mo):
    mo.md("""
    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3
    Repeat the process in Task 2 for 1000 different arrays (all of them of size 500), and store the elapsed time for each one of these runs. Then plot a frequency histogram for the time values.
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(linSearch, np):
    import matplotlib.pyplot as plt
    import time

    N = 1000
    times = np.empty(N)

    for i in range(N):
        arr = np.arange(500)
        np.random.shuffle(arr)

        start = time.time()
        linSearch(arr, 10)
        end = time.time()

        times[i] = end - start

    fig, ax = plt.subplots()
    ax.hist(times, bins=10, edgecolor="black")
    ax.set_xlabel("Time (seconds)")
    ax.set_ylabel("Frequency")
    ax.set_title("Linear Search Timing Across 1000 Runs")

    fig

    return (time,)


@app.cell
def _(mo):
    mo.md("""
    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4:
    Implement the Binary Search Algorithm for a sorted input array.
    """)
    return


@app.cell
def _binsearch(mo, np):
    # Binary Search
    def binSearch(arr, val):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == val:
                return mid
            elif arr[mid] < val:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    # ---- Task 4 run ----
    arr_t4 = np.array([1, 2, 3, 4, 5, 7, 8, 10])
    target_t4 = 4
    idx_t4 = binSearch(arr_t4, target_t4)

    mo.md(
        f"""
    ## Result

    array: {arr_t4}

    value {target_t4} is at index {idx_t4}
    """
    )

    return


@app.cell
def _(mo):
    mo.md("""
    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5:
    Implement the Recursive Binary Search Algorithm for a sorted input array.
    """)
    return


@app.cell
def _(mo, np):
    # Recursive Binary Search
    def binSearchRec(arr, left, right, val):
        # base case: interval empty
        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            return binSearchRec(arr, mid + 1, right, val)
        else:
            return binSearchRec(arr, left, mid - 1, val)

    # ---- Task 5 run ----
    arr_t5 = np.array([1, 2, 3, 4, 5, 7, 8, 10])
    target_t5 = 3
    idx_t5 = binSearchRec(arr_t5, 0, len(arr_t5) - 1, target_t5)

    mo.md(
        f"""
    ## Result

    array: {arr_t5}

    value {target_t5} is at index {idx_t5}
    """
    )

    return


if __name__ == "__main__":
    app.run()
