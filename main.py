import os
import warnings

from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate

warnings.filterwarnings('ignore')

os.environ['OPENAI_API_KEY'] = os.environ['open_ai_key']


def chat_bot(input):
  llm = OpenAI(temperature=0.6)
  prompt_template = PromptTemplate(
    input_variables=["input"],
    template='''
        {input}
    '''
    
  )
  
  answer = llm(prompt_template.format(input=input))
  return answer


if __name__ == '__main__':
  print("Hii ! I am you assistance how can i help you ?")
  while True:
    inp = input("You : ")
    if(inp=='exit'):
      break
    response = chat_bot(inp)
    print(f'''
AI : {response}
    ''',end='\n')
    
