
import argparse
from ast import arg
import os
import sys
import logging
from afrolid.main import classifier
import regex

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=os.environ.get("LOGLEVEL", "INFO").upper(),
    stream=sys.stdout,
)
logger = logging.getLogger("afroli.afrolid_cli")


def get_parser():
    parser = argparse.ArgumentParser(
        description="AfroLID Command Line Interface (CLI)"
    )
    # parser.add_argument('-t', '--text', required='--prox', type=str, help='The input text')
    parser.add_argument('-m', '--model_path', required='--prox', type=str, help="path of the AfroLID model directory")
    parser.add_argument('-o', '--max_outputs', default=3, type=int, help='number of hypotheses to output, default vlaue is 3')
    parser.add_argument('-l', '--logging_file', default=None, type=str, help='the logging file path, default vlaue is None')
    return parser


def afrolid_cli():
    
    parser = get_parser()
    args = parser.parse_args()
    if args.logging_file is not None:
        logger.addHandler(
            logging.FileHandler(
                filename=args.logging_file,
            )
        )
    logger.info("AfroLID Command Line Interface")
    if args.model_path is None :
        logger.info("[Error] please ")
        return None
    cl = classifier(logger, args.model_path)
    source=""
    while source !='q':
        source = input("Type your input text or (q) to STOP: ")
        if source !='q':
            if len(regex.sub('\s+','',source))<5:
                logger.info("Input should be at least 5 characters")
                continue

            predicted_langs = cl.classify(source, args.max_outputs)
            print("Predicted languages:")
            for lang in predicted_langs:
                print("     |-- ISO: {}\tName: {}\tScript: {}\tScore: {}%".format(
                      lang,
                      predicted_langs[lang]['name'], 
                      predicted_langs[lang]['script'],
                      predicted_langs[lang]['score']))
    

if __name__ == "__main__":
    afrolid_cli()
