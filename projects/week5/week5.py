import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import plotly.graph_objects as go
    return go, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 1:
    Implement the Binary Search Algorithm for a sorted input array.
    """)
    return


@app.cell
def _(mo):
    def binary_search(arr, target):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                return mid  
            elif arr[mid] < target:
                left = mid + 1  
            else:
                right = mid - 1  

        return -1 

    numbers = [1, 3, 5, 7, 9, 11]
    mo.md(f"Result: {binary_search(numbers, 7)}")
    return (numbers,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2:
    Implement the Recursive Binary Search Algorithm for a sorted input array.
    """)
    return


@app.cell
def _(mo, numbers):
    def recursive_binary_search(arr, target, left, right):
        if left > right:
            return -1  # base case: not found

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            return recursive_binary_search(arr, target, mid + 1, right)
        else:
            return recursive_binary_search(arr, target, left, mid - 1)


    numbers2 = [1, 3, 5, 7, 9, 11]
    result = recursive_binary_search(numbers, 7, 0, len(numbers) - 1)
    mo.md(f"**Result (recursive):** {result}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3:
    Implement Merge Sort algorithm
    """)
    return


@app.cell
def _(mo, numbers):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])

        return merge(left_half, right_half)

    def merge(left, right):
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])

        return sorted_list



    numbers3 = [8, 3, 5, 4, 7, 6, 1, 2]
    sorted_numbers = merge_sort(numbers)
    mo.md(f"**Original:** {numbers}<br>**Sorted (Merge Sort):** {sorted_numbers}")
    return (sorted_numbers,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4:
    Implement Quicksort (last element as a pivot)
    """)
    return


@app.cell
def _(mo, numbers, sorted_numbers):
    def quicksort(arr):
        if len(arr) <= 1:
            return arr


        pivot = arr[-1]

        left = [x for x in arr[:-1] if x <= pivot]   
        right = [x for x in arr[:-1] if x > pivot]   


        return quicksort(left) + [pivot] + quicksort(right)



    numbers4 = [10, 7, 8, 9, 1, 5]
    sorted_numbers2 = quicksort(numbers)
    mo.md(f"**Original:** {numbers}<br>**Sorted (Quicksort):** {sorted_numbers}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Final Task
    Below you will find a series of cells that help you to plot a tree structure. A tree structure here is something like the following:
    """)
    return


@app.cell
def _():
    exampleTree = [(0, None, [8, 3, 5, 4, 7, 6, 1, 2]), (1, 0, [8, 3, 5, 4]),(2,0,[7,6,1,2]) ,(3,1,[8,3]),(4,1,[5,4]),(5, 2, [7,6])]
    return (exampleTree,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we can use the helper functions to plot this tree structure for different iterations
    """)
    return


@app.cell
def _(build_graph, draw_tree, exampleTree):
    def _():
        F = build_graph(exampleTree,7)
        return draw_tree(F)


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
            r"""
        ---------------------
        The following code was generated initially with GPT-5 plus iterations. The code generated all the helper functions defined in the first cell. The author modified it to be displayed and plotted as a tree structure using networkx library.  

        ----------
        """
        ).callout()
    return


@app.cell(hide_code=True)
def _(mo):
    import networkx as nx
    import matplotlib.pyplot as plt


    def build_graph(tree, step):
        G = nx.DiGraph()
        for node, parent, arr in tree[:step]:
            G.add_node(node, label=str(list(arr)))
            if parent is not None:
                G.add_edge(parent, node)
        return G



    def hierarchy_pos(G, root=None, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):

        if not nx.is_tree(G):
            raise TypeError("hierarchy_pos only works for trees.")

        if root is None:
            root = next(n for n,d in G.in_degree() if d==0)  # find node with in-degree 0

        def _hierarchy_pos(G, node, left, right, vert_loc, pos):
            children = list(G.successors(node))
            pos[node] = ((left + right) / 2, vert_loc)
            if len(children) != 0:
                dx = (right - left) / len(children)
                nextx = left
                for child in children:
                    _hierarchy_pos(G, child, nextx, nextx + dx, vert_loc - vert_gap, pos)
                    nextx += dx
            return pos

        return _hierarchy_pos(G, root, 0, width, vert_loc, {})


    def draw_tree(G):
        pos = hierarchy_pos(G) 
        labels = nx.get_node_attributes(G, "label")
        plt.figure(figsize=(5, 3))
        nx.draw(
            G,
            pos,
            with_labels=True,
            labels=labels,
            font_size=5,
            node_size=500,
            node_color="lightblue",
        )
        plt.axis("off")
        drawM = mo.mpl.interactive(plt.gcf())
        return drawM
    return build_graph, draw_tree, nx


