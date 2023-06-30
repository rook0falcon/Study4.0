import sys
from pathlib import Path
source_path = Path(__file__).parent.resolve()
sys.path.append(source_path)

import numpy as np
from support_py.s001 import pie_chart

if __name__ == '__main__':
    print("s001_introduction.py")
    # Data being at the heart of statistics, we use stats to analyse, interpret, explain and present it.
    # We have categorical and quantitative variables, which are used to specify a characteristic of an 
    # object from a large population.
    # Population size is a quantitative variable, while ResourceGroup is categorical
    # Representation of a categorical variable can be done via a pie-chart
    # 

    var_pie_chart = {"expense":{"Basic":10, "Housing":10, "Children":20, "Study":5, "Grocery":10, "Medical":10, "Utility":5, "Luxury":5}}
    var_pie_chart["expense"]["Others"] = 100 - sum(var_pie_chart["expense"].values())
    results_path = str(source_path/"support_docs")
    pie_chart(var_pie_chart, results_path)