import sys
sys.path.append('.')
import unittest
import pprint
pp = pprint.PrettyPrinter(indent=2, width=1)
import main
import io


sample_dict_01 = { 'header': { 'Acq Mode': 'Spectrum',
              'Acq Time': 'Dec '
                          '7 '
                          '2021  '
                          '05:35 '
                          'pm',
              'Auto Dilution': 'Undiluted',
              'Bkg File': '--------',
              'Bkg Rejected Masses': '--------',
              'Blank File': '--------',
              'Cal Title': '',
              'Cal Type': 'External '
                          'Calibration '
                          'Method',
              'Calibration': 'C:\\ICPCHEM\x01\\DATA\\AECOM\x11L07p00.B9221SG.C',
              'Comments': '',
              'File Name': '29A.D',
              'File Path': 'C:\\ICPCHEM\x01\\DATA\\AECOM\x11L07P00.BMethod       '
                           ': '
                           'C:\\ICPCHEM\x01\\DATA\\AECOM\x11L07p00.B9221SG.M',
              'Interference Correction': 'OFF',
              'Last Calib': 'Jan '
                            '13 '
                            '2022  '
                            '08:14 '
                            'pm',
              'Multi Tune': '#1 '
                            '071221sg.u',
              'Operator Name': 'Juliana',
              'Prep Dilution': '1.000 '
                               '= '
                               '( '
                               '1.000 '
                               '/ '
                               '1.000 '
                               ') '
                               '* '
                               '1.000',
              'Sample Name': '',
              'Sample Type': 'Sample',
              'Total Dilution': '1.000',
              'VIS Fit': 'Point '
                         'to '
                         'Point',
              'Weighting Method': '1/(SD*SD)'},
  'results': { 'CPS': { 'Ag': { 'CPS': 143.7069,
                                'Mass': 107.0,
                                'RSD(%)': 6.25,
                                'SD': 8.981,
                                'Time(sec)': 0.9},
                        'Al': { 'CPS': 43.63535,
                                'Mass': 27.0,
                                'RSD(%)': 0.75,
                                'SD': 0.328,
                                'Time(sec)': 1.5},
                        'As': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'B': { 'CPS': '',
                               'Mass': '',
                               'RSD(%)': '',
                               'SD': '',
                               'Time(sec)': ''},
                        'Ba': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Be': { 'CPS': 6.666716,
                                'Mass': 9.0,
                                'RSD(%)': 10.0,
                                'SD': 0.6667,
                                'Time(sec)': 1.5},
                        'Bi': { 'CPS': 157383.1,
                                'Mass': 209.0,
                                'RSD(%)': 1.02,
                                'SD': 1603.0,
                                'Time(sec)': 0.3},
                        'Cd': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Co': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Cr': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Cu': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Fe': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Hg': { 'CPS': 1.072725,
                                'Mass': 201.0,
                                'RSD(%)': 0.57,
                                'SD': 0.006109,
                                'Time(sec)': 1.5},
                        'Ir': { 'CPS': 119891.1,
                                'Mass': 193.0,
                                'RSD(%)': 0.1,
                                'SD': 123.5,
                                'Time(sec)': 0.3},
                        'Li': { 'CPS': 1383.195,
                                'Mass': 7.0,
                                'RSD(%)': 3.26,
                                'SD': 45.03,
                                'Time(sec)': 1.5},
                        'Mn': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Mo': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Ni': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Pb': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Rh': { 'CPS': 339095.3,
                                'Mass': 103.0,
                                'RSD(%)': 0.94,
                                'SD': 3186.0,
                                'Time(sec)': 0.3},
                        'Sb': { 'CPS': 253.7102,
                                'Mass': 121.0,
                                'RSD(%)': 4.98,
                                'SD': 12.64,
                                'Time(sec)': 0.9},
                        'Se': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Si': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Sn': { 'CPS': 2956.323,
                                'Mass': 118.0,
                                'RSD(%)': 3.01,
                                'SD': 89.0,
                                'Time(sec)': 0.9},
                        'Ti': { 'CPS': '',
                                'Mass': '',
                                'RSD(%)': '',
                                'SD': '',
                                'Time(sec)': ''},
                        'Tl': { 'CPS': 1.753149,
                                'Mass': 205.0,
                                'RSD(%)': 1.63,
                                'SD': 0.02852,
                                'Time(sec)': 1.5},
                        'U': { 'CPS': 92.22342,
                               'Mass': 238.0,
                               'RSD(%)': 10.46,
                               'SD': 9.646,
                               'Time(sec)': 1.5},
                        'V': { 'CPS': '',
                               'Mass': '',
                               'RSD(%)': '',
                               'SD': '',
                               'Time(sec)': ''},
                        'Zn': { 'CPS': 67.44647,
                                'Mass': 66.0,
                                'RSD(%)': 0.31,
                                'SD': 0.2077,
                                'Time(sec)': 0.3}},
               'Conc.': { 'Ag': { 'Conc.': 0.004247,
                                  'Mass': 107.0,
                                  'RSD(%)': 8.07,
                                  'Rep': 3.0,
                                  'SD': 0.0003428},
                          'Al': { 'Conc.': 2.585,
                                  'Mass': 27.0,
                                  'RSD(%)': 1.02,
                                  'Rep': 3.0,
                                  'SD': 0.02644},
                          'As': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'B': { 'Conc.': '',
                                 'Mass': '',
                                 'RSD(%)': '',
                                 'Rep': '',
                                 'SD': ''},
                          'Ba': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Be': { 'Conc.': 0.0,
                                  'Mass': 9.0,
                                  'RSD(%)': 216.61,
                                  'Rep': 3.0,
                                  'SD': 8.556e-05},
                          'Bi': { 'Conc.': 100.0,
                                  'Mass': 209.0,
                                  'RSD(%)': '---',
                                  'Rep': 3.0,
                                  'SD': '---'},
                          'Cd': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Co': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Cr': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Cu': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Fe': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Hg': { 'Conc.': 1.33,
                                  'Mass': 201.0,
                                  'RSD(%)': 0.61,
                                  'Rep': 3.0,
                                  'SD': 0.008084},
                          'Ir': { 'Conc.': 100.0,
                                  'Mass': 193.0,
                                  'RSD(%)': '---',
                                  'Rep': 3.0,
                                  'SD': '---'},
                          'Li': { 'Conc.': 0.01798,
                                  'Mass': 7.0,
                                  'RSD(%)': 8.1,
                                  'Rep': 3.0,
                                  'SD': 0.001457},
                          'Mn': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Mo': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Ni': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Pb': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Rh': { 'Conc.': 100.0,
                                  'Mass': 103.0,
                                  'RSD(%)': '---',
                                  'Rep': 3.0,
                                  'SD': '---'},
                          'Sb': { 'Conc.': 0.01294,
                                  'Mass': 121.0,
                                  'RSD(%)': 6.5,
                                  'Rep': 3.0,
                                  'SD': 0.0008407},
                          'Se': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Si': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Sn': { 'Conc.': 0.2165,
                                  'Mass': 118.0,
                                  'RSD(%)': 3.13,
                                  'Rep': 3.0,
                                  'SD': 0.006786},
                          'Ti': { 'Conc.': '',
                                  'Mass': '',
                                  'RSD(%)': '',
                                  'Rep': '',
                                  'SD': ''},
                          'Tl': { 'Conc.': 0.09938,
                                  'Mass': 205.0,
                                  'RSD(%)': 1.64,
                                  'Rep': 3.0,
                                  'SD': 0.001628},
                          'U': { 'Conc.': 0.00157,
                                 'Mass': 238.0,
                                 'RSD(%)': 20.11,
                                 'Rep': 3.0,
                                 'SD': 0.0003158},
                          'V': { 'Conc.': '',
                                 'Mass': '',
                                 'RSD(%)': '',
                                 'Rep': '',
                                 'SD': ''},
                          'Zn': { 'Conc.': 34.64,
                                  'Mass': 66.0,
                                  'RSD(%)': 0.31,
                                  'Rep': 3.0,
                                  'SD': 0.1087}}}}


