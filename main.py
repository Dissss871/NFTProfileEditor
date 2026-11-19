from typing import Any, List

from base_plugin import BasePlugin
from ui.settings import Header, Text

__id__ = "nft_profile_editor"
__name__ = "NFT Profile Editor"
__description__ = "Локальная NFT-коллекция профиля"
__author__ = "Dissss871"
__version__ = "0.1.0"
__icon__ = "msg_gift"
__app_version__ = ">=12.5.1"
__sdk_version__ = ">=1.4.4.3"


class NFTProfileEditor(BasePlugin):

    def on_plugin_load(self):
        self.logger.info("NFT Profile Editor loaded")

    def create_settings(self) -> List[Any]:
        return [
            Header(text="NFT Profile Editor"),
            Text(
                text="Моя NFT-коллекция",
                subtext="Здесь будет каталог существующих подарков",
                icon="msg_gift",
            ),
            Text(
                text="Локальный режим",
                subtext="Коллекция отображается только на этом устройстве",
                icon="msg_info",
            ),
        ]
