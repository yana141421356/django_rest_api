FROM python:3.12

# 作業ディレクトリの設定
WORKDIR /app

# 必要なパッケージのコピーとインストール
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコピー
COPY . /app/

# ポートの公開
EXPOSE 8000

# サーバーの起動コマンド
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

