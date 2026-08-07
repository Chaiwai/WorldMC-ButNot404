function enable() {
  // 监听物品合并事件
  new Listener(Packages.org.bukkit.event.entity.ItemMergeEvent.class)
    .setPriority(EventPriority.LOWEST)
    .setExecutor(function (event) {
      async(function () {
        loadItem(event.getTarget());
      });
    })
    .register();

  // 监听物品生成事件
  new Listener(Packages.org.bukkit.event.entity.ItemSpawnEvent.class)
    .setPriority(EventPriority.LOWEST)
    .setExecutor(function (event) {
      async(function () {
        loadItem(event.getEntity());
      });
    })
    .register();
}

function getItemName(itemStack) {
  // 检测NI物品
  const itemInfo = ItemUtils.isNiItem(itemStack, true);
  if (itemInfo == null) return null;

  // 获取节点信息
  const data = itemInfo.data;

  // 进行节点判断
  if (data == null) return null;
  if (data["虚拟道具数量"] != null) {
    return HookerManager.getParsedName(itemStack);
  }
  return null;
}

function loadItem(item) {
  // 设置物品显示名
  const itemName = getItemName(item.getItemStack());
  if (itemName != null) {
    item.setCustomName(getItemName(item.getItemStack()));
    item.setCustomNameVisible(true);
  }
}
