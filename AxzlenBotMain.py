#Bu Botun Tüm Hakları Abdullah Emir BİNGÖL'E Aittir
#Yapımcı = Abdullah Emir BİNGÖL
#Yapım Tarihi = 17.04.2024
#Botun Başka Yerde Kullanılması Kesinllikle Yasaktır !
#-----------------------------------------------------------------------------
import discord
import requests
import random
import string
from discord.ext import commands
from tokenmain import token
from tictactoe import TicTacToe, TicTacToeButton 
#-----------------------------------------------------------------------------

intents = discord.Intents.default()
intents.message_content = True

#-----------------------------------------------------------------------------
bot = commands.Bot(command_prefix='!', intents=intents)
#-----------------------------------------------------------------------------

@bot.event
async def on_ready():
    print(f'{bot.user} Olarak Giriş Yaptık')

#-----------------------------------------------------------------------------

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'Merhaba 👋. Ben Bir Discord Sohbet Botuyum🤖')
    await ctx.send(f'Neler Yapabileceklerimi Görmek İçin !yardım Yaz😊')

#-----------------------------------------------------------------------------

@bot.command()
async def site(ctx):
    await ctx.send(f'WebSitem Yapım Aşamasında.😊')

#-----------------------------------------------------------------------------

@bot.command()
async def bothakkında(ctx):
    await ctx.send(f'Merhabalar Bu Bot 15.04.2024 Tarihinde Kodlanmaya Başlayıp 17.04.2024 Tarihinde Biten Bir Sohbet Botudur.')
    await ctx.send(f"Yapımcısı Abdullah Emir B. Botun Birçok İşlevi Bulunmatadır. Python Kodlama Dili İle Kodlandım.😊")
    await ctx.send(f"!yardım Yazarak Neler Yapabildiklerimi Görebilirsin. 🤖")

#-----------------------------------------------------------------------------

@bot.command()
async def yardım(ctx):
    await ctx.send(f'Yapabildiklerim 😊')
    await ctx.send(f'havalı = Bir Kullanıcının Havalı Olup Olmadığını Söyler 😎.')
    await ctx.send(f'katılmak = Bir Kullanıcının Sunucuya Katıldıgını Gösterir.')
    await ctx.send(f'heh = Heh Kelimesini İstediginiz Uzunlukta Yazdırır.')
    await ctx.send(f'doğa = Doğaya Destek Olursunuz 🌲.')
    await ctx.send(f'doğaresmi = Doğa İle resim Gönderir 🌲.')
    await ctx.send(f'köpek =  Rasgele Bir Köpek Resmi Atar.🐕')
    await ctx.send(f'tilki =  Rasgele Bir Tilki Resmi Atar.🦊')
    await ctx.send(f'tic = Tic-Tac-Toe Oyunu Başlatır.❌⭕')
    await ctx.send(f'site = Botumuzun Sitesinin Linkini Atar.')
    await ctx.send(f'tekrarla = Bir Mesajı Birden Çok Kez Tekrarlar...')
    await ctx.send(f'toplar = İki Sayıyı Toplar.')
    await ctx.send(f'merhaba = Bot Karşılık Verir.')
    await ctx.send(f'bothakkında = Botumuzun Detaylarını Verir.')
    await ctx.send(f'sifre = Rastgele Şifre Oluşturur.')
    await ctx.send(f'komikgif = Rastgele Komik GIFler Atar.')
    await ctx.send(f'hava [şehir] = İstediginiz Şehirin Hava Durumunu Gösterir.')

#-----------------------------------------------------------------------------

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

#-----------------------------------------------------------------------------

@bot.command()
async def toplar(ctx, left: int, right: int):
    """İki Sayıyı Toplar."""
    await ctx.send(left + right)

#-----------------------------------------------------------------------------

@bot.command()
async def tekrarla(ctx, times: int, content='Tekrarlanan...'):
    """Bir Mesajı Birden Çok Kez Tekrarlar.."""
    for i in range(times):
        await ctx.send(content)

#-----------------------------------------------------------------------------

@bot.command()
async def katılmak(ctx, member: discord.Member):
    """Bir Üye Katıldı."""
    await ctx.send(f'{member.name} Katıldı {discord.utils.format_dt(member.joined_at)}')

#-----------------------------------------------------------------------------

