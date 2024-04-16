import discord
from discord.ext import commands
from tokenmain import token

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} Olarak Giriş Yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, Bir Discord Sohbet Botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def toplar(ctx, left: int, right: int):
    """İki Sayıyı Toplar."""
    await ctx.send(left + right)

@bot.command()
async def tekrarla(ctx, times: int, content='tekrarlanan...'):
    """Bir mesajı birden çok kez tekrarlar.."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def tema(ctx):
    await ctx.send(f'Merhaba Sende Bizim Gibi Bir Çevre Dostusun Bu Komutu Yazdın Ve Çevreye Destek Olmak Mı İstiyorsun 😊? O Zaman Sana Link Gönderiyorum.')
    await ctx.send(f'Burdaki Linklerden Doğaya Destek Olabilirsin ❤️ https://destek.wwf.org.tr/  https://dogadernegi.org/bagis/  https://www.tema.org.tr/bagislar')

@bot.command()
async def temagörsel(ctx):
    resim = "Resim/TemaResmi (1).jpg"  

    with open(resim, "rb") as f:
        resim = discord.File(f)
        await ctx.send(file=resim)

bot.run(token)
