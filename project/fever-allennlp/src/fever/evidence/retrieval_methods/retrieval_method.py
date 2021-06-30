from allennlp.common import Registrable
## sys.path is added in the jupyter notebook, so this works, sys.path.insert(0, 'src/fever/reader')
from document_database import FEVERDocumentDatabase


class RetrievalMethod(Registrable):

    def __init__(self,database:FEVERDocumentDatabase):
        self.database = database

    def get_sentences_for_claim(self,claim_text,include_text=False):
        pass
