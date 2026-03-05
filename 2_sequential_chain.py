#This script will 1st generate a report by itself and then also summarize by itself.
#for this we are using 2 models , one for report and one for summary

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

# To modify the project name , we dont have to go the .env file each time and change it.
# we can modify the environment variable here in the code itself.
os.environ['LANGCHAIN_PROJECT'] = "Sequential_chain_demo"

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model1 = ChatOpenAI(model = "gpt-4o-mini", temperature=0.7)

model2 = ChatOpenAI(model = "gpt-4o", temperature=0.5)

parser = StrOutputParser()

#Here we are creating a chain connecting the output of the 1st model as the input to the 2nd model
#1st model generates a report and 2nd model generates a summary of that report
chain = prompt1 | model1 | parser | prompt2 | model2 | parser

#This is the additional things like tags and metadata wtever we want according to out wish we can add
config={
    'run_name': 'sequential_chain',
    'tags': ['llm app', 'report generation', 'summarization'],
    'metadata': {'model1':'gpt-4o-mini', 'model1_temp': 0.7 , 'parser':'stroutputparser', 'author': 'dragon'}
}

result = chain.invoke({'topic': 'Unemployment in India'}, config=config)

print(result)
