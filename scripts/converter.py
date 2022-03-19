import pandas as pd

def converter():
    new_names = ['cpf',
                'private',
                'incompleto',
                'data da ultima compra',
                'ticket medio',
                'ticket da ultima compra',
                'loja mais frequente',
                'loja da ultima compra',
                'cpf valido']

    dataframe1 = pd.read_csv('base_teste.txt',
                    names=new_names,
                    header=0,
                    usecols=[0,1,2,3,4,5,6,7,8],
                    delim_whitespace=True)

    dataframe1.to_csv('FF.csv', index = None)