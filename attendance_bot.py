import discord
from discord.ext import commands
import datetime
import pytz
import csv
import pandas as pd

current_time = datetime.datetime.now()

old_timezone = pytz.timezone("US/Eastern")
new_timezone = pytz.timezone("Asia/Manila")
new_timezone_timestamp = old_timezone.localize(current_time).astimezone(new_timezone)
server_timezone = "US/Eastern"

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

bot = commands.Bot(command_prefix='$')
client = discord.Client()

employeeDict = {}

@bot.event
async def on_ready():
    #TODO: add users as keys and allow command to update Name--hide users but add name to spreadsheet
    print("Bot is ready and let's goooo!")
    await bot.change_presence(activity=discord.Game(name="DON'T FORGET TO CLOCK IN"))


@bot.event
async def on_message(message):
    id = client.get_guild(748121973955100763)
    OCPD = ["𝐎𝐂𝐏𝐃-𝐀𝐓𝐓𝐄𝐍𝐃𝐀𝐍𝐂𝐄"]
    OCMD = ["𝐎𝐂𝐌𝐃-𝐀𝐓𝐓𝐄𝐍𝐃𝐀𝐍𝐂𝐄"]
    OCMS = ["𝐎𝐂𝐌𝐒-𝐀𝐓𝐓𝐄𝐍𝐃𝐀𝐍𝐂𝐄"]
    name = str(message.author.display_name)
    Date = str(new_timezone_timestamp.strftime('%A, %B %d, %Y'))
    Time = str(new_timezone_timestamp.strftime('%I:%M%p'))



#POLICE DEPARTMENT
    if str (message.channel) in OCPD:
        if message.author == bot.user:
            return
        if message.content.lower() == '!clock in':
            with open("OCPD.csv", 'a') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([name,Time,'',Date])
            await message.channel.send(name + ' Clocked In!')
            await message.channel.send('**' + new_timezone_timestamp.strftime('%A, %B %d, %Y') + '**')
            await message.channel.send('**' + new_timezone_timestamp.strftime('%I:%M%p') + '**')

        if message.content.lower() == '!clock out':
            raw_data = pd.read_csv('OCPD.csv')
            df = pd.DataFrame(raw_data)
            val = df[df['NAME'] == name].index
            df.loc[val, 'OUT'] = Time
            df.to_csv('OCPD.csv', mode='w', header=True, index=False )
            df.style.set_properties(**{'text-align': 'center'})
            print(df)
            await message.channel.send('You Clocked Out!')
            await message.channel.send('**' + new_timezone_timestamp.strftime('%A, %B %d, %Y') + '**')
            await message.channel.send('**' + new_timezone_timestamp.strftime('%I:%M%p') + '**')


#EMS

    elif str (message.channel) in OCMD:
        if message.author == bot.user:
            return
        if message.content.lower() == '!clock in':
            with open("OCMD.csv", 'a') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([name,Time,'',Date])
            await message.channel.send(name + ' Clocked In!')
            await message.channel.send('**' + new_timezone_timestamp.strftime('%A, %B %d, %Y') + '**')
            await message.channel.send('**' + new_timezone_timestamp.strftime('%I:%M%p') + '**')

        if message.content.lower() == '!clock out':
            raw_data = pd.read_csv('OCMD.csv')
            df = pd.DataFrame(raw_data)
            val = df[df['NAME'] == name].index
            df.loc[val, 'OUT'] = Time
            df.to_csv('OCMD.csv', mode='w', header=True, index=False )
            df.style.set_properties(**{'text-align': 'center'})
            print(df)
            await message.channel.send('You Clocked Out!')
            await message.channel.send('**' + new_timezone_timestamp.strftime('%A, %B %d, %Y') + '**')
            await message.channel.send('**' + new_timezone_timestamp.strftime('%I:%M%p') + '**')

#MECHANIC
    elif str (message.channel) in OCMS:
        if message.author == bot.user:
            return
        if message.content.lower() == '!clock in':
            with open("OCMS.csv", 'a') as f:
                thewriter = csv.writer(f)
                thewriter.writerow([name,Time,'',Date])
            await message.channel.send(name + ' Clocked In!')
            await message.channel.send('**' + new_timezone_timestamp.strftime('%A, %B %d, %Y') + '**')
            await message.channel.send('**' + new_timezone_timestamp.strftime('%I:%M%p') + '**')

        if message.content.lower() == '!clock out':
            raw_data = pd.read_csv('OCMS.csv')
            df = pd.DataFrame(raw_data)
            val = df[df['NAME'] == name].index
            df.loc[val, 'OUT'] = Time
            df.to_csv('OCMS.csv', mode='w', header=True, index=False )
            df.style.set_properties(**{'text-align': 'center'})
            print(df)
            await message.channel.send('You Clocked Out!')
            await message.channel.send('**' + new_timezone_timestamp.strftime('%A, %B %d, %Y') + '**')
            await message.channel.send('**' + new_timezone_timestamp.strftime('%I:%M%p') + '**')

bot.run(token)