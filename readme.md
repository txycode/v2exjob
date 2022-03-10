## 目标

抓去v2ex**酷工作**节点的所有历史数据，分析薪资、城市变化情况
`https://github.com/txycode/v2exjob/tree/master/src`

<!-- more -->

## 方案

### 爬虫部分

* *获取酷工作节点的topic详细信息*

```json
/api/topics/show.json?id=<topic_id>
```

```json
//https://v2ex.com/api/topics/show.json?id=835064
[
    {
        "node": {
        "avatar_large": "https://cdn.v2ex.com/navatar/17e6/2166/43_large.png?m=1643602244",
        "name": "jobs",
        "avatar_normal": "https://cdn.v2ex.com/navatar/17e6/2166/43_normal.png?m=1643602244",
        "title": "酷工作",
        "url": "https://www.v2ex.com/go/jobs",
        "topics": 50793,
        "footer": "",
        "header": "做有趣的有意义的事情。",
        "title_alternative": "Jobs",
        "avatar_mini": "https://cdn.v2ex.com/navatar/17e6/2166/43_mini.png?m=1643602244",
        "stars": 5030,
        "aliases": [],
        "root": false,
        "id": 43,
        "parent_node_name": "work"
        },
    "member": {
        "id": 380499,
        "username": "xianshenglu",
        "url": "https://www.v2ex.com/u/xianshenglu",
        "website": null,
        "twitter": null,
        "psn": null,
        "github": null,
        "btc": null,
        "location": null,
        "tagline": null,
        "bio": null,
        "avatar_mini": "https://cdn.v2ex.com/gravatar/d907dddd8d1cec985c69c00862aa89f6?s=24&d=retro",
        "avatar_normal": "https://cdn.v2ex.com/gravatar/d907dddd8d1cec985c69c00862aa89f6?s=48&d=retro",
        "avatar_large": "https://cdn.v2ex.com/gravatar/d907dddd8d1cec985c69c00862aa89f6?s=73&d=retro",
        "created": 1548596504,
        "last_modified": 1548596504
    },
    "last_reply_by": "",
    "last_touched": 1645250424,
    "title": "[上海][不加班][外企]招 后端、测试、C++\\C#、前端、devOps ，找我内推，帮忙内推，成功送 5000 内推费！",
    "url": "https://www.v2ex.com/t/835064",
    "created": 1645264884,
    "deleted": 0,
    "content": "**一定要找我内推！才有奖金！**\r\n\r\n**一定要找我内推！才有奖金！**\r\n\r\n**一定要找我内推！才有奖金！**\r\n\r\n\r\n查看招聘岗位和详情，戳\r\n\r\n[BOSS 链接]( https://www.zhipin.com/gongsir/626d5f8079a0f7be1nJ40ti4GFc~.html?ka=company-jobs)\r\n\r\n[拉钩链接]( https://m.lagou.com/wn/gongsi/316515.html)\r\n\r\n看到符合的岗位，请联系我内推: 微信搜 18221508921",
    "content_rendered": "<p><strong>一定要找我内推！才有奖金！</strong></p>\n<p><strong>一定要找我内推！才有奖金！</strong></p>\n<p><strong>一定要找我内推！才有奖金！</strong></p>\n<p>查看招聘岗位和详情，戳</p>\n<p><a href=\"https://www.zhipin.com/gongsir/626d5f8079a0f7be1nJ40ti4GFc%7E.html?ka=company-jobs\" rel=\"nofollow\">BOSS 链接</a></p>\n<p><a href=\"https://m.lagou.com/wn/gongsi/316515.html\" rel=\"nofollow\">拉钩链接</a></p>\n<p>看到符合的岗位，请联系我内推: 微信搜 18221508921</p>\n",
    "last_modified": 1645264884,
    "replies": 0,
    "id": 835064
    }
]
```

* *获取酷工作节点的所有topic*

