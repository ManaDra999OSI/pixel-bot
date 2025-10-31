import sys
sys.modules['audioop'] = None  # evita erro em discord.player
import discord
from discord import app_commands
from discord.ext import commands
from pixelize import pixelate_image
import io

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Slash commands sincronizados: {len(synced)}')
    except Exception as e:
        print(e)

@bot.tree.command(name='pixel', description='Pixeliza uma imagem enviada')
@app_commands.describe(image='Envie uma imagem para pixelizar', pixel_size='Tamanho dos pixels (padrão: 10)')
async def pixel(interaction: discord.Interaction, image: discord.Attachment, pixel_size: int = 10):
    await interaction.response.defer()
    img_bytes = await image.read()
    result = pixelate_image(img_bytes, pixel_size)
    await interaction.followup.send(file=discord.File(io.BytesIO(result), filename='pixelated.png'))

if __name__ == '__main__':
    import os
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        print('❌ ERRO: Defina a variável DISCORD_TOKEN no ambiente')
    else:
        bot.run(TOKEN)
