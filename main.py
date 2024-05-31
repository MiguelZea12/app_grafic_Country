import utils
import read_csv
import charts
'''
country, population = utils.get_country()
print(country, population)
'''

def app():
  data = read_csv.read_csv('./app/data.csv')

  #Los nombres de los paises estan en ingles
  country = input('Intruduzca el pais que desea consultar ==> ')

  result = utils.country_input(data, country.title())

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_country(country)
    charts.generate_table(labels, values)


if __name__ == '__main__':
  app()
