# heroku_practice

#### ローカルの内容を最新にするgitコマンド
```git pull origin main```

#### gitコマンド
```git checkout -b "ブランチ名"``` （ブランチを作る）

```git status``` （現在の状態を表示）

```git add .``` （ステージングエリアにあげる）

```git commit -am "コメント"``` （コミットする）

```git push origin "作成したブランチ名"``` （PRを作成する）

#### herokuにpushするgitコマンド
```git push heroku main```

#### blackでpythonコードを自動でフォーマットする
```pipenv run black```

#### flake8でpythonコードのチェック
```pipenv run flake8```

#### 新たにツールをインストールしたらPipfile.lockを更新する
```pipenv install requests --pre```
