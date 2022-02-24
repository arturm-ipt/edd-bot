from pathlib import Path
import pprint
import csv
import io
import datetime


pp = pprint.PrettyPrinter(indent=2, width=1)


CONS_KEYS = ['Mass', 'Conc.', 'SD', 'RSD(%)', 'Rep']
CPS_KEYS = ['Mass', 'CPS', 'SD', 'RSD(%)', 'Time(sec)']
ELEMENT_CODES = ['B', 'V', 'Mn', 'Co', 'Ni', 'Cu', 'As', 'Se', 'Mo', 'Rh', 'Cd', 'Ba', 'Ir', 'Pb', 'Bi', 'Si', 'Ti', 'Cr', 'Fe', 'Li', 'Be', 'Al', 'Zn', 'Ag', 'Sn', 'Sb', 'Hg', 'Tl', 'U']

def files_to_lines():
  for file_path_str in Path('./in').glob('**/*.txt'):
    with open(file_path_str, 'r') as f:
      yield f.readlines()

def extract_numbers(line):
  numbers = []
  numbers_str_list = [x.replace('<', '').replace(',', '') for x in line.split(' ') if x != '']

  for n in numbers_str_list:
    try:
      if n == '---':
        numbers.append(n)
      else:
        numbers.append(float(n))
    except Exception as e:
      pass

  # deve conter 5 números
  assert len(numbers) == 5
  
  return numbers


def add_result(doc, line, test_type, keys):
  """esta função altera o dicionario doc, 
  incluindo o resultado da linha
  """
  assert type(doc) == dict
  assert type(test_type) == str
  assert type(keys) == list
  assert type(line) == str
  
  # pega os numeros da linha 
  numbers = extract_numbers(line)

  #assert len(numbers) == len(keys)

  # pega nome do elemento analisado
  element = (line[0:4]).strip()
  # adiciona registro do elemento
  if element not in doc['results'][test_type]:
    doc['results'][test_type][element] = {}
    # inclui os resultados
    for index, param in enumerate(keys):
      doc['results'][test_type][element][param] = numbers[index]


def parse_file(file_lines_list, cons_keys = CONS_KEYS, cps_keys = CPS_KEYS, cons_elements = ELEMENT_CODES, cps_elements = ELEMENT_CODES):
  non_blank_lines = [line.strip() for line in file_lines_list if line.strip() != '']

  doc = dict({
    'header': {},
    'results': {
      'CPS': {},
      'Conc.': {}
    }
  })

  # flags para regioes do relatorio
  in_header = False
  in_cps = False
  in_conc = False

  
  for line in non_blank_lines:
    
    if 'End of Report' in line:
      break

    if 'Quantitation Report - Detailed (Text Only)' in line:
      in_header = True
      in_cps = False
      in_conc = False
      continue
    
    if '   CPS   ' in line:
      in_header = False
      in_cps = True
      in_conc = False
      continue
    
    if '   Conc.   ' in line:
      in_header = False
      in_cps = False
      in_conc = True
      continue

    if in_header:
      key_value_list = [x.strip() for x in line.split(':', 1)]
      doc['header'][key_value_list[0]] = key_value_list[1]
    
    if in_conc:
      add_result(doc, line, 'Conc.', CONS_KEYS)
    
    if in_cps:
      add_result(doc, line, 'CPS', CPS_KEYS)


  #pp.pprint(doc)
  # caso não tenha algum elemento, define dados em branco
  for element in ELEMENT_CODES:
    if element not in doc['results']['CPS']:
      doc['results']['CPS'][element] = {k: '' for k in CPS_KEYS}
    if element not in doc['results']['Conc.']:
      doc['results']['Conc.'][element] = {k: '' for k in CONS_KEYS}

  # filtra apenas elementos desejados
  for element in ELEMENT_CODES:
    
    if element not in cps_elements:
      del doc['results']['CPS'][element]
    else:
      for k in list(doc['results']['CPS'][element].keys()):
        if k not in cps_keys:
          del doc['results']['CPS'][element][k]    
    

    if element not in cons_elements:
      del doc['results']['Conc.'][element]
    else:
      for k in list(doc['results']['Conc.'][element].keys()):
        if k not in cons_keys:
          del doc['results']['Conc.'][element][k]
    


  return doc


