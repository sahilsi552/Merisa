from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import *
from random import choice
from .. import QuantamBot

START = f""" <b>
๏ ʜᴇʏ, ɪ ᴀᴍ <a href="https://t.me/{QuantamBot.username}"> {QuantamBot.name} </a> ᴍᴏsᴛ ᴄᴏᴍᴘʟᴇᴛᴇ Bᴏᴛ ᴛᴏ ʜᴇʟᴘ ʏᴏᴜ ᴡɪᴛʜ ᴀ Lᴏᴛ ᴏғ Tᴏᴏʟs, Aᴅᴅ ᴍᴇ ɪɴ ᴀ Gʀᴏᴜᴘ, ᴘʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs Aᴅᴍɪɴ, ᴀɴᴅ sᴇᴇ ᴍʏ ᴀᴄᴛɪᴏɴ 🔥!
──────────────────
 ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.

Pᴏᴡᴇʀᴇᴅ Bʏ @Mr_Sukkun  </b>"""
SOURCE_TEXT = f"""<b>
๏ ʜᴇʏ, ɪ ᴀᴍ <a href="https://t.me/{QuantamBot.username}"> {QuantamBot.name} </a>
──────────────────
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ</b>
"""

AI_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /imagine : ɢᴇɴᴇʀᴀᴛᴇ Aɪ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴛᴇxᴛ
➻ /bard : ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ  ʀᴇꜱᴘᴏɴꜱᴇ ꜰʀᴏᴍ  ʙᴀʀᴅ
➻ /chatgpt :ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ  ʀᴇꜱᴘᴏɴꜱᴇ ꜰʀᴏᴍ ᴄʜᴀᴛɢᴘᴛ
➻ /blackbox : ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ  ʀᴇꜱᴘᴏɴꜱᴇ ꜰʀᴏᴍ Bʟᴀᴄᴋʙᴏx
"""
AFK_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /afk : ᴍᴀʀᴋ ʏᴏᴜʀsᴇʟғ ᴀs ᴀғᴋ [ᴀᴡᴀʏ ғʀᴏᴍ ᴋᴇʏʙᴏᴀʀᴅ]
"""

CODE_HELP = f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
ᴛʜɪs ғᴇᴀᴛᴜʀᴇ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ʀᴜɴ ᴍᴜʟᴛɪᴘʟᴇ 
ᴘʀᴏɢʀᴀᴍᴍɪɴɢ ʟᴀɴɢᴜᴀɢᴇs ᴛʜʀᴏᴜɢʜ ᴛʜɪs ʙᴏᴛ .
ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ɪs ᴀ ʟɪsᴛ ᴏғ sᴜᴘᴘᴏʀᴛᴇᴅ ʟᴀɴɢᴜᴀɢᴇs,
ғᴏʀ ᴛᴇᴍᴘᴏʀᴀʀʏ ᴄᴏᴍᴍᴀɴᴅs ᴏɴʟʏ support ᴡɪᴛʜ a 
"!"  ʟɪᴋᴇ ᴛʜᴇ ᴇxᴀᴍᴘʟᴇ ʙᴇʟᴏᴡ.
ʟɪsᴛ ᴏғ sᴜᴘᴘᴏʀᴛᴇᴅ ᴘʀᴏɢʀᴀᴍᴍɪɴɢ ʟᴀɴɢᴜᴀɢᴇs:
~> python
~> c
~> java
~> javascript
~> julia
~> kotlin
~> go
~> assembly
~> ats
~> bash
~> clojure
~> cobol
~> coffeescript
~> cpp
~> crystal
~> csharp
~> d
~> elixir
~> elm
~> erlang
~> fsharp
~> groovy
~> haskell
~> idris
~> lua
~> mercury
~> nim
~> nix
~> ocaml
~> perl
~> php
~> raku
~> ruby
~> rust
~> scala
~> swift
~> typescript
Example:
~>!python print("ᴏᴋ")
"""
# ➻ /codehelp : ɢᴇᴛ ʜᴇʟᴘ ꜰᴏʀ ᴄᴏᴅᴇ ʀᴜɴɴᴇʀ
CARBON_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /carbon :ᴍᴀᴋᴇs ᴄᴀʀʙᴏɴ ɪғ ʀᴇᴩʟɪᴇᴅ ᴛᴏ ᴀ ᴛᴇxᴛ.
➻ /rayso : ᴍᴀᴋᴇ ʀᴀʏsᴏ ᴏғ ɢɪᴠᴇɴ ᴛᴇxᴛ
"""

