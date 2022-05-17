from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from Yukki import BOT_USERNAME


def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Kualitas Suara", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Volume Suara", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Auth Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="❌ Tutup", callback_data="close"),
        ],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📋 Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Pengaturan", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **Ini Adalah {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📋 Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="👥Support Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Ini Adalah {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📋 Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚡Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **Ini Adalah {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📋 Menu Perintah", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="⚙️ Pengaturan", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚡Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="⚡Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Ini Adalah {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📋 Menu Perintah",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Tambahkan Ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **Ini Adalah {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📋 Menu Perintah",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Tambahkan Ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚡Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Ini Adalah {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📋 Menu Perintah",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Tambahkan Ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚡Channel", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **This is {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="📋 Menu Perintah",
                    callback_data="search_helper_mess",
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Tambahkan Ke Group",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="⚡Channel", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="⚡Group", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **Ini Adalah {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Kualitas Suara", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Volume Suara", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Auth Users", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Dashboard", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Tutup", callback_data="close"),
            InlineKeyboardButton(text="🔙 Kembali", callback_data="okaybhai"),
        ],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Reset Volume Audio 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 Vol Rendah", callback_data="LV"),
            InlineKeyboardButton(text="🔉 Vol Medium", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 Vol Tinggi", callback_data="HV"),
            InlineKeyboardButton(text="🔈 Vol Diperkuat", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 Custom Volume 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 Kembali", callback_data="settingm")],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼Custom Volume 🔼", callback_data="AV")],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Semua", callback_data="EVE"),
            InlineKeyboardButton(text="🤴 Admin", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📖 List Pengguna Auth", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 Kembali", callback_data="settingm")],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} Pengaturan**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ Uptime", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Ram", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 Cpu", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Disk", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 Go back", callback_data="settingm")],
    ]
    return f"⚙️  **{MUSIC_BOT_NAME} Pengaturan**", buttons
