
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from pydantic import BaseModel
from fastapi import WebSocket

class Temp(BaseModel):
    query : str
    
    
    


class OpenAIService:
    def __init__(self,temp:int) -> None:
        self.llm = OpenAI(temperature=temp)
        self.prev_chat:{str:list[Temp]} = {}
    
    def get_fun(self,inp:str,client_id:str):
        result:str = ''''''
        if len(self.prev_chat[client_id])<9:
            for i in range(len(self.prev_chat[client_id])):
                result += self.prev_chat[client_id][i].query
            result += inp
        else:
            for i in range(len(self.prev_chat[client_id])-9,len(self.prev_chat[client_id])):
                result+=self.prev_chat[client_id][i].query
            result+=inp
        return result

    def get_reponse(self,input:str,client_id:str)->str:
        prompt_template = PromptTemplate(
            input_variables=["input"],
            template='''
                {input}
            '''
        )
        if client_id not in self.prev_chat.keys():
            self.prev_chat[client_id] = []


        inp = f'''Human : {input}'''
        final_inp = self.get_fun(inp,client_id)
        answer:str = self.llm(prompt_template.format(input=final_inp))
        answer:str = answer.strip()
        
        res:Temp = Temp(query=f'''Human : {input}
AI : {answer}
       ''')
        
        self.prev_chat[client_id].append(res)

        return answer
    
    def remove(self,client_id:str):
        
        self.prev_chat.pop(client_id)


