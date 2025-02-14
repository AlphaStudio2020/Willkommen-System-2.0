import discord
from discord.ext import commands

# Setze deinen Token hier ein
TOKEN = 'TOKEN_HIER'

intents = discord.Intents.default()
intents.members = True  # Erforderlich, um auf Member-Events zuzugreifen

bot = commands.Bot(command_prefix="!", intents=intents)

# Füge hier die ID des Channels ein, in den die Willkommensnachricht gesendet werden soll
WELCOME_CHANNEL_ID = 911335362675216464  # Ersetze diese Zahl durch die Channel-ID
IMAGE_FILE_NAME = "FIEL_NAME.jpg"  # Ersetze dies durch den Dateinamen des Bildes

@bot.event
async def on_ready():
    print(f'Bot ist eingeloggt als {bot.user}')


@bot.event
async def on_member_join(member):
    # Zähle die Mitglieder im Server
    member_count = member.guild.member_count

    # Embed-Nachricht im Channel senden
    channel = bot.get_channel(WELCOME_CHANNEL_ID)  # Hole den Channel mit der ID
    if channel:
        embed = discord.Embed(
            title=f"Willkommen, {member.name}!",
            description="Schön, dass du unserem Server beigetreten bist! 🌟\nWir freuen uns, dich hier zu haben.",
            color=0x00ff00  # Farbe des Embeds
        )
        # Füge das Bild hinzu
        embed.set_image(url=f"attachment://{IMAGE_FILE_NAME}")

        # Sende die Embed-Nachricht mit dem Bild
        await channel.send(embed=embed, files=[discord.File(IMAGE_FILE_NAME)])
    
    # Begrüßungsnachricht per DM
    try:
        dm_embed = discord.Embed(
            title="Willkommen auf unserem Discord-Server!",
            description=(
                "Wir freuen uns, dich hier zu haben. Wenn du Fragen hast oder Hilfe benötigst, zögere nicht, "
                "uns zu kontaktieren oder alphagames20. Ich möchte dich bitte im Kanal ╠🙌regelwerk🙌 unsere Server Regeln zu bestätigen. "
                "Einfach den PIN, der im Regelwerk steht, in den Chat ╠🙌regelwerk🙌 reinschreiben.\n"
                f"Du bist Mitglied Nummer **{member_count}**\n"
                "**Erklär Video**\n"
                "TikTok Handy -> https://www.tiktok.com/@alphagames2020/video/7380740660158156065?is_from_webapp=1&sender_device=pc&web_id=7400029890398963233\n"
                "TikTok PC -> https://www.tiktok.com/@alphagames2020/video/7380740277222247713?is_from_webapp=1&sender_device=pc&web_id=7400029890398963233\n"
                "YouTube Handy -> https://youtu.be/FVNsLAP-a8g\n"
                "YouTube PC -> https://youtu.be/Wp7hd9o0fIc"
            ),
            color=0x00ff00
        )
        await member.send(embed=dm_embed)  # Nachricht per DM senden
    except Exception as e:
        print(f"DM konnte nicht gesendet werden: {e}")

# Startet den Bot
bot.run(TOKEN)