COUPLES_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /couple  : ɢᴇɴᴇʀᴀᴛᴇ ʀᴀɴᴅᴏᴍ ᴄᴏᴜᴘʟᴇ ғʀᴏᴍ ɢʀᴏᴜᴘ
"""
DOWNLOAD_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
COMING SOON...
"""
ENCYRPT_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /encrypt : ᴇɴᴄʀʏᴘᴛ ᴛᴇxᴛ.
➻ /decrypt : ᴅᴇᴄʀʏᴘᴛ ᴇɴᴄʀʏᴘᴛᴇᴅ ᴛᴇxᴛ"""
ENGLISH_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /spellcheck : ᴡʜɪʟᴇ ʀᴇᴘʟʏɪɴɢ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ, ᴡɪʟʟ ʀᴇᴘʟʏ ᴡɪᴛʜ ᴀ ɢʀᴀᴍᴍᴀʀ ᴄᴏʀʀᴇᴄᴛᴇᴅ ᴠᴇʀsɪᴏɴ

"""
# ➻ /synonyms  <ᴡᴏʀᴅ>: ғɪɴᴅ ᴛʜᴇ sʏɴᴏɴʏᴍs ᴏғ ᴀ ᴡᴏʀᴅ
# ➻ /antonyms  <ᴡᴏʀᴅ>: ғɪɴᴅ ᴛʜᴇ ᴀɴᴛᴏɴʏᴍs ᴏғ ᴀ ᴡᴏʀᴅ
# ➻ /define  <ᴛᴇxᴛ>: ᴛʏᴘᴇ ᴛʜᴇ ᴡᴏʀᴅ ᴏʀ ᴇxᴘʀᴇssɪᴏɴ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴇᴀʀᴄʜ\ɴғᴏʀ ᴇxᴀᴍᴘʟᴇ /ᴅᴇғɪɴᴇ ᴋɪʟʟ

INLINE_HELP=f""" <b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ ᴛᴏ ᴜsᴇ ɪɴʟɪɴᴇ ғᴇᴀᴛᴜʀᴇ, ᴊᴜsᴛ ᴛʏᴘᴇ ʙᴏᴛ ᴜsᴇʀɴᴀᴍᴇ [@{QuantamBot.username}] ᴡɪᴛʜ ғᴏʟʟᴏᴡɪɴɢ ᴀʀɢs ʙᴇʟᴏᴡ."""

INFO_HELP = f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention}
➻ /info : ʀᴇᴘʟʏ ᴛᴏ ᴜꜱᴇʀ ᴏʀ ɢɪᴠᴇ [userid|username] ᴛᴏ ɢᴇᴛ ᴜsᴇʀɪɴғᴏ

➻ /alive : ᴄʜᴇᴄᴋ ᴡʜᴇᴛʜᴇʀ ʙᴏᴛ ɪs ᴀʟɪᴠᴇ ᴏʀ ᴅᴇᴀᴅ
➻ /echo <ᴛᴇxᴛ> :ʀᴇᴘʟʏ ᴛᴏ ᴍsɢ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴍsɢ ᴜsɪɴɢ ʙᴏᴛ.

"""

GAME_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
Pʟᴀʏ Gᴀᴍᴇ Wɪᴛʜ EᴍᴏJɪs:
➻ /dice : - ʀᴏʟʟ Dɪᴄᴇ 🎲
➻ /dart : ʀᴏʟʟ Dᴀʀᴛ 🎯
➻ /basket :ʀᴏʟʟ  Bᴀsᴋᴇᴛ Bᴀʟʟ 🏀
➻ /ball :  ʀᴏʟʟ Bᴏᴡʟɪɴɢ Bᴀʟʟ 🎳
➻ /football : ʀᴏʟʟ Fᴏᴏᴛʙᴀʟʟ ⚽️
➻ /jackpot : Sᴘɪɴ sʟᴏᴛ ᴍᴀᴄʜɪɴᴇ 🎰
"""
KARMA_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
Kᴀʀᴍᴀ: 🌟 A ɴᴜᴍᴇʀɪᴄᴀʟ ʀᴇᴘʀᴇsᴇɴᴛᴀᴛɪᴏɴ ᴏғ ʜᴏᴡ ᴍᴜᴄʜ ᴀ ᴜsᴇʀ ʜᴀs ᴄᴏɴᴛʀɪʙᴜᴛᴇᴅ ᴘᴏsɪᴛɪᴠᴇʟʏ (ᴏʀ ɴᴇɢᴀᴛɪᴠᴇʟʏ) ᴛᴏ ᴀ ᴘʟᴀᴛғᴏʀᴍ ʙᴀsᴇᴅ ᴏɴ ᴛʜᴇɪʀ ᴘᴏsᴛs, ᴄᴏᴍᴍᴇɴᴛs, ᴀɴᴅ ɪɴᴛᴇʀᴀᴄᴛɪᴏɴs.

