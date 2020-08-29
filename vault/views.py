from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Mainslide,Video,latestnews,Article,Weeksuggestions,Movie,Series,Animes
from quiz.models import winners,contests
from accounts.models import UserProfile
from django.contrib import messages
from django.contrib.auth.models import auth,User
# Create your views here.
mves = Movie.objects.all()
mves.reverse()
series = Series.objects.all()
series.reverse()
latnetmve=mves.filter(latestnetflixmovie=True)
latnetmve1=latnetmve[:20]
latprimve=mves.filter(latestprimemovie=True)
latprimve1=latprimve[:20]
latnetweb=series.filter(latestnetflixseries=True)
latnetweb1=latnetweb[:20]
latpriweb=series.filter(latestprimeseries=True)
latpriweb1=latpriweb[:20]
upnetmve=mves.filter(upcomingnetflixmovie=True)
upnetmve1=upnetmve[:20]
upprimve=mves.filter(upcomingprimemovie=True)
upprimve1=upprimve[:20]
upnetweb=series.filter(upcomingnetflixseries=True)
upnetweb1=upnetweb[:20]
uppriweb=series.filter(upcomingprimeseries=True)
uppriweb1=uppriweb[:20]
animes = Animes.objects.all()
animes.reverse()
animes1=animes.filter(Top10=True)
mvesug=mves.filter(suggested=True)
actionmve=mves.filter(action=True)
actionmve=actionmve.filter(top=True)
advmve=mves.filter(adv=True)
advmve=advmve.filter(top=True)
dramamve=mves.filter(drama=True)
dramamve=dramamve.filter(top=True)
comedymve=mves.filter(comedy=True)
comedymve=comedymve.filter(top=True)
fanmve=mves.filter(fantasy=True)
fanmve=fanmve.filter(top=True)
horrormve=mves.filter(horror=True)
horrormve=horrormve.filter(top=True)
scifimve=mves.filter(scifi=True)
scifimve=scifimve.filter(top=True)
thrillermve=mves.filter(thriller=True)
thrillermve=thrillermve.filter(top=True)
romancemve=mves.filter(romance=True)
romancemve=romancemve.filter(top=True)
mvesug1=mves.filter(trending=True)
mvesug1=mvesug1[:20]
seriessug=series.filter(suggested=True)
seriessug=seriessug[:20]
seriessug1=series.filter(trending=True)
mwprime=series.filter(mwprime=True)
mwnetflix=series.filter(mwnetflix=True)
mwhotstar=series.filter(mwnetflix=True)
Toprated=mves.filter(toprated=True)
Toprated=sorted(Toprated,key=lambda x:x.rating,reverse=True)
latestnews=latestnews.objects.all()
latestnews.reverse()

Toprated=mves.filter(toprated=True)

def home(request):
    mainslides=Mainslide.objects.all()
    vids=Video.objects.all()
    articles=Article.objects.all()
    articles.reverse()   
    winn=winners.objects.all()
    winn.reverse()
    cont=contests.objects.all()
    weeksuggestions=Weeksuggestions.objects.all()
    weeksuggestions.reverse()
    userpro=None
    if request.user.is_authenticated:
        userpro=UserProfile.objects.get(user=request.user)

    return render(request,'index.html',{'vids':vids,'articles':articles,'mainslides':mainslides,'weeksuggestions':weeksuggestions,'latestnews':latestnews,'contests':cont,'winners':winn,'userpro':userpro} )
def about(request):
    return render(request,'about.html')
def latest(request): 
    return render(request,'latest.html',{'latnetmve':latnetmve1,'latprimve':latprimve1,'latnetweb':latnetweb1 ,'latpriweb':latpriweb1,'anime': animes1})
def latestnetflix(request): 
    
    return render(request,'latestnetflix.html',{'netflixmves' : latnetmve})    
def latestprime(request):
    return render(request,'latestprime.html',{'primemves': latprimve})    
def latestnetflixseries(request):
    return render(request,'latestnetflixseries.html',{'netflixseries': latnetweb})
def latestprimeseries(request):
    return render(request,'latestprimeseries.html',{'primeseries': latpriweb})
def upcoming(request):
    return render(request,'upcoming.html',{'upnetmve':upnetmve1,'upprimve':upprimve1,'upnetweb':upnetweb1,'uppriweb':uppriweb1,'anime':animes1})
def upcomingnetflix(request):
    return render(request,'upcomingnetflix.html',{'upnetmve':upnetmve})
def upcomingprime(request):
    return render(request,'upcomingprime.html',{'upprimve':upprimve})
def upcomingnetflixseries(request):
    return render(request,'upcomingnetflixseries.html',{'upnetmve':upnetmve})
