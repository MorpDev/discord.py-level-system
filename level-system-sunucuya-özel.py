@client.event
async def on_message(message):
    if not message.author.bot:
        print('function yükleme')
        with open('level.json','r') as f:
            users = json.load(f)
            print('dosya yükleme')
        await update_data(users, message.author,message.guild)
        await add_experience(users, message.author, 4, message.guild)
        await level_up(users, message.author,message.channel, message.guild)

        with open('level.json','w') as f:
            json.dump(users, f)
    await client.process_commands(message)



#burası bana ait değil pek anlamadım
async def update_data(users, user,server):
    if not str(server.id) in users:
        users[str(server.id)] = {}
        if not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['tecrube'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1
    elif not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['tecrube'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1

async def add_experience(users, user, exp, server):
  users[str(user.guild.id)][str(user.id)]['tecrube'] += exp

async def level_up(users, user, channel, server):
  experience = users[str(user.guild.id)][str(user.id)]['tecrube']
  lvl_start = users[str(user.guild.id)][str(user.id)]['level']
  lvl_end = int(tecrube ** (1/4))
  if str(user.guild.id) != 'sunucuID': #sunucu ID girin
    if lvl_start < lvl_end:
      await channel.send('{} Level Atladı Yeni Levelin {}'.format(user.mention, lvl_end))
      users[str(user.guild.id)][str(user.id)]['level'] = lvl_end


@client.command(aliases = ['rank','lvl'])
async def level(ctx,member: discord.Member = None):

    if not member:
        user = ctx.message.author
        with open('level.json','r') as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(user.id)]['level']
        exp = users[str(ctx.guild.id)][str(user.id)]['experience']

        embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP " ,color = discord.Color.green())
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
    else:
      with open('level.json','r') as f:
          users = json.load(f)
      lvl = users[str(ctx.guild.id)][str(member.id)]['level']
      exp = users[str(ctx.guild.id)][str(member.id)]['tecrube']
      embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP" ,color = discord.Color.green())
      embed.set_author(name = member, icon_url = member.avatar_url)

      await ctx.send(embed = embed)