Uᴘᴠᴏᴛᴇ: (👍 ,+,+1)  A ᴡᴀʏ ғᴏʀ ᴜsᴇʀs ᴛᴏ sʜᴏᴡ ᴀᴘᴘʀᴇᴄɪᴀᴛɪᴏɴ ᴏʀ ᴀɢʀᴇᴇᴍᴇɴᴛ ᴡɪᴛʜ ᴀ ᴘᴏsᴛ ᴏʀ ᴄᴏᴍᴍᴇɴᴛ, ᴄᴏɴᴛʀɪʙᴜᴛɪɴɢ ᴛᴏ ᴛʜᴇ ᴘᴏsᴛᴇʀ's ᴋᴀʀᴍᴀ ʙʏ ɢɪᴠɪɴɢ ᴛʜᴇᴍ ᴀ ᴘᴏsɪᴛɪᴠᴇ ᴠᴏᴛᴇ.

Dᴏᴡɴᴠᴏᴛᴇ: (👎,-,-1 )Tʜᴇ ᴏᴘᴘᴏsɪᴛᴇ ᴏғ ᴀɴ ᴜᴘᴠᴏᴛᴇ, ɪɴᴅɪᴄᴀᴛɪɴɢ ᴅɪsᴀɢʀᴇᴇᴍᴇɴᴛ ᴏʀ ᴅɪsᴀᴘᴘʀᴏᴠᴀʟ ᴡɪᴛʜ ᴀ ᴘᴏsᴛ ᴏʀ ᴄᴏᴍᴍᴇɴᴛ, ᴡʜɪᴄʜ ᴄᴀɴ ʟᴏᴡᴇʀ ᴛʜᴇ ᴘᴏsᴛᴇʀ's ᴋᴀʀᴍᴀ sᴄᴏʀᴇ.

"""

LOGO_HELP = f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention}
➻ /logo : ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴄʀᴇᴀᴛᴇ ʟᴏɢᴏ ʙᴀʙᴇ​ !

</b>
 """
NEWS_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /news : Tᴏᴘ Nᴀᴛɪᴏɴᴀʟ Hᴇᴀᴅʟɪɴᴇs Tᴏᴅᴀʏ & Bʀᴇᴀᴋɪɴɢ Nᴇᴡs - Tʜᴇ Hɪɴᴅᴜ 
"""
QUOTE_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /quote :ᴛᴏ ɢᴇᴛ Rᴀɴᴅᴏᴍ  Qᴜᴏᴛᴇ
"""

RANDOM_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻  /joke :ᴛᴏ ɢᴇᴛ Rᴀɴᴅᴏᴍ Jᴏᴋᴇ 

"""
# ➻ /loveshayri : ʟᴏᴠᴇ ꜱʜᴀʏʀɪ
# ➻ /hateshayri : ʜᴀᴛᴇ ꜱʜᴀʏʀɪ
SHORTNER_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /shorturl : sʜᴏʀᴛᴇɴs ᴛʜᴇ ɢɪᴠᴇɴ ᴜʀʟ.
➻ /unshorturl : ᴜɴsʜᴏʀᴛᴇɴs ᴛʜᴇ ɢɪᴠᴇɴ ᴜʀʟ"""

SUDO_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /eval  :...
➻ /sh  :..."""

STICKER_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /sticker : ᴘʀᴏᴠɪᴅᴇ sᴏᴍᴇ ᴛᴇʀᴍ ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ ᴀ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ.
"""

