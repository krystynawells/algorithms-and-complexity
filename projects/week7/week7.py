import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Graphs
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout("Disclaimer: no AI tools were used to create this notebook.")
    return


@app.cell
def _():
    import marimo as mo
    import networkx as nx, matplotlib.pyplot as plt, numpy as np
    return mo, np, nx, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 1
    Modify ```edge_list.txt```,```adjacency_list.txt``` to obtain the given graph
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 1. Adjacency list:
    """)
    return


@app.cell
def _(nx):
    fh = open('adjacency_list.txt', 'rb')
    G = nx.read_adjlist(fh)
    return (G,)


@app.cell
def _(G):
    G.edges()
    return


@app.cell
def _(G, nx, plt):
    nx.draw(G,with_labels = True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 2. Edge list:
    """)
    return


@app.cell
def _(nx):
    _fh = open('edge_list.txt', 'rb')
    H = nx.read_edgelist(_fh)
    _fh.close()
    return (H,)


@app.cell
def _(H, nx, plt):
    nx.draw(H,with_labels = True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 3. Adjacency Matrix
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now create a 2D numpy.array that defines the adjacency matrix
    """)
    return


@app.cell
def _(np):
    A = np.array([
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0]
    ])
    return (A,)


@app.cell
def _(A, nx, plt):
    G_1 = nx.from_numpy_array(A)
    nx.draw(G_1, with_labels=True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2
    Implement the Depth-first search algorithm. You only need to complete the recursive part ```DSF_rec()```
    """)
    return


@app.cell
def _():
    def DFS(source_node, adj_list):
        # Track whether each node has been visited
        visited = [False] * len(adj_list)

        # Start recursive DFS from the source node
        DFS_rec(source_node, visited, adj_list)


    def DFS_rec(n, visited, adj_list):
        # Base case: if node already visited, stop recursion
        if visited[n]:
            return

        # Visit the current node
        print(n)
        visited[n] = True

        # Recursively visit each neighbour
        for neighbour in adj_list[n]:
            DFS_rec(neighbour, visited, adj_list)

    return (DFS,)


@app.cell
def _(DFS):
    adj = [[1,2,5],[0,4,3],[0,4],[1,4],[1,2,3,5],[4,0]]

    DFS(3,adj)
    return (adj,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3
    Implement the Breadth-first search algorithm.
    """)
    return


@app.cell
def _():
    from collections import deque

    def BFS(source_node, adjacency_list):
        # Keep track of which nodes have already been visited
        visited = [False] * len(adjacency_list)

        queue = deque([source_node])

        # Mark the starting node as visited
        visited[source_node] = True

        # Continue until there are no nodes left in the queue
        while queue:
            n = queue.popleft()
            print(n)

            # Add all unvisited neighbours to the queue
            for neighbour in adjacency_list[n]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)

    return BFS, deque


@app.cell
def _(BFS, adj):
    BFS(4,adj)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4
    """)
    return


@app.cell
def _():
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
    return (graph,)


@app.cell
def _():
    def dijkstra(g, source):
        # Number of vertices in the graph
        n = len(g)

        dist = [10000] * n
        dist[source] = 0

        # Track which vertices have been finalised
        visited = [False] * n

        # Repeat once for each vertex
        for _ in range(n):
            u = minDistance(dist, visited, g)
            visited[u] = True

            for v in range(n):
                if g[u][v] != 0 and not visited[v]:
                    if dist[u] + g[u][v] < dist[v]:
                        dist[v] = dist[u] + g[u][v]
    # Output final shortest distances from the source
        print(dist)


    # Helper Function
    def minDistance(dist, visited, g):
        minDist = 10000
        min_index = -1

        for v in range(len(g)):
            if dist[v] < minDist and not visited[v]:
                minDist = dist[v]
                min_index = v

        return min_index
    return (dijkstra,)


