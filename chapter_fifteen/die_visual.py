from die import Die
import plotly.express as px

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

freq = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    f = results.count(value)
    freq.append(f)

fig = px.bar(x=poss_results, y=freq)
fig.show()