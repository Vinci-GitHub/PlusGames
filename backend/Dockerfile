#ベースイメージの決定
FROM python:3.9.0

# 環境変数 PYTHONUNBUFFEREDを設定
ENV PYTHONUNBUFFERED 1

#コンテナにbackendディレクトリを作りそこをワークディレクトリとする
RUN mkdir /backend/
WORKDIR backend/

# ローカルのrequirements.txtをコンテナにコピー
COPY requirements.txt /./backend/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


COPY ./ /backend/