@app.cell
def _(dijkstra, graph):
    dijkstra(graph,0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Final Task:
    Re-use the code from previous weeks (in particular, where we visualised trees like Binary Search or Merge Sort) to visualise the traversal of a graph. Your code should allow the user to show in a dropdown menu between BFS and DFS. then, the code would iterate every time the user presses a ```Next``` button. The visualisation should show nodes that have been visited in a different colour than the not visited.

    ### Extra task (not compulsory):
    - Add a third colour to the node that is currently being visited.
    - Use the ```mo.refresh()``` function to create an automated animation, instead of the user pressing each time for the next iteration.
    """)
    return


@app.cell
def _():
    from marimo import ui
    return (ui,)


@app.cell
def _(A, deque, nx, plt):
    ft_adj_matrix = A # Use the adjacency matrix A 

    ft_n = ft_adj_matrix.shape[0]
    # Convert adjacency matrix to adjacency list representation
    # Each node maps to a list of neighbours where an edge exists
    ft_adj = {i: [j for j in range(ft_n) if ft_adj_matrix[i, j] != 0] for i in range(ft_n)}
    ft_nodes = sorted(ft_adj.keys())

    def ft_bfs_order(start: int):
         # Track visited nodes
        seen = {start}
        q = deque([start])
        # Stores the order in which nodes are visited
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in ft_adj[u]: # Explore all unvisited neighbours
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        return order

    def ft_dfs_order(start: int):
        # Track visited nodes
        seen = set()
        # Stores the DFS traversal order
        order = []
        def rec(u):
            # Stop if node already visited
            if u in seen:
                return
            seen.add(u)
            order.append(u)
            # Recursively visit neighbours
            for v in ft_adj[u]:
                rec(v)
        rec(start)
        return order

    def ft_draw_step(order, step, algo_name):
        # Create a NetworkX graph from the adjacency matrix
        G = nx.from_numpy_array(ft_adj_matrix)
        pos = nx.spring_layout(G, seed=7)

        step = max(0, min(step, len(order) - 1))
        current = order[step]
        visited = set(order[: step + 1])

        plt.figure(figsize=(6.5, 5.5))
        # Draw edges
        nx.draw_networkx_edges(G, pos, alpha=0.6)

        # Currently visited node
        nx.draw_networkx_nodes(
            G, pos,
            nodelist=[n for n in G.nodes if n not in visited],
            node_color="lightgrey",
            node_size=650
        )

        # visited
        nx.draw_networkx_nodes(
            G, pos,
            nodelist=[n for n in visited if n != current],
            node_color="lightskyblue",
            node_size=650
        )

        # current
        nx.draw_networkx_nodes(
            G, pos,
            nodelist=[current],
            node_color="pink",
            node_size=750
        )

        nx.draw_networkx_labels(G, pos, font_size=10)
        plt.axis("off")
        plt.title(f"{algo_name} traversal (step {step + 1}/{len(order)})")
        plt.show()

        return current, visited
    return ft_bfs_order, ft_dfs_order, ft_draw_step, ft_nodes


@app.cell
def _(ft_nodes, mo, ui):
    # Dropdown to select traversal algorithm (BFS or DFS)
    ft_algo = ui.dropdown(options=["BFS", "DFS"], value="BFS", label="Traversal")
    ft_start = ui.dropdown(options=ft_nodes, value=ft_nodes[0], label="Start")
    ft_next = ui.button(label="Next ▶")
    ft_reset = ui.button(label="Reset ↺")

    mo.hstack([ft_algo, ft_start, ft_next, ft_reset])
    return ft_algo, ft_next, ft_reset, ft_start


@app.cell
def _(
    ft_algo,
    ft_bfs_order,
    ft_dfs_order,
    ft_draw_step,
    ft_next,
    ft_reset,
    ft_start,
    mo,
):
    # Read current UI values
    algo_name = ft_algo.value
    start_node = int(ft_start.value)

    # Compute traversal order based on selected algorithm
    order = ft_bfs_order(start_node) if algo_name == "BFS" else ft_dfs_order(start_node)
    if not order:
        order = [start_node]
    # Count button presses
    clicks = int(ft_next.value or 0)
    resets = int(ft_reset.value or 0)

    # rewind on reset
    step = clicks - resets * len(order)
    step = max(0, min(step, len(order) - 1))

    # Draw the current traversal step
    current, visited = ft_draw_step(order, step, algo_name)

    # Display current traversal state as text
    mo.md(
        f"""
    **Traversal:** `{algo_name}`  
    **Start:** `{start_node}`  
    **Current:** `{current}`  
    **Visited:** `{sorted(list(visited))}`  

    *Legend:* **orange** = current, **blue** = visited, **grey** = not visited.
    """
    )

    return


if __name__ == "__main__":
    app.run()
