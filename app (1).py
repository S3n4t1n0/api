import streamlit as st
from openai import OpenAI

class Page1:
  def_init_(self):
    #Initialize the OpenAI Client using the API key from secrets.

    from secret_keys import openai_api_key
    self.client = OpenAI(api_key=openai_api_key)

    prompt = """

    Asuma el rol de un asesor de viajes experimentado que se especializa en brindarle experiencias de viajes unicas.
    Tiene un amplio conocimiento sobre varios destinos, ha leido mucho sobre tendencias de viajes y """

    #Using st.session_state to store the exchange of messages.
    if "trip_adviser_messages" not in st.session_state:
      st.session_state["trip_adviser_messages"] = [
          {"role": "system", "content":prompt}
      ]

      #Function for interecting with a chatbot
      def communicate():
