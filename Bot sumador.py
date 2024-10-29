import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


botsito = commands.Bot(command_prefix="/", intents=intents)

@botsito.event 
async def on_ready():
    print(f"Hemos iniciaso el bot")

@botsito.command() 
async def hola(ctx):
    await ctx.send("hola, como estas")


@botsito.command()
async def suma(ctx, num1:int, num2: int):
    suma = num1 + num2
    await ctx.send(f"las suma {num1} + {num2} = {suma}")

@botsito.command()
async def resta(ctx, num1:int, num2: int):
    resta = num1 - num2
    await ctx.send(f"las resta de {num1} - {num2} = {resta}")


@botsito.command()
async def multi(ctx, num1:int, num2: int):
    multi = num1 * num2
    await ctx.send(f"la multiplicacion de {num1} * {num2} = {multi}")

botsito.run("")
