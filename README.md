# ai_training-task
training task

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>
IMPORTANT NOTE: to run the jupyter code please download the used survey data from :
https://survey.stackoverflow.co/datasets/stack-overflow-developer-survey-2024.zip and unpack it in your workspace.

There should be no necessary python libraries to run the code here beyond the Anaconda distribution of Python.  The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

Given the large progress in AI tools I am interested in better understanding the following questiosn based on Stack Overflow data from 2024 :

1. What are the main AI tools used in the developer community?
2. Which tools do the developers plan to use in the near future?
3. How does the number of tools planned to be used in future correlate with number of tools used,the stance for AI, work experience and the job satisfaction?"
4. What characteristics of an individual developer determine his usage of and view on AI tools?


## File Descriptions <a name="files"></a>

- AnalyseToolsUsedAndPlannedToUse.ipynb : Notebook for answering question 1 and 2 by analysis of survey data, selecting the columns related to the AI tools currently used and intended to use. Generates the diagram shown in the blog post
- AnalyseImpactOfNumberOfToolsUsedAndIntendedToUseOnStanceForAI.ipynb : Notebook for answering question 2 by searching for correlation between number of AI tools planned to used and a subset of developers characteristics like years of work experience, job satisfaction, stance for the use of AI and the current number of tools used (linear regression approach).
- AnalyseThePossibleCharacteristicsForUsingAIAsADeveloper.ipynb : Notebook to answer question 4 by analysing dependecies between the usage of AI and characteristics of developers like practical coding experience, education level, age, employment situation and organizational size (ClassificationTree approach)
- my_functions.py :python function to extract the selected data from a data file 

## Results<a name="results"></a>
The sumary of the findings can be found on https://open.substack.com/pub/gelatti04/p/what-fosters-ai-tools-usage-in-software?r=5sc8w7&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Credits to Stack Overflow for the data from the survey 2024.  Source: Stack Overflow Developer Survey 2024  : Link: https://survey.stackoverflow.co/2024/ 
