
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate

class OpenAIService:
    def __init__(self,temp:int) -> None:
        self.llm = OpenAI(temperature=temp)

    def get_reponse(self,input:str)->str:
        prompt_template = PromptTemplate(
            input_variables=["input"],
            template='''
                {input}
            '''
        )
        
        answer:str = self.llm(prompt_template.format(input=input))
        answer:str = answer.strip()
        return answer


