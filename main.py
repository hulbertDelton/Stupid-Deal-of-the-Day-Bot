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
    print(dealscrape.GetDealOfTheDayTitle())
    
    info = dealscrape.GetDealOfTheDayTitle()
    deal_info = dealscrape.GetDealOfTheDayText()
    try:
        if type(deal_info) is list:
            for d in deal_info:
                if len(d) > 0:
                    info += "\n" + d
        else:
            info += "\n" + (deal_info)
    except:
        info += "\n" + ("For more info, visit " + dealscrape.MUSICIANS_FRIEND_URL)
    
    await ctx.send(info)
    await ctx.send(dealscrape.GetDealOfTheDayImage())
    return

dealbot.start()