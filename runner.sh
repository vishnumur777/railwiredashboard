#!/bin/bash

python3 extractdataset.py
python3 extractuser.py
streamlit run app.py --server.port=8501 --server.address="0.0.0.0"
