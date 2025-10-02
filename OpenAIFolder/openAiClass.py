## Importando a biblioteca da API e a biblioteca DotEnv ##
import openai
import dotenv
import os

## Loading .env ##
dotenv.load_dotenv()

## Chave da API ##
openAiApiKey = os.getenv('OPENAI_KEY')

## Criando a classe para facilitar a criação de respostas ##
class OpenAiClass():

    ## Método construtor da classe #
    def __init__(self):

        ## Criando um objeto próprio da classe da openai ##
        self.openAi = openai.OpenAI(api_key=openAiApiKey)

    ## Criando um método para fazer o plano de estudos ##
    def makeStudyPlan(self, info):
        return self.openAi.responses.create(model='gpt-4', input=f'Me faça um plano de estudos, isto é, oque preciso saber e os links, para vídeos e páginas web, para estudar e ter o conhecimento necessário para fazer esta atividade: {info}.', instructions='Language: pt-br. Text: Dont write any bold words on the response').output_text
