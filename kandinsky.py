"""author`s discord - xeon-m#7477

import needed modules"""
import discord
from discord import option
from discord.ext import commands
import replicate
from dotenv import load_dotenv
import os
from colorama import init, Fore, Back, Style
import json
#load variables with replicate and discord api token
load_dotenv()
ds_token = os.environ['DISCORD_TOKEN']
#define discord bot
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())
#event that will print message when bot will be ready
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='>help'))
    print("-----------------------------------")
    print(f"{Fore.GREEN}       loggined as {bot.user.display_name}       {Fore.RESET}")
    print("-----------------------------------")
#define slash command kandinsky
@bot.slash_command(name="kandinsky", description="Create images with Kandinsky2.1")
@option("prompt", description="Enter a prompt for image")
@option("steps", description="Enter steps value(1-500)", min_value=1, max_value=500, default=50) #define options for slash command
@option("scale", description="Enter scale value(1-20)", min_value=1, max_value=20, default=4)
async def kandinsky(ctx, prompt:str, steps:int, scale:float): #function of slash command
    embed1 = discord.Embed(title="Job in progress...", color=0xff0000,
                           description=f"```propmpt:{prompt}\nsteps:{steps}\nscale:{scale}```")
    msg = await ctx.respond(embed=embed1)#send text that will be used in generation
    model = replicate.models.get("cjwbw/kandinsky-2")# get replicate model
    version = model.versions.get("65a15f6e3c538ee4adf5142411455308926714f7d3f5c940d9f7bc519e0e5c1a")# get version of replicate model
    image = version.predict(prompt=prompt, num_inference_steps=steps, guidance_scale=scale) # make a predict and get answer as url of image
    embed2 = discord.Embed(title="Kandinsky Art", color=0xff0000,
                           description=f"```prompt:{prompt}\nsteps:{steps}\nscale:{scale}```")
    embed2.set_image(url=image)#set url of embed
    await msg.edit_original_response(content=ctx.author.mention, embed=embed2) #edit first response with adding generated image

bot.run(ds_token) #run the bot
