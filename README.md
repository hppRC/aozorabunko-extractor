# AozoraBunko Extractor

青空文庫のテキストデータをShift-JISからUTF-8へと変換し、ルビやその他の記号を削除、元ファイルごとに二重改行で区切った単一のテキストファイルを生成します。


## Download data

200MB程度のzipファイルがダウンロードされます。通信環境にご留意ください。


```bash
curl -OL https://github.com/aozorahack/aozorabunko_text/archive/master.zip
unzip master.zip
```


```bash
poetry install
poetry run aozorabunko-extractor --input_dir aozorabunko_text-master --output_dir out --break_sentence --min_chars 3
```