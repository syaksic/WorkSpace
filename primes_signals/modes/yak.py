#print('>run.py')
import utils
reload(utils)

from utils import load_tok
Tok=load_tok('Tok')

from utils import check
Tok=check('Tok')

#import Yak
#Yak.createYak(Tok,'Yak')


from utils import save_Tok
save_Tok(Tok,'Yak00')

#from utils import printTok
#printTok(Tok)

#print('<run.py')