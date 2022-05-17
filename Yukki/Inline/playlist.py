from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def check_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"playlist_check {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"playlist_check {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Tutup Menu", callback_data="close")],
    ]
    return buttons


def playlist_markup(user_name, user_id, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Tutup Menu", callback_data="close")],
    ]
    return buttons


def play_genre_playlist(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Metal",
                callback_data=f"play_playlist {user_id}|{type}|Metal",
            ),
            InlineKeyboardButton(
                text=f"Remix",
                callback_data=f"play_playlist {user_id}|{type}|Remix",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Pop",
                callback_data=f"play_playlist {user_id}|{type}|Pop",
            ),
            InlineKeyboardButton(
                text=f"Lofi",
                callback_data=f"play_playlist {user_id}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Sad",
                callback_data=f"play_playlist {user_id}|{type}|Sad",
            ),
            InlineKeyboardButton(
                text=f"Poppunk",
                callback_data=f"play_playlist {user_id}|{type}|Poppunk",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Hiphop",
                callback_data=f"play_playlist {user_id}|{type}|Hiphop",
            ),
            InlineKeyboardButton(
                text=f"Lainnya",
                callback_data=f"play_playlist {user_id}|{type}|Lainnya",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Go Back",
                callback_data=f"main_playlist {videoid}|{type}|{user_id}",
            ),
            InlineKeyboardButton(text="🗑 Tutup", callback_data="close"),
        ],
    ]
    return buttons


def add_genre_markup(user_id, type, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"✚ Poppunk",
                callback_data=f"add_playlist {videoid}|{type}|Poppunk",
            ),
            InlineKeyboardButton(
                text=f"✚ Sad",
                callback_data=f"add_playlist {videoid}|{type}|Sad",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ Pop",
                callback_data=f"add_playlist {videoid}|{type}|Pop",
            ),
            InlineKeyboardButton(
                text=f"✚ Lofi",
                callback_data=f"add_playlist {videoid}|{type}|Lofi",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ Metal",
                callback_data=f"add_playlist {videoid}|{type}|Metal",
            ),
            InlineKeyboardButton(
                text=f"✚ Remix",
                callback_data=f"add_playlist {videoid}|{type}|Remix",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"✚ Hiphop",
                callback_data=f"add_playlist {videoid}|{type}|Hiphop",
            ),
            InlineKeyboardButton(
                text=f"✚ Lainnya",
                callback_data=f"add_playlist {videoid}|{type}|Lainnya",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ Go Back", callback_data=f"goback {videoid}|{user_id}"
            ),
            InlineKeyboardButton(text="🗑 Tutup Menu", callback_data="close"),
        ],
    ]
    return buttons


def check_genre_markup(type, videoid, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Poppunk", callback_data=f"check_playlist {type}|Poppunk"
            ),
            InlineKeyboardButton(
                text=f"Sad", callback_data=f"check_playlist {type}|Sad"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Pop", callback_data=f"check_playlist {type}|Pop"
            ),
            InlineKeyboardButton(
                text=f"Lofi", callback_data=f"check_playlist {type}|Lofi"
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Metal",
                callback_data=f"check_playlist {type}|Metal",
            ),
            InlineKeyboardButton(
                text=f"Remix",
                callback_data=f"check_playlist {type}|Remix",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"Hiphop",
                callback_data=f"check_playlist {type}|Hiphop",
            ),
            InlineKeyboardButton(
                text=f"Lainnya", callback_data=f"check_playlist {type}|Lainnya"
            ),
        ],
        [InlineKeyboardButton(text="🗑 Tutup", callback_data="close")],
    ]
    return buttons


def third_playlist_markup(user_name, user_id, third_name, userid, videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Group's Playlist",
                callback_data=f"show_genre {user_id}|Group|{videoid}",
            ),
            InlineKeyboardButton(
                text=f"{user_name[:8]}'s Playlist",
                callback_data=f"show_genre {user_id}|Personal|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{third_name[:16]}'s Playlist",
                callback_data=f"show_genre {userid}|third|{videoid}",
            ),
        ],
        [InlineKeyboardButton(text="🗑 Tutup", callback_data="close")],
    ]
    return buttons


def paste_queue_markup(url):
    buttons = [
        [
            InlineKeyboardButton(text="▶️", callback_data=f"resumecb"),
            InlineKeyboardButton(text="⏸️", callback_data=f"pausecb"),
            InlineKeyboardButton(text="⏭️", callback_data=f"skipcb"),
            InlineKeyboardButton(text="⏹️", callback_data=f"stopcb"),
        ],
        [InlineKeyboardButton(text="Periksa Daftar Putar Antrian", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Tutup", callback_data=f"close")],
    ]
    return buttons


def fetch_playlist(user_name, type, genre, user_id, url):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Play {user_name[:10]}'s {genre} Playlist",
                callback_data=f"play_playlist {user_id}|{type}|{genre}",
            ),
        ],
        [InlineKeyboardButton(text="Periksa Daftar Putar Antrian", url=f"{url}")],
        [InlineKeyboardButton(text="🗑 Tutup", callback_data=f"close")],
    ]
    return buttons


def delete_playlist_markuup(type, genre):
    buttons = [
        [
            InlineKeyboardButton(
                text=f"Ya! Hapus",
                callback_data=f"delete_playlist {type}|{genre}",
            ),
            InlineKeyboardButton(text="Tidak!", callback_data=f"close"),
        ],
    ]
    return buttons
