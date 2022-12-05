# -*- coding: utf-8 -*-
from afrolid import tasks
import argparse
from fairseq import checkpoint_utils, data
import torch
import torch.nn.functional as F
import regex
import sentencepiece as spm
import pandas as pd
import logging
import os
import sys
logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=os.environ.get("LOGLEVEL", "INFO").upper(),
    stream=sys.stdout,
)
# import math
class classifier():
  def __init__(self, model_path):
    self.logger = logging.getLogger(__name__)
    self.model_path = model_path
    self.afrolid_task, self.model, self.tokenizer= self.init_task_model()
    self.lang_info = self.load_langs_info()
    print(self.lang_info)
  def init_task_model(self):
    print("dddsssssssss")
    self.logger.info("Initalizing AfroLID's task and model.")
    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument("--task", metavar="TASK", default='afrolid_task',)
    parser.add_argument('-d', "--data", type=str,default=self.model_path)
    args, _ = parser.parse_known_args()
    afrolid_task = tasks.setup_task(args)
    models, _model_args = checkpoint_utils.load_model_ensemble([self.model_path+"/afrolid_v1_checkpoint.pt"], task=afrolid_task)
    model = models[0]
    model.eval()
    tokenizer = spm.SentencePieceProcessor()
    tokenizer.Load(self.model_path+"/afrolid_spm_517_bpe.model")
    return afrolid_task, model, tokenizer
  def load_langs_info(self):
    langs={}
    df = pd.read_csv(os.path.dirname(__file__)+"/langs_info.tsv", sep='\t')
    for index, row in df.iterrows():
      lang_iso = row['ISO']
      lang_name = row['lang_name']
      lang_script = row['script']
      langs[lang_iso]={'name': lang_name, 'script': lang_script}
    return langs

  def classify(self, text, max_outputs=3):
    max_outputs = int(max_outputs)
    self.logger.info("Input text: {}".format(text))
    tokens = " ".join(self.tokenizer.EncodeAsPieces(text.strip()))
    # print(tokens)
    tokens = self.afrolid_task.source_dictionary.encode_line(tokens, add_if_not_exist=False,)
    # print("*****", tokens)
    # print (">>>>>>", torch.IntTensor(self.tokenizer.EncodeAsIds(text.strip())))
    # tokens=torch.IntTensor(self.tokenizer.EncodeAsIds(text))
    tokens=torch.IntTensor(tokens)
    # print(tokens)
    dummy_target = torch.tensor([-1])
    batch = data.language_pair_dataset.collate(
                samples=[{'id': -1, 'source': tokens, 'target':dummy_target}],  # bsz = 1
                pad_idx=self.afrolid_task.source_dictionary.pad(),
                eos_idx=self.afrolid_task.source_dictionary.eos(),
                left_pad_source=False,
                left_pad_target=False,
                input_feeding=True,
                pad_to_length={'source': 128, 'target': 1},
            )
    # print(batch)
    outputs = self.model(**batch['net_input'])
    probabilities, predictions_idx = F.softmax(outputs[0], dim=-1).topk(k=max_outputs)
    # print()
    results={}
    if max_outputs==1:
      label_name = self.afrolid_task.target_dictionary.string([predictions_idx])
      predicted_score = round(float(torch.squeeze(probabilities).detach().numpy())*100, 2)
      results[label_name]={'score':predicted_score, 'name': self.lang_info[label_name]['name'], 'script':self.lang_info[label_name]['script']}
    else:
      for score, prediction_idx in zip(torch.squeeze(probabilities),torch.squeeze(predictions_idx)):
        label_name = self.afrolid_task.target_dictionary.string([prediction_idx])
        predicted_score = round(float(torch.squeeze(score).detach().numpy())*100, 2)
        if predicted_score<=0:
          break
        # print(score, prediction_idx, label_name, predicted_score)
        # print(score, prediction_idx, label_name, predicted_score)
        results[label_name]={'score':predicted_score, 'name': self.lang_info[label_name]['name'], 'script':self.lang_info[label_name]['script']}
        
        # print ("ISO: {}\tName: {}\tScript: {}\tScore: {}%".format(
        #               label_name,
        #               self.lang_info[label_name]['name'], 
        #               self.lang_info[label_name]['script'],
        #               label_name))
      # print(text)
    return results