TOKEN_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /token : ɢᴇɴᴇʀᴀᴛᴇ ʏᴏᴜʀ ᴛᴏᴋᴇɴ
➻ /revoke : ʀᴇᴠᴏᴋᴇ ʏᴏᴜʀ ᴛᴏᴋᴇɴ"""
TRANS_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /tr  /tl (ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇ) ᴀs ʀᴇᴘʟʏ ᴛᴏ ᴀ ʟᴏɴɢ ᴍᴇssᴀɢᴇ
ᴇxᴀᴍᴘʟᴇ: 
➻ /tr en: ᴛʀᴀɴsʟᴀᴛᴇs sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ ᴇɴɢʟɪsʜ
➻ /tr hi-en: ᴛʀᴀɴsʟᴀᴛᴇs ʜɪɴᴅɪ ᴛᴏ ᴇɴɢʟɪsʜ

ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇs
af,am,ar,az,be,bg,bn,bs,ca,ceb,co,cs,cy,da,de,el,en,eo,es,
et,eu,fa,fi,fr,fy,ga,gd,gl,gu,ha,haw,hi,hmn,hr,ht,hu,hy,
id,ig,is,it,iw,ja,jw,ka,kk,km,kn,ko,ku,ky,la,lb,lo,lt,lv,mg,mi,mk,
ml,mn,mr,ms,mt,my,ne,nl,no,ny,pa,pl,ps,pt,ro,ru,sd,si,sk,sl,
sm,sn,so,sq,sr,st,su,sv,sw,ta,te,tg,th,tl,tr,uk,ur,uz,
vi,xh,yi,yo,zh,zh_CN,zh_TW,zu
"""
TRUTH_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
ᴛʀᴜᴛʜ & ᴅᴀʀᴇ
➻ /truth  : sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴛʀᴜᴛʜ sᴛʀɪɴɢ.
➻ /dare  : sᴇɴᴅs ᴀ ʀᴀɴᴅᴏᴍ ᴅᴀʀᴇ sᴛʀɪɴɢ.
"""
TOOLS_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /bininfo <ʙɪɴ> :ғᴇᴛᴄʜ ᴄᴀʀᴅ ɪɴꜰᴏ ғʀᴏᴍ ʙɪɴ.
➻ /detect : ᴅᴇᴛᴇᴄᴛ ᴛᴇxᴛ ғʀᴏᴍ ɪᴍᴀɢᴇ  
➻ /scan :ʀᴇᴘʟʏ ᴛᴏ ǫʀᴄᴏᴅᴇ ᴛᴏ sᴄᴀɴ ɪᴛ
➻ /qrcode : ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ǫʀᴄᴏᴅᴇ.
➻ /unidecode : ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴜɴɪᴅᴇᴄᴏᴅᴇ ɪᴛ.
➻ /livecc <ʙɪɴ> : ɢᴇɴᴇʀᴀᴛᴇ ʟɪᴠᴇ ᴄᴄ .
➻ /github <ᴜsᴇʀɴᴀᴍᴇ> : ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ɢɪᴛʜᴜʙ ᴜsᴇʀ
➻ /fonts <text> : ᴄᴏɴᴠᴇʀᴛs sɪᴍᴩʟᴇ ᴛᴇxᴛ ᴛᴏ ʙᴇᴀᴜᴛɪғᴜʟ ᴛᴇxᴛ ʙʏ ᴄʜᴀɴɢɪɴɢ ɪᴛ's ғᴏɴᴛ.
➻ /lyrics <song name>: ғᴇᴛᴄʜ ʟʏʀɪᴄs ғʀᴏᴍ sᴏɴɢ ɴᴀᴍᴇ ғʀᴏᴍ Jɪᴏsᴀᴠᴀɴ.
➻ /wiki <ᴛᴇxᴛ>:sᴇᴀʀᴄʜs ᴀʙᴏᴜᴛ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴏɴ ᴡɪᴋɪᴘᴇᴅɪᴀ
➻ /wallpaper : ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴡᴀʟʟᴘᴀᴘᴇʀ ʙᴀʙᴇ !
➻ /paste  : ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ ғɪʟᴇ
➻ /country : ᴛᴏ ɢᴇᴛ ᴄᴏᴜɴᴛʀʏ ɪɴғᴏ
➻ /hastag :ɢᴇɴᴇʀᴀᴛᴇ ᴡᴏʀᴅ ᴛᴏ ʜᴀꜱᴛᴀɢ.
➻ /github <ᴜsᴇʀɴᴀᴍᴇ> : ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ɢɪᴛʜᴜʙ ᴜsᴇʀ
➻ /time <ǫᴜᴇʀʏ>: ɢɪᴠᴇs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀ ᴛɪᴍᴇᴢᴏɴᴇ
➻ /fonts <text> : ᴄᴏɴᴠᴇʀᴛs sɪᴍᴩʟᴇ ᴛᴇxᴛ ᴛᴏ ʙᴇᴀᴜᴛɪғᴜʟ ᴛᴇxᴛ ʙʏ ᴄʜᴀɴɢɪɴɢ ɪᴛ's ғᴏɴᴛ.
➻ /weather <ᴄɪᴛʏ>:ɢᴇᴛ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛᴜs ᴏғ ᴡᴇᴀᴛʜᴇʀ
➻ /figlet: ᴍᴀᴋᴇs ғɪɢʟᴇᴛ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ
"""
TELEGRAPH_HELP=f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {QuantamBot.mention} </b>
➻ /tgm : ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴏғ ʀᴇᴘʟɪᴇᴅ ᴍᴇᴅɪᴀ
➻ /tgt : ɢᴇᴛ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴏғ ʀᴇᴘʟɪᴇᴅ ᴛᴇxᴛ
"""


HELP = [
    [
        IKB("Aɪ", callback_data="HELP_AI"),
        IKB("Aғᴋ", callback_data="HELP_AFK"), 
        IKB("Cᴀʀʙᴏɴ", callback_data="HELP_CARBON"),
        
    ],
       [ IKB("Cᴏᴅᴇ Rᴜɴɴᴇʀ", callback_data="HELP_CODE"),
        IKB("Cᴏᴜᴘʟᴇ", callback_data="HELP_COUPLE"),
        IKB("Dᴏᴡɴʟᴏᴀᴅ", callback_data="HELP_DOWNLOAD"),
        
        
    ],
    [
       
        IKB("Eɴᴄʀʏᴘᴛ", callback_data="HELP_ENCRYPT"),
        IKB("Eɴɢʟɪsʜ", callback_data="HELP_ENGLISH"),
        IKB("Gᴀᴍᴇ", callback_data="HELP_GAME"), 
        
    ],
    [
         IKB("ɪɴғᴏ", callback_data="HELP_INFO"),
        IKB("ɪɴʟɪɴᴇ", switch_inline_query_current_chat=""),
        IKB("Kᴀʀᴍᴀ", callback_data="HELP_KARMA"),
        
        
    ],
    [
        IKB("ʟᴏɢᴏ", callback_data="HELP_LOGO"),
        IKB("Nᴇᴡs", callback_data="HELP_NEWS"),
        IKB("Qᴜᴏᴛᴇ", callback_data="HELP_QUOTE"),
        
    ],
    [
       
        IKB("Rᴀɴᴅᴏᴍ", callback_data="HELP_RANDOM"),
        IKB("sʜᴏʀᴛᴇɴᴇʀ", callback_data="HELP_SHORTNER"),
        IKB("Sᴜᴅᴏ", callback_data="HELP_SUDO"),
        
        
        
    ],
    [
        IKB("sᴛɪᴄᴋᴇʀ", callback_data="HELP_STICKER"),
        IKB("ᴛᴇʟᴇɢʀᴀᴘʜ", callback_data="HELP_TELEGRAPH"),
        IKB("ᴛʀᴀɴsʟᴀᴛᴇ", callback_data="HELP_TRANS"),
        
        
    ],
    [
        IKB("Tᴏᴋᴇɴ", callback_data="HELP_TOKEN"),
        IKB("ᴛʀᴜᴛʜ ᴅᴀʀᴇ", callback_data="HELP_TRUTH"),
        IKB("Tᴏᴏʟs", callback_data="HELP_TOOLS"),
        
    ],
     [IKB(" Hᴏᴍᴇ ", callback_data="RETURN")]
]
x = ["❤️", "🎉", "✨", "🪸", " 🎉 ", " 🎈 ", "🎯"]
g = choice(x)


MAIN = [
    [
        IKB(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{QuantamBot.username}?startgroup=true",
        ),
    ],
    [
        IKB(text="ʜᴇʟᴘs", callback_data="HELP"),
    ],
    [
        IKB(text="sᴏᴜʀᴄᴇ ", callback_data="HELP_source"),
        
        IKB(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID),
]
]
IMGX = [
    [
        IKB(text="Dᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID),
        IKB(text="Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_GRP}"),
    ]
]
PNG_BTN = [
    [
        IKB(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{QuantamBot.username}?startgroup=true",
        ),
    ],
    [
        IKB("sᴜᴘᴘᴏʀᴛ",
            url=f"https://t.me/{SUPPORT_GRP}",
        ),
    ],
]


HELP_BACK = [

    [
        IKB("ʙᴀᴄᴋ ", callback_data="HELP_BACK"),
    ],
]
#  force
M =IKM( [
    [IKB(text="ᴄʟᴏsᴇ", callback_data="closeforce")]
])
ADD_ME= [
    [
        IKB(
        "ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{QuantamBot.username}?startgroup=true",
        )
    ]]
VERIFY=  IKM([
    [
        IKB(
        "verify",
            url=f"https://t.me/{QuantamBot.username}?start=true",
        )
    ]])
SOURCE_BUTTONS = IKM(
    [
        [IKB("sᴏᴜʀᴄᴇ", callback_data="HELP_hurr")],
        [
            IKB(" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
            IKB(text="ʙᴀᴄᴋ ", callback_data="RETURN")
        ]
    ]
)


