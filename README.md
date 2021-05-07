# heroku_practice

#### ローカルの内容を最新にするgitコマンド
```git pull origin main```

#### ブランチを作成するgitコマンド
```git checkout -b "ブランチ名"```

#### PRをあげるgitコマンド
```git status```

```git add .``` （ファイルを追加した場合）

```git commit -am "コメント"```

```git push origin "作成したブランチ名"```

#### herokuにpushするgitコマンド
```git push origin main```

#### 新たにツールをインストールしたらPipfile.lockを更新する
```pipenv install requests --pre```
