import torch
from torch.utils.data import Dataset
import os
import binaryfile

class RankingDataset(Dataset):
    def __init__(self, queries, mention2id, names, mode = 'train', emb_file = os.path.join("./vec_50.bin")) -> None:
        super().__init__()
        word2vec = open(emb_file,"rb")
        self.name_array = names
        self.mention2id =  mention2id
        self.query_id_array = queries
        self.name2id, self.query2id  = self.process_data_dict()
        word2vec = binaryfile.read(word2vec)
        for idx, line in enumerate(word2vec):
            print(line)
            if idx==50:
                break

    def process_data_dict(self):
        name2id = {}
        for name_ in self.name_array:
            id_number =  self.mention2id[str(name_)]
            name2id[str(name_)] = id_number
        query2id  = {}
        for item in self.query_id_array:
            query2id[item] =  self.mention2id[item]
        return name2id, query2id

