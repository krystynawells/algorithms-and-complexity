import marimo

__generated_with = "0.17.6"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import random, numpy as np, matplotlib.pyplot as plt
    return np, plt, random


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Example 1: Maxone
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 1: Initialisation
    Implement the ```createInital(nInd,nBits)``` function that creates ```nInd``` arrays of ```nBits``` bits each one, where each bit is 1 or 0 with 50% chance.
    """)
    return


@app.cell
def _(np):
    def createInitial(nInd,nBits):
        population = np.random.randint(0, 2, size=(nInd, nBits))
        return population
    return (createInitial,)


@app.cell
def _(createInitial):
    createInitial(5,5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 2: Evaluation
    Implement the ```fitness(individual)``` function that receives an array ```individual``` and it returns ```nOnes```, the number of ones that the array contains (you can assume the array only contains zeros or ones).
    """)
    return


@app.function
def fitness(individual):
    nOnes = sum(individual)
    return nOnes


@app.cell
def _():
    print(fitness([1, 6, 1, 1, 8, 4]))   
    print(fitness([7, 8, 2, 5, 2, 1]))  
    print(fitness([4, 1, 8, 1, 5, 7]))  
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 3: Selection
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Implement the ```selectThreeWinners(population)``` function, that takes as an input the whole population. This function should do the following:
    1. Select randomly two individuals from ```population```, then compare their fitness and select the one with highest fitness. This individual is called ```firstWinner```
    2. Repeat the above step twice, in order to obtain ```secondWinner``` and ```thirdWinner```
    3. Return ```firstWinner```,```secondWinner```, and ```thirdWinner```

    You can use the ```random.sample(population,k)``` for randomly extract ```k``` elements from ```population```
    """)
    return


@app.cell
def _(random):
    def selectThreeWinners(population):
        # Convert population into a Python list
        pop_list = list(population) #

        def tournament(pop):
            # Randomly select two individuals from the population
            ind1, ind2 = random.sample(pop, 2)
            # Compare their fitness values and return the fitter individual
            return ind1 if fitness(ind1) >= fitness(ind2) else ind2

        firstWinner  = tournament(pop_list)
        secondWinner = tournament(pop_list)
        thirdWinner  = tournament(pop_list)
        # Return the three selected individuals
        return firstWinner, secondWinner, thirdWinner
    return (selectThreeWinners,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 4: Crossover
    Implement the ```crossover(parent1,parent2)``` function, that takes as an input two individuals ```parent1``` and ```parent2``` and returns ```firstChild``` and ```secondChild``` which are obtained with the following procedure:
    1. Create a random crossover point x, with ```x=[1,len(parent1)-1]```
    2. Create ```firstChild```, an array containing the same elements from ```parent1``` from index 0 to x-1, and containing the same elements from ```parent2``` from index x to len(parent)-1.
    3. Create ```secondChild``` as the inverse combination from ```firstChild```
    """)
    return


@app.cell
def _(np, random):
    def crossover(parent1, parent2):
        # Choose a random crossover point x
        x = random.randint(1, len(parent1) - 1)
        child1 = np.concatenate([parent1[:x], parent2[x:]])
        child2 = np.concatenate([parent2[:x], parent1[x:]])
        # Return the two offspring
        return child1, child2
    return (crossover,)


@app.cell
def _(crossover, np):
    p1 = np.array([1, 0, 1, 1, 0, 1, 0, 1])
    p2 = np.array([0, 1, 0, 0, 1, 0, 1, 0])

    c1, c2 = crossover(p1, p2)
    print("Crossover point and results:")
    print(c1)
    print(c2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 5: Mutation
    Implement the ```mutation(individual,pMut)``` function, that takes as an input an array ```individual``` and ```pMut```, the probability of mutation, and for each element of ```individual``` it changes its value (from 0 to 1 or from 1 to 0) with probability ```pMut```
    """)
    return


@app.cell
def _(np, random):
    def mutation(individual, pMutation):
        # Create an empty list to store the mutated individual
        mutated = []
        for gene in individual:
            mutated.append(1-gene if random.random() < pMutation else gene)
        return np.array(mutated, dtype=int)
    return (mutation,)


@app.cell
def _(mutation):
    individual = [7, 4, 9, 2, 1]
    pMutation = 0.5   

    print("Before:", individual)
    new_individual = mutation(individual.copy(), pMutation)
    print("After: ", new_individual)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Putting all together
    Now we implement our ```runGA()``` function, that will call every other function we created.
    """)
    return


