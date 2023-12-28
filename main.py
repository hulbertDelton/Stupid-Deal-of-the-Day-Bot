import interactions
from interactions import Task, IntervalTrigger, slash_command, SlashContext
from decouple import config
import dealscrape

TOKEN = config('TOKEN')
DEALTIME = '10:30' #fix this once you learn how to do static times

dealbot = interactions.Client(token = TOKEN)

@slash_command(
        name = 'post_stupid_deal',
        description = "post the musician's friend stupid deal of the day"
        )
async def PostStupidDeal(ctx: SlashContext):
    print("Posting Stupid Deal of the Day\n")
    title = dealscrape.GetDealOfTheDayTitle() 
    if len(title) > 0 and type(title) != None:
        print(title)
    
    info = title
    deal_info = dealscrape.GetDealOfTheDayText()
    if len(deal_info) > 0 and type(deal_info) != None:
        try:
            if type(deal_info) is list:
                for d in deal_info:
                    if len(d) > 0:
                        info += f"\n{d}"
            else:
                info += f"\n{deal_info}"
        except:
            info += f"\nFor more info, visit {dealscrape.MUSICIANS_FRIEND_URL}"
        await ctx.send(info)
    img = dealscrape.GetDealOfTheDayImage()
    if len (img) > 0 and type(img) != None:
        await ctx.send(img)
    return

dealbot.start()