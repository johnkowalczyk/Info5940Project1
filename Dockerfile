FROM public.ecr.aws/docker/library/python:3.11-slim-bookworm as base

RUN apt-get update \
    && apt-get install -y \
        curl \
        git \
        unzip \
        vim \
        wget \
        gcc \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean 

RUN pip install --no-cache "poetry>1.7,<1.8" 
RUN poetry config virtualenvs.create false

WORKDIR /code

COPY ./pyproject.toml ./poetry.lock* ./

RUN poetry install --no-dev --no-interaction --no-ansi --no-root -vv \
    && rm -rf /root/.cache/pypoetry

FROM base as devcontainer

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-$(uname -m).zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install --update \
    && echo 'complete -C '/usr/local/bin/aws_completer' aws' >> ~/.bashrc \
    && rm -rf awscliv2.zip ./aws

RUN poetry install --all-extras --no-interaction --no-ansi --no-root -vv \
    && rm -rf /root/.cache/pypoetry

WORKDIR /workspace

EXPOSE 8501

CMD ["streamlit", "run", "/workspace/rag_chatbot.py", "--server.address=0.0.0.0"]
