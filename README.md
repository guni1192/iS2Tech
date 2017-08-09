# iS2Tech

技術的知識の蓄積と共有
所謂ナレッジマネジメント用のアプリ

## How to use

- Version: **Python** `>=` *3.6*
- Framework: **Django** `==` *1.11.2*
- DataBase: **PostgreSQL** `>=` *9.4*


1. データベースとユーザーを作成する

  ```bash
  $ createdb platcoders
  $ psql
  ```

  ```postgresql
  CREATE ROLE platcoders with PASSWORD 'platcoders';
  ALTER ROLE platcoders with LOGIN;
  ```

2. 仮想環境を用意する

  ```bash
  $ python -m venv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt
  ```

3. テスト環境の準備

  マイグレーションと管理者ユーザの作成
  ```bash
  $ python manage.py migrate
  $ python manage.py createsuperuser
  ```

  手元で動かしてテストする
  ```bash
  $ python manage.py runserver
  ```

