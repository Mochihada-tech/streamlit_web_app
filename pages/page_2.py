import streamlit as st

with st.form(key='profile_form'): 
        
    # textbox
    name = st.text_input('NAME')
    address = st.text_input('ADDRESS')

    # selectbox
    age_category = st.radio(
        'age',
        ('child(under 18y old)', 'adalt(over 18y old)')
    )
    
    # multiselect
    hobby = st.multiselect(
        'your hobby',
        ('sports','read book','watch movie','music','study','purchase')
    )

    # button
    submit_btn = st.form_submit_button('send')
    cancel_btn = st.form_submit_button('cancel')

    if submit_btn:
        st.text(f'Welcome! Mr.{name}! I send mails {address}!')
        st.text(f'your age category is...{age_category}!')
        st.text(f'your hobby is {", ".join(hobby)}')
