import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    render = csv.reader(csvfile, delimiter=',')
    header = next(render)
    data = []
    for row in render:
      inter = zip(header, row)
      union = {key: values for key, values in inter}
      data.append(union)
    return data


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])
  read_csv(data)