file_lines_array = '''


                    Quantitation Report - Detailed (Text Only)      

 

File Name    : 29A.D
File Path    : C:\ICPCHEM\1\DATA\AECOM\21L07P00.B\
Method       : C:\ICPCHEM\1\DATA\AECOM\21L07p00.B\071221SG.M
Calibration  : C:\ICPCHEM\1\DATA\AECOM\21L07p00.B\071221SG.C
Acq Time     : Dec 7 2021  05:35 pm 
Sample Name  :  
Sample Type  : Sample
Comments     :  
Prep Dilution  : 1.000 = ( 1.000 / 1.000 ) * 1.000
Auto Dilution  : Undiluted
Total Dilution : 1.000
Operator Name: Juliana
Acq Mode     : Spectrum
Cal Title    :  
Cal Type     : External Calibration Method
Last Calib   : Jan 13 2022  08:14 pm
Bkg File     : --------
Bkg Rejected Masses: --------
Interference Correction : OFF
Blank File   : --------
VIS Fit      : Point to Point
Weighting Method: 1/(SD*SD)
Multi Tune   : #1 071221sg.u


 Element Mass ISTD Tune          CPS                     SD    RSD(%) Time(sec)
   Li       7        #1       1,383.195 P             45.03    3.26     1.50
   Be       9        #1        6.666716 P            0.6667   10.00     1.50
   Al      27  VIS   #1        43.63535 P            0.3280    0.75     1.50
   Zn      66  VIS   #1        67.44647 P            0.2077    0.31     0.30
   Rh     103        #1       339,095.3 P             3,186    0.94     0.30

   Ag     107        #1        143.7069 P             8.981    6.25     0.90
   Sn     118        #1       2,956.323 P             89.00    3.01     0.90
   Sb     121        #1        253.7102 P             12.64    4.98     0.90
   Ir     193        #1       119,891.1 P             123.5    0.10     0.30
   Hg     201  VIS   #1        1.072725 P          0.006109    0.57     1.50

   Tl     205  VIS   #1        1.753149 P           0.02852    1.63     1.50
   Bi     209        #1       157,383.1 P             1,603    1.02     0.30
   U      238        #1        92.22342 P             9.646   10.46     1.50

 Element Mass      Tune         Conc.                    SD    RSD(%)    Rep   VIS
   Li       7        #1     1.798E-02 ppb          0.001457      8.10      3      
   Be       9        #1        <0.000 ppb          8.556E-5    216.61      3      
   Al      27        #1         2.585 ppb           0.02644      1.02      3      
   Zn      66        #1         34.64 ppb            0.1087      0.31      3      
   Rh     103        #1       [ 100.0 ppb ]             ---       ---    [ 3 ]   *

   Ag     107        #1     4.247E-03 ppb          3.428E-4      8.07      3      
   Sn     118        #1     2.165E-01 ppb          0.006786      3.13      3      
   Sb     121        #1     1.294E-02 ppb          8.407E-4      6.50      3      
   Ir     193        #1       [ 100.0 ppb ]             ---       ---    [ 3 ]   *
   Hg     201        #1         1.330 ppb          0.008084      0.61      3      

   Tl     205        #1     9.938E-02 ppb          0.001628      1.64      3      
   Bi     209        #1       [ 100.0 ppb ]             ---       ---    [ 3 ]   *
   U      238        #1     1.570E-03 ppb          3.158E-4     20.11      3      
 

End of Report

                         Thu Jan 13 20:15:38 2022


'''.split('\n')

