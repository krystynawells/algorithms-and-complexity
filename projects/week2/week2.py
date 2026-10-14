import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium", layout_file="layouts/week2.grid.json")


@app.cell
def _():
    import numpy as np
    import marimo as mo
    import plotly.graph_objs as go
    return go, mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 1: Insertion sort
    From the discussion in class, implement insertion sort.
    """)
    return


@app.function
def insertionSort(A):
    for j in range(1, len(A)):     
        key = A[j]                 
        i = j - 1                 


        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1


        A[i + 1] = key

    return A


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 2:
    Calculate the time that Insertion Sort takes to sort an array of 1000 random elements.
    """)
    return


@app.cell
def _(np):
    import time

    def measure_insertion_sort_time():
        # Generate 1000 random numbers
        arr = np.random.randint(0, 10000, 1000).tolist()

        start = time.time()
        insertionSort(arr)
        end = time.time()

        return end - start

    measure_insertion_sort_time()
    return (time,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Task 3: Bubble sort
    Now implement Bubble Sort
    """)
    return


@app.cell
def _():
    def bubbleSort(arr):
        n = len(arr)
        for i in range(n - 1):
            for j in range(n - i - 1):

                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    bubbleSort([1, 13, 2, 11, 29])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    -----------------------------------------------------------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Final Task (for next week)
    Use the code below to build your own interactive visualiser of sorting algorithms.
    Your visualiser should have the following functions:
    - It should allow the user choosing between three algorithms to use: Insertion sort, Bubble sort, and a third one of your choice (you can create your own crazy algorithm if you want).
    - Once that the user chooses their algorithm, they press "restart" to initiate. Then, the user can press "Increment" to run the next step of the sorting algorithm. This means that the user can run the algoithm step by step, every time the button is pressed.
    - The interface should colour the part of the array that has been sorted in a different colour than the unsorted part. This has been already implemented for the bubble sort case, but you will have to implement it for the other algorithms
    - Add interactive messages. For example, when choosing an algorithms, a pop-up message could appear explaining the basics of the chosen sorting algorithm.

    #### If you want to go beyond...
    - For bubble sort, add a different colour to the pairs that have had a swap in the last step, so the user can lnow which values have recently changed.
    - Add a monitor that shows the average time that the last step took (or you can average the last couple of steps to get a more accurate value)
    - Add the capability so the user can input custom arrays, of variable size and with particular structures (not only random arrays, for example reversed arrays, arrays with patterns, etcetera).

    Push your changes to your git.arts account by the beginning of the class next week.
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    # Gif Link 

    gif_url = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnI3OWc5emoydjI4ZjBuNHBhNjY5Z2FpajQxeHNyZzIyZ3R5dDN5NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NJGmiH9E5pMYM6qs6l/giphy.gif"

    mo.image(
        src=gif_url,
        width="220px",    
        height="auto",
        rounded=True,
    )
    return


@app.cell
def _(mo):
    # Gif Link 

    gif_url2 = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnI3OWc5emoydjI4ZjBuNHBhNjY5Z2FpajQxeHNyZzIyZ3R5dDN5NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/NJGmiH9E5pMYM6qs6l/giphy.gif"

    mo.image(
        src=gif_url2,
        width="220px",      
        height="auto",
        rounded=True,
    )
    return


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="
        max-width: 900px;
        margin: 24px auto;
        padding: 22px 28px;
        border-radius: 16px;
        background: linear-gradient(135deg, #ccffda, #ccffda
                                   );
        border: 2px solid #84bf94;
        text-align: center;
        box-shadow: 0 8px 18px rgba(111,112,111,0.5);
    ">
        <div style="
            font-size: 28px;
            font-weight: 600;
            color: #232e23;
            margin-bottom: 8px;
        ">
            Interactive Sorting Algorithm Visualizer
        </div>

        <div style="
            font-size: 16px;
            color: #555;
            line-height: 1.4;
        ">
            Choose an algorithm and interact to sort step-by-step with real-time visualizations
        </div>
    </div>
    """)
    return


@app.cell
def _(mo):
    # UI controls for the sorting visualiser

    # Dropdown menu allowing the user to choose which sorting algorithm to run.
    algo_dropdown = mo.ui.dropdown(
        options=["bubble", "insertion", "selection"],
        value="bubble",
        label="Sorting algorithm:"
    )



    # Slider that controls the length of the array to be generated and sorted.

    size_slider = mo.ui.slider(
        start=10, stop=150, value=60, step=1,
        label="Array size"
    )

    # Slider that determines the incremental step value used in some comparisons

    step_slider = mo.ui.slider(
        start=0, stop=50, value=0, step=1,
        label="Increment"
    )

    mo.vstack([
        mo.hstack([algo_dropdown, size_slider]),
        step_slider,
    ])
    return algo_dropdown, size_slider, step_slider


@app.cell
def _(algo, algo_dropdown, mo):
    # Retrieve the currently selected sorting algorithm from the dropdown 

    algo2 = algo_dropdown.value


    # Explanations for each sorting algorithm 

    algo_descriptions = {
        "bubble": (
            "**Bubble sort**\n\n"
            "• Repeatedly compares *neighbouring* elements and swaps them if they are in the wrong order.\n"
            "• After each pass, the largest element “bubbles” to the end of the array.\n"
            "• Simple but slow on large lists (O(n²))."
        ),
        "insertion": (
            "**Insertion sort**\n\n"
            "• Builds the sorted array one element at a time.\n"
            "• Takes the next element and inserts it into the correct place in the already-sorted prefix.\n"
            "• Efficient for small or nearly sorted arrays."
        ),
        "selection": (
            "**Selection sort**\n\n"
            "• Repeatedly scans the *unsorted* part of the array to find the minimum.\n"
            "• Swaps that minimum into the next position of the sorted prefix.\n"
            "• Always does the same number of comparisons (O(n²))."
        ),
    }

    # Display the correct description based on the selected algorithm 

    mo.md(algo_descriptions.get(algo, "Choose an algorithm to see an explanation."))
    return


