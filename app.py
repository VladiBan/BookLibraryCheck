import streamlit as st 

books = [
    "the hobbit",
    "Hari potnia",
    "Mythology",
    " 1984"

]

st.title("Vook checer app")
st.write("enter book title to see if it exists in our data base.")
user_input = st.text_input("book title")
if st.button("check book"):
    if user_input.strip() == "":
        st.warning(" please enter book title")
    elif user_input in books:
        st.succsess(" the book exists in our data base ")
    else:
        st.error(" the book does NOT exist in our data base ")

new_book = st.text_input("add book")
if st.button("Add"):
    st.write(new_book)

