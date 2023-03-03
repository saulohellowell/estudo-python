a = 'qqqqqq'
b = 'b'
c = 'c'
string = 'a={2} b={1} c={0}' #dentro na chaves eu posso escolher qual eu quero
formato = string.format(a,b,c)
                  #     0,1,2 referente
print(formato)