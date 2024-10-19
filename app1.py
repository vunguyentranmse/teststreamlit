import streamlit as st

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
def main():
    st.title('Factorial Caculator')
    number = st.number_input("Enter a number :",min_value=0,max_value=900)
    if st.button("Calculate"):
        result=fact(number)
        st.write(f"The factorial at {number} is {result}.")
        st.balloons()

if __name__=="__main__":
        main()
    


#terminal dung lenh streamlit run app1.py

# deploy trên github
# vào trang streamlit
#   + dung acct github dang nhap streamlit
#   + dang nhap github, up project len github, dat ten
#   + vao lai streamlit 

#

