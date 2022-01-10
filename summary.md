<span style="font-size:120%">

### Djangoの概要・ポイント
<hr>

#### ファイル構成
##### Project
- `manage.py` : プロジェクトに関する処理を行うファイル
<br>

- `wsgi.py` : 「web server gateway interface」の略、web serverからの情報をDjangoで受け取れるように情報を加工するプログラムファイル
<br>

- `urls.py` : HTTPリクエストオブジェクトを受け取る処理を行うファイル
    - 第1引数 : URLの指定パス
    - 第2引数 : 第一引数がURLに追記された場合に表示するファイル
    - 第1引数に合致するURLであれば、受け取ったHTTPリクエストオブジェクトを`views.py`に送る
    - Projectディレクトリ内の`urls.py`中のurlpatternsリストに、作成した各アプリのディレクトリ内の`urls.py`を読み込めるようincludeで指定する
<br>

- `views.py`
    - `urls.py`からHTTPリクエストオブジェクトを受け取り、表示するHTMLファイルをTemplatesディレクトリから、表示するデータを`models.py`から取得し、それらをHTTPレスポンスオブジェクトとしてwebサーバに返す
<br>

- `setting.py` : 各種設定
    - BASE_DIR : `manage.py`が置いてあるディレクトリのパス
    - SECRET_KEY : パスワードと共に使用される暗号鍵 (リモートリポジトリに保存する場合や、サービスを公開する際はSECRET_KEYを秘匿できるようにする)
    - DEBUG : 詳細なログを見たい場合はTrue、本番環境ではFalseにした方が安全
    - ALLOWED_HOST : 情報を受け取るサーバーを指定
    - INSTALLED_APPS : Project内のApplicationのリスト
    - MIDDLEWARE : serverとDjangoの中間処理プログラム
    - ROOT_URLCONF : Djangoがリクエストを受け取ったときに、どのディレクトリの`urls.py`を参照するかを指定
    - TEMPLATES : HTMLテンプレートの情報
    - WSGI_APPLICATION : アプリケーションサーバからの情報取得場所
    - AUTH_PASSWORD_VALIDATORS : パスワード検証
    - STATIC_URL : 様々なファイルを読み込むための設定を行うファイルのURL
<br>

##### App
- 
<br>

<hr>

#### Tips
- `python manage.py runserver`でローカルサーバを起動し、/adminにアクセスした際にエラーが生じる場合は、`python manage.py migrate`でデータベース中でテーブルを作成し、管理画面機能を有効化する
<br>

- `view.py`に定義するclassBasedView vs functionBasedView
    - classBasedView : 手軽に記述できるが拡張性は低い
        - TemplateView : django.views.genericファイル内に存在
    - functionBasedView : 1から記述する必要があるが拡張性は高い
<br>

- プロジェクト : 全体管理
- アプリ : 各ホームページ管理
<br>

- makemigrations : `models.py`の変更差分をファイルとして保存
- migrate : `models.py`の内容からデータベース(テーブル)作成
<br>

- CRUDとDjangoの対応 (ClassBasedView)
    - C : CreateView
    - R : ListView(全データのリスト), DetailView(個別データの詳細)
    - U : UpdateView
    - D : DeleteView
<br>

- 

</span>