from matplotlib import pyplot as plt

x_values = [0, 1, 2, 3, 4, 5]
x_values_labels = ['aluminum', 'elegharn', 'symcloudscan', 'virus_total',
                   'sonar_bypass_rule', 'human']
y_values = [629, 84, 2558, 45, 234, 1868]

ax = plt.subplot()
bars = ax.bar(x_values, y_values)
ax.set_xticks(x_values)
ax.set_xticklabels( x_values_labels)
ax.set_ylabel('Scan Source')
ax.set_ylabel('Files count')
plt.subplots_adjust(wspace=10)

# Add texts
rects = ax.patches
total = float(sum(y_values))
for rect, value in zip(rects, y_values):
    height = rect.get_height()
    text = '{}({:.1%})'.format(value, value/total)
    ax.text(rect.get_x() + rect.get_width() / 2, height + 5, text,
            ha='center', va='bottom')

# Set colors
bars[4].set_color('r')
bars[5].set_color('r')

plt.show()
