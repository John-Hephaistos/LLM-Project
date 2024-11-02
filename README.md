# LLM-Project
Final project for our LLM course

Instructions on setting the code locally:
Click on the Code button:


Copy the url of the repository:


Fetch the repository code on your own device using git:

    git clone https://github.com/John-Hephaistos/LLM-Project.git

Select the folder where your repository is stored in - try "group-16-project":

    cd group-16-project

Make sure to install the python packages from the requirements.txt file!

    pip install -r requirements.txt

Instructions on running the code:
Firstly, we must mention that our project makes usage of proprietary models from OpenAI. This means that to run our project, an API key thethered to my OpenAI dev account is required. For now I am leaving it in the code, despite the risks it poses. I will also have it included in the submission message on brightspace. 
You may have noticed that our code uses Jupyter notebooks only. This is done for the sake of simplicity and modularity. The outputs of the previous run of all files are left over, if you do not wish to run every single cell (many of them just showcase shapes and how inputs and outputs have been reformated).
As a user, all you have to do is:

    1. Run the entire Dataset_Preprocessing.ipynb - This will process and bring the IMDB movie data into the specific formats for each of our models 
    2. Run any of the other files, in any order you wish - Each file will save its predictions and performances in csv files for latter views, as well as in the Jupiter notebook cells

Quick run-down of each of the files

    0. Dataset_Preprocessing: Formats the data, does the train-test-validation split. Creates the json files in the required format for Fine-Tuning. All these should be saved in .csv or .json for further usage and      viewing.
    I. Prompt Engineering: This handles the prompt engineering GPT. Its by far the simples model to run. The api key is already inserted, all you mus do is just run the code cell by cell.
    II. Fine-Tuning: This handles the fine-tuned GPT model. If you wish to re-train the model, keep it mind it may take 20-30 minutes. Otherwise, all the model IDs are saved up for instant usage! You will require the json files created from the Dataset_Preprocessing, so do not forget to run those cells!
    III. Embeddings GPT: Serves as a replacement for our lack of PEFT. Warning, the embeddings produced by the model are rather large (139 mb) - given the size of the dataset


Issues and Limitations:

The first problem I would like to address is the usage of close-source models. Due to this choice, our project cannot produce a model that can be saved locally (save for the Random Forest model - which does not count). This means that viewing the models is limited to the Dashboard feature that OpenAI offers, which is a great drawback of our project that we did not consider. This was our first LLM-transformer project, and our lack of awarness greatly reduced its potential. 

The second problem is the lack of PEFT. We cannot create a GPT 4.o mini PEFT model. We instead looked to our main source paper and decided to add an Embeddings GPT. In the next section we attempted to further address this limitation

The last key issue is the operational cost of our project. OpenAI charges a small fee for the usage of its models and services. Working with such a factor made us understand the importance of using open-source software as much as possible. We assume full responsibility for these costs - running and testing the models will be covered by us.

Further Improvements:

We are sorry than we could not deliver on a PEFT model as well. However, we tried in the little time between the Presentation and the Code+Report submission to re-create the project using the open-source GPT-2. In the repo you will notice the following files:

    I.  - A GPT-2 implementation of the prompt engineering. Does not work
    II. - GPT-2 fine tuned for sentiment analysis using our dataset. Code works, however, we could not complete the fine-tuning (due to trouble with habrok) before the deadline
    III. - GPT-2 fine tuned with LORA for sentiment analysis using our dataset. Code works, however, we could not complete PEFT (due to trouble with habrok) before the deadline


    

    

