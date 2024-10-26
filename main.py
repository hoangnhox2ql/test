import streamlit as st
st.title('My project')
st.header('this is header')
st.subheader("this is subheader")
st.divider()
st.text('AIVN')
st.caption("this is a caption")
st.markdown('[AIVN](http://)')
st.markdown("""
    1. Machine learning
    2. Deep learning
""")
st.markdown('$ \sqrt{2x} $')
st.divider()
st.latex('\sqrt{2x}')

st.divider()

st.write('AI VIET NAM')
st.write('# HEADING 1')
st.write('[google](https://google.com)')
st.write(r'$ \sqrt{2x}$')
#st.write('1 + 1 = ',2)

st.divider()
st.code("""
    import random
    value = random.randint(3,10)
    print(value)
""")
def get_year():
    return '2003'

with st.echo():
    st.write('AI VIET NAM')
    def get_name():
        return 'Hoang'
    name = get_name()
    year = get_year()
    st.write(name,year)

st.divider()

st.logo('E:/AIO_VN_2024/AIO_StreamLit/logo.jpg')
st.image('E:/AIO_VN_2024/AIO_StreamLit/logo.jpg', caption='Mercedes')
st.audio('E:/AIO_VN_2024/AIO_StreamLit/messenger.mp3')
st.video('E:/AIO_VN_2024/AIO_StreamLit/Video.mp4')

st.divider()

def get_fullName():
    print('Hoang')

agree = st.checkbox("I agree!",on_change=get_fullName)
if agree:
    st.write("Thanks")

status = st.radio('Your Favorite Color:',['Yellow','Blue'],captions=['vang','xanh'])
print(status)
status = st.selectbox('Your Contact:',['Email','Address'])
print(status)
option = st.multiselect('Color:',['green','yellow','blue'])
print(option)
st.select_slider('Your Colors:',['Red','Yellow','Blue'])

st.divider()

if st.button("Say Hello"):
    st.write('Hello')
else:
    st.write('Goodbye')
value = st.text_input("Your Name:",value='Hoang')
st.write(value)

st.divider()

uploaded_file = st.file_uploader('Chosse Files:',accept_multiple_files= True)
for upload in uploaded_file:
    read_f = upload.read()
    st.write("File Name:", upload.name)

st.divider()

# with st.form('My Form'):
#     col1, col2 = st.columns(2)
#     f_name = col1.text_input("Name:")
#
#     f_age = col2.text_input("Age:")
#
#     submit = st.form_submit_button('Submit')
#     if submit:
#         st.write(f_name)
#         st.write(f_age)

st.divider()

import random
value = random.randint(1,10)
if 'key' not in st.session_state:
    st.session_state['key'] = value 
st.write(st.session_state.key)
