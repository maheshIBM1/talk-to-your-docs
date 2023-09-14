exp_query = 'Generate top 5 questions that I can ask about this data. Questions should be very precise and short, ideally less than 10 words.'

waitText_initialize = 'Preparing the documents, please wait...'

initialize_prompt = 'Write a short welcome message to the user. Describe the data with a comprehensive overview including short summary.\
 If this data is about a person, mention his name instead of using pronouns. After describing the overview, you should mention top 3 example questions that the user can ask about this data.\
 \n\nYour response should be short and precise. Format of your response should be Summary:\n{Description and Summary} \n\n Example Questions:\n{Example Questions}'

nustian_exps = ['Tell me about NUSTIAN',
                'Who is the NUSTIAN regional lead for Silicon Valley?',
                'Tell me details about NUSTIAN coaching program.',
                'How can we donate to NUSTIAN fundraiser?',
                'Who is the president of NUSTIAN?',
                "What are top five missions of NUSTIAN?",
            ]

stdlQs_rb_info = 'Standalone question is a new rephrased question generated based on your original question and chat history'

stdlQs_rb_choices =  ['Retrieve relavant docs using original question, send original question to LLM (Chat history not considered)'\
                    , 'Retrieve relavant docs using standalone question, send original question to LLM'\
                    , 'Retrieve relavant docs using standalone question, send standalone question to LLM']



model_dd_info = 'You can also input any OpenAI model name, compatible with /v1/completions or /v1/chat/completions endpoint. Details: https://platform.openai.com/docs/models/'

model_dd_choices = ['gpt-3.5-turbo', 'gpt-3.5-turbo-16k', 'gpt-4', 'text-davinci-003 (Legacy)', 'text-curie-001 (Legacy)', 'babbage-002']

url_tb_info = 'Upto 100 domain webpages will be crawled for each URL. You can also enter online PDF files.'

url_tb_ph = 'https://example.com, https://another.com, https://anyremotedocument.pdf'


md_title_general = """
    ## Chat with your documents and websites<br>
    Step 1) Enter your OpenAI API Key, and click Submit.<br>
    Step 2) Upload your documents and/or enter URLs, then click Load Data.<br>
    Step 3) Once data is loaded, click Initialize Chatbot (at the bottom of the page) to start talking to your data.<br>

    Your documents should be semantically similar (covering related topics or having the similar meaning) in order to get the best results.
    You may also play around with Advanced Settings, like changing the model name and parameters.
    """

md_title_nustian = """
    ## Chat with NUSTIAN website<br>
    Step 1) Submit your OpenAI API Key.<br>
    Step 2) Click Initialize Chatbot to start sending messages.<br>

    You may also play around with Advanced Settings, like changing the model name and parameters.
    """

md_title_arslan = """
    ## Talk to Arslan<br>
    Welcome to Arslan Ahmed's Chatbot!<br>
    This is LLM-based question-answer application built using Retrieval Augmented Generation (RAG) approach with Langchain, implementing Generative AI technology.\
    He has developed this application to help people get quick answers on frequently asked questions and topics, rather than waiting for his personal reply.\
    Currently, this chatbot is trained on Arslan's resume and LinkedIn profile, with plans to incorporate additional data in the future.<br><br>
    By default, this chatbot is powered by OpenAI's Large Language Model gpt-3.5-turbo. For those interested to explore, there are options under Advanced Settings to change the model and its parameters.
    """


welcomeMsgArslan = """Summary: The document provides a comprehensive overview of Arslan Ahmed\'s professional background and expertise as a data scientist.\
 It highlights his experience in various industries and his proficiency in a wide range of data analysis tools and techniques.\
 The document also mentions his involvement in research projects, publications, and academic achievements.\
\n\nExample Questions:
1. What are some of the key projects that Arslan has worked on as a data scientist?
2. What tools and technologies did Arslan Ahmed utilize in his data science work at IBM?
3. Tell me about Arslan's educational background.
"""


class TtydMode():
    def __init__(self, name='', title='', type='', dir=None, files=[], urls=[], vis=False, welMsg='', def_k=4):
        self.name = name
        self.title = title # markdown title for the top display
        self.type = type # userInputDocs, fixedDocs, personalBot
        self.inputDir=dir
        self.file_list=files
        self.url_list=urls
        self.uiAddDataVis = vis # load data from user - this will be true for type = userInputDocs
        self.welcomeMsg = welMsg #welcome msg constant - if not provided LLM will generate it
        self.k = def_k # default k docs to retrieve



mode_general = TtydMode(name='general', title=md_title_general, type='userInputDocs', vis=True)
mode_nustian = TtydMode(name='nustian', title=md_title_nustian, type='fixedDocs', urls=['https://nustian.ca'])
mode_arslan = TtydMode(name='arslan', title=md_title_arslan, type='personalBot', dir='./documents/', welMsg=welcomeMsgArslan, def_k=8)