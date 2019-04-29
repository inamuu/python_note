# ツール名

ツール作るときにtemplatesをコピーして使うと便利そう。

### Setup

.env.sampleをコピーして.envを作り、中身をAWS Credentialsにあわせて修正する。

```sh
cp .env.sample .env
```

### Install

```sh
pip3 install -r requirements.txt
```

### Usage

使い方

```sh
$ python main.py student1
配列: {'name': 'taro', 'age': 20}
名前: taro
年齢: 20
$ python main.py student2
配列: {'name': 'jiro', 'age': 21}
名前: jiro
年齢: 21
$ python main.py student3
配列: {'name': 'saburo', 'age': 17}
名前: saburo
年齢: 17
```
