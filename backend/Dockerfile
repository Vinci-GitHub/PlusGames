#ベースイメージの決定
FROM python:3.9.0

WORKDIR /app

# 環境変数 PYTHONUNBUFFEREDを設定
ENV PYTHONUNBUFFERED 1

# ローカルのrequirements.txtをコンテナにコピー
COPY requirements.txt /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./ /app/

CMD ["bash"]

EXPOSE 8000