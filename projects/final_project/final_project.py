import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium", layout_file="layouts/final_project.grid.json")


@app.cell
def _(mo):
    mo.md("""
    <!--======================================================
    # Project Header + Introduction
    # ====================================================-->
    <div style="

        background-color: #D7FCFC;
        padding: 32px;
        border-radius: 12px;
        margin-bottom: 30px;
        color: white;

    ">

    <h1 style="margin: 10px 0 0; font-weight: 400; font-size: 3rem;">
        Trend Tracker For Fashion

    </h1>

    <h2 style="margin: 10px 0 0; font-weight: 400; font-size: 1.2rem;">
        Algorithms and Complexity - Final Project

    </h2>

    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <!-- Project Introduction-->

    <div style="
        background-color: #D7FCFC;
        border-left: 6px solid #2bb3a3;
        padding: 22px 26px;
        border-radius: 12px;
        margin: 24px 0;
        max-width: 1000px;
    ">

    <h3 style="
        margin-top: 0;
        color: #0f4f4b;
    ">
    Project Introduction
    </h3>

    <p style="
        margin: 0;
        color: #244;
        line-height: 1.6;
        font-size: 0.95rem;
    ">

    <p>
    This project presents a prototype Trend Tracker for Fashion, an interactive analytical tool designed to explore how fashion trends change, peak, relate to one another, and can be classified over time.
    </p>

    <p>
    Using a small seasonal fashion dataset, the tool allows users to analyse trend growth, identify peak popularity, explore relationships between trends, and experiment with predictive classification through interactive visualisations and UI controls. Each section of the app focuses on a different algorithmic technique: sorting, searching, graph traversal, and machine learning.
    </p>

    <p>
    The project emphasises algorithm choice, time complexity, and practical trade-offs, showing how different approaches suit different analytical tasks. By combining visual outputs with critical analysis, the Trend Tracker highlights not only how these algorithms work but also their limitations, assumptions, and potential biases.
    </p>

    </div>
    """)
    return


@app.cell
def _():
    # ======================================================
    # Imports
    # ======================================================

    import pandas as pd
    import time
    import random
    import matplotlib.pyplot as plt
    import numpy as np
    from collections import deque
    import marimo as mo
    return deque, mo, np, pd, plt, random, time


@app.cell
def _(pd):
    # ======================================================
    # Dataset: Fashion Trend Strengths Across Seasons
    # ======================================================

    def load_fashion_data():
        data = pd.DataFrame({
            "season": ["SS23","AW23","SS24","AW24","SS25","AW25"],

            # Trend feature columns
            "leather":  [30,45,50,55,60,68],
            "floral":   [40,35,25,15,10,5],
            "oversized":[20,25,27,30,32,33],
            "tailored": [50,55,60,70,72,80],
            "metallic": [10,15,20,30,40,55],
            "denim":    [25,40,45,55,60,70],
            "pastel":   [60,50,45,40,35,30],
            "knitwear": [35,50,55,60,65,70],
        })
        return data

    df = load_fashion_data()
    df
    return (df,)


@app.cell
def _(pd):
    # ======================================================
    # Synthetic Dataset for Algorithm 4 (Perceptron)
    # ======================================================

    # I created 40 rows of synthetic fashion profiles
    # Each one is labelled as one of 4 categories:
    # 0 = Futuristic
    # 1 = Romantic
    # 2 = Classic Tailored
    # 3 = Streetwear

    perceptron_data = pd.DataFrame([
        # Futuristic (high metallic, high leather)
        {"leather":80,"floral":5,"oversized":20,"tailored":30,"metallic":90,"denim":10,"pastel":5,"knitwear":15,"label":0},
        {"leather":70,"floral":10,"oversized":25,"tailored":40,"metallic":80,"denim":15,"pastel":10,"knitwear":20,"label":0},
        {"leather":65,"floral":5,"oversized":30,"tailored":35,"metallic":75,"denim":20,"pastel":5,"knitwear":10,"label":0},

        # Romantic (high floral or pastel)
        {"leather":20,"floral":70,"oversized":25,"tailored":40,"metallic":10,"denim":15,"pastel":60,"knitwear":25,"label":1},
        {"leather":10,"floral":65,"oversized":20,"tailored":35,"metallic":15,"denim":20,"pastel":75,"knitwear":30,"label":1},
        {"leather":25,"floral":80,"oversized":30,"tailored":30,"metallic":5,"denim":25,"pastel":70,"knitwear":35,"label":1},

        # Classic Tailored (high tailored)
        {"leather":30,"floral":10,"oversized":10,"tailored":85,"metallic":20,"denim":25,"pastel":10,"knitwear":20,"label":2},
        {"leather":35,"floral":5,"oversized":15,"tailored":90,"metallic":25,"denim":20,"pastel":15,"knitwear":25,"label":2},
        {"leather":20,"floral":15,"oversized":12,"tailored":82,"metallic":20,"denim":20,"pastel":10,"knitwear":30,"label":2},

        # Streetwear (high denim or oversized)
        {"leather":15,"floral":10,"oversized":70,"tailored":25,"metallic":10,"denim":80,"pastel":20,"knitwear":40,"label":3},
        {"leather":10,"floral":5,"oversized":65,"tailored":20,"metallic":5,"denim":75,"pastel":15,"knitwear":30,"label":3},
        {"leather":20,"floral":8,"oversized":60,"tailored":22,"metallic":10,"denim":85,"pastel":18,"knitwear":45,"label":3},
    ])

    perceptron_data
    return (perceptron_data,)