@app.cell
def _(algo_dropdown, mo, np, size_slider, time):
    # Retrieve the user’s selections from the UI widgets

    algo3 = algo_dropdown.value
    n2 = size_slider.value


    # Main sorting function 
    # This function generates a random array of size n2 and applies the selected algorithm.

    def run_sort():
        # Generate a random list of integers between 0 and 100
        arr = np.random.randint(0, 100, size=n2).tolist()

        # --------------------------- Bubble Sort ---------------------------

        if algo3 == "bubble":
            for i in range(len(arr)):
                for j in range(0, len(arr) - i - 1):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]

        # ------------------------- Insertion Sort -------------------------

        elif algo3 == "insertion":
            for j in range(1, len(arr)):
                key = arr[j]
                i = j - 1
                while i >= 0 and arr[i] > key:
                    arr[i + 1] = arr[i]
                    i -= 1
                arr[i + 1] = key

        # ------------------------- Selection Sort -------------------------

        else:
            n_local = len(arr)
            for i in range(n_local):
                m = i
                for j in range(i + 1, n_local):
                    if arr[j] < arr[m]:
                        m = j
                arr[i], arr[m] = arr[m], arr[i]


    # Measure execution time for performance comparison 

    num_runs = 5
    times = []

    for _ in range(num_runs):
        t0 = time.time()
        run_sort()
        t1 = time.time()
        times.append((t1 - t0) * 1000)  

    avg_ms = sum(times) / num_runs

    # Display results back in the interface

    mo.md(
        f"""### Step Time Monitor  
    **Algorithm:** {algo3.capitalize()} · **Array size:** {n2}  
    Average sort time over {num_runs} runs: **{avg_ms:.3f} ms**"""
    )
    return


@app.cell
def _(algo_dropdown, go, mo, np, size_slider, step_slider):

    # Generate a reproducible starting array for all algorithms


    def make_array(n: int, seed: int = 0):
        rng = np.random.default_rng(seed)
        return rng.integers(0, 100, size=n).tolist()

    base_arr = make_array(size_slider.value)



    # BUBBLE SORT — Partial execution
    # Runs only a given number of passes ('steps') for animation.

    def bubble_partial(a, steps):
        A = a.copy()
        n = len(A)
        step = 0

        for i in range(n - 1):
            if step >= steps:
                break  # stop early for animation

            for j in range(0, n - 1 - i):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]

            step += 1

        # Sorted tail size grows each pass
        sorted_tail = min(step, n - 1)
        return A, sorted_tail



    # INSERTION SORT — Partial execution
    # After each step, one more element is inserted into the
    # correct place in the already-sorted prefix.

    def insertion_partial(a, steps):
        A = a.copy()
        n = len(A)
        step = 0

        for j in range(1, n):
            key = A[j]
            i = j - 1

            while i >= 0 and A[i] > key:
                A[i + 1] = A[i]
                i -= 1
            A[i + 1] = key

            step += 1
            if step >= steps:  
                break  # stop early

        sorted_prefix = min(step + 1, n)
        return A, sorted_prefix



    # SELECTION SORT — Partial execution
    # Each step places the next minimum element at its correct index.

    def selection_partial(a, steps):
        A = a.copy()
        n = len(A)
        step = 0

        for i in range(n - 1):
            min_idx = i
            for j in range(i + 1, n):
                if A[j] < A[min_idx]:
                    min_idx = j

            A[i], A[min_idx] = A[min_idx], A[i]
            step += 1

            if step >= steps:
                break  # animate early stop

        sorted_prefix = min(step, n)
        return A, sorted_prefix



    # Select which sorting algorithm to animate

    steps = step_slider.value
    algo = algo_dropdown.value

    if algo == "bubble":
        arr, sorted_tail = bubble_partial(base_arr, steps)
        sorted_prefix = 0     
    elif algo == "insertion":
        arr, sorted_prefix = insertion_partial(base_arr, steps)
        sorted_tail = 0
    else:  # selection
        arr, sorted_prefix = selection_partial(base_arr, steps)
        sorted_tail = 0



    # Build colour array for plot
    # skyblue  = unsorted
    # lightgreen = sorted portion

    n = len(arr)
    colors = ["skyblue"] * n

    if algo == "bubble":
        # Bubble sort 
        for k in range(n - sorted_tail, n):
            if 0 <= k < n:
                colors[k] = "lightgreen"
    else:
        # Insertion & Selection
        for k in range(sorted_prefix):
            if 0 <= k < n:
                colors[k] = "lightgreen"



    # Create the bar plot representing the array at the current step

    fig = go.Figure(data=[go.Bar(
        x=np.arange(n),
        y=arr,
        marker_color=colors
    )])

    fig.update_layout(
        title=f"{algo.capitalize()} — Step {steps}",
        xaxis_title="Index",
        yaxis_title="Value",
        template="plotly_white",
        width=800,
        height=400,
    )

    # Display animated chart
    mo.ui.plotly(fig)
    return (algo,)


if __name__ == "__main__":
    app.run()
