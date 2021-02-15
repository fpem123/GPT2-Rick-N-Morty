# GPT2-Rick-N-Morty

[![Run on Ainize](https://ainize.ai/images/run_on_ainize_button.svg)](https://ainize.web.app/redirect?git_repo=https://github.com/fpem123/GPT2-Rick-N-Morty)

This project generates Rick and Morty script using GPT-2 model.

Model: https://huggingface.co/e-tony/gpt2-rnm

    How to use:
      * First, Choose Rick and Morty character name.
      * Second, Fill what the character will say in text. This will be base of script.
      * And then, Fill number in length. Text is created as long as "length". I recommend between 100 and 300.
      * If length is so big, generate time will be long.

### Post parameter
    
    name: The Rick and Morty character name.
    text: The base of script.
    length: The size of generated text. (min: 50)

### Output foramt

    {"0": [[character name, dialog], [character name, dialog], ...]}


### ** With CLI **

### Input example

    curl -X POST "https://master-gpt2-rick-n-morty-fpem123.endpoint.ainize.ai/Rick-N-Morty" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "name=Rick" -F "text=Hey Morty" -F "length=150"

### Output example

    {
      "0": [
        [
          "Rick",
          " Hey Morty, I got a dream tonight…"
        ],
        [
          "Narrator",
          "(Rick and Morty make out inside the bedroom)"
        ],
        [
          "Morty",
          " Aaahhh, look at me. That's a monster! Look at me, look at me! Look at me! Look at me! Look at me! Look at me! Look at me! Look at me!"
        ],
        [
          "Narrator",
          "(Rick and Morty start shooting.)"
        ],
        [
          "Rick",
          " Rick, you're the best guy in the galaxy, Morty. It's time for the Morty and Morty"
        ]
      ]
    }


### ** With swagger **

API page: https://ainize.ai/fpem123/GPT2-Rick-N-Morty?branch=master

### ** With a demo **

Demo page: https://master-gpt2-rick-n-morty-fpem123.endpoint.ainize.ai/

### Image reference

    static/README.md

--
