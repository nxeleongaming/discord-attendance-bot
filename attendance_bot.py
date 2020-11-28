import discord
from discord.ext import commands
import datetime
import pytz
import csv
import pandas as pd

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
token = read_token()

bot = commands.Bot(command_prefix='$')
client = discord.Client()

@bot.event
async def on_ready():
    print("TIME TO WORK!")
    await bot.change_presence(activity=discord.Game(name="DON'T FORGET TO CLOCK IN"))


@bot.event
async def on_message(message):
    current_time = datetime.datetime.now()
    server_timezone = "Etc/UTC"
    channel = ["channel name"]  #replace channel name with channel name of your attendance logs
    name = str(message.author.display_name)
    Date = current_time.strftime('%A, %B %d, %Y')
    Time = current_time.strftime('%I:%M%p')



#POLICE DEPARTMENT
    if str (message.channel) in OCPD:
        if message.author == bot.user:
            return
        if message.content.lower() == '!clock in':
            with open("Time Logs.csv", 'a') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([name,str(Time),'',Date])
            await message.channel.send(name + ' Clocked In!')
            await message.channel.send('**' + str (Time) + '**')
            await message.channel.send('**' + str (Time) + '**')

        if message.content.lower() == '!clock out':
            raw_data = pd.read_csv('Time Logs.csv')
            df = pd.DataFrame(raw_data)
            val = df[df['NAME'] == name].index
            df.loc[val, 'OUT'] = Time
            df.to_csv('OCPD.csv', mode='w', header=True, index=False )
            df.style.set_properties(**{'text-align': 'center'})
            print(df)
            await message.channel.send('You Clocked Out!')
            await message.channel.send('**' + str(Time) + '**')
            await message.channel.send('**' + str(Time) + '**')

bot.run(token)
