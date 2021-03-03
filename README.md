# AozoraBunko Extractor

青空文庫のテキストデータをShift-JISからUTF-8へと変換し、ルビやその他の記号を削除、元ファイルごとに二重改行で区切った単一のテキストファイルを生成します。


## Download data

200MB程度のzipファイルがダウンロードされます。通信環境にご留意ください。


```bash
curl -OL https://github.com/aozorahack/aozorabunko_text/archive/master.zip
unzip master.zip
```


## Run with poetry


```bash
poetry install
poetry run aozorabunko-extractor --input_dir aozorabunko_text-master --output_dir out --break_sentence --min_chars 3
```

## Run with local python

```
pip install konoha argparse
python src/aozorabunko_extractor/cli.py --input_dir aozorabunko_text-master --output_dir out --break_sentence --min_chars 3
```

## Options

```
-i, --input_dir aozorabunko_text-master # 入力データが存在するディレクトリを指定、指定ディレクトリ以下の.txtファイルを全て対象にします
-o, --output_dir out # 抽出したテキストを出力するディレクトリを指定
--break_sentence # フラグを有効にすると、文を「。」を基準に改行区切り
--min_chars 3 # 一行の最小文字数を指定
--num_process 8 # 最大並列実行プロセス数を指定
```