class TestEddBot(unittest.TestCase):
  def setUp(self):
    pass

  def test_extract_numbers(self):
    res = main.extract_numbers('Be       9        #1        <0.000 ppb          8.556E-5    216.61      3      ')
    self.assertEqual(res, [9.0, 0.0, 8.556e-05, 216.61, 3.0])

  def test_extract_numbers_dash_and_brackets(self):
    res = main.extract_numbers('Rh     103        #1       [ 100.0 ppb ]             ---       ---    [ 3 ]   *')
    self.assertEqual(res, [103.0, 100.0, '---', '---', 3.0])

  def test_extract_numbers_1k(self):
    # substitui tira separador de milhares
    res = main.extract_numbers('   Li       7        #1       1,383.195 P             45.03    3.26     1.50')
    self.assertEqual(res, [7.0, 1383.195, 45.03, 3.26, 1.5])

  def test_parse_file(self):
    res = main.parse_file(file_lines_array)
    #pp.pprint(res)
    expected = sample_dict_01
    self.assertEqual(res, expected)

  def test_docs_to_csv(self):
    writer_file =  io.StringIO()
    main.docs_to_csv(writer_file, [sample_dict_01, sample_dict_01], tables = ['Conc.'])
    content = writer_file.getvalue()
    content = content.encode('utf-8')

    #print(repr(content))

    res = content

    expected = b'File Name;Operator Name;Acq Time;Conc.Ag.Conc.;Conc.Ag.Mass;Conc.Ag.RSD(%);Conc.Ag.Rep;Conc.Ag.SD;Conc.Al.Conc.;Conc.Al.Mass;Conc.Al.RSD(%);Conc.Al.Rep;Conc.Al.SD;Conc.As.Conc.;Conc.As.Mass;Conc.As.RSD(%);Conc.As.Rep;Conc.As.SD;Conc.B.Conc.;Conc.B.Mass;Conc.B.RSD(%);Conc.B.Rep;Conc.B.SD;Conc.Ba.Conc.;Conc.Ba.Mass;Conc.Ba.RSD(%);Conc.Ba.Rep;Conc.Ba.SD;Conc.Be.Conc.;Conc.Be.Mass;Conc.Be.RSD(%);Conc.Be.Rep;Conc.Be.SD;Conc.Bi.Conc.;Conc.Bi.Mass;Conc.Bi.RSD(%);Conc.Bi.Rep;Conc.Bi.SD;Conc.Cd.Conc.;Conc.Cd.Mass;Conc.Cd.RSD(%);Conc.Cd.Rep;Conc.Cd.SD;Conc.Co.Conc.;Conc.Co.Mass;Conc.Co.RSD(%);Conc.Co.Rep;Conc.Co.SD;Conc.Cr.Conc.;Conc.Cr.Mass;Conc.Cr.RSD(%);Conc.Cr.Rep;Conc.Cr.SD;Conc.Cu.Conc.;Conc.Cu.Mass;Conc.Cu.RSD(%);Conc.Cu.Rep;Conc.Cu.SD;Conc.Fe.Conc.;Conc.Fe.Mass;Conc.Fe.RSD(%);Conc.Fe.Rep;Conc.Fe.SD;Conc.Hg.Conc.;Conc.Hg.Mass;Conc.Hg.RSD(%);Conc.Hg.Rep;Conc.Hg.SD;Conc.Ir.Conc.;Conc.Ir.Mass;Conc.Ir.RSD(%);Conc.Ir.Rep;Conc.Ir.SD;Conc.Li.Conc.;Conc.Li.Mass;Conc.Li.RSD(%);Conc.Li.Rep;Conc.Li.SD;Conc.Mn.Conc.;Conc.Mn.Mass;Conc.Mn.RSD(%);Conc.Mn.Rep;Conc.Mn.SD;Conc.Mo.Conc.;Conc.Mo.Mass;Conc.Mo.RSD(%);Conc.Mo.Rep;Conc.Mo.SD;Conc.Ni.Conc.;Conc.Ni.Mass;Conc.Ni.RSD(%);Conc.Ni.Rep;Conc.Ni.SD;Conc.Pb.Conc.;Conc.Pb.Mass;Conc.Pb.RSD(%);Conc.Pb.Rep;Conc.Pb.SD;Conc.Rh.Conc.;Conc.Rh.Mass;Conc.Rh.RSD(%);Conc.Rh.Rep;Conc.Rh.SD;Conc.Sb.Conc.;Conc.Sb.Mass;Conc.Sb.RSD(%);Conc.Sb.Rep;Conc.Sb.SD;Conc.Se.Conc.;Conc.Se.Mass;Conc.Se.RSD(%);Conc.Se.Rep;Conc.Se.SD;Conc.Si.Conc.;Conc.Si.Mass;Conc.Si.RSD(%);Conc.Si.Rep;Conc.Si.SD;Conc.Sn.Conc.;Conc.Sn.Mass;Conc.Sn.RSD(%);Conc.Sn.Rep;Conc.Sn.SD;Conc.Ti.Conc.;Conc.Ti.Mass;Conc.Ti.RSD(%);Conc.Ti.Rep;Conc.Ti.SD;Conc.Tl.Conc.;Conc.Tl.Mass;Conc.Tl.RSD(%);Conc.Tl.Rep;Conc.Tl.SD;Conc.U.Conc.;Conc.U.Mass;Conc.U.RSD(%);Conc.U.Rep;Conc.U.SD;Conc.V.Conc.;Conc.V.Mass;Conc.V.RSD(%);Conc.V.Rep;Conc.V.SD;Conc.Zn.Conc.;Conc.Zn.Mass;Conc.Zn.RSD(%);Conc.Zn.Rep;Conc.Zn.SD\r\n29A.D;Juliana;Dec 7 2021  05:35 pm;0,004247;107,0;8,07;3,0;0,0003428;2,585;27,0;1,02;3,0;0,02644;;;;;;;;;;;;;;;;0,0;9,0;216,61;3,0;8,556e-05;100,0;209,0;---;3,0;---;;;;;;;;;;;;;;;;;;;;;;;;;;1,33;201,0;0,61;3,0;0,008084;100,0;193,0;---;3,0;---;0,01798;7,0;8,1;3,0;0,001457;;;;;;;;;;;;;;;;;;;;;100,0;103,0;---;3,0;---;0,01294;121,0;6,5;3,0;0,0008407;;;;;;;;;;;0,2165;118,0;3,13;3,0;0,006786;;;;;;0,09938;205,0;1,64;3,0;0,001628;0,00157;238,0;20,11;3,0;0,0003158;;;;;;34,64;66,0;0,31;3,0;0,1087\r\n29A.D;Juliana;Dec 7 2021  05:35 pm;0,004247;107,0;8,07;3,0;0,0003428;2,585;27,0;1,02;3,0;0,02644;;;;;;;;;;;;;;;;0,0;9,0;216,61;3,0;8,556e-05;100,0;209,0;---;3,0;---;;;;;;;;;;;;;;;;;;;;;;;;;;1,33;201,0;0,61;3,0;0,008084;100,0;193,0;---;3,0;---;0,01798;7,0;8,1;3,0;0,001457;;;;;;;;;;;;;;;;;;;;;100,0;103,0;---;3,0;---;0,01294;121,0;6,5;3,0;0,0008407;;;;;;;;;;;0,2165;118,0;3,13;3,0;0,006786;;;;;;0,09938;205,0;1,64;3,0;0,001628;0,00157;238,0;20,11;3,0;0,0003158;;;;;;34,64;66,0;0,31;3,0;0,1087\r\n'

    self.assertEqual(res, expected)

  def test_parse_file_custom_cons_and_cps_keys(self):
    res = main.parse_file(file_lines_array, cons_keys = ['Conc.'], cps_keys = [], cons_elements = ['Ag', 'Al', 'As', 'B', 'Ba', 'Be', 'Cd', 'Co', 'Cr', 'Cu', 'Fe', 'Hg', 'Li', 'Mn', 'Mo', 'Ni', 'Pb', 'Sb', 'Se', 'Si', 'Sn', 'Ti', 'Tl', 'U', 'V', 'Zn'], cps_elements = [])
    expected = {'results': { 'CPS': { },
               'Conc.': { 'Ag': { 'Conc.': 0.004247},
                          'Al': { 'Conc.': 2.585},
                          'As': { 'Conc.': ''},
                          'B': { 'Conc.': ''},
                          'Ba': { 'Conc.': ''},
                          'Be': { 'Conc.': 0.0},
                          'Cd': { 'Conc.': ''},
                          'Co': { 'Conc.': ''},
                          'Cr': { 'Conc.': ''},
                          'Cu': { 'Conc.': ''},
                          'Fe': { 'Conc.': ''},
                          'Hg': { 'Conc.': 1.33},
                          'Li': { 'Conc.': 0.01798},
                          'Mn': { 'Conc.': ''},
                          'Mo': { 'Conc.': ''},
                          'Ni': { 'Conc.': ''},
                          'Pb': { 'Conc.': ''},
                          'Sb': { 'Conc.': 0.01294},
                          'Se': { 'Conc.': ''},
                          'Si': { 'Conc.': ''},
                          'Sn': { 'Conc.': 0.2165},
                          'Ti': { 'Conc.': ''},
                          'Tl': { 'Conc.': 0.09938},
                          'U': { 'Conc.': 0.00157},
                          'V': { 'Conc.': ''},
                          'Zn': { 'Conc.': 34.64}}}}

    self.assertEqual(res['results'], expected['results'])
    #pp.pprint(res)

  def test_docs_to_matrix(self):
    matrix = main.docs_to_matrix([sample_dict_01, sample_dict_01], tables = ['Conc.'])
    expected = [['File Name', 'Operator Name', 'Acq Time', 'Conc.Ag.Conc.', 'Conc.Ag.Mass', 'Conc.Ag.RSD(%)', 'Conc.Ag.Rep', 'Conc.Ag.SD', 'Conc.Al.Conc.', 'Conc.Al.Mass', 'Conc.Al.RSD(%)', 'Conc.Al.Rep', 'Conc.Al.SD', 'Conc.As.Conc.', 'Conc.As.Mass', 'Conc.As.RSD(%)', 'Conc.As.Rep', 'Conc.As.SD', 'Conc.B.Conc.', 'Conc.B.Mass', 'Conc.B.RSD(%)', 'Conc.B.Rep', 'Conc.B.SD', 'Conc.Ba.Conc.', 'Conc.Ba.Mass', 'Conc.Ba.RSD(%)', 'Conc.Ba.Rep', 'Conc.Ba.SD', 'Conc.Be.Conc.', 'Conc.Be.Mass', 'Conc.Be.RSD(%)', 'Conc.Be.Rep', 'Conc.Be.SD', 'Conc.Bi.Conc.', 'Conc.Bi.Mass', 'Conc.Bi.RSD(%)', 'Conc.Bi.Rep', 'Conc.Bi.SD', 'Conc.Cd.Conc.', 'Conc.Cd.Mass', 'Conc.Cd.RSD(%)', 'Conc.Cd.Rep', 'Conc.Cd.SD', 'Conc.Co.Conc.', 'Conc.Co.Mass', 'Conc.Co.RSD(%)', 'Conc.Co.Rep', 'Conc.Co.SD', 'Conc.Cr.Conc.', 'Conc.Cr.Mass', 'Conc.Cr.RSD(%)', 'Conc.Cr.Rep', 'Conc.Cr.SD', 'Conc.Cu.Conc.', 'Conc.Cu.Mass', 'Conc.Cu.RSD(%)', 'Conc.Cu.Rep', 'Conc.Cu.SD', 'Conc.Fe.Conc.', 'Conc.Fe.Mass', 'Conc.Fe.RSD(%)', 'Conc.Fe.Rep', 'Conc.Fe.SD', 'Conc.Hg.Conc.', 'Conc.Hg.Mass', 'Conc.Hg.RSD(%)', 'Conc.Hg.Rep', 'Conc.Hg.SD', 'Conc.Ir.Conc.', 'Conc.Ir.Mass', 'Conc.Ir.RSD(%)', 'Conc.Ir.Rep', 'Conc.Ir.SD', 'Conc.Li.Conc.', 'Conc.Li.Mass', 'Conc.Li.RSD(%)', 'Conc.Li.Rep', 'Conc.Li.SD', 'Conc.Mn.Conc.', 'Conc.Mn.Mass', 'Conc.Mn.RSD(%)', 'Conc.Mn.Rep', 'Conc.Mn.SD', 'Conc.Mo.Conc.', 'Conc.Mo.Mass', 'Conc.Mo.RSD(%)', 'Conc.Mo.Rep', 'Conc.Mo.SD', 'Conc.Ni.Conc.', 'Conc.Ni.Mass', 'Conc.Ni.RSD(%)', 'Conc.Ni.Rep', 'Conc.Ni.SD', 'Conc.Pb.Conc.', 'Conc.Pb.Mass', 'Conc.Pb.RSD(%)', 'Conc.Pb.Rep', 'Conc.Pb.SD', 'Conc.Rh.Conc.', 'Conc.Rh.Mass', 'Conc.Rh.RSD(%)', 'Conc.Rh.Rep', 'Conc.Rh.SD', 'Conc.Sb.Conc.', 'Conc.Sb.Mass', 'Conc.Sb.RSD(%)', 'Conc.Sb.Rep', 'Conc.Sb.SD', 'Conc.Se.Conc.', 'Conc.Se.Mass', 'Conc.Se.RSD(%)', 'Conc.Se.Rep', 'Conc.Se.SD', 'Conc.Si.Conc.', 'Conc.Si.Mass', 'Conc.Si.RSD(%)', 'Conc.Si.Rep', 'Conc.Si.SD', 'Conc.Sn.Conc.', 'Conc.Sn.Mass', 'Conc.Sn.RSD(%)', 'Conc.Sn.Rep', 'Conc.Sn.SD', 'Conc.Ti.Conc.', 'Conc.Ti.Mass', 'Conc.Ti.RSD(%)', 'Conc.Ti.Rep', 'Conc.Ti.SD', 'Conc.Tl.Conc.', 'Conc.Tl.Mass', 'Conc.Tl.RSD(%)', 'Conc.Tl.Rep', 'Conc.Tl.SD', 'Conc.U.Conc.', 'Conc.U.Mass', 'Conc.U.RSD(%)', 'Conc.U.Rep', 'Conc.U.SD', 'Conc.V.Conc.', 'Conc.V.Mass', 'Conc.V.RSD(%)', 'Conc.V.Rep', 'Conc.V.SD', 'Conc.Zn.Conc.', 'Conc.Zn.Mass', 'Conc.Zn.RSD(%)', 'Conc.Zn.Rep', 'Conc.Zn.SD'], ['29A.D', 'Juliana', 'Dec 7 2021  05:35 pm', 0.004247, 107.0, 8.07, 3.0, 0.0003428, 2.585, 27.0, 1.02, 3.0, 0.02644, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0.0, 9.0, 216.61, 3.0, 8.556e-05, 100.0, 209.0, '---', 3.0, '---', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 1.33, 201.0, 0.61, 3.0, 0.008084, 100.0, 193.0, '---', 3.0, '---', 0.01798, 7.0, 8.1, 3.0, 0.001457, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 100.0, 103.0, '---', 3.0, '---', 0.01294, 121.0, 6.5, 3.0, 0.0008407, '', '', '', '', '', '', '', '', '', '', 0.2165, 118.0, 3.13, 3.0, 0.006786, '', '', '', '', '', 0.09938, 205.0, 1.64, 3.0, 0.001628, 0.00157, 238.0, 20.11, 3.0, 0.0003158, '', '', '', '', '', 34.64, 66.0, 0.31, 3.0, 0.1087], ['29A.D', 'Juliana', 'Dec 7 2021  05:35 pm', 0.004247, 107.0, 8.07, 3.0, 0.0003428, 2.585, 27.0, 1.02, 3.0, 0.02644, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 0.0, 9.0, 216.61, 3.0, 8.556e-05, 100.0, 209.0, '---', 3.0, '---', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 1.33, 201.0, 0.61, 3.0, 0.008084, 100.0, 193.0, '---', 3.0, '---', 0.01798, 7.0, 8.1, 3.0, 0.001457, '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 100.0, 103.0, '---', 3.0, '---', 0.01294, 121.0, 6.5, 3.0, 0.0008407, '', '', '', '', '', '', '', '', '', '', 0.2165, 118.0, 3.13, 3.0, 0.006786, '', '', '', '', '', 0.09938, 205.0, 1.64, 3.0, 0.001628, 0.00157, 238.0, 20.11, 3.0, 0.0003158, '', '', '', '', '', 34.64, 66.0, 0.31, 3.0, 0.1087]]
    self.assertEqual(matrix, expected)

  def test_agrupar_matrix_por_arquivo(self):
    matrix = [['File Name', 'Operator Name', 'Acq Time', 'x', 'y'],
              ['A', 'J', 'Dec 3 2021  10:12 pm', 1, ''],
              ['B', 'J', 'Dec 13 2021  10:12 pm', '', 2],
              ['A', 'J', 'Dec 7 2021  10:12 am', '', 3],
              ['B', 'J', 'Dec 2 2021  10:12 am', 4, '']]

    expected = [['File Name', 'Operator Name', 'Acq Time', 'x', 'y'],
                ['A', 'J', 'Dec 3 2021  10:12 pm', 1, 3],
                ['B', 'J', 'Dec 2 2021  10:12 am', 4, 2]]

    res = main.agrupar_matrix_por_arquivo(matrix)

    self.assertEqual(res, expected)


if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestEddBot)
  unittest.TextTestRunner(stream=None, verbosity=3).run(suite)