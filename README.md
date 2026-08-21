# WorldMC · 开源存档

<p align="center">
  <img src="WorldMC-ButNot404-Icon.png" width="128" alt="WorldMC-ButNot404 Icon">
</p>

> 一个承载了四代"冒险小镇"血脉的 Minecraft 服务器开源存档。
> 本仓库记录了 WorldMC 系列从起源到落幕的全部配置碎片,供后人考古、学习与延续。
>
> 这个库是 XAY4 时期的 WorldMC,里面的文件为这周期中我认为对服务器比较有用的内容。
> 如果有缺漏可以向我提问,插件详情内容并不会真正开源,至少在我彻底跑路前(
>
> 本仓库还保存了 **WorldMC-ButNot404 一周目至二周目的存档**(2026-02-25):
> 📥 https://github.com/Chaiwai/WorldMC-ButNot404/releases/tag/v1.0-save

---

## 📖 历史沿革

本服务器最初为不知名服主制作的 **「冒险小镇服务器」**,源文件地址:
<https://www.tinksp.com/resources/1-20-1.830/>

按时间顺序:

```
① De404 ──► WorldMC 一周目
            在"冒险小镇服务器"基础上修改创作

② De404 ──► WorldMC 二周目
            使用 NeigeItems 插件改写 MMOItems 中的内容

③ De404 ──► WorldMC 三周目
            完全独立使用 NeigeItems 编写的插件

④ XAY4 ──► WorldMC-ButNot404 一周目
            XAY4 为 WorldMC 一、二、三周目玩家,三周目后服务器长期未开服,
            自行开服;源文件同为"冒险小镇服务器",
            按 De404 所做内容 1:1 复刻

⑤ De404 ──► WorldMC 四周目(00服务器)
            完全独立使用 NeigeItems 编写的插件

⑥ XAY4 ──► WorldMC-ButNot404 二周目
            采用一周目存档 + MMOItems + NeigeItems 插件,
            1:1 复刻 De404 二、四周目内容

⑦ ShuRuMingZi ──► WorldMC-ButNotXAY4
```

之后 **De404 跑路,XAY4 跑路**;XAY4 关服后,**ShuRuMingZi** 开服 **WorldMC-ButNotXAY4**。
WorldMC-ButNot404 应该彻底关服了,未来也许 XAY4 还会开服,但大概率不会以此存档开服——MC 存档的寿命太短了。

*万一还会开服呢?*

---

## 📁 仓库结构

```
kaiyuan/
├── start/                    # 服务器本体
│   ├── purpur-1.21.4-2416.jar    # 服务器核心(1.21.4 / Purpur)
│   └── zzz_sc1.bat               # 启动脚本(自动重启)
├── core/                     # 核心配置(历代开服配置精华)
│   ├── 一周目物品插件/            # MMOItems 配置
│   │   ├── 一周目配置文件/
│   │   └── 二周目配置文件/
│   ├── 二周目物品插件/            # NeigeItems 配置
│   ├── 商店/                      # ShopPro 商店配置
│   ├── 材质包/                    # ItemsAdder 自定义物品/材质配置
│   ├── 菜单/                      # Invero 菜单配置
│   └── 附魔插件/                  # Aiyatsbus / NereusOpus 附魔配置
├── resourcePack/             # 材质包资源
│   ├── 404材质/                   # 四周目材质
│   ├── ItemsAdder/                # ItemsAdder 资源(含打包的 ItemsAdder.rar)
│   ├── MythicMobs/
│   ├── old/                       # 旧版材质
│   └── tr/
├── plugins.txt               # 服务器插件清单(74 个)
├── server.txt                # 服务器环境信息
└── save.txt                  # 世界存档下载(GitHub Release)
```

## 🔧 服务器环境

| 项目     | 内容                                 |
| -------- | ------------------------------------ |
| 游戏版本 | **1.21.4**                           |
| 服务端   | **Purpur**(`purpur-1.21.4-2416.jar`) |
| 代理端   | **Waterfall**                        |
| 插件数量 | 74 个(Paper 5 + Bukkit 69)           |

## 📦 插件列表

**Paper 插件(5)**:EconomyShopGUI · HuskHomes · HuskSync · nightcore · PlugManX

**Bukkit 插件(69)**:Aiyatsbus · ajLeaderboards · AuthMe · Citizens · CMI · CMILib ·
CompanionsPlus · CoreProtect · CtOnlineReward · CustomCrafting · CustomNameplates ·
DecentHolograms · eco · ExcellentCrates · GlobalMarketPlus · HuskHomesGUI ·
Interactions · Invero · ItemEdit · ItemsAdder · ItemSoulBind · Join-Leave · LagFixer ·
LiteBans · LiteSignIn · LoneLibs · LuckPerms · mcMMO · McmmoView · MMOItems ·
ModelEngine · Multiverse-Core · MyPet · MythicLib · MythicMobs · NBTAPI · NeigeItems ·
NereusOpus · NoBuildPlus · NoCheatPlus · packetevents · PlaceholderAPI ·
PlayerCurrency · PlayerGuild · PlayerPoints · PlayerTask · PlayerTitle · PlayerTop ·
PlayerWarp · PlotSquared · ProtocolLib · QuickShop-Hikari · RandomShop · Residence ·
ResidenceEnhance · SetMaxHealth · ShopPro · SkinsRestorer · TAB-Bridge · TrChat ·
Vault · ViaBackwards · ViaRewind · ViaVersion · WolfyUtilities · WorldEdit ·
WorldListTrashCan · XConomy · XMcPay

## 🚀 使用方法

1. 准备 **Java 21** 环境;
2. 将 `start/` 目录作为服务器根目录,放入本体与配置;
3. 下载世界存档(见 [`save.txt`](./save.txt),GitHub Release 分卷);
4. 运行 `zzz_sc1.bat` 启动(内含崩溃自动重启逻辑);
5. 玩家端需加载对应材质包(见 `resourcePack/` 与 `core/材质包/`)。

> ⚠️ 本仓库不含 `plugins/` 完整目录,需根据 `plugins.txt` 自行补齐插件,
> 并将 `core/` 下的配置放入对应插件的配置目录。

## ⚠️ 注意事项

- 部分插件为**付费插件,需购买激活码使用**(如 `NereusOpus`、`Aiyatsbus`),
  请前往作者处购买,并在确认作者允许再分发的前提下使用本仓库内相关内容;
- 世界存档体积较大,通过 GitHub Release 分卷分发(见 [`save.txt`](./save.txt));
- 本仓库仅作学习与纪念用途,请勿用于商业牟利。

## 🙏 致谢

感谢 **冒险小镇服务器** 的原作者、**De404** 与 **XAY4** 为这个世界付出的心血,
也感谢每一位在 WorldMC 世界中留下足迹的玩家。

by DeepSeek-v4-flash

---

## 📬 联系我(XAY4)

📧 **xay1615@163.com**

> 最近太懒了不想开服,以后也许会神归也可能陨落;
> 开服太麻烦了,而且付出成本和回报不成正比;
> 相信 WorldMC 不会消失 :)
>
> 有任何插件 / 存档 / 开服任何问题,发送邮件。
> 也许我会回复。