```html
<div class="cell from_571756 t_835327">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/john2245"><img src="https://cdn.v2ex.com/avatar/5207/29ca/571756_xlarge.png?m=1645407768" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="john2245" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/835327#reply0" class="topic-link">OCBC HACK-IT China - OCBC Wing Hang is hiring full-stack developers!</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/john2245">john2245</a></strong> &nbsp;•&nbsp; <span title="2022-02-21 10:31:34 +08:00">38 分钟前</span></span>
</td>
<td width="70" align="right" valign="middle">
</td>
</tr>
</table>
</div>
<div class="cell from_18380 t_805195">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/yuanyiz"><img src="https://cdn.v2ex.com/avatar/12a7/b657/18380_large.png?m=1641262860" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="yuanyiz" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/805195#reply117" class="topic-link">「墨刀秋招」「郑州」前后端岗位全面开放（高级/校招），拿一线薪资，享二线生活「25-50k」</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/yuanyiz">yuanyiz</a></strong> &nbsp;•&nbsp; <span title="2022-02-21 08:58:09 +08:00">2 小时 11 分钟前</span> &nbsp;•&nbsp; 最后回复来自 <strong><a href="/member/yuanyiz">yuanyiz</a></strong></span>
</td>
<td width="70" align="right" valign="middle">
<a href="/t/805195#reply117" class="count_livid">117</a>
</td>
</tr>
</table>
</div>
<div class="cell from_84014 t_835140">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/tonychenc"><img src="https://cdn.v2ex.com/avatar/916d/8160/84014_large.png?m=1645321051" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="tonychenc" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/835140#reply4" class="topic-link">[全职远程] 招聘 React 前端工程师</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/tonychenc">tonychenc</a></strong> &nbsp;•&nbsp; <span title="2022-02-21 08:57:46 +08:00">2 小时 11 分钟前</span> &nbsp;•&nbsp; 最后回复来自 <strong><a href="/member/Originalee">Originalee</a></strong></span>
</td>
<td width="70" align="right" valign="middle">
<a href="/t/835140#reply4" class="count_livid">4</a>
</td>
</tr>
</table>
</div>
<div class="cell from_330389 t_835171">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/SSSYYOO"><img src="https://cdn.v2ex.com/avatar/7d5d/2590/330389_large.png?m=1567476127" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="SSSYYOO" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/835171#reply0" class="topic-link">[北京-移动出海游戏公司] [社招] [2022 春招] -Unity 游戏开发工程师/高级工程师/主程</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/SSSYYOO">SSSYYOO</a></strong> &nbsp;•&nbsp; <span title="2022-02-20 11:55:04 +08:00">23 小时 14 分钟前</span></span>
</td>
<td width="70" align="right" valign="middle">
</td>
</tr>
</table>
</div>
<div class="cell from_549709 t_834699">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/Banzhang"><img src="https://cdn.v2ex.com/avatar/4d7a/a77c/549709_xlarge.png?m=1639965413" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="Banzhang" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/834699#reply68" class="topic-link">[日本东京][CTW]招开发/运维/产品，团队持续扩大中；新办公室已经租好，就缺你了。</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/Banzhang">Banzhang</a></strong> &nbsp;•&nbsp; <span title="2022-02-21 10:18:17 +08:00">51 分钟前</span> &nbsp;•&nbsp; 最后回复来自 <strong><a href="/member/Banzhang">Banzhang</a></strong></span>
</td>
<td width="70" align="right" valign="middle">
<a href="/t/834699#reply68" class="count_livid">68</a>
</td>
</tr>
</table>
</div>
<div class="cell from_460950 t_834901">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/YadongZhang"><img src="https://cdn.v2ex.com/avatar/f71e/defc/460950_large.png?m=1645185047" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="YadongZhang" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/834901#reply16" class="topic-link">开源项目 远程 Vue2 + TS 全职/兼职</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/YadongZhang">YadongZhang</a></strong> &nbsp;•&nbsp; <span title="2022-02-20 18:20:12 +08:00">16 小时 49 分钟前</span> &nbsp;•&nbsp; 最后回复来自 <strong><a href="/member/kunkunzhang">kunkunzhang</a></strong></span>
</td>
<td width="70" align="right" valign="middle">
<a href="/t/834901#reply16" class="count_livid">16</a>
</td>
</tr>
</table>
</div>
<div class="cell from_490617 t_835088">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/zzzzming"><img src="https://cdn.v2ex.com/avatar/cb16/659e/490617_xlarge.png?m=1644491737" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="zzzzming" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/835088#reply0" class="topic-link">[北上广深杭] 网易员工内推，非 hr 非猎头~</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/zzzzming">zzzzming</a></strong> &nbsp;•&nbsp; <span title="2022-02-19 21:18:01 +08:00">1 天前</span></span>
</td>
<td width="70" align="right" valign="middle">
</td>
</tr>
</table>
</div>
<div style="border-bottom: 1px solid var(--box-border-color);">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5060390720525238" crossorigin="anonymous"></script>
<ins class="adsbygoogle" style="display: block; height: 72px;" data-ad-format="fluid" data-ad-layout-key="-hs-19-p-2z+is" data-ad-client="ca-pub-5060390720525238" data-ad-slot="1009394990"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div>
<div class="cell from_469593 t_832674">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/v2lhr"><img src="https://cdn.v2ex.com/avatar/f94c/5d9c/469593_large.png?m=1643183082" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="v2lhr" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/832674#reply58" class="topic-link">[广州/深圳]新年央企内推，职位多多，福利多多，七险二金！</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/v2lhr">v2lhr</a></strong> &nbsp;•&nbsp; <span title="2022-02-21 09:39:29 +08:00">1 小时 30 分钟前</span> &nbsp;•&nbsp; 最后回复来自 <strong><a href="/member/v2lhr">v2lhr</a></strong></span>
</td>
<td width="70" align="right" valign="middle">
<a href="/t/832674#reply58" class="count_livid">58</a>
</td>
</tr>
</table>
</div>
<div class="cell from_565054 t_835069">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/travelWorld"><img src="https://cdn.v2ex.com/gravatar/b8a3a238684c890fdb773ac041f0d7ea?s=48&d=retro" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="travelWorld" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/835069#reply0" class="topic-link">[北京][成都] 字节跳动抖音团队 持续招聘 ing</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/travelWorld">travelWorld</a></strong> &nbsp;•&nbsp; <span title="2022-02-19 18:38:55 +08:00">1 天前</span></span>
</td>
<td width="70" align="right" valign="middle">
</td>
</tr>
</table>
</div>
<div class="cell from_427745 t_835026">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/v5excom"><img src="https://cdn.v2ex.com/gravatar/1fd26f01880e0728c3af72bc054c56c4?s=48&d=retro" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="v5excom" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/835026#reply6" class="topic-link">[北京][社招] AWS 中国区 招聘信息更新</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/v5excom">v5excom</a></strong> &nbsp;•&nbsp; <span title="2022-02-20 12:17:15 +08:00">22 小时 52 分钟前</span> &nbsp;•&nbsp; 最后回复来自 <strong><a href="/member/b1ackjack">b1ackjack</a></strong></span>
</td>
<td width="70" align="right" valign="middle">
<a href="/t/835026#reply6" class="count_livid">6</a>
</td>
</tr>
</table>
</div>
<div class="cell from_510562 t_835016">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/allengui"><img src="https://cdn.v2ex.com/gravatar/cb07c8aee2e234b24fddb9d3de78a8b0?s=48&d=retro" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="allengui" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/835016#reply10" class="topic-link">[广州][硅谷大厂] Salesforce 后端开发/产品经理招聘</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/allengui">allengui</a></strong> &nbsp;•&nbsp; <span title="2022-02-20 14:39:47 +08:00">20 小时 29 分钟前</span> &nbsp;•&nbsp; 最后回复来自 <strong><a href="/member/allengui">allengui</a></strong></span>
</td>
<td width="70" align="right" valign="middle">
<a href="/t/835016#reply10" class="count_livid">10</a>
</td>
</tr>
</table>
</div>
<div class="cell from_557316 t_835050">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/shiivanscut"><img src="https://cdn.v2ex.com/gravatar/e9c63541010e76777462b9780101caf6?s=48&d=retro" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="shiivanscut" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/835050#reply0" class="topic-link">[深圳][Amber Group] 前端开发工程师 20k-50k·18 薪</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/shiivanscut">shiivanscut</a></strong> &nbsp;•&nbsp; <span title="2022-02-19 16:09:58 +08:00">1 天前</span></span>
</td>
<td width="70" align="right" valign="middle">
</td>
</tr>
</table>
</div>
<div class="cell from_380499 t_835064">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/xianshenglu"><img src="https://cdn.v2ex.com/gravatar/d907dddd8d1cec985c69c00862aa89f6?s=48&d=retro" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="xianshenglu" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/835064#reply0" class="topic-link">[上海][不加班][外企]招 后端、测试、C++\C#、前端、devOps ，找我内推，帮忙内推，成功送 5000 内推费！</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/xianshenglu">xianshenglu</a></strong> &nbsp;•&nbsp; <span title="2022-02-19 18:01:24 +08:00">1 天前</span></span>
</td>
<td width="70" align="right" valign="middle">
</td>
</tr>
</table>
</div>
<div class="cell from_482911 t_835012">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/huihuiy"><img src="https://cdn.v2ex.com/avatar/d451/04af/482911_large.png?m=1588769727" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="huihuiy" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/835012#reply0" class="topic-link">[深圳][非远程] Python 开发工程师 [30-60w] AI 公司</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/huihuiy">huihuiy</a></strong> &nbsp;•&nbsp; <span title="2022-02-19 13:32:26 +08:00">1 天前</span></span>
</td>
<td width="70" align="right" valign="middle">
</td>
</tr>
</table>
</div>
<div class="cell from_551648 t_835165">
<table cellpadding="0" cellspacing="0" border="0" width="100%">
<tr>
<td width="48" valign="top" align="center"><a href="/member/realizers"><img src="https://cdn.v2ex.com/gravatar/0b64389dd6469e024472d5f3b2c6be29?s=48&d=retro" class="avatar" border="0" align="default" width="48" style="width: 48px; max-height: 48px;" alt="realizers" /></a></td>
<td width="10"></td>
<td width="auto" valign="middle"><span class="item_title"><a href="/t/835165#reply0" class="topic-link">虾皮内推，内推码 NTAG0Ii
或者私聊看岗位
shopee ， 深圳、上海、北京都有岗位。</a></span>
<div class="sep5"></div>
<span class="topic_info"><strong><a href="/member/realizers">realizers</a></strong> &nbsp;•&nbsp; <span title="2022-02-20 11:28:14 +08:00">23 小时 41 分钟前</span></span>
</td>
<td width="70" align="right" valign="middle">
</td>
</tr>
</table>
</div>
```

