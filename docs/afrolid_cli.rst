Interactive Command Line
=====================
   -  Turjuman interactive cli ``turjuman_interactive`` support only beam search with the following default setting:

      -  ``-m`` or ``--model_path``: Rath of the AfroLID model directory, (``Required``)
      -  ``-o`` or ``--max_outputs``: The maximum of the output tanslations (``default value is 3``)
      -  ``-l`` or ``--logging_file``: Number of beams (``default value is 1``)
      -  ``-n`` or ``--no_repeat_ngram_size``: Number of n-gram that doesn't appears twice (``default value is 2``)

   -  ``afrolid_cli`` command asks you you to input your input text. Moreover, you can write q to exsit as shown in the following image.

.. raw:: html

   <img src="https://github.com/UBC-NLP/afrolid/raw/main/images/afrolid_cli.jpg" alt="afrolid_cli"/>



Usage and Arguments
-------------------
.. code-block:: console

      turjuman_interactive -h

.. code-block:: console
            usage: afrolid_cli [-h]
                  -m MODEL_PATH
                  [-o MAX_OUTPUTS]
                  [-l LOGGING_FILE]

            AfroLID Command Line Interface (CLI)

            optional arguments:
                  -h, --help   show this help message and  exit
                  -m MODEL_PATH, --model_path MODEL_PATH   path of the  AfroLID   model    directory
                  -o MAX_OUTPUTS, --max_outputs MAX_OUTPUTS  number of hypotheses to output,  default vlaue is 3
                  -l LOGGING_FILE, --logging_file LOGGING_FILE the logging file path, default vlaue is  None

AfrlioLID Interactive
---------------------------

.. code-block:: console

      !afrolid_cli --model_path /path/to/model

.. code-block:: console

            2022-12-06 18:01:24 | INFO | afroli.afrolid_cli | AfroLID Command Line Interface
            2022-12-06 18:01:24 | INFO | afroli.afrolid_cli | Initalizing AfroLID's task and model.
            | [input] dictionary: 64001 types
            | [label] dictionary: 528 types
            Type your input text or (q) to STOP: ዮሃንስ ኣብ ኢድ እቲ ብርቱዕ መልኣኽ እንታይ ይርኢ ፧ 5 ዮሃንስ
            2022-12-06 18:01:41 | INFO | afroli.afrolid_cli | Input text: ዮሃንስ ኣብ ኢድ እቲ ብርቱዕ መልኣኽ እንታይ ይርኢ ፧ 5 ዮሃንስ
            Predicted languages:
                  |-- ISO: tir	Name: Tigrinya	Script: Ethiopic	Score: 100.0%
            Type your input text or (q) to STOP:  ከ ሀ እከ ፖ የኮሜዲያን ቶማስ እና ናቲ ኮሜዲ ድራማ እና 50
            2022-12-06 18:01:57 | INFO | afroli.afrolid_cli | Input text:  ከ ሀ እከ ፖ የኮሜዲያን ቶማስ እና ናቲ ኮሜዲ ድራማ እና 50
            Predicted languages:
                  |-- ISO: amh	Name: Amharic	Script: Ethiopic	Score: 49.74%
                  |-- ISO: tir	Name: Tigrinya	Script: Ethiopic	Score: 49.34%
                  |-- ISO: gof	Name: Goofa	Script: Latin	Score: 0.82%
            Type your input text or (q) to STOP: أوشا يبد ارايس ن ڒفقها ينا-ٱس إ عيسى : ما وار
            2022-12-06 18:02:09 | INFO | afroli.afrolid_cli | Input text: أوشا يبد ارايس ن ڒفقها ينا-ٱس إ عيسى : ما وار
            Predicted languages:
                  |-- ISO: rif	Name: Tarifit	Script: Arabic	Score: 100.0%
            Type your input text or (q) to STOP: Vamteta vakulu na vagogo va vandu vamkotili
            2022-12-06 18:02:18 | INFO | afroli.afrolid_cli | Input text: Vamteta vakulu na vagogo va vandu vamkotili
            Predicted languages:
                  |-- ISO: ngo	Name: Ngoni	Script: Latin	Score: 99.95%
                  |-- ISO: rwk	Name: Rwa	Script: Latin	Score: 0.01%
                  |-- ISO: asa	Name: Asu	Script: Latin	Score: 0.01%
            Type your input text or (q) to STOP: q

Google Colab Link
-----------------

You can find the full examples on the Google Colab on the following link
https://colab.research.google.com/github/UBC-NLP/afrolid/blob/main/examples/afrolid_interactive_cli.ipynb