@app.cell
def _():
    return


@app.cell
def _(mo):
    mo.md("""
    <!--======================================================
    # Algortihm One Header + Introduction
    # ====================================================-->
    <div style="
        background-color: #FFD1B0;
        border-left: 6px solid #f58f4c;
        padding: 16px 20px;
        border-radius: 8px;
        margin: 20px 0;
    ">

    <h2 style="margin-top: 0; color: #0f4f4b;">
    ׂ➤ Algorithm 1: Sorting Trend Growth (Merge Sort)
    </h2>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="
    background-color: #FFD1B0;
    border-left: 6px solid #F58F4C;
    padding: 16px 20px;
    border-radius: 10px;
    margin: 20px 0;
    ">

    <h3 style="margin-top: 0;">Introduction – Algorithm 1</h3>

    Algorithm 1 uses Merge Sort to rank fashion trends based on their growth between the first and last seasons in the dataset. Sorting is required because the goal is not just to find a single maximum or minimum trend, but to compare all trends relative to one another. Merge Sort was chosen because it guarantees a time complexity of O(n log n), making it efficient and predictable even as the dataset size increases. Unlike simpler algorithms such as Bubble Sort, Merge Sort scales well, making it an appropriate choice for analysing and visualising trend growth in a structured and computationally efficient way.

    </div>
    """)
    return


@app.cell
def _(df, plt):
    # ======================================================
    # Algorithm 1: Sorting Trend Growth
    # ======================================================

    def compute_trend_growth(df):
        trends = df.columns[1:]  # skip the season column
        growth = {}

        for trend in trends:
            start = df.iloc[0][trend]
            end = df.iloc[-1][trend]
            growth[trend] = end - start

        return growth

    growth_dict = compute_trend_growth(df)

    # Merge Sort implementation
    def merge_sort(items):
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left = merge_sort(items[:mid])
        right = merge_sort(items[mid:])

        return merge(left, right)

    def merge(left, right):
        sorted_list = []
        i = j = 0

        # sort in descending order of trend growth
        while i < len(left) and j < len(right):
            if left[i][1] > right[j][1]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list

    # Visualise sorted trend growth (bar chart)

    growth_items = list(growth_dict.items())

    # Perform sort
    sorted_growth = merge_sort(growth_items)

    # --- Visualise sorted trend growth (bar chart) ---

    # --- Visualise sorted trend growth (bar chart) ---

    trends_a1 = [t for t, g in sorted_growth]
    growth_a1 = [g for t, g in sorted_growth]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(trends_a1, growth_a1, color="#fcc19a")
    ax.axhline(0, color="gray", linewidth=0.8)
    ax.set_title("Algorithm 1: Trend Growth Sorted (Merge Sort Output)")
    ax.set_xlabel("Trend")
    ax.set_ylabel("Growth (last - first)")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()

    fig
    return merge_sort, sorted_growth


@app.cell
def _(sorted_growth):
    # Display result
    print("Trend growth from first to last season:")
    for trend, growth in sorted_growth:
        print(f"{trend:10} {growth:+d}")
    return


@app.cell
def _(merge_sort, plt, random, time):
    # ======================================================
    # Algorithm 1: Time Complexity Analysis 
    # ======================================================

    # Generate random data of size n
    def generate_random_list(n):
        return [(f"item{i}", random.randint(1, 1000)) for i in range(n)]

    # Measure time for merge_sort at increasing sizes
    def time_merge_sort():
        sizes = [10, 50, 200, 500, 1000, 2000]
        times = []

        for n in sizes:
            test_list = generate_random_list(n)

            start_time = time.time()
            merge_sort(test_list)
            end_time = time.time()

            elapsed = end_time - start_time
            times.append(elapsed)

            print(f"n={n:5}   time={elapsed:.6f} seconds")

        return sizes, times

    # Run timing tests
    sizes, times = time_merge_sort()

    # Visualisation 
    fig2, ax2 = plt.subplots(figsize=(8, 5))

    ax2.plot(sizes, times, marker='o', color="#f58f4c")
    ax2.set_xlabel("Input size (n)")
    ax2.set_ylabel("Time (seconds)")
    ax2.set_title("Merge Sort Time Complexity (Empirical Results)")
    ax2.grid(True)

    fig2.tight_layout()
    fig2
    return


