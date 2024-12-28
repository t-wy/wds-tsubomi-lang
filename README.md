# wds-tsubomi-lang
ワールドダイスター — 蕾語データベース<br>
World Dai Star — Tsubomi Language Database

## Structure (構造)
### Index (索引)
- data.csv
- data.json
#### Data Fields
- phrase (用語)
- pronunciation (読み方)
  - only used if the pronunciations are different from the typical ones
    - leave it blank if it is pronounced as-is, but a delivering some special meaning.
  - can be in hiragana (当て字) or katakana (loan words・外来語)
  - include "・" only if there are official furigana (振り仮名) having appeared in text form
    - except established prefixes like (「ザ・」＝the)
  - 「バ」行 vs 「ヴァ」行？
    - undecided（未定）
    - not sure if Tsubomi makes distinction between these two consonants
      - tell me if you are familiar with the difference between these two and know whether Tsubomi differentiate so.
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
- notes (ノート)
  - extra information regarding the word / URL(s)
### Images (画像)
- img/

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
`#ワーダイ` `#ユメステ` `#wds` `#yumesute`
