import streamlit as st
from APIClient import APIClient

client = APIClient()

st.set_page_config(layout='wide')

with st.sidebar:
    st.markdown('# Janela de contexto')
    st.markdown('## Adicione a base')
    
    with st.form(key='my_form'):
        id_input = st.text_area(label='Id', value='Insira um id unico para o contexto')
        text_input = st.text_area(label='Adicionar contexto', value='Adicione os contextos a base de dados')
        submit_context = st.form_submit_button(label='submit')
        
        if submit_context:
            try:
                text_inputs = {'query_id': id_input, 'text': text_input}
                response = client.post([text_inputs])
                st.success("Context added successfully!")
            except Exception as e:
                st.error(f"Error adding context: {e}")
        
        st.markdown('---')
        st.markdown('## Procure na base de dados')
    
    with st.form(key='get_context'):
        get_text = st.text_area(label='Procurar contexto', value='Procure na base')
        get_n_responses = st.number_input('Insira quantas respostas deseja', value = 1)
        get_context = st.form_submit_button(label='submit')
        
        if get_context:
            try:
                get_texts = {'query': get_text, 'n_results':get_n_responses}
                context_response = client.get(get_texts)
                st.text(context_response)
            except Exception as e:
                st.error(f"Error retrieving context: {e}")

with st.form('create_background'):
    st.markdown('## Escolha o background para o modelo')
    background_input = st.text_area(label = 'Background', value = 'Escolha um background para o modelo')

    submit_bg = st.form_submit_button(label = 'submit')

if submit_bg:
    client.post_background(background = {'bg': background_input})

st.markdown('# Janela de resposta')
column1, column2 = st.columns(2)

with st.form('get_response'):
    with column1:
        st.markdown('## Pergunta passada para a llm')
        llm_input = st.text_area(label='Pergunta', value='Insira sua pergunta aqui')   

    with column2:
        st.markdown('## Insira aqui a quantidade de contextos necessarios')
        n_contexts = st.number_input(label='Quantidade', value=1)
    
    submit = st.form_submit_button(label = 'submit')

if submit:
    try:
        question = {'question': llm_input}
        llm_response = client.get_llm_response(question)
        st.text(llm_response)
    except Exception as e:
        st.error(f"Error getting LLM response: {e}")