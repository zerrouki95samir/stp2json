FROM continuumio/miniconda3

COPY . /app
WORKDIR /app

RUN conda update conda

# Create the environment:
RUN conda create -n cad_env python=3.7

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "cad_env", "/bin/bash", "-c"]

RUN conda install -c dlr-sc pythonocc-core=7.4.0

RUN pip install flask requests  

COPY run.py .

ENTRYPOINT ["conda", "run", "-n", "cad_env", "python", "run.py"]