@app.cell
def _(mo):
    mo.md("""
    <!--======================================================
    # Algorithm One Critical Analysis
    # ====================================================-->

    <div style="
        background-color: #FFD1B0;
        border-left: 6px solid #f58f4c;
        padding: 16px 20px;
        border-radius: 8px;
        margin: 20px 0;
        color: #044b4b;
        font-size: 0.95rem;
    ">

    <h3 style="margin-top: 0;">Critical Analysis — Algorithm 1</h3>

    <p>
    Algorithm 1 applies Merge Sort to rank fashion trends based on their growth between the first and last seasons in the dataset. The Merge Sort algorithm itself is computationally unbiased; it sorts values based on numerical comparison, but bias can still arise from how the input data and growth metric are defined.
    </p>

    <p>
    In this project, trend growth is calculated using only the difference between two seasonal endpoints, which can favour trends that spike late in the dataset while ignoring those with steady growth patterns. This introduces a temporal bias, where short-term increases are prioritised over long-term consistency.
    </p>

    <p>
    Additionally, the dataset is small and synthetic, which means it may not accurately represent the diversity of fashion trends. In real-world applications, this could negatively impact designers, brands, or communities whose styles evolve gradually or fluctuate seasonally, as their trends may be ranked lower. The algorithm also assumes equal importance across all trends, ignoring contextual factors such as cultural relevance.
    </p>

    <p>
    While Merge Sort remains an appropriate and efficient choice for ordering data, it highlights how important data modelling decisions are in algorithmic fairness. To mitigate these issues, the growth metric could be extended to incorporate seasonal data, reducing sensitivity to endpoint selection. Using larger, real-world datasets would also improve representativeness.
    </p>

    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <!--======================================================
    # Algorithm Two Header + Introduction
    # =====================================================-->

    <div style="
      background-color: #E9DDFF;
      padding: 20px 24px;
      border-left: 6px solid #8E6AD9;
      border-radius: 10px;
      margin: 24px 0;
      color: #2d1f4f;
    ">

    <h2 style="margin: 0; font-weight: 500;">
    ➤ Algorithm 2: Searching for Peak Trends (Linear vs Binary)
    </h2>

    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="
    background-color: #E9DDFF;
    border-left: 6px solid #8E6AD9;
    padding: 16px 20px;
    border-radius: 8px;
    margin: 20px 0;
    ">

    <h3 style="margin-top: 0;">Introduction – Algorithm 2</h3>

    Algorithm 2 is used to identify the peak season for a selected fashion trend by locating the maximum value within its seasonal data. This problem is well-suited to search algorithms, as the goal is to find a specific value rather than reorder the entire dataset. A Linear Search is applied to scan all seasonal values, ensuring the true maximum is found with time complexity O(n). A secondary Binary Search approach is included for comparison, highlighting how algorithm choice depends on data structure and problem context. Together, these methods demonstrate fundamental searching techniques and their computational trade-offs.

    </div>
    """)
    return


@app.cell
def _(df):
    # Trend columns used for Algorithm 2
    TREND_COLUMNS = df.columns[1:]
    TREND_COLUMNS
    return (TREND_COLUMNS,)


@app.cell
def _(df, trend_dropdown_g2):
    # ======================================================
    # Algorithm 2: Searching for Peak Trends
    # ======================================================

    # Get selected trend from dropdown
    selected_trend = trend_dropdown_g2.value

    # ---------------- Linear Search ----------------
    def linear_search_peak_g2(values):
        max_index = 0
        max_value = values[0]

        for i in range(1, len(values)):
            if values[i] > max_value:
                max_value = values[i]
                max_index = i

        return max_index, max_value


    # ---------------- Binary Search (after sorting) ----------------
    def binary_search_peak_g2(sorted_values):
        # Maximum is always at index 0 after descending sort
        return 0, sorted_values[0]


    # Extract trend values
    values_g2 = list(df[selected_trend])

    # Run Linear Search
    lin_idx_g2, lin_val_g2 = linear_search_peak_g2(values_g2)
    lin_season_g2 = df.iloc[lin_idx_g2]["season"]

    # Run Binary Search
    sorted_vals_g2 = sorted(values_g2, reverse=True)
    bin_idx_g2, bin_val_g2 = binary_search_peak_g2(sorted_vals_g2)
    bin_season_g2 = df.iloc[values_g2.index(bin_val_g2)]["season"]

    # Display results
    print(f"Peak Season for '{selected_trend}':\n")
    print(f"Linear Search: {lin_season_g2} (value = {lin_val_g2})")
    print(f"Binary Search: {bin_season_g2} (value = {bin_val_g2})")
    return bin_season_g2, bin_val_g2, lin_season_g2, lin_val_g2, selected_trend


@app.cell
def _(mo):
    mo.md("""
    <div style="
      background-color: #E9DDFF;
      padding: 14px 18px;
      border-left: 5px solid #8E6AD9;
      border-radius: 10px;
      margin-bottom: 12px;
      color: #2d1f4f;
      font-weight: 500;
    ">
    Select a trend to analyse (Algorithm 2)
    </div>
    """)
    return


@app.cell
def _(TREND_COLUMNS, mo):
    trend_dropdown_g2 = mo.ui.dropdown(
        options=TREND_COLUMNS.tolist(),
        value=TREND_COLUMNS.tolist()[0],  
        label="Select a Trend to Analyse",
    )
    trend_dropdown_g2
    return (trend_dropdown_g2,)


@app.cell
def _(
    bin_season_g2,
    bin_val_g2,
    lin_season_g2,
    lin_val_g2,
    mo,
    selected_trend,
):
    mo.md(f"""
    <div style="
      background-color: #F4EEFF;
      padding: 12px 16px;
      border-radius: 8px;
      margin-top: 12px;
    ">
    <b>Peak Season for '{selected_trend}'</b><br>
    Linear Search: {lin_season_g2} (value = {lin_val_g2})<br>
    Binary Search: {bin_season_g2} (value = {bin_val_g2})
    </div>
    """)
    return