* *结构化储存json到mongodb*

```json
{
    "id": "文档id",
    "create_time": "linux时间戳",
    "create_datetime": "gmt时间",
    "title": "topic的标题",
    "contents": "渲染后的内容",
    "replies": "主题回复人数",
    "clicks": "主题点击次数 (可选)"
}
```

* *注意事项*

1. v2ex api限速120次/小时。
2. html 解析 `<a href="/t/835140#reply4" class="topic-link">` topic_id 部分。
3. content_rendered需要去掉html标签，方便分词。
4. click需要 `https://v2ex.com/t/826021#reply37` 页面抓取。

```html
<small class="gray"><a href="/member/yuanyiz">yuanyiz</a> · <span title="2022-01-04 10:39:21 +08:00">48 天前</span> · 8984 次点击 &nbsp; </small>
```


### 分词部分

* *离线BERT中文分词*

```python
import torch
from transformers import BertTokenizer
from IPython.display import clear_output

# 指定繁简中文 BERT-BASE预训练模型
PRETRAINED_MODEL_NAME = "bert-base-chinese"  
# 获取预测模型所使用的tokenizer
tokenizer = BertTokenizer.from_pretrained(PRETRAINED_MODEL_NAME)
text = "[CLS] 他移开这[MASK]桌子，就看到他的手表了。"
tokens = tokenizer.tokenize(text)
ids = tokenizer.convert_tokens_to_ids(tokens)
 
print(text)
print(tokens[:10], '...')
print(ids[:10], '...')
```

1. 通过google BERT预训练模型分词mongodb文档中的title、content。
2. 统计token的个数与文档id的关系数据存入mongodb

```json
//token count
{
    "北京": 100,
    "25k": 124,
    "上海": 23
}
{
    "id": "文档id",
    "include": {
        "xxx": 1,
        "yyy": 2
    }
}

```

### 数据透视部分

* *NUMPY, PANDAS, MATLIBPLOT*

* *待续*

