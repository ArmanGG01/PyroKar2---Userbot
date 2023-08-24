from pyrogram import Client, filters
from pyrogram.types import Message
DEVS = 1694909518
from PyroKar.modules.basic.profile import extract_user
from PyroKar import SUDO_USER
from config import OWNER_ID
from PyroKar.modules.basic.help import add_command_help

ok = []


@Client.on_message(filters.command("sudolist", ".") & filters.me)
async def gbanlist(client: Client, message: Message):
    users = (SUDO_USER)
    ex = await message.edit_text("`Processing...`")
    if not users:
        return await ex.edit("No Users have been set yet")
    gban_list = "**Sudo Users:**\n"
    for count, i in enumerate(users, start=1):
        gban_list += f"**{count} -** `{i}`\n"
    return await ex.edit(gban_list)


@Client.on_message(filters.command("addsudo", ".") & filters.user(OWNER_ID))
async def gmute_user(client: Client, message: Message):
    args = await extract_user(message)
    reply = message.reply_to_message
    ex = await message.edit_text("`Processing...`")
    if args:
        try:
            user = await client.get_users(args)
        except Exception:
            await ex.edit("`Please specify a valid user!`")
            return
    elif reply:
        user_id = reply.from_user.id
        user = await client.get_users(user_id)
    else:
        await ex.edit("`Please specify a valid user!`")
        return
    if user.id == client.me.id:
        return await ex.edit("**Okay Sure.. 🐽**")

    try:
        if user.id in SUDO_USER:
            return await ex.edit("`User already gmuted`")
        SUDO_USER.append(user.id)
        await ex.edit(f"[{user.first_name}](tg://user?id={user.id}) Added To Sudo Users!")

    except Exception as e:
        await ex.edit(f"**ERROR:** `{e}`")
        return



add_command_help(
    "sudos",
    [
        [
            "addsudo <reply/username/userid>",
            "Add any user as Sudo (Use This At your own risk maybe sudo users can control ur account).",
        ],
        ["rmsudo <reply/username/userid>", "Remove Sudo access."],
        ["sudolist", "Displays the Sudo List."],
    ],
)
