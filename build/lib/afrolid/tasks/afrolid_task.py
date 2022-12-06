# -*- coding: utf-8 -*-
import os
import torch

from fairseq.data import Dictionary, LanguagePairDataset
from afrolid.tasks import FairseqTask, register_task
 
@register_task('afrolid_task')
class afrolid_task(FairseqTask):

    @staticmethod
    def add_args(parser):
        #Add some command-line arguments for specifying where the data is located and the maximum supported input length.
        parser.add_argument('data', metavar='FILE', help='file prefix for data')
        parser.add_argument('--max-positions', default=1024, type=int, help='max input length')
    
    @classmethod
    def setup_task(cls, args, **kwargs):
        #Here we can perform any setup required for the task. This may include loading Dictionaries, initializing shared
        #Embedding layers, etc. In this case we'll just load the dictionaries.
        input_vocab = Dictionary.load(os.path.join(args.data, 'dict.input.txt'))
        label_vocab = Dictionary.load(os.path.join(args.data, 'dict.label.txt'))
        print('| [input] dictionary: {} types'.format(len(input_vocab)))
        print('| [label] dictionary: {} types'.format(len(label_vocab)))

        return afrolid_task(args, input_vocab, label_vocab)

    def __init__(self, args, input_vocab, label_vocab):
        super().__init__(args)
        #self.args = args
        self.input_vocab = input_vocab
        self.label_vocab = label_vocab
    def load_dataset(self, split, **kwargs):
        """ Load a given dataset split (e.g., train, dev, test."""

        prefix = os.path.join(self.cfg.data, '{}.input-label'.format(split))

        # Read input sentences.
        sentences, lengths = [], []
        with open(prefix + '.input', encoding="utf-8") as file:

            for line in file:
                sentence = line.strip()

                #Tokenize the sentence, splitting on spaces
                tokens = self.input_vocab.encode_line(sentence, add_if_not_exist=False,)
                sentences.append(tokens)
                lengths.append(tokens.numel())

        # Read labels.
        labels = []
        with open(prefix + '.label', encoding="utf-8") as file:
            for line in file:
                label = line.strip()
                labels.append(
                    # Convert labels to a numeric ID.
                    torch.LongTensor([self.label_vocab.add_symbol(label)])
                )
        assert len(sentences) == len(labels)
        print('| {} {} {} example'.format(self.cfg.data, split, len(sentences)))

        # We reuse LanguagePairDataset since classification can be modeled as a
        # sequence-to-sequence task where the target sequence has length 1.
        
        self.datasets[split] = LanguagePairDataset(
            src=sentences,
            src_sizes=lengths,
            src_dict=self.input_vocab,
            tgt=labels,
            tgt_sizes=torch.ones(len(labels)), #targets have length 1
            tgt_dict=self.label_vocab,
            left_pad_source=False,
            # Since our target is a single class label, there's no need for
            # teacher forcing. If we set this to "True" then our Model's 
            # "forward()" method would receive an additional argument called
            # *prev_output_tokens* that would contain a shifted version of the
            # target sequence.
            input_feeding=True,
        )
    def max_positions(self):
     #   """ Return the max input length allowed by the task."""
       # The source should be less than *args.max_positions and the "target"
        # has max length 1.
        return (self.cfg.max_positions, 1)

    @property
    def source_dictionary(self):
        """ Return the max input length allowed by the task."""
        return self.input_vocab

    @property
    def target_dictionary(self):
        """ Return the max input length allowed by the task."""
        return self.label_vocab



                       
