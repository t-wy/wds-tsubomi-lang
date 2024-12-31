# wds-tsubomi-lang
ワールドダイスター — 蕾語データベース<br>
World Dai Star — Tsubomi Language Database

## Missing Screenshots
- サイドストーリー ★4【デンキウィズザ……！？】猫足蕾
- サイドストーリー ★4【追想の帰路】猫足蕾

## Structure (構造)
### Index (索引)
- data.csv
- data.json
- data.js
- checklist.csv
  - Include all known episodes with tsubomi
    - checked:
      - already checked 蕾語があるかどうか調べました
      - can double-check if you wish
    - missing_images:
      - missing screenshots right now
      - would be grateful if anyone can provide so
      - 求：スクリーンショット
#### Data Fields
- phrase (用語)
- pronunciation (読み方)
  - only used if the pronunciations are different from the typical ones
    - leave it blank if the phrase is pronounced as-is, but is delivering some special meaning.
      - include so in the "meaning" field
  - leave it blank if you know it sounds unfamiliar, but cannot identify the words
  - can be in hiragana (当て字) or katakana (loan words・外来語)
  - include "・" only if there are official furigana (振り仮名) having appeared in text form
    - except established prefixes like (「ザ・」＝the)
  - 外来語の表記のゆれ
    - 「バ」行 vs 「ヴァ」行？
      - currently using the 「ヴ」 one if the corresponding word contains a "v"
        - to use this database in quizzes, consider normalizing 「ヴァ、ヴィ、(略)」to the corresponding 「バ、ビ、(略)」to treat both as correct
      - not sure if Tsubomi makes distinction between these two consonants
        - tell me if you are familiar with the difference between these two and know whether Tsubomi differentiate so.
    - Trailing "ー" (語尾の「ー」)
      - Sometimes both variants are used in texts (e.g. Computer (コンピューター vs コンピュータ))
      - The way to differentiate so from speech is to notice how the vowels sound like (long vs short) and count the mora（モーラ） of the ending sound
      - to use this database in quizzes, we recommend ignoring the trailing ー when doing comparisons, or even filter the 「ー」 out.
        - if the question is shown with number of characters like 〇〇〇〇 style, it is recommended to just show the trailing "ー" in the text (e.g. 〇〇〇〇〇〇ー) 
- english (英語)
  - if the wordings come from an English phrase but written in katakana
  - not english translation (英訳ではない)
    - follow the katakana form as possible (including the shortened forms)
  - also reserved for alternative romanization from the orilang if English speakers may transliterate the term different to the one native speakers use.
- orilang (原語)
  - corresponding words in the source language
  - if the wordings come from other languages than English (e.g. Latin), or mixed languages
  - if the language does not mainly use latin script (e.g. Chinese), use **romanized form native speakers mainly use** (e.g. pinyin), and state the original script in the "notes" field
    - If English speakers may recognize a different romanized form, put such form in the "english" field.
- screenshot (スクリーンショット)
  - the original image containing the phrase
- highlight (ハイライト)
  - the screenshot, but with all furigana (振り仮名) removed, and with the phrase colored in red.
- meaning (意味)
  - if there are announced official meaning
  - (e.g. 漆黒の刻（ダーク・クロノス）＝夜)
- source (出典)
  - the place the screenshot is captured (e.g. スポットストーリー 歌川高等学校 猫足蕾、鳳ここな 「ふむ……なるほど。」)
- speaker (発言者)
  - 蕾 (default (デフォルト))
  - Others (e.g. 知冴)
    - May filter those out if one want to have pure 蕾語 list
- hasruby (公式ルビー)
  - 0：あり
  - 1：なし
- notes (ノート)
  - extra information regarding the word / URL(s)
### Images (画像)
- img/
### Scripts (スクリプト)
- scripts/
- csv_to_json.py, json_to_csv.py
  - convert between csv and json to sync both versions
- checker.py
  - check whether the data are synced, and whether provided image paths exists
- roll.py
  - a sample script to pick a random entry without biases towards duplicate entries

## Additional Information (補足)
- Only those with pronunciations different from the typical ones are included with pronunciations.
  - i.e. Leave the pronunciation field blank if those Chūnibyō-style phrases with words are pronounced as-is.
- Include the meaning in the meaning field if it is officially announced.
  - Remember to include the source.
- Not intended for copyright infringement.
  - Refer to [『ワールドダイスター 夢のステラリウム』関連二次創作・ゲーム実況配信及び動画投稿に関するガイドライン](https://world-dai-star.com/news/1947)
    - ※「投稿または配信NG」に関する補足
    - 感想、及び感想に動画やスクリーンショットを添付しての投稿であれば問題ございませんが、<ins>ゲームをプレイしなくてもネタバレ行為に該当するものは問題が生じます</ins>ので、ご注意ください。
  - By principle, contents in the 「投稿または配信NG」 category are restricted to a single screenshot per phrase in order not to spoil the contents.
- Project (プロジェクト): ©Sirius/Project WDS
- Game (ゲームアプリ): ©Sirius/Project WDS Developed and Published by KMS,inc.

## Tags (タグ)
`#ワーダイ` `#ユメステ` `#wds` `#yumesute`<br>
`#蕾語でGO` (?)
