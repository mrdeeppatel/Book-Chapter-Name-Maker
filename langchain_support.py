import os
from langchain_groq import ChatGroq
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain_core.prompts import PromptTemplate

'''
1 - Creating AT model

2 - Making templet(PromptTemplate) for chapter name
3 - Making a object form LLMChain using chapter name templet

4 - Making templet(PromptTemplate) for chapter paragraph 
5 - Making a object from LLMChain using paragraph templet

6 - Creating a Simple Sequential chains (SimpleSequentialChain) using both chain object created above
'''
# 1 - Creating AT model
os.environ['GROQ_API_KEY'] = 'YOUR API'
model = ChatGroq(model='llama3-8b-8192')


def get_paagraph_content(book_name):
    # 2 - Making templet(PromptTemplate) for chapter name
    book_name_templet = PromptTemplate(
        input_variables=['book_name'],
        template='I am Writing a book named {book_name}.Give me 3 suggestion for my first chapter_name. return just 3 names for chapter one not else'
    )

    # 3 - Making a object form LLMChain using chapter name templet
    book_name_LLMChain = LLMChain(llm=model, prompt=book_name_templet)

    # 4 - Making templet(PromptTemplate) for chapter paragraph
    content_patagraph_chapter_one_template = PromptTemplate(
        input_variables=['chapter_name'],
        template='give one small paragraph for each {chapter_name}.'
    )

    # 5 - Making a object from LLMChain using paragraph templet

    content_patagraph_chapter_one_LLMChain = LLMChain(
        llm=model,
        prompt=content_patagraph_chapter_one_template
    )

    final_chain = SimpleSequentialChain(chains=[book_name_LLMChain, content_patagraph_chapter_one_LLMChain],
                                        verbose=True)

    result = final_chain.invoke(book_name)

    return result

# if __name__=="__main__":
#     get_paagraph_content('A great day')jkm


