import matplotlib.pyplot as plt


def generate_table(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()


def generate_table_pai(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  plt.axis('equal')
  plt.show()


if __name__ == '__main__':
  labels = ['ale', 'antho', 'alej']
  values = [30, 40, 10]
  generate_table(labels, values)
