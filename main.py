import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"soy un nuevo bot porfavor usa un ! antes de decir algo {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot pon materiales reutilisables y te ejecutare una maqueta{bot.user}!')

@bot.command()
async def carton(ctx):
    
    await ctx.send(image_url0,"recolecta carton de tu casa y ayuda a tu hijo a crear casas")
    picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def plastico(ctx):
    
    await ctx.send(image_url1,"recicla muchas tapas de plastico y crea un jugete para tu hijo y a la vez ayudas al planeta")
    picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command()
async def botellas(ctx):
    image_url3 = get_maqueta3_image_url
    await ctx.send(image_url3, "atentos a lus adultos amantes de las plantas al cortar la botella a la mitad")
    picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
bot.run("")