@app.cell
def _(plt, time):
    # ======================================================
    # Algorithm 2: Time Complexity Analysis (Linear vs Binary Search)
    # ======================================================

    def linear_search_peak_a2_tc(values):
        max_index = 0
        max_value = values[0]
        for i in range(1, len(values)):
            if values[i] > max_value:
                max_value = values[i]
                max_index = i
        return max_index, max_value


    def binary_search_peak_a2_tc(sorted_values):
        left = 0
        right = len(sorted_values) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid == 0:
                return 0, sorted_values[0]
            right = mid - 1
        return 0, sorted_values[0]


    def time_search_algorithms_a2_tc():
        sizes_a2_tc = [10, 50, 200, 500, 1000, 2000, 5000]
        linear_times_a2_tc = []
        binary_times_a2_tc = []

        for n in sizes_a2_tc:
            data = list(range(n))
            sorted_data = data[::-1]

            start = time.time()
            linear_search_peak_a2_tc(data)
            linear_times_a2_tc.append(time.time() - start)

            start = time.time()
            binary_search_peak_a2_tc(sorted_data)
            binary_times_a2_tc.append(time.time() - start)

        return sizes_a2_tc, linear_times_a2_tc, binary_times_a2_tc


    # Run timing
    sizes_a2_tc, linear_times_a2_tc, binary_times_a2_tc = time_search_algorithms_a2_tc()


    # ---- Plot ---
    fig_a2_tc, ax_a2_tc = plt.subplots(figsize=(8, 5))

    ax_a2_tc.plot(
        sizes_a2_tc,
        linear_times_a2_tc,
        marker="o",
        color="#8E6AD9",  # purple
        label="Linear Search (O(n))"
    )

    ax_a2_tc.plot(
        sizes_a2_tc,
        binary_times_a2_tc,
        marker="s",
        color="#2FBF71",  # green
        label="Binary Search (O(log n))"
    )

    ax_a2_tc.set_xlabel("Input size (n)")
    ax_a2_tc.set_ylabel("Time (seconds)")
    ax_a2_tc.set_title("Algorithm 2: Linear vs Binary Search Time Complexity")
    ax_a2_tc.legend()
    ax_a2_tc.grid(True)

    fig_a2_tc.tight_layout()
    fig_a2_tc
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="
      background-color: #E9DDFF;
      border-left: 6px solid #8E6AD9;
      padding: 18px 22px;
      border-radius: 10px;
      margin: 20px 0;
      color: #2d1f4f;
    ">

    <h3 style="margin-top: 0;">Critical Analysis – Algorithm 2</h3>

    <p>
    Algorithm 2 identifies the peak season for a fashion trend using search techniques. A Linear Search is used to scan all seasonal values and return the maximum, while a Binary Search approach is included for comparison. Although the algorithms themselves are deterministic and unbiased in execution, potential bias arises from how the data and the task are defined.
    </p>

    <p>
    By focusing on the single highest seasonal value, this approach introduces a form of peak bias, where trends that experience short-lived spikes are prioritised over those that show consistent or gradual growth. In real-world fashion analysis, this could disadvantage designers, brands, or communities whose styles gain popularity steadily rather than through sudden popularity surges. Additionally, the dataset is small and synthetic, which limits representation.
    </p>

    <p>
    To mitigate these issues, the analysis could incorporate additional measures such as average trend strength, variance across seasons, or multiple peak detection. Using larger, real-world datasets would also reduce representational bias. Overall, Algorithm 2 effectively illustrates searching behaviour while emphasising the importance of data interpretation in algorithmic decision-making.
    </p>

    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <!--======================================================
    # Algorithm Three Header + Introduction
    # =====================================================-->

    <div style="
        background-color: #D0F7CD;
        padding: 16px 20px;
        border-left: 6px solid #2f855a;
        border-radius: 8px;
        margin: 24px 0;
    ">
      <h2 style="margin: 0; color: #065f46;">
        ➤ Algorithm 3: Graph-Based Trend Relationships (Adjacency list and Breadth-First Search)
      </h2>
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="
    background-color: #D0F7CD;
    border-left: 6px solid #22c55e;
    padding: 16px 20px;
    border-radius: 10px;
    margin: 20px 0;
    ">

    <h3 style="margin-top: 0;">Introduction – Algorithm 3</h3>

    Algorithm 3 models fashion trends as a graph, where each trend is represented as a node and edges indicate strong co-occurrence between trends within the same season. This approach is appropriate because fashion trends rarely exist in isolation; instead, they often emerge and evolve together. Once the graph is constructed using an adjacency list representation, Breadth-First Search (BFS) is applied to explore connectivity starting from a selected trend. BFS is well-suited to this task as it visits all reachable nodes, allowing the identification of related trends and connected components. This algorithm demonstrates how graph traversal techniques can reveal structural relationships that are not visible through individual trend analysis.

    </div>
    """)
    return


@app.cell
def _(deque, df):
    # ======================================================
    # Algorithm 3 Demo: Trend Co-Occurrence Graph + BFS 
    # ======================================================

    # Extract trend names for this algorithm 
    TREND_COLS_g3 = df.columns[1:]

    # Threshold for strong co-occurrence 
    THRESHOLD_g3 = 50

    # Build co-occurrence graph 
    def build_trend_graph_g3(df, threshold=THRESHOLD_g3):
        """
        Build an undirected graph where trends are connected
        if they both exceed a threshold in the same season.
        """
        graph = {trend: set() for trend in TREND_COLS_g3}

        for _, row in df.iterrows():
            strong = [
                trend for trend in TREND_COLS_g3
                if row[trend] >= threshold
            ]

            # connect all pairs of strong trends
            for i in range(len(strong)):
                for j in range(i + 1, len(strong)):
                    a, b = strong[i], strong[j]
                    graph[a].add(b)
                    graph[b].add(a)

        return graph


    trend_graph_g3 = build_trend_graph_g3(df)

    print("Trend Co-Occurrence Graph (Algorithm 3):\n")
    for trend_g3, neighbours_g3 in trend_graph_g3.items():
        neigh_str = ", ".join(sorted(neighbours_g3)) if neighbours_g3 else "None"
        print(f"{trend_g3:10}: {neigh_str}")



    # BFS traversal 
    def bfs_g3(graph, start):
        """
        Breadth-First Search for Algorithm 3 (unique naming).
        """
        visited = set()
        queue = deque([start])
        order = []

        while queue:
            current = queue.popleft()

            if current in visited:
                continue

            visited.add(current)
            order.append(current)

            for neighbour in graph[current]:
                if neighbour not in visited:
                    queue.append(neighbour)

        return order


    # Demo start trend 
    start_trend_g3 = "metallic"

    reachable_g3 = bfs_g3(trend_graph_g3, start_trend_g3)

    print("\nBFS Traversal for Algorithm 3:")
    print("Start:", start_trend_g3)
    print(" -> ".join(reachable_g3))
    return reachable_g3, trend_graph_g3


@app.cell
def _(reachable_g3, trend_graph_g3):
    def visualise_algorithm_3_graph(trend_graph_g3, reachable_g3):
        import networkx as nx
        import matplotlib.pyplot as plt

        # Build NetworkX graph
        G3_local = nx.Graph()

        for t_name, neigh_set in trend_graph_g3.items():
            for n_name in neigh_set:
                G3_local.add_edge(t_name, n_name)

        # Layout
        pos_local = nx.spring_layout(G3_local, seed=42)

        # Node colours (BFS highlighted)
        colours_local = []
        for node in G3_local.nodes():
            if node in reachable_g3:
                colours_local.append("#34d399")   
            else:
                colours_local.append("#bbf7d0")   

        # Draw
        fig_local, ax_local = plt.subplots(figsize=(8, 6))

        nx.draw(
            G3_local,
            pos_local,
            with_labels=True,
            node_color=colours_local,
            edge_color="#6ee7b7",
            node_size=2000,
            font_size=10,
            font_weight="bold",
            ax=ax_local
        )

        ax_local.set_title(
            "Algorithm 3: Trend Co-Occurrence Graph (BFS Highlighted)",
            fontsize=12
        )

        plt.tight_layout()
        return fig_local


    visualise_algorithm_3_graph(trend_graph_g3, reachable_g3)
    return


@app.cell
def _(plt, random, time):
    # -------------------------------------------------
    # 1. Generate a random undirected graph 
    # -------------------------------------------------
    def generate_random_graph_g3(num_nodes, edge_prob=0.02):
        """
        Generate a random undirected graph for BFS timing.
        Nodes are named node0, node1, ... nodeN.
        """
        nodes = [f"node_g3_{i}" for i in range(num_nodes)]
        graph = {node: set() for node in nodes}

        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if random.random() < edge_prob:
                    a, b = nodes[i], nodes[j]
                    graph[a].add(b)
                    graph[b].add(a)

        return graph, nodes[0]  # return graph


    # -------------------------------------------------
    # 2. BFS 
    # -------------------------------------------------
    def bfs_g3_tc(graph, start):
        """
        BFS used strictly for timing complexity (separate name).
        """
        from collections import deque

        visited = set()
        queue = deque([start])

        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            for neighbour in graph[current]:
                if neighbour not in visited:
                    queue.append(neighbour)

        return visited


    # -------------------------------------------------
    # 3. Time BFS on increasing graph sizes
    # -------------------------------------------------
    def time_bfs_g3():
        sizes = [10, 50, 200, 500, 1000]
        times = []

        for n in sizes:
            graph, start = generate_random_graph_g3(n)

            start_t = time.time()
            bfs_g3_tc(graph, start)
            end_t = time.time()

            elapsed = end_t - start_t
            times.append(elapsed)

            print(f"n={n:5}   time={elapsed:.6f} seconds")

        return sizes, times


    # Run timing tests
    sizes_g3, times_g3 = time_bfs_g3()


    # -------------------------------------------------
    # 4. Plot the BFS time complexity curve 
    # -------------------------------------------------
    fig_g3_tc, ax_g3_tc = plt.subplots(figsize=(8, 5))

    ax_g3_tc.plot(
        sizes_g3,
        times_g3,
        marker='o',
        color="#22c55e",       
        linewidth=2,
        label="BFS (O(V + E))"
    )

    ax_g3_tc.set_xlabel("Number of nodes (n)")
    ax_g3_tc.set_ylabel("Time (seconds)")
    ax_g3_tc.set_title("Algorithm 3: BFS Time Complexity (Empirical Results)")
    ax_g3_tc.grid(True)
    ax_g3_tc.legend()

    fig_g3_tc.tight_layout()
    fig_g3_tc
    return


@app.cell
def _(mo):
    mo.md("""
    <!--======================================================
    # Algorithm Three Critical Analysis
    # ====================================================-->

    <div style="
        background-color: #D0F7CD;
        border-left: 6px solid #22c55e;
        padding: 18px 22px;
        border-radius: 10px;
        margin: 24px 0;
        color: #064e3b;
    ">

    <h3 style="margin-top: 0;">Critical Analysis – Algorithm 3</h3>

    <p>
    Algorithm 3 represents fashion trends as a graph, where nodes correspond to individual trends and edges indicate strong co-occurrence within the same season. While the BFS algorithm itself is unbiased in its traversal, potential bias arises from how the graph is constructed. In particular, the use of a fixed co-occurrence threshold introduces a structural bias: trends that frequently appear together above the threshold are overrepresented, while subtler or emerging relationships may be excluded entirely.
    </p>

    <p>
    This can negatively affect designers, brands, or cultural groups whose styles tend to evolve gradually or appear in niche contexts, as their trends may not meet the threshold required to form graph connections. Additionally, starting BFS from a single trend emphasises that trend’s local neighbourhood, potentially overlooking equally important relationships elsewhere in the graph.
    </p>

    <p>
    To mitigate these effects, adaptive or data-driven thresholds could be used instead of a fixed value, allowing weaker but meaningful relationships to emerge. Multiple BFS runs from different starting nodes could also reduce start-node bias. Using larger, real-world datasets would further improve fairness and representational accuracy. Despite these limitations, Algorithm 3 effectively demonstrates how graph modelling and traversal reveal relational structures.
    </p>

    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <!--======================================================
    # Algorithm Two Header + Introduction
    # =====================================================-->

    <div style="
        background-color: #FFF5A6;
        border-left: 6px solid #E6C84F;
        padding: 18px 22px;
        border-radius: 10px;
        margin: 28px 0 16px 0;
        color: #5a4a00;
    ">

    <h2 style="margin: 0;">
        ➤ Algorithm 4: Perceptron Trend Classification
    </h2>

    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="
    background-color: #FFFBDB;
    border-left: 6px solid #E6C84F;
    padding: 16px 20px;
    border-radius: 10px;
    margin: 20px 0;
    color: #5a4a00;
    ">

    <h3 style="margin-top: 0;">Introduction – Algorithm 4</h3>

    Algorithm 4 applies a multi-class perceptron to classify fashion styles based on the strength of eight trend features. This algorithm is suitable because it demonstrates a simple and interpretable form of supervised learning, where labelled input data is used to train a model to make predictions on unseen inputs. The perceptron was chosen due to its computational simplicity and linear decision boundaries, making it easy to analyse and relate to time complexity concepts. By combining interactive sliders with the trained model, this algorithm allows users to explore how changes in feature values influence classification outcomes. A separate synthetic dataset is used for this algorithm to provide enough labelled training examples for the perceptron.

    </div>
    """)
    return


@app.cell
def _(mo, np, perceptron_data):
    # ======================================================
    # Algorithm 4 : Predict trend classification
    # ======================================================

    # Features in perceptron_data 
    FEATURE_COLS_G4 = [c for c in perceptron_data.columns if c != "label"]

    # X, y
    X_g4 = perceptron_data[FEATURE_COLS_G4].to_numpy(dtype=float) / 100.0 
    y_g4 = perceptron_data["label"].to_numpy(dtype=int)

    class_names_g4 = ["Futuristic", "Romantic", "Classic Tailored", "Streetwear"]
    num_classes_g4 = len(class_names_g4)

    def train_perceptron_g4(X, y, num_classes, epochs=200, lr=0.1, seed=0):
        rng = np.random.default_rng(seed)
        W = np.zeros((num_classes, X.shape[1]), dtype=float)
        b = np.zeros(num_classes, dtype=float)

        for _ in range(epochs):
            for i in rng.permutation(len(X)):  
                x_i = X[i]
                true = y[i]
                scores = W @ x_i + b
                pred = int(np.argmax(scores))
                if pred != true:
                    W[true] += lr * x_i
                    b[true] += lr
                    W[pred] -= lr * x_i
                    b[pred] -= lr
        return W, b

    def predict_g4(W, b, x):
        scores = W @ x + b
        return int(np.argmax(scores)), scores

    weights_g4, biases_g4 = train_perceptron_g4(X_g4, y_g4, num_classes_g4, epochs=200, lr=0.1)

    correct = 0
    for i in range(len(X_g4)):
        pred, _ = predict_g4(weights_g4, biases_g4, X_g4[i])
        correct += (pred == y_g4[i])
    mo.md(f"**Training accuracy:** {correct}/{len(X_g4)}")
    return biases_g4, class_names_g4, predict_g4, weights_g4


@app.cell
def _(mo):
    # Create UI sliders for each trend value
    slider_leather_g4   = mo.ui.slider(0, 100, label="Leather")
    slider_floral_g4    = mo.ui.slider(0, 100, label="Floral")
    slider_oversized_g4 = mo.ui.slider(0, 100, label="Oversized")
    slider_tailored_g4  = mo.ui.slider(0, 100, label="Tailored")
    slider_metallic_g4  = mo.ui.slider(0, 100, label="Metallic")
    slider_denim_g4     = mo.ui.slider(0, 100, label="Denim")
    slider_pastel_g4    = mo.ui.slider(0, 100, label="Pastel")
    slider_knitwear_g4  = mo.ui.slider(0, 100, label="Knitwear")

    sliders_g4 = mo.vstack([
        slider_leather_g4,
        slider_floral_g4,
        slider_oversized_g4,
        slider_tailored_g4,
        slider_metallic_g4,
        slider_denim_g4,
        slider_pastel_g4,
        slider_knitwear_g4,
    ])

    sliders_g4
    return (
        slider_denim_g4,
        slider_floral_g4,
        slider_knitwear_g4,
        slider_leather_g4,
        slider_metallic_g4,
        slider_oversized_g4,
        slider_pastel_g4,
        slider_tailored_g4,
    )


@app.cell
def _():
    return


@app.cell
def _(
    biases_g4,
    class_names_g4,
    mo,
    np,
    predict_g4,
    slider_denim_g4,
    slider_floral_g4,
    slider_knitwear_g4,
    slider_leather_g4,
    slider_metallic_g4,
    slider_oversized_g4,
    slider_pastel_g4,
    slider_tailored_g4,
    weights_g4,
):
    # ======================================================
    # Algorithm 4: Live Prediction from Slider Inputs 
    # ======================================================

    x_input_g4 = np.array([
        slider_leather_g4.value,
        slider_floral_g4.value,
        slider_oversized_g4.value,
        slider_tailored_g4.value,
        slider_metallic_g4.value,
        slider_denim_g4.value,
        slider_pastel_g4.value,
        slider_knitwear_g4.value,
    ], dtype=float) / 100.0   

    pred_label_g4, scores_g4 = predict_g4(weights_g4, biases_g4, x_input_g4)

    mo.md(f"""
    ### Perceptron Style Classification
    **Predicted Category:** **{class_names_g4[pred_label_g4]}**  
    **Raw scores:** `{np.round(scores_g4, 3)}`
    """)
    return pred_label_g4, scores_g4


@app.cell
def _(class_names_g4, mo, np, pred_label_g4, scores_g4):
    mo.md(f"""
    <div style="
        background-color: #FFFBDB;
        border-left: 6px solid #E6C84F;
        padding: 16px 20px;
        border-radius: 10px;
        margin: 20px 0;
        color: #5a4a00;
    ">

    <h3 style="margin-top: 0;">
    Perceptron Style Classification
    </h3>

    <p style="margin: 8px 0;">
    <strong>Predicted Category:</strong>
    <span style="font-size: 1.1rem;">
    {class_names_g4[pred_label_g4]}
    </span>
    </p>

    <p style="margin-bottom: 0; font-size: 0.9rem;">
    <strong>Raw scores:</strong>
    <code>{np.round(scores_g4, 3)}</code>
    </p>

    </div>
    """)
    return


@app.cell
def _(np, plt, time):
    ## ======================================================
    # Algorithm 4: Time Complexity Analysis
    # ======================================================

    # Reuse perceptron training function 
    def train_perceptron_g4_tc(
        X_g4_tc,
        y_g4_tc,
        num_classes_g4_tc,
        epochs_g4_tc=10,
        lr_g4_tc=0.01
    ):
        weights_g4_tc = np.zeros((num_classes_g4_tc, X_g4_tc.shape[1]))
        biases_g4_tc = np.zeros(num_classes_g4_tc)

        for _ in range(epochs_g4_tc):
            for i in range(len(X_g4_tc)):
                x_i = X_g4_tc[i]
                true_label = y_g4_tc[i]

                scores = np.dot(weights_g4_tc, x_i) + biases_g4_tc
                predicted = np.argmax(scores)

                if predicted != true_label:
                    weights_g4_tc[true_label] += lr_g4_tc * x_i
                    biases_g4_tc[true_label] += lr_g4_tc
                    weights_g4_tc[predicted] -= lr_g4_tc * x_i
                    biases_g4_tc[predicted] -= lr_g4_tc

        return weights_g4_tc, biases_g4_tc


    # -------------------------------------------------------------
    # Time the perceptron for increasing training set sizes
    # -------------------------------------------------------------
    def time_perceptron_training_g4_tc():
        sizes_g4_tc = [10, 50, 100, 200, 300, 400, 500]
        times_g4_tc = []

        for n in sizes_g4_tc:
            # synthetic dataset of n samples, 8 features each
            X_rand_g4_tc = np.random.rand(n, 8)
            y_rand_g4_tc = np.random.randint(0, 4, size=n)

            start_g4_tc = time.time()
            train_perceptron_g4_tc(
                X_rand_g4_tc,
                y_rand_g4_tc,
                num_classes_g4_tc=4,
                epochs_g4_tc=10
            )
            elapsed_g4_tc = time.time() - start_g4_tc

            times_g4_tc.append(elapsed_g4_tc)
            print(f"n={n:4}   time={elapsed_g4_tc:.6f} seconds")

        return sizes_g4_tc, times_g4_tc


    # Run timing
    sizes_g4_tc, times_g4_tc = time_perceptron_training_g4_tc()


    # -------------------------------------------------------------
    # Plot empirical runtime
    # -------------------------------------------------------------
    fig_g4_tc, ax_g4_tc = plt.subplots(figsize=(8, 5))

    ax_g4_tc.plot(
        sizes_g4_tc,
        times_g4_tc,
        marker="o",
        color="#B8860B",   
        linewidth=2
    )

    ax_g4_tc.set_xlabel("Training set size (n)")
    ax_g4_tc.set_ylabel("Time (seconds)")
    ax_g4_tc.set_title("Algorithm 4: Perceptron Training Time Complexity (Empirical)")
    ax_g4_tc.grid(True)

    fig_g4_tc.tight_layout()
    fig_g4_tc
    return


@app.cell
def _(mo):
    mo.md("""
    <!--======================================================
    # Algorithm Four Critical Analysis
    # ====================================================-->
    <div style="
        background-color: #FFFBDB;
        border-left: 6px solid #E6C84F;
        padding: 18px 22px;
        border-radius: 10px;
        margin: 24px 0;
        color: #5a4a00;
    ">

    <h3 style="margin-top: 0;">Critical Analysis – Algorithm 4</h3>

    <p>
    Algorithm 4 uses a multi-class perceptron to classify fashion styles based on the strength of eight trend features. While the perceptron algorithm itself is deterministic, potential bias arises primarily from the training data and labelling process rather than from the learning mechanism. In this project, the labels are based on simple rules, which may reflect subjective choices about what defines each style.
    </p>

    <p>
    This can negatively affect fashion styles that do not conform strongly to predefined categories, such as hybrid aesthetics, as the perceptron is forced to assign each input to a single class. Additionally, because the perceptron is a linear classifier, it cannot capture complex or non-linear relationships between features, which may oversimplify real-world fashion dynamics. As a result, some combinations of trend features may be systematically misclassified.
    </p>

    <p>
    Algorithm 4 effectively demonstrates key supervised learning concepts while highlighting how data quality, model choice, and algorithmic assumptions influence classification outcomes. To mitigate these issues, a larger and more diverse real-world dataset could be used, reducing representational bias and improving generalisation. More flexible classification models, such as non-linear classifiers, could also better capture complex relationships between trends.
    </p>

    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    <p>
    AI tools were used as a <strong>supportive aid</strong> throughout the development of this project, rather than as a replacement for my own understanding or implementation.
    </p>

    <p><strong>Specifically, AI was used to:</strong></p>
    <ul>
      <li>Clarify <strong>algorithmic concepts</strong> (e.g. optimisation logic, genetic algorithm stages)</li>
      <li>Debug errors by explaining <strong>why</strong> code was failing, not just how to fix it</li>
    </ul>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="text-align:center; margin: 20px 0;">
      <img
        src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNG15Nm1jajJyOHI2YnY2M3BzMG90bzVud2V3N2JxZHBicTB6MXAwdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xkQ18QAYX0MfDG55SL/giphy.gif"
        alt="Runway fashion visual"
        style="width:100%; max-width:420px; border-radius:12px;"
      >
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="text-align:center; margin: 20px 0;">
      <img
        src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnNidzdxdXJkNWh6ZTB6Z3RtNzYzYzh4bmgzN3BwcnV5azNhNHZuOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l2Sq3RY0XM6IRTJYI/giphy.gif"
        alt="Fashion runway visual"
        style="width:100%; max-width:420px; border-radius:12px;"
      >
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="text-align:center; margin: 20px 0;">
      <img
        src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3c2pxMTJ1dnlqZm5zcTJoOGFjdTlpNzVvZWQ3MXpoZjZ3c2hsajQ5NSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/3oEdv48EYEKlD1MpQk/giphy.gif"
        alt="Fashion visual"
        style="width:100%; max-width:420px; border-radius:12px;"
      >
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="text-align:center; margin: 20px 0;">
      <img
        src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnc4cm43djJsZ202ZnhxMmRxMjF1MTMzYnZjeHRxbWtqeHhsc3ZrcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26tn8w5rBnrCeECOI/giphy.gif"
        style="width:100%; max-width:420px; border-radius:12px;"
      >
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="text-align:center; margin: 20px 0;">
      <img
        src="https://images.unsplash.com/photo-1765815442424-5acf90d01e41?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        alt="Fashion visual"
        style="width:100%; max-width:420px; border-radius:12px;"
      >
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="text-align:center; margin: 20px 0;">
      <img
        src="https://images.unsplash.com/photo-1612261357585-993398d338b4?q=80&w=1036&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        style="width:100%; max-width:420px; border-radius:12px;"
      >
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="text-align:center; margin: 20px 0;">
      <img
        src="https://images.unsplash.com/photo-1718358345678-889a08b96114?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        style="width:100%; max-width:420px; border-radius:12px;"
      >
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="text-align:center; margin: 20px 0;">
      <img
        src="https://images.unsplash.com/photo-1554881070-74595ca2b74c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        alt="Fashion visual"
        style="width:100%; max-width:420px; border-radius:12px;"
      >
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md(r"""
    <div style="text-align:center; margin: 20px 0;">
      <img
        src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3pqeTA1Y3h6b2VsbWk0NjhramxvcDc0bnUyd2RiZWZmZmtvczdiZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/li0a9ltRF07Sw/giphy.gif"
        style="width:100%; max-width:420px; border-radius:12px;"
      >
    </div>
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    <div style="text-align:center; margin: 20px 0;">
      <img
        src="https://images.unsplash.com/photo-1650057961082-d77233053b1b?q=80&w=988&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        style="width:100%; max-width:420px; border-radius:12px;"
      >
    </div>
    """)
    return


if __name__ == "__main__":
    app.run()