def upcomingprimeseries(request):
    return render(request,'upcomingprimeseries.html',{'upprimve':upprimve})
def suggestions(request):
    return render(request,'suggestion.html',{'mves':mvesug1,'actionmve':actionmve,'advmve':advmve,'comedymve':comedymve,'dramamve':dramamve,'fantasymve':fanmve,'horrormve':horrormve,'scifimve':scifimve,'thrillermve':thrillermve,'romancemve':romancemve,'series':seriessug,'mwprime':mwprime,'mwhotstar':mwhotstar,'mwnetflix':mwnetflix})
def mvesuggestion(request):
    engmves=mves.filter(language="english")
    trendhol=engmves.filter(trending=True)
    engmves=engmves.filter(suggested=True)

    hinmves=mves.filter(language="hindi")
    upbol=hinmves.filter(upcoming=True)
    trendbol=hinmves.filter(trending=True)
    hinmves=hinmves.filter(suggested=True)

    telmves=mves.filter(language="telugu")
    uptel=telmves.filter(upcoming=True)
    trendtel=telmves.filter(trending=True)
    telmves=telmves.filter(suggested=True)

    tammves=mves.filter(language="tamil")
    uptam=tammves.filter(upcoming=True)
    trendtam=tammves.filter(trending=True)
    tammves=tammves.filter(suggested=True)

    malmves=mves.filter(language="malyalam")
    upmal=malmves.filter(upcoming=True)
    trendmal=malmves.filter(trending=True)
    malmves=malmves.filter(suggested=True)

    return render(request,'mvesuggestion.html',{'trendhol':trendhol,'engmves':engmves,'upbol':upbol,'trendbol':trendbol,'hindimves':hinmves,'uptel':uptel,'trendtel':trendtel,'telmves':telmves,'uptam':uptam,'trendtam':trendtam,'tamilmves':tammves,'upmal':upmal,'trendmal':trendmal,'malmves':malmves,})
def wbssuggestion(request):
    actionser=series.filter(action=True)
    advser=series.filter(adv=True)
    comedyser=series.filter(comedy=True)
    dramaser=series.filter(drama=True)
    fantasyser=series.filter(fantasy=True)
    horrorser=series.filter(horror=True)
    thrillerser=series.filter(thriller=True)
    scifiser=series.filter(scifi=True)
    romanceser=series.filter(romance=True)
    return render(request,'wbssuggestion.html',{'actionseries':actionser,'advseries':advser,'comseries':comedyser,'dramaseries':dramaser,'fanseries':fantasyser,'horrorseries':horrorser,'scifiseries':scifiser,'thrillerseries':thrillerser,'romanceseries':romanceser})
def topanime(request):
    return render(request,'topanime.html',{'anime':animes})
def toprated(request):
    actmves=Toprated.filter(action=True)
    advmves=Toprated.filter(adv=True)
    cmdymves=Toprated.filter(comedy=True)
    dramamves=Toprated.filter(drama=True)
    fanmves=Toprated.filter(fantasy=True)
    hormves=Toprated.filter(horror=True)
    scifimves=Toprated.filter(scifi=True)
    thrillermves=Toprated.filter(thriller=True)
    rommves=Toprated.filter(romance=True)
    return render(request,'toprated.html',{'actionmves':actmves,'advmves':advmves,'commves':cmdymves,'drammves':dramamves,'fanmves':fanmves,'hormves':hormves,'scifimves':scifimves,'thrilermves':thrillermves,'rommves':rommves})
'''def toprated2(request):
    return render(request,'toprated2.html',{'toprated':Toprated2})
def toprated3(request):
    return render(request,'toprated3.html',{'toprated':Toprated3})
def toprated4(request):
    return render(request,'toprated4.html',{'toprated': Toprated4})
def toprated5(request):
    return render(request,'toprated5.html',{'toprated':Toprated5})'''
def article(request,id):
    article=Article.objects.get(pk=id)
    return render(request,'single.html',{'article':article,'latestnews': latestnews})
def articles(request):
    return render(request,'articles.html',{'articles':articles})
def trending(request):
    return render(request,'trending.html',{'mves':mvesug1})
def trendingseries(request):
    return render(request,'trending.html',{'series': seriessug1})
def movie(request,id):
    movie=mves.get(pk=id)
    return render(request,'movie.html',{'mve':movie})
def tv(request,id):
    tv=series.objects.get(pk=id)
    return render(request,'series.html',{'tv':tv})
def anime(request,id):
    anim=animes.objects.get(pk=id)
    return render(request,'series.html',{'anime':anim})
def weeksuggestions(request,id):
    ws=weeksuggestions.objects.get(pk=id)
    return render(request,'movie.html',{'ws':ws})