@bot.group()
async def havalı(ctx):
    """Bir Kullanıcının Havalı Olup Olmadığını Söyler.

    Gerçekte Bu Sadece Bir Alt Komutun Çağrılıp Çağrılmadığını Kontrol Eder.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'Hayır❌, {ctx.subcommand_passed} Havalı Değil.')


@havalı.group(name='bot')
async def _bot(ctx):
    """Bot Güzel Mi ?"""
    await ctx.send('Evet Bot Harika.')

#-----------------------------------------------------------------------------

@bot.command()
async def doğa(ctx):
    await ctx.send(f'Merhaba Sende Bizim Gibi Bir Çevre Dostusun Bu Komutu Yazdın Ve Çevreye Destek Olmak Mı İstiyorsun 😊? O Zaman Sana Link Gönderiyorum.')
    await ctx.send(f'Burdaki Linklerden Doğaya Destek Olabilirsin ❤️ https://destek.wwf.org.tr/  https://dogadernegi.org/bagis/  https://www.tema.org.tr/bagislar')

@bot.command()
async def doğaresim(ctx):
    resim = "Resim/TemaResmi (1).jpg"  

    with open(resim, "rb") as f:
        resim = discord.File(f)
        await ctx.send(file=resim)

#-----------------------------------------------------------------------------

@bot.command()
async def tic(ctx: commands.Context):
    """Tic-Tac-Toe Oyunu Başlatır."""
    await ctx.send('Tic Tac Toe: X Önce Gider', view=TicTacToe())

#-----------------------------------------------------------------------------

def köpekresimleri():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('köpek')
async def köpek(ctx):
    '''Köpek Komutunu Çağırdığımızda, Program , köpekresimleri Fonksiyonunu Çağırır.'''
    image_url = köpekresimleri()
    await ctx.send(image_url)

#-----------------------------------------------------------------------------

def tilkiresimleri():    
    url = ' https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('tilki')
async def tilki(ctx):
    '''Tilki Komutunu Çağırdığımızda, Program , tilkiresimleri Fonksiyonunu Çağırır.'''
    image_url = tilkiresimleri()
    await ctx.send(image_url)

#-----------------------------------------------------------------------------

def rasgele_sifre_olustur(length=12):
    """Rasgele Şifre Oluşturur."""
    karakterler = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(karakterler) for _ in range(length))

@bot.command()
async def sifre(ctx, uzunluk: int = 12):
    """Belirli Bir Uzunlukta Rasgele Şifre Oluşturur. Varsayılan Uzunluk 12'Dir."""
    if uzunluk < 4 or uzunluk > 100:
        await ctx.send("Şifre Uzunluğu 4 İle 100 Arasında Olmalıdır.")
    else:
        rasgele_sifre = rasgele_sifre_olustur(uzunluk)
        await ctx.send(f"Rasgele Oluşturulan Şifre = {rasgele_sifre}")

#-----------------------------------------------------------------------------

def get_random_gif():
    """Tenor API'sini Kullanarak Rastgele Komik Bir GIF Alır."""
    api_key = "LIVDSRZULELA"
    url = f"https://api.tenor.com/v1/random?q=funny&key={api_key}&limit=1"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        gif_url = data['results'][0]['media'][0]['gif']['url']
        return gif_url
    else:
        return None

@bot.command()
async def komikgif(ctx):
    """Rastgele Komik Bir GIF Gönderir."""
    gif_url = get_random_gif()
    if gif_url:
        await ctx.send(gif_url)
    else:
        await ctx.send("Üzgünüm, Bir Hata Oluştu. Daha Sonra Tekrar Deneyin.")

#-----------------------------------------------------------------------------

def get_weather(city):
    """Belirli Bir Şehrin Hava Durumu Bilgisini Alır."""
    api_key = "3f95891ff71036d0fe76ebadf93bfr22c15r"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        return f"Hava Durumu {city}:\nDurum: {weather_description}\nSıcaklık: {temperature}°C\nNem: {humidity}%\nRüzgar Hızı: {wind_speed} m/s"
    else:
        return "Üzgünüm, Hava Durumu Bilgisini Alırken Bir Hata Oluştu. Lütfen Daha Sonra Tekrar Deneyin."

@bot.command()
async def hava(ctx, *, city: str):
    """Belirli Bir Şehrin Hava Durumu Bilgisini Gönderir."""
    weather_info = get_weather(city)
    await ctx.send(weather_info)

#-----------------------------------------------------------------------------

bot.run(token)


