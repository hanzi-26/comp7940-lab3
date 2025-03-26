FROM python
WORKDIR /comp7940-lab3
COPY . /comp7940-lab3

RUN pip install update
RUN pip install -r requirements.txt

#ENV TLG_ACCESS_TOKEN=7793512749:AAGaOvF1iT2J6GfB_8oFArW8IjsgyGapyAs
#ENV BASICURL = https://genai.hkbu.edu.hk/general/rest
#ENV MODELNAME = gpt-4-o-mini
#ENV APIVERSION = 2024-05-01-preview
#ENV GPT_ACCESS_TOKEN=0f6ba6fa-d977-46a8-8c6e-38156ebfc422


CMD python chatbox.py
