import os
import warnings

from langchain_community.llms import OpenAI
from keys.key import open_ai_key
from langchain.prompts import PromptTemplate
import re

warnings.filterwarnings('ignore')

os.environ['OPENAI_API_KEY'] = open_ai_key


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


prev_chat = []


def get_fun(inp):
  result = ''''''
  if len(prev_chat)<9:
    for i in range(len(prev_chat)):
      result+=prev_chat[i]['chat']
    result+=inp
  else:
    for i in range(len(prev_chat)-9,len(prev_chat)):
      result+=prev_chat[i]['chat']
    result+=inp
  return result
    
    
if __name__ == '__main__':
  print("Hii ! I am you assistance how can i help you ?")
  while True:
    inp = input("You : ")
    if(inp=='exit'):
      break
    inp = f'''Human : {inp}'''
    final_inp = get_fun(inp)
    # print(final_inp)
    response = chat_bot(final_inp)
    response=response.strip()

    res = {
      "chat" : f'''{inp}
{response}
      '''
    }
    prev_chat.append(res)

    
    print(f'''{response.split(":")[1].strip()}
    ''',end='\n')
    