@app.cell(hide_code=True)
def _(mo):
    arr_input = mo.ui.text(label="Enter array (comma-separated)", value="8,3,5,4,7,6,1,2")
    return (arr_input,)


@app.cell(hide_code=True)
def _(mo):
    next_btn = mo.ui.button(label="Next Step ▶️")
    return (next_btn,)


@app.cell(hide_code=True)
def _(mo):
    reset_btn = mo.ui.button(label="🔄 Reset")
    return (reset_btn,)


@app.cell(hide_code=True)
def _(mo):
    get_count, set_count = mo.state(1)
    return get_count, set_count


@app.cell(hide_code=True)
def _(get_count, next_btn, set_count):
    next_btn
    set_count(get_count()+1)
    print(get_count())
    return


@app.cell(hide_code=True)
def _(reset_btn, set_count):
    reset_btn
    set_count(0)
    return


@app.cell(hide_code=True)
def _(arr_input):
    arr_text = arr_input.value
    arr = [int(x.strip()) for x in arr_text.split(",") if x.strip().isdigit()]
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Tasks:
    - Modify the previous cell so it allows the user to input the value to search for (now it is fixed to 5)
    - Create a new function ```tree_merge_sort()```. This function is similar to ```tree_bin_search()``` but it created the tree for a Merge Sort algorithm (i.e. instead of only opening one branch like binary search, now it always open two branches). Use the same helper functions to plor the merge sort tree for each iteration.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Extra Tasks (not compulsory, just if you want to learn more):
    - Add a dropdown menu that allows you to choose between Binary Search and Mergesort and then it shows the corresponding tree.
    - Add as a third option the Quicksort algorithm with its corresponding tree
    - Modify the helper functions so for the Binary search algorithm it displays the whole tree (not only the chosen left or right child node), and it also show the chosen path (i.e. chosen nodes) with a different colour. You might have to add an extra attribute to the nodes of the tree that accounts whether they belong to the path or not. Then, in the ```draw_tree()``` helper function (particularly, in the ```nx.draw()``` part) you can give a ```color``` option to nodes.
    """)
    return


@app.cell
def _(go, nx):
    # Computes positions for nodes so a tree can be drawn hierarchically
    def hierarchy_pos2(G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
        if not nx.is_tree(G):
            raise TypeError("hierarchy_pos only works for trees.")
    # Recursive helper function to position children
        def _hierarchy_pos2(G, root, left, right, vert_loc, pos):
            pos[root] = ((left + right) / 2.0, vert_loc)
            children = list(G.successors(root))
            if not children:
                return
            gap = (right - left) / len(children)
            for i, child in enumerate(children):
                child_left = left + i * gap
                child_right = left + (i + 1) * gap
                _hierarchy_pos2(G, child, child_left, child_right,
                               vert_loc - vert_gap, pos)
        pos = {}
        _hierarchy_pos2(G, root, 0.0, width, vert_loc, pos)
        return pos

    # Builds a graph from a tree structure
    def build_graph2(tree):
        G = nx.DiGraph()
        for node_id, parent, values, colour in tree:
            G.add_node(node_id, label=str(values), colour=colour)
            if parent is not None:
                G.add_edge(parent, node_id)
        return G

    # Draws the tree using Plotly
    def draw_tree2(G, root=0):
        pos = hierarchy_pos2(G, root)

        edge_x, edge_y = [], []
        for u, v in G.edges():
            x0, y0 = pos[u]
            x1, y1 = pos[v]
            edge_x += [x0, x1, None]
            edge_y += [y0, y1, None]

        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y, mode="lines",
            line=dict(width=1, color="black"),
            hoverinfo="none"
        ))

        node_x = [pos[n][0] for n in G.nodes()]
        node_y = [pos[n][1] for n in G.nodes()]
        labels = [G.nodes[n]["label"] for n in G.nodes()]
        colours = [G.nodes[n]["colour"] for n in G.nodes()]

        fig.add_trace(go.Scatter(
            x=node_x, y=node_y,
            mode="markers+text",
            marker=dict(size=24, color=colours, line=dict(width=2, color="black")),
            text=labels,
            textposition="top center"
        ))

        fig.update_layout(showlegend=False, margin=dict(l=20, r=20, t=40, b=20))
        return fig
    return build_graph2, draw_tree2


@app.function
# --- Binary Search tree ---
def tree_bin_search(arr, val):
    tree = []
    if not arr:
        return tree

    try:
        target_idx = arr.index(val)
    except ValueError:
        target_idx = None

    def helper(lo, hi, parent, next_id):
        if lo > hi:
            return next_id
        mid = (lo + hi) // 2
        segment = arr[lo:hi + 1]

        on_path = target_idx is not None and lo <= target_idx <= hi
        if target_idx == mid:
            colour = "tomato"   
        elif on_path:
            colour = "orange"     
        else:
            colour = "lightblue"  

        my_id = next_id
        next_id += 1
        tree.append((my_id, parent, segment, colour))

        next_id = helper(lo, mid - 1, my_id, next_id)
        next_id = helper(mid + 1, hi, my_id, next_id)
        return next_id

    helper(0, len(arr) - 1, None, 0)
    return tree


@app.cell
def _():
    # --- Merge Sort tree ---
    def tree_merge_sort(arr):
        tree = []

        def helper(subarr, parent, next_id):
            my_id = next_id
            next_id += 1

            colour = "lightgreen" if len(subarr) <= 1 else "lightblue"
            tree.append((my_id, parent, subarr, colour))

            if len(subarr) <= 1:
                return next_id

            mid = len(subarr) // 2
            left = subarr[:mid]
            right = subarr[mid:]
            next_id = helper(left, my_id, next_id)
            next_id = helper(right, my_id, next_id)
            return next_id

        helper(arr, None, 0)
        return tree


    # --- Quicksort tree  ---
    def tree_quicksort(arr):
        tree = []

        def helper(subarr, parent, next_id):
            my_id = next_id
            next_id += 1

            if not subarr:
                tree.append((my_id, parent, [], "lightblue"))
                return next_id

            pivot = subarr[-1]
            less = [x for x in subarr[:-1] if x <= pivot]
            greater = [x for x in subarr[:-1] if x > pivot]

            label = f"{subarr} | p={pivot}"
            colour = "plum"          # pivot node in different colour
            tree.append((my_id, parent, label, colour))

            if less:
                next_id = helper(less, my_id, next_id)
            if greater:
                next_id = helper(greater, my_id, next_id)
            return next_id

        helper(arr, None, 0)
        return tree
    return tree_merge_sort, tree_quicksort


@app.cell
def _(mo):
    # Dropdown to select which algorithm to visualise
    alg_choice = mo.ui.dropdown(
        options=["Binary Search", "Merge Sort", "Quicksort"],
        value="Binary Search",
        label="Choose algorithm"
    )

    array_input = mo.ui.text(
        label="Enter array (comma-separated)",
        value="8,3,5,4,7,6,1,2"
    )

    target_input = mo.ui.number(
        label="Value to search for (Binary Search only)",
        value=5
    )

    mo.hstack([alg_choice, array_input, target_input])
    return alg_choice, array_input, target_input


@app.cell
def _(
    alg_choice,
    array_input,
    build_graph2,
    draw_tree2,
    mo,
    target_input,
    tree_merge_sort,
    tree_quicksort,
):
    def _():
        try:
            arr_values = [int(x.strip())
                          for x in array_input.value.split(",")
                          if x.strip()]
        except ValueError:
            return mo.md("**Please enter only integers separated by commas.**")
        
     # Get selected algorithm
        algo = alg_choice.value
    
        # Binary Search requires a sorted array and a target value
        if algo == "Binary Search":
            arr_sorted = sorted(arr_values)
            target = int(target_input.value)
        
            # Build binary search tree highlighting the search path
            tree = tree_bin_search(arr_sorted, target)
            title = f"Binary Search Tree (target={target}) on {arr_sorted}"

       
        # Merge Sort tree visualisation 
    
        elif algo == "Merge Sort":
            tree = tree_merge_sort(arr_values)
            title = f"Merge Sort Tree for {arr_values}"

        # Quicksort tree visualisation
        else:
            tree = tree_quicksort(arr_values)
            title = f"Quicksort Tree for {arr_values}"

    # Convert tree structure into a graph
        G = build_graph2(tree)
        fig = draw_tree2(G, root=0)

        return mo.vstack([
            mo.md(f"### {title}"),
            fig
        ])

    _()
    return


if __name__ == "__main__":
    app.run()
