"""DSM 6 datas."""
from .const_7_api_auth import (
    DSM_7_AUTH_LOGIN,
    DSM_7_AUTH_LOGIN_2SA,
    DSM_7_AUTH_LOGIN_2SA_OTP,
)
from .const_7_api_info import DSM_7_API_INFO
from .core.const_7_core_external_usb import (
    DSM_7_CORE_EXTERNAL_USB_DS1821_PLUS_EXTERNAL_USB,
)
from .core.const_7_core_upgrade import DSM_7_CORE_UPGRADE_FALSE, DSM_7_CORE_UPGRADE_TRUE
from .dsm.const_7_dsm_info import DSM_7_DSM_INFORMATION
from .photos.const_7_photo import (
    DSM_7_FOTO_ALBUMS,
    DSM_7_FOTO_ITEMS,
    DSM_7_FOTO_ITEMS_SEARCHED,
    DSM_7_FOTO_SHARED_ITEMS,
)
from .videos.const_7_video import (
    DSM_7_VIDEO_MOVIES,
    DSM_7_VIDEO_TVSHOW,
    DSM_7_VIDEO_TVSHOW_EPISODES,
    DSM_7_VIDEO_DEVICES,
)

__all__ = [
    "DSM_7_AUTH_LOGIN",
    "DSM_7_AUTH_LOGIN_2SA",
    "DSM_7_AUTH_LOGIN_2SA_OTP",
    "DSM_7_API_INFO",
    "DSM_7_CORE_EXTERNAL_USB_DS1821_PLUS_EXTERNAL_USB",
    "DSM_7_CORE_UPGRADE_FALSE",
    "DSM_7_CORE_UPGRADE_TRUE",
    "DSM_7_DSM_INFORMATION",
    "DSM_7_FOTO_ALBUMS",
    "DSM_7_FOTO_ITEMS",
    "DSM_7_FOTO_ITEMS_SEARCHED",
    "DSM_7_FOTO_SHARED_ITEMS",
    "DSM_7_VIDEO_MOVIES",
    "DSM_7_VIDEO_TVSHOW",
    "DSM_7_VIDEO_TVSHOW_EPISODES",
    "DSM_7_VIDEO_DEVICES",
]
