Integrate AfroLID with python code
=========================================

.. container:: cell markdown

   .. rubric:: (1) Install AfroLID
      :name: 1-install-turjuman

.. code-block:: console

      pip install git+https://github.com/UBC-NLP/afrolid.git --q

.. container:: cell markdown

Initial AfroLID object
----------------------------
Import related packges 

.. code:: python

      import os, sys
      import logging
      from afrolid.main import classifier

.. code:: python

      logging.basicConfig(
            format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            level=os.environ.get("LOGLEVEL", "INFO").upper(),
            force=True, # Resets any previous configuration
      )
      logger = logging.getLogger("afrolid")

Create turjuman object

.. code:: python

      cl = classifier(logger, model_path=/path/to/model)



Get language prediction(s)
-------------------------------------

.. code:: python

     ## Gold label = dip
      text="6Acï looi aya në wuöt dït kɔ̈k yiic ku lɔ wuöt tɔ̈u tëmec piny de Manatha ku Eparaim ku Thimion , ku ɣään mec tɔ̈u të lɔ rut cï Naptali"
      predicted_langs = cl.classify(text) # default max_outputs=3
      print("Predicted languages:")
      for lang in predicted_langs:
      print("     |-- ISO: {}\tName: {}\tScript: {}\tScore: {}%".format(
                      lang,
                      predicted_langs[lang]['name'], 
                      predicted_langs[lang]['script'],
                      predicted_langs[lang]['score']))



.. code:: python
      ## Gold label = kmy
      text="Ama vuodieke nɩŋ mana n Chʋa Ŋmɩŋ dɩ nagɩna yɩ mɩŋ , nan keŋ n jigiŋ a yi mɩŋ yada , ta n kaaŋ yagɩ vuodieke nɩŋ dɩ kienene n jigiŋ"
      predicted_langs = cl.classify(text)  # default max_outputs=3
      print("Predicted languages:")
      for lang in predicted_langs:
      print("     |-- ISO: {}\tName: {}\tScript: {}\tScore: {}%".format(
                      lang,
                      predicted_langs[lang]['name'], 
                      predicted_langs[lang]['script'],
                      predicted_langs[lang]['score']))    


Integrate with Pandas
-----------------------------------
 .. code:: python

      wget https://raw.githubusercontent.com/UBC-NLP/afrolid/main/examples/examples.tsv -O examples.tsv


.. code:: python

      import pandas as pd
      from tqdm import tqdm
      tqdm.pandas()
      df = pd.read_csv("examples.tsv", sep="\t")
      
      def get_afrolid_prediction(text):
            predictions = cl.classify(text, max_outputs=1)
            for lang in predictions:
                  return lang, predictions[lang]['score'], predictions[lang]['name'], predictions[lang]['script']

      df['predict_iso'], df['predict_score'], df['predict_name'], df['predict_script'] = zip(*df['content'].progress_apply(get_afrolid_prediction))

.. code-block:: console

         {'source': 'As US reaches one million COVID deaths, how are Americans coping?', 'target': ['وبما أن الولايات المتحدة تصل إلى مليون حالات وفاة بسبب كوفيد-19 ، كيف يعالج الأميركيون الأمر ؟']}

Read and translate text from file
--------------------------------------

   -  ``-f`` or ``--input_file``: import the text from file. The translation will saved on the JSON format file
   -  ``-bs`` or ``--batch_size``: The maximum number of source examples utilized in one iteration (``default value is 25``)
   - ``gen_options``: Generation options

.. code:: python

      gen_options = {"search_method":"beam", "seq_length": 300, "num_beams":5, "no_repeat_ngram_size":2, "max_outputs":1}
      torj.translate_from_file("samples.txt", batch_size=25, **gen_options)


Google Colab Link
-----------------

You can find the full examples on the Google Colab on the following link
https://colab.research.google.com/github/UBC-NLP/afrolid/blob/main/examples/Integrate_afrolid_with_your_code.ipynb