def docs_to_matrix(doc_list, tables = ['CPS', 'Conc.']):
  written_header = False

  matrix = [None] # a primeira linha será o cabeçalho
  for doc in doc_list:

    doc_header_fields = ['File Name', 'Operator Name', 'Acq Time']
    header = doc_header_fields
    row = [doc['header'][header_field] for header_field in doc_header_fields]
    
    for test_type in tables:
      for element in sorted(doc['results'][test_type].keys()):
        for k in sorted(doc['results'][test_type][element].keys()):
          row += [doc['results'][test_type][element][k]]
          header += [f'{test_type}.{element}.{k}'.replace('..', '.')]
    
    # escreve cabeçalho do csv
    if not written_header:
      matrix[0] = header
      written_header = True
    
    matrix.append(row)

  return matrix

def docs_to_csv(file, doc_list, tables = ['CPS', 'Conc.'], agrupar = False):
  matrix = docs_to_matrix(doc_list, tables = tables)

  if agrupar:
    matrix = agrupar_matrix_por_arquivo(matrix)

  if type(file) == str:
    csvfile = open(file, 'w', newline='')
  else:
    # handle StringIO to unit testing
    csvfile = file
  writer = csv.writer(csvfile, delimiter=';', dialect='excel')
  for i, row in enumerate(matrix):
    if i == 0:
      writer.writerow(row)
    else:
      row_proc = []
      # temos que pular as primeiras colunas 
      # de informações não numéricas
      for col in row[0:3]:
        row_proc.append(col)
      for col in row[3:]:
        row_proc.append(str(col).replace('.', ','))
      
      writer.writerow(row_proc)

def agrupar_matrix_por_arquivo(matrix):
  file_name_index = matrix[0].index('File Name')
  acq_time_index = matrix[0].index('Acq Time')

  def parse_date(date_str):
    #datetime.datetime.strptime('Dec 13 2021  10:12 pm', '%b %d %Y  %I:%M %p').timestamp()
    return datetime.datetime.strptime(date_str, '%b %d %Y  %I:%M %p').timestamp()

  sorted_matrix = sorted(matrix[1:], key = lambda row: parse_date(row[acq_time_index]))

  file_names = sorted(list(set([x[file_name_index] for x in sorted_matrix])))

  matrix_agrupada = []

  matrix_agrupada.append(matrix[0])

  for file_name in file_names:
    matrix_filter = [x for x in sorted_matrix if x[file_name_index] == file_name]
    # inicializa linha
    linha_agrupada = [''] * len(matrix_filter[0])

    for row in matrix_filter:
      for i, val in enumerate(row):
        if linha_agrupada[i] == '' and val != '' and val != None:
          linha_agrupada[i] = val

    matrix_agrupada.append(linha_agrupada)

  return matrix_agrupada



if __name__ == '__main__':
  doc_list = []
  for file_lines_list in files_to_lines():
    doc_list.append(parse_file(file_lines_list, cons_keys = ['Conc.'], cps_keys = [], cons_elements = ['Ag', 'Al', 'As', 'B', 'Ba', 'Be', 'Cd', 'Co', 'Cr', 'Cu', 'Fe', 'Hg', 'Li', 'Mn', 'Mo', 'Ni', 'Pb', 'Sb', 'Se', 'Si', 'Sn', 'Ti', 'Tl', 'U', 'V', 'Zn'], cps_elements = []))
  
  docs_to_csv('out.csv', doc_list, tables = ['Conc.'], agrupar = True)
  docs_to_csv('out_desagrupado.csv', doc_list, tables = ['Conc.'], agrupar = False)
