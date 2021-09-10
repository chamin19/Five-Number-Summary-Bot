import discord 
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

import bot_functions
import random

load_dotenv(".env")

client = commands.Bot(command_prefix = "!")
server_token = getenv('TOKEN')
channel_token = getenv('CHANNELID')

temp = None

class Data:
    def __init__(self,user_entry):
        self.user_entry = user_entry
        self.data_list = []
        self.num_of_elements = 0

    def set_properties(self):
        self.user_entry = self.user_entry.replace(",", " ")
        self.data_list = [float(num) for num in self.user_entry.split()]
        self.data_list.sort()
        self.num_of_elements = len(self.data_list)


@client.event
async def on_ready():
    channel = client.get_channel(int(channel_token))
    greetings = ["Hi, there!", "Howdy!", "Hello!", "Hey, there!"]
    await channel.send(f"{random.choice(greetings)} Five-Number Summary Bot is now online.")

    embed = discord.Embed(title="Commands", inline=False)
    embed.add_field(name="!A", value="Mean, Median, Mode", inline=False)
    embed.add_field(name="!B", value="Sample Variance, Standard Deviation", inline=False)
    embed.add_field(name="!C", value="First Quartile, Third Quartile, Interquartile Range", inline=False)
    embed.add_field(name="!D", value="Lower Fence, Upper Fence, Outliers", inline=False)
    embed.add_field(name="!E", value="Mininum, Maximum", inline=False)
    embed.add_field(name="!F", value="Minimum and Maximum w/in lower/upper fence", inline=False)
    embed.add_field(name="!new_data", value="followed by list of nums separated by spaces/commas", inline=False)
    await channel.send(embed=embed)

@client.command()
async def new_data(ctx, *, data_entry):
    global temp
    temp = Data(data_entry)
    temp.set_properties()

@client.command()
async def A(ctx):
    await ctx.reply(str(temp.data_list) 
    + "\nMean: " + str(bot_functions.mean(temp)) 
    + "\nMedian: " + str(bot_functions.median(temp)) 
    + "\nMode: " + str(bot_functions.mode(temp)))

@client.command()
async def B(ctx):
    await ctx.reply(str(temp.data_list) 
    + "\nSample variance: " + str(bot_functions.sample_variance(temp))
    + "\nStandard deviation: " + str(bot_functions.standard_deviation(temp)))

@client.command()
async def C(ctx):
    await ctx.reply(str(temp.data_list) 
    + "\nQ1: " + str(bot_functions.first_quartile(temp))
    + "\nQ3: " + str(bot_functions.third_quartile(temp))
    + "\nIQR: " + str(bot_functions.interquartile_range(temp)))

@client.command()
async def D(ctx):
    await ctx.reply(str(temp.data_list) 
    + "\nLower fence: " + str(bot_functions.lower_fence(temp))
    + "\nUpper fence: " + str(bot_functions.upper_fence(temp))
    + "\nOutliers: " + str(bot_functions.outliers(temp)))

@client.command()
async def E(ctx):
    await ctx.reply(str(temp.data_list) 
    + "\nMinimum: " + str(bot_functions.minimum(temp))
    + "\nMaximum: " + str(bot_functions.maximum(temp)))

@client.command()
async def F(ctx):
    await ctx.reply(str(temp.data_list) 
    + "\nMinimum within lower & upper fence: " + str(bot_functions.minimum_fence(temp))
    + "\nMaximum within lower & upper fence: " + str(bot_functions.maximum_fence(temp)))


client.run(server_token)