@app.cell
def _(createInitial, crossover, mutation, selectThreeWinners):
    def runGA(totalIndividuals, numberBits, numberIterations, pMutation):
        fitnesses = []
        population = createInitial(totalIndividuals, numberBits)

        for k in range(numberIterations):
            print("Iteration:", k)

            # tournament selection of 3 winners
            winners = selectThreeWinners(population)

            # crossover to create children
            next_gen = []
            for i in [0, 1]:
                for j in range(i + 1, 3):
                    children = crossover(winners[i], winners[j])
                    next_gen.append(children[0])
                    next_gen.append(children[1])

            # combine current population and children, keep the best 6
            combined = list(population) + next_gen
            # Create a list of tuples
            evaluated = [(ind, fitness(ind)) for ind in combined]
            # Sort by fitness
            evaluated.sort(key=lambda x: x[1])
            # Keep the 6 best individuals 
            population = [ind for ind, score in evaluated[-6:]]

            # mutation
            for i in range(len(population)):
                population[i] = mutation(population[i], pMutation)

            # record best fitness in this generation
            fitnesses.append(max(fitness(ind) for ind in population))

        return fitnesses
    return (runGA,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    And we call the function with specific values for the parameters
    """)
    return


@app.cell
def _(plt, runGA):
    # Run the genetic algorithm
    results = runGA(
        totalIndividuals=100,      # population size
        numberBits=50,             # length of each individual
        numberIterations=100,      # number of generations
        pMutation=0.01             # mutation probability
    )

    # Plot the best fitness over time
    plt.plot(results)
    plt.xlabel("Generation")
    plt.ylabel("Best Fitness")
    plt.title("GA Optimization Progress")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Task 6:
    Explore modifying the selection and crossover processes to achieve a better fitness. You can also modify how the ```next_gen``` is being defined in ```runGA()```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---------
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Example 2: Maximising a real-valued function
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We want to find the values $x^{*}$ and $y^{*}$ such that $f(x,y)=-(x+y)^2$ has a maximum.

    We can start with random arrays of two elements $[x_0,y_0]$ where $x_0,y_0\in[-1,1]$ and use genetic algorithm to see if we find the optimal solution.

    Let's visualise $f(x,y)$:
    """)
    return


@app.cell(hide_code=True)
def _(np, plt):
    plt.rcParams['figure.dpi'] = 300

    from matplotlib import cm
    from matplotlib.ticker import LinearLocator
    _fig, _ax = plt.subplots(subplot_kw={'projection': '3d'})
    _X = np.arange(-5, 5, 0.25)
    _Y = np.arange(-5, 5, 0.25)
    # Make data.
    _X, _Y = np.meshgrid(_X, _Y)
    _Z = -(_X ** 2 + _Y ** 2)
    _surf = _ax.plot_surface(_X, _Y, _Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    _ax.set(xlabel='X', ylabel='Y', zlabel='Z')
    # Plot the surface.
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ------------
    Now let's create some initial points and plot them together
    """)
    return


@app.cell(hide_code=True)
def _(mo, np, random):
    ## This code was created with the help of GPT-5 for the rendering of the points + surface

    import plotly.graph_objects as go

    # Generate population
    population = []
    for i in range(100):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        population.append([x, y])

    # Compute z = -x^2 - y^2
    x_vals = [p[0] for p in population]
    y_vals = [p[1] for p in population]
    z_vals = [-x**2 - y**2 for x, y in population]

    # Scatter points
    scatter = go.Scatter3d(
        x=x_vals,
        y=y_vals,
        z=z_vals,
        mode='markers',
        marker=dict(size=5, color=z_vals, colorscale='Viridis', opacity=0.8),
        name='Points'
    )

    # Surface
    X = np.linspace(-1, 1, 50)
    Y = np.linspace(-1, 1, 50)
    X, Y = np.meshgrid(X, Y)
    Z = -X**2 - Y**2

    surface = go.Surface(
        x=X, y=Y, z=Z,
        colorscale='Viridis', opacity=0.5, showscale=False
    )

    fig = go.Figure(data=[surface, scatter])
    fig.update_layout(
        title="Interactive 3D Plot of f(x,y) = -x² - y²",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z = -x² - y²",
        ),
        width=700,
        height=600,
    )

    mo.ui.plotly(fig)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Final Task:
    Implement the following functions to run a genetic algorithm for the probklem stated above.
    your algorithm should do the following:
    - Create an initial population of 100 points scattered randomnly in the range $x=[-1,1]$ and $y=[-1,1]$
    - Calculate the fitness of each point is given by evaluating the point in the function $f(x,y)$.
    - Selection process is similar as Example 1 (i.e. selecting three winners)
    - You can implement whatever crossover you consider adequate.
    - For each step, each individual suffers a mutation on each of its coordinates $x$ and $y$ which are modified by a random noise $\delta$, where $\delta=[-0.05,0.05]$ (uniformly distributed).
    - Implement the ```runGA_1()``` function so it runs 100 iterations of the algorithm. Check if the points converge to a solution.

    ## Extra task (not compulsory):
    - Plot the points for each iteration of the algorithm together with the surface. Visualise how the points move through the surface
    - Visualise how the points move through the surface by plotting the path or trail that they leave when they move from one iteration to the next one.
    """)
    return


@app.function
def f(x, y):
    return -(x**2 + y**2)


@app.cell
def _(np):
    def createInitialPoints(nInd):
        return np.random.uniform(-1, 1, size=(nInd, 2))
    return (createInitialPoints,)


