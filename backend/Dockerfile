#ベースイメージの決定
FROM python:3.9.0

# 環境変数 PYTHONUNBUFFEREDを設定
ENV PYTHONUNBUFFERED 1

# ローカルのrequirements.txtをコンテナにコピー
COPY ./backend/requirements.txt /requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8000