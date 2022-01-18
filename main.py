from pathlib import Path
import pprint
import csv
import io


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

  assert len(numbers) == len(keys)

  # pega nome do elemento analisado
  element = (line[0:4]).strip()
  # adiciona registro do elemento
  if element not in doc['results'][test_type]:
    doc['results'][test_type][element] = {}
    # inclui os resultados
    for index, param in enumerate(keys):
      doc['results'][test_type][element][param] = numbers[index]


def parse_file(file_lines_list):
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


  # caso não tenha algum elemento, define dados em branco
  for element in ELEMENT_CODES:
    if element not in doc['results']['CPS']:
      doc['results']['CPS'][element] = {k: '' for k in CPS_KEYS}
    if element not in doc['results']['Conc.']:
      doc['results']['Conc.'][element] = {k: '' for k in CONS_KEYS}
  
  return doc

def docs_to_csv(file, doc_list):

  if type(file) == str:
    csvfile = open(file, 'w', newline='')
  else:
    # handle StringIO to unit testing
    csvfile = file

  writer = csv.writer(csvfile, delimiter=';', dialect='excel')

  written_header = False
  for doc in doc_list:

    doc_header_fields = ['File Name', 'Operator Name', 'Acq Time']
    header = doc_header_fields
    row = [doc['header'][header_field] for header_field in doc_header_fields]
    
    for test_type in ['CPS', 'Conc.']:
      for element in sorted(doc['results'][test_type].keys()):
        for k in sorted(doc['results'][test_type][element].keys()):
          row += [doc['results'][test_type][element][k]]
          header += [f'{test_type}.{element}.{k}'.replace('..', '.')]
    
    # escreve cabeçalho do csv
    if not written_header:
      writer.writerow(header)
      written_header = True
    
    writer.writerow(row)

if __name__ == '__main__':
  doc_list = []
  for file_lines_list in files_to_lines():
    doc_list.append(parse_file(file_lines_list))
  
  docs_to_csv('out.csv', doc_list)
