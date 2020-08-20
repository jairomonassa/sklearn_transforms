from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
    def transforma_perfil (valor):
        # MUDADO O TARGET PARA BINÁRIO, TALVEZ NÃO USE
        if valor == 'EXATAS':
            return 0
           
        elif  valor == 'DIFICULDADE':
              return 1
          
        elif  valor =='HUMANAS':
             return 2
       
        elif  valor =='MUITO_BOM':
              return 3
             
        elif  valor =='EXCELENTE':
              return 4
            
    def transforma_nota (valor):
        #NOTAS QUE NÃO SÃO MAIOR QUE 10
        if valor > 10.0:
            return 10.0
        else:
            return valor