@app.function
def fitness_point(point):
    x, y = point
    return f(x, y)


@app.cell
def _(random):
    def selectThreeWinners_final(population):
        # Convert the population into a Python list
        pop_list = list(population)

        def tournament():
            # Randomly select two individuals from the population
            a, b = random.sample(pop_list, 2)
            # Compare their fitness values and return the fitter individual
            return a if fitness_point(a) >= fitness_point(b) else b

        # Run the tournament selection three times to select three winners
        return [tournament(), tournament(), tournament()]
    return


@app.cell
def _(random):
    def crossover_points(p1, p2):
        alpha = random.random()  #
        c1 = alpha * p1 + (1 - alpha) * p2
        c2 = alpha * p2 + (1 - alpha) * p1
        return c1, c2
    return (crossover_points,)


@app.cell
def _(np):
    def mutation_point(point, delta=0.05):
        noise = np.random.uniform(-delta, delta, size=2)
        mutated = point + noise
        return np.clip(mutated, -1, 1)
    return (mutation_point,)


@app.cell
def _(
    createInitialPoints,
    crossover_points,
    mutation_point,
    np,
    selectThreeWinners,
):
    def runGA_1(totalIndividuals=100, numberIterations=100, delta=0.05):
        # Create the initial population of points in the search space
        population = createInitialPoints(totalIndividuals)

        # Lists to track the best fitness value and point per iteration
        history = [population.copy()]
        best_fitnesses = []
        best_points = []

        for k in range(numberIterations):
            # Select three parents using tournament selection
            winners = selectThreeWinners(population)

            # Generate offspring from all unique pairs of winners
            next_gen = []
            for i in [0, 1]:
                for j in range(i + 1, 3):
                    c1, c2 = crossover_points(winners[i], winners[j])
                    next_gen.append(mutation_point(c1, delta))
                    next_gen.append(mutation_point(c2, delta))

            # Combine the current population with the newly generated offspring
            combined = np.vstack([population, np.array(next_gen)])
            scored = [(pt, fitness_point(pt)) for pt in combined]
            # Sort individuals by fitness
            scored.sort(key=lambda t: t[1])
            best = scored[-totalIndividuals:]
            population = np.array([pt for pt, _ in best])

            best_pt, best_fit = max(((pt, fitness_point(pt)) for pt in population), key=lambda t: t[1])
            best_fitnesses.append(best_fit)
            best_points.append(best_pt)

            history.append(population.copy())

        # Return fitness history, best points, final population, and full history
        return best_fitnesses, best_points, population, history
    return (runGA_1,)


@app.function
def animate_ga(history):
    import numpy as np
    import plotly.graph_objects as go

    # Surface grid
    grid = np.linspace(-1, 1, 60)
    Xs, Ys = np.meshgrid(grid, grid)
    Zs = -(Xs**2 + Ys**2)

    # Initial population 
    pop0 = np.asarray(history[0])
    Z0 = -(pop0[:, 0]**2 + pop0[:, 1]**2)

    # Build frames
    frames = []
    for t, pop in enumerate(history):
        pop = np.asarray(pop)
        Zp = -(pop[:, 0]**2 + pop[:, 1]**2)

        frames.append(
            go.Frame(
                data=[
                    go.Scatter3d(
                        x=pop[:, 0],
                        y=pop[:, 1],
                        z=Zp,
                        mode="markers",
                        marker=dict(size=4),
                        name="Population",
                    )
                ],
                traces=[1],        
                name=str(t),
            )
        )

    # Layout + animation controls
    fig_local = go.Figure(
        data=[
            go.Surface(x=Xs, y=Ys, z=Zs, opacity=0.7, showscale=False, name="Surface"),
            go.Scatter3d(
                x=pop0[:, 0],
                y=pop0[:, 1],
                z=Z0,
                mode="markers",
                marker=dict(size=4),
                name="Population",
            ),
        ],
        frames=frames,
    )

    fig_local.update_layout(
        title="GA evolution on f(x,y) = -x^2 - y^2",
        scene=dict(
            xaxis_title="x",
            yaxis_title="y",
            zaxis_title="f(x,y)",
        ),
        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[
                            None,
                            {
                                "frame": {"duration": 80, "redraw": True},
                                "transition": {"duration": 0},
                                "fromcurrent": True,
                                "mode": "immediate",
                            },
                        ],
                    ),
                    dict(
                        label="Pause",
                        method="animate",
                        args=[
                            [None],
                            {
                                "frame": {"duration": 0, "redraw": False},
                                "transition": {"duration": 0},
                                "mode": "immediate",
                            },
                        ],
                    ),
                ],
            )
        ],
        margin=dict(l=0, r=0, b=0, t=40),
    )
# Display the interactive animation
    fig_local.show()


@app.cell
def _(runGA_1):
    best_fitnesses, best_points, final_pop, history = runGA_1(100, 100, 0.05)
    animate_ga(history)
    return


if __name__ == "__main__":
    app.run()
