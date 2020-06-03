# CIS RASA BOT

## 🏄 Introduction
The purpose of this repo is to showcase a contextual AI assistant built with the open source Rasa framework.
	CIS RASA BOT is an alpha version and lives in our docs,
	helping developers getting started with our open source tools.
	It supports the following user goals:
	
   *  Discover Career Tracks test
   *  Answering some FAQs around CareerLabs
   *  Directing technical questions to specific documentation

## :heavy_check_mark: Compatibility
This [repo](https://gitlab.com/internshiptasks/cis-rasa-bot.git) is compatible with

> | SDK version | compatible Rasa X version |
> | ------ | ------ |
> | 1.3.x | >=0.24.7 |
> 
> | Pythan version |
> | ------ |
> | >=3.6.10 | 
> 
> | pip version |
> | ------ |
> | >=20.0.1 | 

## 👷 Installation(Windows 10 OS)

To install CIS RASA BOT, please clone the [repo](https://gitlab.com/internshiptasks/cis-rasa-bot.git) and run:
>  `cd cis-rasa-bot` (Going [repo](https://gitlab.com/internshiptasks/cis-rasa-bot.git) directory)
>  
>  `create -n rasa python=3.6`(Optional: If you don't want to create a Rasa Environment )
>  
>  `activate rasa`(If You not using Optional Step then ***Skip*** this Step)
>  
>  `pip install rasa-x --extra-index-url https://pypi.rasa.com/simple` (For Installing RASA)

## :new: To Create a new Chatbot in RASA

>   `rasa init` (It will create a Chatbot with default Dataset)
	
## :rocket: To run CIS RASA BOT(Windows 10 OS)
Use rasa train to train a model (this will take a significant amount of memory to train,
	if you want to train it faster, try the training command with --augmentation 0).
	Then, to run, 
* **Setup 1** your action server in one terminal window:
	
>  `rasa run actions -vv`(To run Custom-Actions)

* **Setup 2** In second terminal window:

>  `rasa shall`(It will run command line based chatbot)
>  
> `rasa train`(It will train your model)
> 
> `rasa x`(It will run GUI for interactive learning and for debugging Flow of Rasa Chatbot)
>
>  `rasa x --endpoints endpoints.yml`(It will run your bot with backend database)
>
> `rasa run -m models --enable-api --cors "*" ` (If are Using your own ***custom website*** then use this command to run backend server and your bot. )

* **Setup 3** Open [repo](https://gitlab.com/internshiptasks/cis-rasa-bot.git) directory :

>  `index.html`(Open as Chrome Browser)

## 👷 Installation(Windows 10 OS + Anaconda Environment)

To install CIS RASA BOT, please clone the [repo](https://gitlab.com/internshiptasks/cis-rasa-bot.git) and run:
>  Open Anaconda Prompt(Anaconda 3)
>
>  `cd cis-rasa-bot` (Going [repo](https://gitlab.com/internshiptasks/cis-rasa-bot.git) directory)
>  
>  `conda install python=3.6` (Installing Python 3.6.10)
>
>  `conda create -n rasa python=3.6` (Optional: If you don't want to create a Rasa Environment )
>
>  `conda activate rasa` (If You not using Optional Step then ***Skip*** this Step)
>  
>  `pip install rasa-x --extra-index-url https://pypi.rasa.com/simple` (For Installing RASA)

	
## :rocket: To run CIS RASA BOT(Windows 10 OS + Anaconda Environment)
Use rasa train to train a model (this will take a significant amount of memory to train,
	if you want to train it faster, try the training command with --augmentation 0).
	Then, to run, 
* **Setup 1** your action server in one terminal window:
	
>  `rasa run actions -vv`(To run Custom-Actions)

* **Setup 2** In second terminal window:

>  `rasa shall`(It will run command line based chatbot)
>  
> `rasa train`(It will train your model)
> 
> `rasa x`(It will run GUI for interactive learning and for debugging Flow of Rasa Chatbot)
>
>  `rasa x --endpoints endpoints.yml`(It will run your bot with backend database)
>
> `rasa run -m models --enable-api --cors "*" ` (If are Using your own ***custom website*** then use this command to run backend server and your bot. )

* **Setup 3** Open [repo](https://gitlab.com/internshiptasks/cis-rasa-bot.git) directory :

>  `index.html`(Open as Chrome Browser)	
## 💻 Overview of the files Structure 

> 1.  data/stories.md - contains stories
> 2.  data/nlu.md - contains NLU training data
> 3.  actions.py - contains custom action/api code
> 4.  domain.yml - the domain file, including bot response templates
> 5.  config.yml - training configurations for the NLU pipeline and policy ensemble
> 6.  index.html - this html for run web chatbot	
> 7.  _init_.py -  It is An empty file that helps python to find your actions.
>
> Detailed File Structure [View](https://docs.google.com/document/d/16dvFlcgwkbhUp1D2SHC8B3vRUhmgqVk6HCYfGbpTYSM/edit?usp=sharing)


## :link: Links
> Career Interest Survey using RASA BOT Port form  [CareerPaths](https://thecareerlabs.net/cta)
>
> More About [RASA](https://rasa.com/)
>
>Project Report [Link](https://docs.google.com/document/d/16dvFlcgwkbhUp1D2SHC8B3vRUhmgqVk6HCYfGbpTYSM/edit?usp=sharing)
