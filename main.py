import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space


st.set_page_config('Emotions', layout='centered')

if 'circumstances' not in st.session_state:
    st.session_state.circumstances = []
if 'emotions' not in st.session_state:
    st.session_state.emotions = []
if 'past_experience' not in st.session_state:
    st.session_state.past_experience = []
if 'past_stories' not in st.session_state:
    st.session_state.past_stories = []
if 'past_actions' not in st.session_state:
    st.session_state.past_actions = []
if 'truth' not in st.session_state:
    st.session_state.truth = []


st.markdown(f"<h1 style='text-align: center; font-size: 30px'>Engaging Your Story</h1>", unsafe_allow_html=True)   
st.write('') 
st.write('Take 5 min to walk through each of the follow questions that correspond to the diagram below. This is designed as a tool to help you dig up stories and events from your past that are still affecting you today.')
st.divider()
add_vertical_space(3)

# with st.expander('Process'):
st.image('Processing Emotions.drawio.png')

with st.expander('Questions to Answer'):
    x1 = st.text_input('What are your current circumstances?')

    if x1:
        st.session_state.circumstances.append(x1)
        for i in st.session_state.circumstances:
            st.write(i)

    add_vertical_space(5)

    x2 = st.text_input('What are your current emotions?')

    if x2:
        st.session_state.emotions.append(x2)
        for i in st.session_state.emotions:
            st.write(i)

    add_vertical_space(5)

    x3 = st.text_input('When have you experienced either similar circumstances or emotions?')

    if x3:
        st.session_state.past_experience.append(x3)
        for i in st.session_state.past_experience:
            st.write(i)

    add_vertical_space(5)

    x4 = st.text_input('What stories come to mind?')

    if x4:
        st.session_state.past_stories.append(x4)
        for i in st.session_state.past_stories:
            st.write(i)

    add_vertical_space(5)


    x5 = st.text_input('What did you do in the past?')

    if x5:
        st.session_state.past_actions.append(x5)
        for i in st.session_state.past_actions:
            st.write(i)

    add_vertical_space(5)


    x6 = st.text_input("Are their stories/verses/passages/or truth about God that resonate with those old stories?")

    if x6:
        st.session_state.truth.append(x6)
        for i in st.session_state.truth:
            st.write(i)

    add_vertical_space(5)
    
    
    
with st.expander('Pray'):
    
    if st.session_state.circumstances and st.session_state.emotions:
        st.markdown(f"Current = {st.session_state.circumstances} * {st.session_state.emotions}")
    else:
        st.markdown("Current = Circumstances * Emotions")
        
        
    if st.session_state.circumstances and st.session_state.emotions and st.session_state.past_stories:
        st.markdown(f"Future = {st.session_state.past_stories} + ({st.session_state.circumstances} * {st.session_state.emotions})")
    else:
        st.markdown("Future = Past + (Circumstances * Emotions)")
    
    
    
if st.button('Reset'):
    
    st.session_state.circumstances.clear()
    st.session_state.emotions.clear()
    st.session_state.past_experience.clear()
    st.session_state.past_stories.clear()
    st.session_state.past_actions.clear()
    st.session_state.truth.clear()
    
    