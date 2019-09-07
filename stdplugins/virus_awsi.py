"""command: .virus"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "virus":

        await event.edit(input_str)

        animation_chars = [
        
            "`Inietto il virus nella chat`\n\n`I inject the virus into the chat`",
            "`Inietto il virus nella chat.`\n\n`I inject the virus into the chat.`",
            "`Inietto il virus nella chat..`\n\n`I inject the virus into the chat..`",
            "`Inietto il virus nella chat...`\n\n`I inject the virus into the chat...`",
            "`Connessione al server dell'utente.`\n\n`Connection to the user's server.`",
            "`Connessione al server dell'utente..`\n\n`Connection to the user's server..`",
            "`Connessione al server dell'utente...`\n\n`Connection to the user's server....`",
            "`Connessione al server dell'utente.`\n\n`Connection to the user's server.`",
            "`Connessione al server dell'utente..`\n\n`Connection to the user's server..`",
            "`Target selezionato.\n\nTarget Selected.`",
            "`Injection in progress. 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Injection in progress.. 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Injection in progress... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Injection in progress. 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Injection in progress.. 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Injection in progress... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Injection in progress. 84%\n█████████████████████▒▒▒▒ `",
            "`Injection completed.. 100%\n█████████████████████████ `",
            "`Account Mirato Compromesso...\n\nPagare 50€ a @AnataWaShindeIru per rimuovere questo Virus`\n\n`Targeted Account Hacked...\n\nPay 50$ to @AnataWaShindeIru o remove this Virus`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
