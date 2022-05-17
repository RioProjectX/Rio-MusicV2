from Yukki import BOT_USERNAME, LOG_GROUP_ID, app
from Yukki.Database import blacklisted_chats, is_gbanned_user, is_on_off


def checker(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "Anda adalah __Admin Anonim__ di Grup Obrolan ini!\nKembali ke Akun Pengguna Dari Hak Admin."
            )
        blacklisted_chats_list = await blacklisted_chats()
        if message.chat.id in blacklisted_chats_list:
            await message.reply_text(
                f"**Group Daftar Hitam**\n\nGroup Anda telah dimasukkan dalam daftar hitam oleh Pengguna Sudo. Minta __SUDO USER__ untuk masuk daftar putih.\nPeriksa Daftar Pengguna Sudo [Dari Sini](https://t.me/{BOT_USERNAME}?start=sudolist)"
            )
            return await app.leave_chat(message.chat.id)
        if await is_on_off(1):
            if int(message.chat.id) != int(LOG_GROUP_ID):
                return await message.reply_text(
                    f"Bot sedang dalam Pemeliharaan. Maaf untuk ketidaknyamanannya!"
                )
        if await is_gbanned_user(message.from_user.id):
            return await message.reply_text(
                f"**Pengguna yang Diblokir**\n\nAnda dilarang menggunakan Bot. Tanyakan __SUDO USER__ apa pun ke ungban.\nPeriksa Daftar Pengguna Sudo [Dari Sini](https://t.me/{BOT_USERNAME}?start=sudolist)"
            )
        return await mystic(_, message)

    return wrapper


def checkerCB(mystic):
    async def wrapper(_, CallbackQuery):
        blacklisted_chats_list = await blacklisted_chats()
        if CallbackQuery.message.chat.id in blacklisted_chats_list:
            return await CallbackQuery.answer(
                "Obrolan Daftar Hitam", show_alert=True
            )
        if await is_on_off(1):
            if int(CallbackQuery.message.chat.id) != int(LOG_GROUP_ID):
                return await CallbackQuery.answer(
                    "Bot sedang dalam Pemeliharaan. Maaf untuk ketidaknyamanannya!",
                    show_alert=True,
                )
        if await is_gbanned_user(CallbackQuery.from_user.id):
            return await CallbackQuery.answer(
                "Anda di-Gbanned", show_alert=True
            )
        return await mystic(_, CallbackQuery)

    return wrapper
