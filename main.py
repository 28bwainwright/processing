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


t1, t2, t3, t4 = st.tabs(['Diagram', 'Overview', 'How to Use', 'Verses'])

with t1:
    st.image('Processing Emotions.drawio.png')


with t2:
    
    st.markdown("""# What is this?  
                
This diagram is designed to help you identify your current circumstances and emotions, 
so that you can hopefully find connections to past stories and experiences that might be driving you towards unwanted sexual behavior.
The aim of this diagram and app is to provide you a shovel to dig up and uncover things from the past that, 
whether you knew it or not, continue to drive your unwanted sexual behavior today. 

Our past contains both good and bad memories, which have shaped us into the man or woman we currently are. 
But ignored or hidden pain from the past has a nasty way of influencing how we respond to circumstances/emotions in the present. 
By engaging the past, with love and truth and in the context of community, one can begin to heal past wounds that we have spent much of our
lives either trying to run and hide from or working to reverse the narrative that was written long ago. When past wounds are brought to the light healing begins to take place. 
         
God is adament about redemption. He created you fearfully and wonderfully. He created you perfectly. You do not need to be changed. 
You need to be redeemed back to the person that God created you to be. Sin, in your life, your family's and this world, has marred and twisted the image
of God that you were supposed to reflect to the world with your life. 

But Jesus died so that the punishment you deserved for not reflecting God's image to the world
was put on Him, not on you. And He was raised to prove that His sacrifice on your behalf was accepted and that new life is possible. 

Whatever your past you can be free from it by the blood of Christ. If you haven't put your faith in His work on the cross and trust Him to redeem you for the rest of your days.

*For by one sacrifice He has made perfect forever those who are being made holy. Hebrews 10:14*
                """)
        
      
with t3: 

    st.markdown("""# To use this follow these steps:   
                
1. Answer each of the following questions below    
    - What are your current circumstances?
    - What are your current emotions?
    - When have you experienced either similar circumstances or emotions?
    - What stories come to mind?
    - What did you do in the past?
    - What stories/verses from the Bible come to mind when you think of your stories?
    
    """)
    st.write('')   
        
    st.markdown("""
    2. Pray after answering all of the questions
        
    - *Remember the gospel*
        - God is Holy
        - We have sinned
        - Jesus died and was raised
        - What is your response?

    - *Remember about prayer*
        - God hears your prayers
        - It doesn't have to be pretty just honest
        - God knows your story and your brokeness
            """)
    
    st.write('')    
    
    st.markdown("""                     
    3. Connect with a friend 
        - Share a story you just remembered
        - Share what truth came to mind
        - Invite them to engage their story too
        - Are there other steps you need to take?
                
                """)


with t4:
    st.markdown('# For each step here are some verses')
    
    
    tc1, tc2 = st.columns(2)
    
    with tc1:
        st.markdown("""
            Old Response: 
            - Romans 7
            - Luke 6:43-45

            Circumstances:
            - 1 Corinthians 6:18
            - 1 Peter 2:11
            - Ephesians 5:3 
            - Titus 2:11

            Emotions:
            - Most Psalms
            - 1 John 3:19-24
            - 1 Corinthians 10:13
            
            Old Story:
            - 1 Peter 1:18-19
            - Romans 8
            - Luke 6:20-26
            - Mark 8
            - Genesis 3-5
            
            """)
        
        
    with tc2:
        st.markdown("""
            

            Gospel:
            - John 3
            - 2 Corithians 5:17
            - John 1:5 
            - John 1:14
            - Romans 6
            - 2 Corithians 5:21

            New Story:
            - 1 John 3:1-3
            - John 4
            - Romans 12
            - Ephesians 2:8-10

            New Response:
            - 1 John 1:9
            - Romans 12:1-2
            - Hebrews 11:6
            - John 10:10
            - Peter 4:7
                                    """)
    
    
        
def view_answer(x, sess):
    
    if x:
        if x in sess:
            pass
        else:
            sess.append(x)
    
    
    sess_len = len(sess)
    
    
    c1, c2 = st.columns(2)
    
    
    for i in range(sess_len):
        if i < 10:
            if i % 2 == 0:
                with c1:
                    sess[i]
                
            else:
                with c2:
                    sess[i]
        else:
            st.warning('Too many values to display')
        

with st.expander('Questions'):
    with st.form('Questions to Answer', clear_on_submit=True, border=True):
        x1 = st.text_input('What are your current circumstances?', None)
        
        view_answer(x1, st.session_state.circumstances)
                
        x2 = st.text_input('What are your current emotions?', '')
        
        view_answer(x2, st.session_state.emotions)
        
        x3 = st.text_input('When have you experienced either similar circumstances or emotions?', '')
        
        view_answer(x3, st.session_state.past_experience)

        x4 = st.text_input('What stories come to mind?', '')
        
        view_answer(x4, st.session_state.past_stories)

        x5 = st.text_input('What did you do in the past?', '')

        view_answer(x5, st.session_state.past_actions)

        x6 = st.text_input("What stories or verses from the Bible come to mind when you think of those stories?", '')

        view_answer(x6, st.session_state.truth)
        
        


        st.form_submit_button(use_container_width=True)

    
        
        
    
with st.expander('Pray'):
    
   
    st.markdown("""# Talk to God about what you just walked through
                
Look back through what you just wrote and bring those stories and verses and everything in between to God.

- Ask Him to heal what is broken from the past. 

- Ask Him to redeem your past that you may bring Him glory by boasting in your weaknesses.
""")

    st.divider()
    st.divider()
    st.markdown("""

    *"This is how we know that we belong to the truth and how we set our hearts at rest in his presence: 
    If our hearts condemn us, we know that God is greater than our hearts, and he knows everything. 
    Dear friends, if our hearts do not condemn us, we have confidence before God 
    and receive from him anything we ask, because we keep his commands and do what pleases him. 
    And this is his command: to believe in the name of his Son, Jesus Christ, and 
    to love one another as he commanded us. The one who keeps Gods commands lives 
    in him, and he in them. And this is how we know that he lives in us: We know it by the 
    Spirit he gave us."* 1 John 3:19-24               """)
        
    
