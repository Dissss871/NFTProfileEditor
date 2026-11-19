from typing import Any, Dict, List

from base_plugin import BasePlugin, MenuItemData, MenuItemType
from ui.settings import Header, Text
from ui.bulletin import BulletinHelper
__id__ = "nft_profile_editor"
__name__ = "NFT Profile Editor"
__description__ = "Локальная NFT-коллекция профиля"
__author__ = "Dissss871"
__version__ = "0.2.2"
__icon__ = "msg_gift"
__app_version__ = ">=12.5.1"
__sdk_version__ = ">=1.4.4.3"
__category__ = ["tools"]


class NFTProfileEditor(BasePlugin):

    def on_plugin_load(self):
        self.profile_item_id = self.add_menu_item(
            MenuItemData(
                menu_type=MenuItemType.PROFILE_ACTION_MENU,
                text="NFT Profile Editor",
                on_click=self.open_profile_editor,
                icon="msg_gift",
                subtext="Локальная NFT-коллекция",
            )
        )
        self.logger.info("NFT Profile Editor loaded")

    def open_profile_editor(self, context: Dict[str, Any]):
    self.logger.info("NFT Profile Editor: click received")

    try:
        BulletinHelper.show_info(
            "Кнопка NFT Profile Editor работает!"
        )
    except Exception:
        self.logger.exception(
            "Failed to show NFT Profile Editor bulletin"
        )
    )
        )

    def create_settings(self) -> List[Any]:
        return [
            Header(text="NFT Profile Editor"),
            Text(
                text="Моя NFT-коллекция",
                subtext="Выбор существующих подарков появится здесь",
                icon="msg_gift",
            ),
            Text(
                text="Локальный режим",
                subtext="Изменения не отправляются на сервер Telegram",
                icon="msg_info",
            ),
        ]
