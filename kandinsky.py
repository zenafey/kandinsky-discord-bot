"""author`s discord - @zenafey

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
    print("-----------------------------------")
    print(f"{Fore.GREEN}       loggined as {bot.user.display_name}       {Fore.RESET}")
    print("-----------------------------------")
    
    
@bot.slash_command(name="kandinsky", description="Create images with Kandinsky2.1")
@option("prompt", description="Enter a prompt for image")
@option("aspect_ratio", desciption="Choose aspect ratio for image(default is 1:1)", choices=["1:1", "2:3", "3:2"], default="1:1")
@option("steps", description="Enter steps value(1-50)", min_value=1, max_value=500, default=50)
@option("scale", description="Enter scale value(1-10)", min_value=1, max_value=20, default=4)
async def kandinsky(ctx, prompt:str, aspect_ratio:str, steps:int, scale:float):
    text = f"```propmpt:{prompt}\naspect_ratio:{aspect_ratio}\nsteps:{steps}\nscale:{scale}```"
    embed1 = discord.Embed(title=" Job in progress...", color=discord.Color.blue(), description=text)
    msg = await ctx.respond(embed=embed1)
    if aspect_ratio == "1:1":
        width = 512
        height = 512
    elif aspect_ratio == "2:3":
        width = 512
        height = 768
    elif aspect_ratio == "3:2":
        width = 768
        height = 512
    inputs = {
        "prompt": prompt,
        "num_inference_steps": steps,
        "guidance_scale": scale,
        "width": width,
        "height": height
    }
    image = replicate.run("ai-forever/kandinsky-2:601eea49d49003e6ea75a11527209c4f510a93e2112c969d548fbb45b9c4f19f", input=inputs)
    embed2 = discord.Embed(title="<:draw:1090244543280066560> Kandinsky Art", color=discord.Color.blue(), description=text)
    embed2.set_image(url=image)
    await msg.edit_original_response(content=ctx.author.mention, embed=embed2)

bot.run(ds_token) #run the bot
