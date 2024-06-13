import discord
from discord.ext import commands
import asyncio
import random
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Tu bot está en linea: {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'¡Hola! Soy tu asistente para la clasificación de residuos. Dime el objeto que quieres desechar y te diré si va a la basura o al reciclaje. A sus servicios , {bot.user}!')
    await asyncio.sleep(2)  # Espera 5 segundos
    await ctx.send('Si no sabes qué preguntar, puedes usar estos comandos para ayudarte: papel, carton, botella de plástico, vidrio, restos de comida, baterías, electrodomésticos')
    await asyncio.sleep(2)
    await ctx.send('También puedes preguntarme por consejos para reutilizar algunos de estos en bonitos accesorios con el comando $reciclar')
    await ctx.send(file=discord.File('ruta/a/tu/imagen.png'))

@bot.command()
async def papel(ctx):
    await ctx.send("El papel va al contenedor azul de reciclaje.")
    await ctx.send(file=discord.File('ruta/a/tu/imagen.png'))

@bot.command()
async def carton(ctx):
    await ctx.send("El cartón va al contenedor azul de reciclaje.")
    await ctx.send(file=discord.File('ruta/a/tu/imagen.png'))

@bot.command()
async def botella(ctx):
    await ctx.send("La botella de plástico va al contenedor amarillo de reciclaje.")
    await ctx.send(file=discord.File('ruta/a/tu/imagen.png'))

@bot.command()
async def vidrio(ctx):
    await ctx.send("El vidrio va al contenedor verde de reciclaje.")
    await ctx.send(file=discord.File('ruta/a/tu/imagen.png'))
@bot.command()
async def restos(ctx):
    await ctx.send("Los restos de comida van al contenedor de residuos orgánicos.")
    await ctx.send(file=discord.File('ruta/a/tu/imagen.png'))
    await ctx.send(file=discord.File('ruta/a/tu/imagen.png'))

@bot.command()
async def baterias(ctx):
    await ctx.send("Las baterías deben llevarse a un punto de recogida especial para residuos peligrosos.")
    await ctx.send(file=discord.File('ruta/a/tu/imagen.png'))

@bot.command()
async def electrodomesticos(ctx):
    await ctx.send("Los electrodomésticos deben llevarse a un punto limpio para su correcto reciclaje.")
    await ctx.send(file=discord.File('ruta/a/tu/imagen.png'))
    #ya vi es que un argumento no esta declarado
@bot.command()
async def reciclar(ctx):
    imagen = random.choice(os.listdir('ima'))
    with open(f'ima/{imagen}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("token")
