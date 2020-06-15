import numpy as np

def Di_rel(X,DIo):
  nrow=len(X[:,0])
  ncol=len(X[0,:])
  # nrow,ncol=(np.array(X)).shape()
  soma=0
  for j in range(ncol):
    for i in range(nrow):
        Xj=np.mean(X[:,j])
        soma=soma+(X[i,j]-Xj)**2
  DI=(soma/nrow)**0.5
  DIr=DI/DIo
  return DIr,DI


def Adjust_F_CR(DIr,Fo,CRo,y_cod_F,y_cod_CR,Fc):

  Fd=DIr
  CRa=np.copy(CRo)
  Fa=np.copy(Fo)

  if(y_cod_F>0):
    Fo=Fo*(1+Fd) #Fo=Fo+Fc
  else:
    Fo=Fo*(1-Fd) 
  Fo=(3*Fo+Fa)/4 # para suavizar
    
  if(y_cod_CR>0):
    CRo=CRo*(1+Fd) 
  else:
    CRo=CRo*(1-Fd) 
  CRo=(3*CRo+CRa)/4 # para suavizar
     
  # reajuste do intervalo (se necessario)
  if(CRo> 1):
    CRo=1
  if(CRo< Fc):
    CRo=Fc
      
  # reajuste do intervalo (se necessario)
  if(Fo> 1):
    Fo=1
  if(Fo< Fc):
    Fo=Fc
      
  return Fo,CRo
