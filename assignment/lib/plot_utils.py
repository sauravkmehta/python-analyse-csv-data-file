"""
Utlity module for drawing different type of charts/graph.

@Author: Saurav
"""

from matplotlib import pyplot as plt


def drawHistogram(ax, title, xlabel, ylabel, xdata, ydata):
    """
    To draw a histogram in the provided axes.

    Parameters
    ----------
    ax : `.axes.Axes` object or array of Axes objects.
        A single `~matplotlib.axes.Axes` object.
    title : str
         Title for the axes.
    xlabel : str
        Label for x axis.
    ylabel : string
        Label for y axis.
    xdata : list
        list of data for x axis.
    ydata : list
        list of data for y axix.

    Returns
    -------
    None.

    """
    # Set the title
    ax.set_title(title)
    # set the axis labels
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    # set the ticks on the x-axis
    ax.set_xticks(range(0, 101, 10))
    # draw a histogram
    ax.hist(xdata, ydata, ec="red")


def drawBoxplot(ax, title, ylabel, data):
    """
    To draw a boxplot in the provided Axes.

    Parameters
    ----------
    ax : `.axes.Axes` object or array of Axes objects.
        A single `~matplotlib.axes.Axes` object.
    title : str
         Title for the axes.
    ylabel : str
        Label for y axis.
    data : list
        A list of data.

    Returns
    -------
    None.

    """
    # Set the title
    ax.set_title(title)
    # set the axis labels
    ax.set_ylabel(ylabel)
    ax.boxplot(data, showfliers=False)


def drawPieChart(ax, title, data):
    """
    To draw a piechart for given dict in the provided Axes.

    Parameters
    ----------
    ax : `.axes.Axes` object or array of Axes objects.
        A single `~matplotlib.axes.Axes` object.
    title : str
         Title for the axes..
    data : dict
        A dict containing key and value which will be represented in PieChart.

    Returns
    -------
    None.

    """
    # set the title
    ax.set_title(title)
    # draw a pie chart
    ax.pie(data.values(), labels=data.keys(), autopct="%.0f%%")


def drawScatterGraph(ax, title, xlabel, ylabel, xdata, ydata):
    """
    To draw a scatter graph of two list in the provided Axes.

    Parameters
    ----------
    ax : `.axes.Axes` object or array of Axes objects.
        A single `~matplotlib.axes.Axes` object.
    title : str
         Title for the axes.
    xlabel : str
        Label for x axis.
    ylabel : str
        Label for y axis.
    xdata : list
        list of data for x axix.
    ydata : list
        list of data for y axix..

    Returns
    -------
    None.

    """
    # Set the title
    ax.set_title(title)
    # set the axis labels
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.scatter(xdata, ydata, marker='.')


def drawHorizontalBar(ax, title, xlabel, ylabel, data):
    """
    To draw horizontal bar in the provided Axes.

    Parameters
    ----------
    ax : `.axes.Axes` object or array of Axes objects.
        A single `~matplotlib.axes.Axes` object.
    title : str
         Title for the axes.
    xlabel : str
        Label for x axis.
    ylabel : str
        Label for y axis.
    data : dict
        A dict containing key and value which will be represented
        in horizontal bar.

    Returns
    -------
    None.

    """
    ax.set_title(title)
    # set the y positions
    y_pos = [i for i in range(len(data))]
    # set the y tick labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels(data.keys())
    # set the labels on the axes
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    # do a horizontal bar chart
    ax.barh(y_pos, data.values(), align="center")


def getFigureAndAxes(number_row, number_column):
    """
    To create a figure and a set of subplots.

    Parameters
    ----------
    number_row : int
         Number of rows of the subplot grid.
    number_column : int
         Number of columns of the subplot grid.

    Returns
    -------
    fig : `~.figure.Figure`
        DESCRIPTION.
    ax : `.axes.Axes` object or array of Axes objects.
        *ax* can be either a single `~matplotlib.axes.Axes` object or an
        array of Axes objects if more than one subplot was created..

    """
    # Create the figure and axes
    fig, ax = plt.subplots(number_row, number_column, figsize=(25, 25))
    return fig, ax


if __name__ == '__main__':
    # Create the figure and axes
    print("Hello")
    fig, ax = plt.subplots()
    grades = [0, 40, 50, 60, 70, 100]
    drawHistogram(ax, "histogram", "x", "y",
                  [10, 20, 40, 70, 80, 90, 95], grades)
    # show the plot
    plt.show()
    # Save the figure (bbox = "tight" eliminates whitespace padding)
    fig.savefig("marks_histogram.png", bbox_inches="tight")
