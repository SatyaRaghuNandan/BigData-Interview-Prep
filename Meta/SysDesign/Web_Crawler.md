all right welcome back everyone uh it's time to break down another really common system design problem this time we're
going to take on WebCrawler think WebCrawler needs no introduction it's a super popular problem I'm sure you've
all heard it a number of times but now you're going to get my take on it um so
apologies this video is a little bit late a week later than I usually like to do I was traveling bear with me we got
the Hat on uh was feeling a little too lazy to shower this morning so hopefully it won't have any negative impact on our
system design skills um but for those who haven't seen this vide As you're' Seen It For the First Time quick introduction my name is Evan I'm a
former staff engineer and interviewer at meta and I've asked all of these questions dozens tens in some cases
hundreds of times so in this kind of series of videos we walk through a system design problem together I point
out exactly what interviewers are looking for at the different levels based on my experience um now I said
former staff engineer at meta I spend my days nowadays as the co-founder of hello interview and at hello interview we help
candidates prepare for upcoming interviews and this is largely via in-person mocks with Fang senior plus
engineers and managers like myself so if that's something that you're interested head over to hello interview.com and
take a look now before I jump in videos might not be your thing that's totally fine I also wrote up a detailed written
kind of guide to this problem so if you head over to hello interview you can check out designer WebCrawler you can go
through it see all my tips there break down good bad and great solution Solutions um you'll see that we also
have about 11 other common problem breakdowns here on the side take a look at those as well as how we recommend
that you approach system design interviews in the first place lastly you click on that suggust the question and
you can let us know what we should do next so feel free to either propose a question or just vote as you see here
all right without further Ado let's jump into it and design a web crawler
The Approach
all right so before we jump into actually solving the problem let's just take a really quick moment to talk about the road map that we're going to follow
throughout this interview and this is the road map that I suggest that you follow in any of your system design interviews so the very first thing that
we're going to do is we're going to define the requirements of the system this is the functional requirements or the features of the system as well as
the non-functional requirements the qualities and constraints of the system we're then going to just document the
core entities this is just a list of basically like the tables that you would
have I don't go into the full schema yet because often times this early in the interview I don't know it so I kind of
communicate with the interviewer that I'm going to come back and maybe I'll fill out fill out this full schema as I need to but that's where we go next
third is that we talk about either the API in the case of a user facing application or in the case of something like a WebCrawler the interface so just
the inputs and outputs of the system fourth and this one's optional depending on the system but for something like
WebCrawler we'll do it because it's going to be really useful and that's to enumerate how data is going to flow
through our system and this is important because we're actually going to use that enumeration of the different steps in a
web crawler in order to inform our highle design and so step five highle
design is where we head to the Whiteboard and things start to get fun we draw out a simple diagram that is
able to fulfill and this is crucial are functional requirements of our system so at this point the design should be
really straightforward it should be really simple and it just meets those functional requirements now step six deep Dives is
where you really earn your value particularly as a senior candidate staff plus candidate this is where you go back
to those non-functional requirements and you uh evolve your highle design one by
one through each non-functional requirement such that your ultimate design eventually satisfies the
functional and non-functional requirements of your system so that's the process that we're going to follow
you're going to get to watch me walk through exactly that
now before we get into those functional requirements just quickly what is a WebCrawler and so a web crawler is a
Requirements
program that automatically traverses the internet traverses the web and it does this by downloading pages and then
following links from one page to another and repeating that process recursively and so it's used to index the web for
search engines like Google for collecting data for research maybe monitoring websites for changes
collecting data to train machine learning models Etc and so if you get
told to design a WebCrawler in an interview the first question you might want to ask is well what's the purpose of the WebCrawler what am I going to be
using it for because that's going to have some consequences to your design so I narrow in our scope here this is the
problem definition that you can assume the interviewer gave you this is actually the the version that I ask and
it's to design a WebCrawler that extracts text Data from the web and stores it with the goal being to use
that text data to train an llm a large language model like open AI chat
GPT and so um your crawler this is an additional constraint that I provide
your crawler can only run for 5 days we need this data quick like open AI is killing it they have chaty PT we're
maybe over at Google or we're over at Microsoft or apple or wherever Facebook
and so we need to get this data ASAP so we can start training this model so that's kind of an additional constraint there
notably of course this design isn't going to go into training the model even the tokenization any of that our job
ends when we store that text data and then that's where the machine learning team can pick it up from there so that's
the problem definitions now let's jump right into the functional requirements so those functional requirements are uh
relatively straightforward for a problem like this I'm actually just going to paste them in so you don't all have to watch me struggle to type but we just
need to be able to crawl the full web starting from a set of seed URLs we'll Define that here in a second
and then we need to extract text Data from those websites and store them somewhere probably in a
database um now before I get into the non-functional requirements I would
pause and ask my interviewer a little bit about the scale of the system so I might ask them how many websites are
there and maybe they tell me or maybe they ask me to estimate but in either case I'm going to say 10 billion web
pages and then I'm going to estimate that a web page on average is maybe 2 megabytes so per page on average
maybe I asked them for this maybe I estimated it myself and then we already know that we have 5 days to scrape so
there's some scale some constraints that we need to know I might also ask them who are we are we a big organization
that kind of has infinite resources from a money perspective or do we need to be really costc conscientious Etc in this
case I'm going to say you know unlimited resources within reason so within reason
that's the that's what we'll design for and so now we move on to those nonfunctional requirements and
non-functional requirements they're the how of your system they're the constraints that your system most must
operate under so let's kind of think of some that makes sense for us here um in
the case of WebCrawler some non-functional requirements that stick out as interesting are things like we
need to be let me get in here we need to be fault tolerant and this is because we need to
be able to handle failures gracefully so that we can resume crawling without losing a ton of progress it would suck
if we got maybe halfway through crawling um and then we lost everything that we had been working towards that would
certainly be a bummer another one that's really common for web crawlers is something called politeness and so
politeness is adhering to robots.txt in order to not overload website servers
inappropriately so websites can have a robots.txt on their servers which
defines how often they can be crawled and so we don't want to be hitting any given website over and over and over
again effectively dodsing it such that that site goes down that would be inappropriate bad practice and something
that we want to avoid doing so we'll see some examples of robots.txt and how to adhere to it later in the
interview another thing is that of course we need to be able to scale to those 10 billion Pages uh so we need to
be able to handle scalability in order to get up to 10 billion Pages that's quite a bit and then another one here is
that we need to be efficient um and efficiency here means the efficiency to crawl the web page in
under five days so crawl in under five days and so those questions were
important because non-functional requirements to the extent that it's reasonable should be
Quantified and so by understanding the scale of our system we were able to better quantify here
efficiently right so there's the functional scale and non-functional requirements of our system now I'm going
to just take a quick moment to note that in many things that you read online Etc
uh they'll encourage you to do back of the envelope estimations at this point I'm not going to do that and if you've
seen many of my YouTube videos you'll know my opinion on this but estimations are important they're actually very
important and we'll do some later on but what I find in conducting so many of these interviews is that candidates just
take a moment to do this basic math about scale about throughput daily
active users when that's relevant Etc and then at the end of that math they say wow that's a lot and then they keep
going and what I learned as an interviewer is absolutely nothing other than the fact that you can do basic math
and what you learned as a candidate is equally nothing you learned that you're going to create a distributed system
yeah of course we we kind of knew that when we asked some questions about the scale of a system so instead it's my
suggestion to you that you communicate with your interviewer at this point that's very crucial communicate with your interviewer that I'm actually not
going to do math at this point because I want the calculations that I do to directly influence or inform my design
and I don't have math at this point that will do that so while I'm designing maybe in my high level design or deep Dives if I have a critical Junction for
which math will inform my direction I'm going to do math at that point in my opinion this is much more sophisticated
uh it's more realistic it's more indicative of what you would do on the real job so take it or leave it that's my suggestion for you there all in all
we have the problem set up and now it's time for us to to jump into that next step which is the core entities um the
core entities the interface and the data flow
System Interface & Data Flow
following along with our road map we move on to the core entities the core entities are meant to help you
understand the data central to your design and they're going to give you a foundation to build upon and so these
are the core entities that your interface or your API are going to exchange and that your system is going
to persist in the data model so in our case some of the core entities are of course the text Data that's our output
as well as URL metadata the URL itself and metadata about whether we've crawled
it or not and then we'll probably also want some domain metadata and this is so that we can adhere to those policies in
robots.txt which are the domain Nevel level not a URL level so you may know these right away for user-facing product
type system design questions these are more straightforward and reasonable than than in infer questions but they're
still useful to outline nonetheless and so next up we go over to that API or interface given that this is isn't a
clear user facing product that has user facing apis we're going to choose that interface route so we'll write interface
here and what this does is it just outlines the basic inputs and outputs of the system so you want to clearly
outline what data the system receives and what it outputs and this establishes a really clear boundary of your system's
functionality so we can say in our case the input is going to be a set of seed URLs that URL metadata and then the the
output is of course going to be that text data that we parsed from all the websites so hopefully relatively straightforward
up until this point and now the more interesting bit is this data flow which
is dotted here again because it's optional but makes a lot of sense for this style WebCrawler infr type question
so we're going to come down here and we're going to add a data flow and what the data flow is is it describes the
highlevel sequence of actions or processes that your system performs on the desired input in order to produce
that desired output so this is really just a simple list and you're going to use this flow then to inform Your highle
Design moving forward so let's look at what RS would look like in order to
construct a web crawler the very first thing that we do is we take those seed URLs from a frontier Set uh and we
request the IP from DNS and now Frontier I should Define
this Frontier is the set of URLs that are yet to be crawled so in the beginning this is is just our seed URLs
you have some set of seed URLs we're going to pull each of those URLs off the list and then we're going to go fetch
their IP from DNS so we can hit those websites of course and then the second
thing is that we're going to fetch the HTML we're going to go fetch that page straightforward enough next up we're
going to extract text from that HTML okay and then fourth we'll store that
text in a database fifth we're going to need to extract the URLs in the text right so
whatever URLs we're in that web page let's extract them and add to our
Frontier and then lastly this is the recursive bit we're going to repeat steps 1 through five until all urls have
been C until the frontier set is empty so of course I wrote These really
quickly because this was uh you know something I've done so many times it wouldn't be so quick for a candidate and
it often times isn't and that's fine core entities would have been pretty quick interface pretty quick as well and then data flow is where you spend some
time maybe fiveish minutes really thinking through what are the steps here what do I do when I start with a given
seed URL how do I get to my end goal of having all of this text in a database and this is the loose process that you
might arrive at now you'll notice that like this is a really high level process that's intentional it's the highle
process that's going to inform now our high level design there's going to be far more steps to this once we get into
more detail into those non-functional requirements but this is our starting point this is how we unblock ourselves this is how we sit here and just think
really critically what are the simple steps to make this happen so that I can now head to the Whiteboard and start
diagramming them
High Level Design
out all right so we've spent the first 10 to 15 minutes of the interview kind
of working on the setup here defining our requirements understanding our interface and our data flow all for us
to be able to now move into that highle design and so if you're a mid-level
candidate then maybe you spent more time here 15 or so minutes if you're a senior
staff candidate this part probably went pretty quick and maybe you're getting to this High Lev design just 10 minutes in
or so leaving yourself plenty of time to get into the interesting stuff um in
either case we're now moving on to this highle design where we're going to focus on getting a simple system up and
running that satisfies those core functional requirements and to do this we're simply going to follow that data
flow that we outlined uh and then we're going to improve on this later as we go so let's have that data flow close by to
the left of us here and let's think of a simple system that can meet this so the first thing that I'm going to do is I'm
going to add some sort of a Quee and I'm going to call this my Frontier queue and
so this could be Kafka it could be sqs we'll talk about a little bit later on which is going to make most sense but
for now I have some message q and this is going to start by having my seed URLs
so it starts with the seed URLs in this que okay great now we're going to have
some set of workers that pull off of this que so I'll have a worker here this
guy I'm going to call our crawler and what it's going to do is it's going to
pull a URL off the queue and then it's going to fetch the web page and then
it's going to extract the text and then it's going to extract the URLs so that's
all the things that this really simple big computational resource our worker here is going to do and in order to do
that it's going to reach up here it's going to need to hit some
DNS DNS and then go up here and actually
fetch the web page itself so the actual web page and then
once it gets that text Data then this worker This Server is going to write to
a database here and in this case we're going to want to use blob storage of course so I'm going to go with S3 and
this is where we're going to have that text data so we're going to store that in there and then any URLs that we
pulled off of that web page we're going to put right back into our Frontier
queue so this is going to be put extracted urls back on the Queue and then just repeat
repeat repeat and so I'm going to kind of Mark this as these are the things that are within our system DNS and the
web page are external to our system but ultimately this is a really
high level design of a WebCrawler and so you might be watching this thinking wow this is so simple this YouTube video
might not even be relevant to me how simple this is um hang tight we're going to now go into our Deep dive which is
where we're going to spend the majority of the remainder of the interview making sure that this very simple system which
currently meets our functional requirements is able to scale to meet our non-functional requirements handling
fault tolerance politeness efficiency scalability Etc so this is where things
are going to get fun as we move on to the final step the
Deep Dives
Deep Dives here and for this interview it's the place where we spend the majority of the time it's worth outlining the expectations in the
interview for different levels of candidates so it's the case that for mid-level candidates your interview
should really have a lot of breadth 80% breadth and maybe 20% depth and so that
means that you've gotten to this high level design you've hopefully been able to talk through it it probably took you maybe a little bit longer to get here um
and now you're in a conversation with your interviewer they're going to maybe be leading you in the direction of some
of these pitfalls you'll also be referencing your non-functional requirements and hopefully still leading the conversation where it makes sense
but there's a bit more of a back and forth and it's totally okay if you don't see all of the bottlenecks or issues and
they're pointing things out you just need to be able to answer those questions competently and evolve your
design accordingly on the other end of the spectrum is Staff candidates where they should get to this point much
sooner and kind of confidently go one by one through those non-functional requirements knocking each of them out
independently while of course still leaving room for the interviewer to provide any feedback or Point them in
any directions where necessary this shouldn't be a monopolization of the conversation ever and then Senior
candidates you know they fall somewhere in the middle there so it's important to note the degree to which you're
proactive in this section is a consequence of your level and I'll kind of talk throughout about what I'd expect
from each level respectively but what we're going to do is that we have these deep Dives that want to satisfy our
non-functional requirements regardless of your level so you're going to come here to your non-functional requirements and you're going to look first at fault
tolerance so this is how can we ensure that default tolerance such that our systems robust and we don't lose any
progress so zooming back into our design and I'm going to get rid of this dotted line the first thing that you're going
to notice is that this crawler is is doing a lot it's pulling URLs off the queue it's fetching the web page
extracting the text extracting the URLs Etc and the difficulty here is that if
any of these given tasks fail then we've lost all the other progress and so this
isn't strictly true of course we could fetch the website store it in S3 and then if this thing failed we would still
have that URL in the queue we'd pull it off in the crawler the crawler would check you know have some condition have
I already fetch to this if yes go get it from here otherwise get it from up here um and that's possible but there's a
number of limitations to this the first is that we have no separation of responsibility so this doesn't allow us
to scale each of our workers independently it also really inhibits overall observability in monitoring
because we can't have a clear understanding of where we are are in each stage uh and it also makes us
subject to fragility as it pertains to changing requirements so for this reason
if you get a data pipelining question like this your first thought should be how can I split this into smaller more
reasonable stages um and in our case the most reasonable thing to do is to split this
into at least two phases where that first phase is to fetch the HTML and then the second phase is to parse that
HTML of course storing the text and putting the extracted URLs and the reason for this natural breakdown is
because the most difficult to the most aerone process here is the fetching of the HTML so we want to really isolate
that as a single task F fetch the HTML understanding that web pages will be down they'll be throwing errors they'll
have servers that are slow to respond we'll get rate limited Etc so let's have this crawler really focus on that singular task store that raw HTML in S3
and then we're safe we've done that first hard thing and then we can put it into the second stage of the pipeline
and retry as many times as we may need to the parsing the extraction of the uh of the URLs Etc on the HTML that we've
stored as opposed to having to go crawl it again so let's make that update here
briefly so I'm going to have S3 for HTML data and so the crawler here is simply
going to pull off the que and fetch the web page and then it's going to save
that HTML into the HTML data and then it's going to need some additional oops it's
going to need some additional State here and this is going to be that URL metadata we kind of alluded to this
earlier and so you can imagine a URL table maybe it has an ID maybe the primary key is just the URL it's not too
important there and then relevantly it's going to have that link to S3 so that S3
link to HTML right that's going to be important and so the first thing this guy does is that it
crawls stores that raw HTML data in S3 and then updates the URL
metadata and this really could be anything this could be Dynamo DB this could be postgress it doesn't matter
this is this is quite simple there's uh kind of no strong requirements there on
the database type and then like I said update the URL status so once we've done
that then we want to introduce our second phase so I'm going to put our second phase down here this is going to
be a new que this is going to be called our parsing que and so we'll kind of
delineate each stage here with a new Q so put that in
there and so what we're going to put in the que is going to be that um link to
S3 or the URL so we can fetch the HTML data importantly you may be wondering
why don't I just put the HTML in the queue so that my parsing worker can then pull that HT HML directly off the queue
and do its job and the reason for this is that CFA actually by default supports
messages of size 1 Megabyte now that could be configured you'll remember that
we said our average websites were 2 megabytes but in general it's best practice to minimize the size of the
payload that you put on the que here for efficiencies so this cues are not meant
to have large bytes of data that's what blob storage is highly optimized for of
course right so instead the pattern here is that we typically just put a pointer to that blob storage in the Q and so in
our case maybe what that is is just some Json blob of the URL and the S3 link and
by putting the S3 link directly in here then we don't have to go fetch it from uh URL metadata we just have a single
fetch from our parsing worker to go get to go get
the HTML so maybe I should instead fetch the HTML from S3
link and now this parsing worker parsing worker now this parsing worker has that
HTML that's the first thing that it's going to do it's going to parse so it's going
to extract the text right so this takes raw HTML breaks down that Dom breaks
down that tree into just the text that's relevant and then save that text
and then extract URLs from that text and so we can then take those
URLs and put them back into our Q which means that this
guy is no longer needed he got replaced by this big loop fix up my drawing a little bit here
and so just to recap we have our Frontier set which has some URLs in here
starting with our seed URLs our crawler pulls off that URL fetches the website this is the raw HTML saves that raw HTML
in S3 and then updates our URL metadata into a URL table where we importantly have that URL and the link to the HTML
we then also put on the next phases Q the parsing q that URL and S3 link or
maybe just even the S3 link and then our P parsing worker will pull off of this queue for the next phase the second
stage and last stage in our pipeline it's going to fetch that HTML and then do the extraction put the URLs back on
the Queue and then importantly the second thing that it's going to do along this arrow is of
course store Back Store the raw text so
this is going to be S3 that's going to have both the raw HTML first and then
the final text
data now conveniently in this pipeline approach we're also now robust to any changing requirements so you can imagine
maybe that the uh ml team comes back and says all this text is great but we actually also want the text from OCR the
text from images or maybe the alt text on images in the HTML and our parsing worker uh on the first go around didn't
consider this so instead of having to recrawl the entire internet now we just need to load up all of our URLs into our
parsing queue update our parsing logic and rerun that so that's far robust that's far better than having to go do
that kind of expensive sloppy fetching of the web pages all over again great um so continuing on fault
tolerance and robustness what happens if we fail to fetch a URL again internet's a messy place it's very likely that
websites are going to go down so what do we do in that case well the first thing that we could do the obvious and bad
answer is that we could just wait a couple seconds in our crawler so we fetch a website we get a 500 whatever it
is we get some errors and then we just set an inmemory timer here to wait 5 to 10 seconds and then we try it again and
so this sucks for a couple reasons if our crawler goes down then we lost that timer of course it was just an in memory
timer and then it's also true that that web page may not be ready in just five more seconds in fact it probably isn't
if the site's down or if the server is having issues or it's overwhelmed then it could be uh ready again in 5 seconds
but it also may not be and very likely may not be so instead we need a more
sophisticated retry strategy something like maybe an exponential back off and so to accomplish exponential backoff
we're going to need to introduce some sort of state and we can manage this backoff in CFA itself if we assumed that
our Frontier queue is CFA which is one option we still haven't made a decision there and so interestingly Kafka does
not support retries out of the box we would need to implement them ourselves so you could have a separate topic here
in your Frontier Q uh and that separate topic would be for those failed URLs and
in order to know how much a back off for each of them we would determine that back off time in our crawler and add
that to the message that we put back on the Queue so then when the next worker the next crawler pulls off of that topic
it's also going to have the amount of time uh not the time that it should wait but the time that it should run more
importantly and it's going to wait until that time to then go try to fetch or refetch that URL if it fails again and
the crawler has some logic to increase that time in an exponential way and put it back onto that fail
topic um so this way if the crawler goes down the message will still be processed just by another worker who knows that
right time because it's in the message so this works it's it's just a bit of a mess um and so what we could do instead
which is wonderful is that we can use Amazon sqs here and in fact that's what I'm going to do in this design I'm going
to use sqs and conveniently sqs actually supports retries with configurable
exponential back off directly out of the box so initially messages that fail to process are retried once per visibility
timeout and that default is 30 seconds now in sqs a visibility timeout I threw
a new word at you there it's just the period of time when other consumers are prevented from receiving and processing
messages so if a crawler pulled something off and the visibility timeout prevents anyone else from seeing it I'm
actually going to go into go into that I think a bit deeper here uh really soon
but this this timeout this visibility timeout increases then exponentially after each retry attempt so we put it
back on 30 seconds and then 2 minutes 5 minutes becomes 15 minutes um and this
solves us needing to implement that ourselves in Kafka by just configuring it via configuration file with sqs
that's awesome um so this is great but we're not totally out of the woods just yet the thing that we need to consider
now is that we don't want to retry indefinitely that would be foolish the reality is that maybe after our fifth
attempt this site is just offline it's an old URL it's a bad URL that server no longer exists this website's gone out of
business whatever it may be so you want to set some Maximum and maybe we want that to be five attempts and this can be
said again just by an sqs configuration file it's the field approximate receive count is what it's called but you could
set that to five and then what that does is that if that five is reached if that approximate receive count is reached
then failed URLs are automatically moved to a configured dead letter q and so
you'd have some dead letter Q in our case in our AWS ecosystem we have some dead letter Q here this is just another
message Q uh these dead letter cues are just they're special types of message cues I guess you can think of them as
that store messages that can't be processed so on Fifth attempt uh let me
just put it here why won't it let me type so on
Fifth attempt move to dead letter Q I'm going to put that right right there and
so we'll retry with exponential back off via sqs on Fifth attemp we'll go to the dead letter Q these dead letter cues are
probably web pages that are down so we don't care about them at all we could talk to the product team or who whomever else to say what do you want us to do
with these is there something special um but that handles
that so there's really no expectation from any level of candidate that you know that level of depth or intricacies
about the difference between different messages use CF sqs that is one potential area where you can show a lot
of technical depth and so if you're a staff candidate I'm expecting to see technical depth in three-ish places and
maybe you have a lot of experience with message cues so you could have shown that depth there like I just did fantastic that's one of your places
senior candidates I want to see like one to two really deep places um again that
could have been one of them for for mid-level candidates the expectation for that level of depth is a lot lower so
alternatively if you you didn't know this this level of detail then what you would have derived is just that an inmemory timer certainly won't work I'll
need some exponential back off and maybe that solution that I mentioned about just keeping it in a separate topic with
State about when to run it is totally sufficient and that would have been a great answer both at senior and staff
and of course at mid level um and then you'll just need to look for other opportunities throughout the interview to go into more
depth now we keep we keep talking about what happens if a crawler goes down we should probably go into a bit more
detail there so what happens if one of these crawler workers trying to fetch a URL and and one of them goes down well
pretty simple we're going to just spin up a new crawler that Parts straightforward uh the good news here is that the URL is going to stay in the
queue until it's confirmed to have been fetched by a crawler in the HTML store and blob storage so even though a
crawler kind of we say it pulls off the queue pulls a URL off the que strictly speaking this is a little bit inaccurate
that URL will stay in the queue until it's confirmed to have been processed and then it'll be removed from the queue
and so just quickly the way that that actually happens cuz I think this is is is pretty interesting is different based
on message CU so in the case of cfco what happens is that each message is uniquely identified by an offset and
then crawlers are all part of the same consumer group and consumer groups are used just to ensure that a given message
is read only once by Any Given worker in a consumer Group which is what we want here right so we don't process the same
URL multiple times and then when a URL is successfully fetched meaning we've stored it into S3 then the worker needs
to commit that offset back to Kafka so that other crawlers know that that message has been processed and then that
message is is committed others won't pull off it and then messages are only deleted based on some configurable
retention policy so I think the default retention policy in CF is is 7 Days this can be changed and so that means that
those messages that have already been read are going to be deleted after 7 days I think in cfco you can also do
this by size uh I want to say like 10 GB is the default nobody quote me on that I
might be making it up um but I think that if this queue gets to a certain size then we'll also start to delete um
some of those messages that have already been confirmed to be readed so that's the way that Kafka does it uh of course we decided in our case to go with sqs
sqs um uses that visibility timeout that we talked about so messages uh basically
remain in the queue until they're explicitly deleted and instead we use that visibility timeout to just hide
messages so you have that default visibility timeout one crawler pulls it off say that time out's 30 seconds that
message is still in the queue but it's quote unquote invisible to other Crawlers for 30 seconds if this crawler
went down the one that pulled it off then after 30 seconds that visibility timeouts elapsed it can be seen now to
be pulled off by other crawlers um that's the way that it it works there and then if the crawler is successful in
storing the HTML then it can issue a command back to sqs to basically delete that message off of the que it's the way
that it works there so again you don't need to know this level of detail necessarily in your interview it's one place where you could go into depth you
sure certainly shouldn't waste an exorbitant amount of time on it um but I think it's really interesting and good
to know so do want to share it with you all so with fault tolerance and
robustness checked off our list boom we can move on to the next one which is how can we ensure politeness and adherence
to that robots.txt so first off let me come over here and show you all an
example I'm going to zoom in so you can read an example robots. txt so again robot. txt is a file that
can be on the on each of the web servers that specify rules per domain so here's an example the user agent line specifies
the crawler uh that these rules apply to so
in this case star just means it supplies to every crawler whether you're Google or whomever else and then disallow says
the paths that you're not allowed to crawl so you cannot uh crawl any path in private in this case and then the crawl
delay specifies how many seconds a crawler should wait between requests and this is in seconds so between crawling
any two pages on this domain we need to wait 10 seconds it's a long time but this is what a robots.txt looks like so
what we're going to want to do then is that anytime that we fetch a domain for the first time we're going to need to go
up and get its robots.txt and then add some additional State here so let me
move all this over so that we have some more room and I'm going to add an additional t table uh is it going to let
me maybe I'll just do it right under this one so I'm going to add a domain table to our metadata DB here and this
domain table is of course going to have the actual domain it's going to have the last crawled time maybe the last time we
crawled this domain and then it's going to have all that information from the robots so maybe the user agent the
disallow and that craw delay craw delay so we'll pull all that in here so the
first time that we fetch any domain we're going to get it to robot stack txt we're going to open up the uh go into the URL metadata this is easy right
we'll just check if it exists if it doesn't we'll fetch it for any given domain put it here and then on any
subsequent craws we're going to look here for any of these rules and so the very first thing that we're going to do
for any given URL is that we're going to check its domain and we're going to see is this path allowed if it's not allowed
let me move this over so you all can see a little better if it's not allowed then we'll acknowledge the message essentially moving it off of the Q
removing it from the que and so of course in Kafka case uh this would be you know moving the cursor in sqs case
this would be explicitly deleting that message it's not allowed it's something that we can't crawl uh the next thing
that we'll do is we'll check that last crawled time and we'll see if the crawl delay uh exceeds basically now minus
last crawl delay is greater than now minus last crawled time is greater than crawl delay and hopefully that makes
sense and if so we're allowed to crawl it and if not then we'll need to put it back on the Queue and in the case of sqs
we'll set that visibility timeout to be whatever that crawl delay is so we'll wait that amount of time before we do it
again so that's very simply how we're going to adhere to robots.txt now a couple things that are worth calling out
uh the robot set txt might change so is it worth us periodically fetching it maybe I'm not going to go into detail
there that's something you could talk about in your interview maybe this has some TTL if the TTL is expired we go and
fetch the robots.txt again again of course this read maybe is slow um and so
maybe you want to have a cache here that caches that domain specific data to make this a little bit quicker in memory
certainly an option I don't know that it's the most important thing here considering we're really IO Bound by this web page fetch but it's something
certainly to consider um the next thing that you're going to want to consider is just the
general rate limiting to be polite so the standard limit across the internet
is that you shouldn't send more than one request a second this is sort of the industry standard so even if no crawl
delay is set as most companies uh and most websites won't have a craw delay set you want to make sure that for any
given domain you're not uh fetching it more than once per second and so to do
this we can simply have a rate limiter we can add a rate limiter here this can
be something like reddis so this going to be an inmemory domain specific rate limiter so it's going to be a limit per
domain and we can have some like sliding window algorithm for example that counts the amount of requests that we've made
in the last second and make sure that we don't make uh more than that number of requests so our crawler is going to need
to also hit our rate limiter here this should be quick we're talking tens of milliseconds probably uh check our rate
limiter see if we're allowed to crawl if it's not then again put it back in the queue with some visibility timeout and
you'll want to be wise here to apply some Jitter and so Jitter is just the concept of adding some random time such
that if we had 10 crawlers that all for example had the same domain and they all exceeded the rate limiter they'd all get
put on the Queue they'd all get pulled off then again around the same time potentially they'd hit the rate limiter
again only one of them would get through and that process would repeat and so by introducing some Jitter we introduce Randomness and make sure that that
doesn't happen so here's a simple setup that that is totally reasonable now you might notice that
even with Jitter you run into this problem where when you extract URLs from a given web site there's a very high
probability that many of those URLs are from the same domain so you put them on the Queue and then you have in your
queue this backlog of maybe 20 100 200 500 depending on the size of the site
URLs all from the same domain and so they all get pulled off by the same crawler they all hit either a crawl
delay or a rate limiter and they all get put back on and this is inefficient it's wasted cycles and so that's true one
area for potential depth here that I've seen candidates go into is that they recognize this problem and and their
suggestion basically and and I'm not going to put this in my design cuz I don't want to go into too much detail it's a bit abstract even when candidates
propose it but you basically have some scheduler here call it a smart
scheduler and what it does is that instead of putting these URLs directly back on the Queue we'll put these URLs
just directly into the metadata so there's more URLs here and maybe we have some additional state that says crawled
or not crawled maybe a last crawled time on any given URL and so this smart scheduler then what it does is it needs
to go fetch URLs periodically maybe every time this Q gets low it's going to fetch URLs from the URL metadata and
then it's going to make some smart decision based on an algorithm that you've crafted as to the order of those
URLs that you're going to put back on the Queue or make this a priority cue and similarly ass assign some priority
kind of same thing there so the smart schedule is responsible for making sure that we avoid that case where all
crawlers are are going through those the same domain over and over again hitting the rate limiter and hitting the craw
DeLay So this is definitely a smart thing to do just for Simplicity I'm going to exclude it from from my design
um but it's absolutely valid a good conversation and something that particularly staff candidates even
senior candidates maybe you want to bring up in the interview if you want to go deep on this particular
problem all right so that should cover politeness so now we can move on to scale to 10 billion pages and
efficiently crawl in under 5 days and so since scalability and efficiency really go hand in hand we need to be able to
scale in order to be efficient we're going to tackle those together uh it's worth noting that I really recommend you
save scalability for the last thing that you talk about and this is because the system continues to evolve so you'll
note that if we had talked about scalability right away we would have talked about scaling our crawler or whatever but we could have completely missed bottlenecks in our parser or our
paring Q CU these are things that we added later so get your full design down and then scale it at the end
so the first question that we might ask here is that we have a really strict requirement that we need to finish this crawling in under 5 days so how many
machines here how many crawlers are we going to need in order to satisfy that requirement and so we talked about in
the beginning how you shouldn't do math necessarily up front just for the sake of doing math but you should do math during your design to inform some
decision and right now I have a clear decision I need to make I have a clear problem how many crawlers do I need to
scrape or to crawl 10 billion pages in under 5 days and this will be a time now where we could do math so I'm going to
come up here and I'm going to say up front this is going to be pretty handwavy in reality what you would do
for a system like this is that you would run a test you would run a test to understand your throughput and then with
the results of that test you would multiply that out uh and determine the number of machines we can't do that in
an interview so I might say that to my interviewer I might say in reality this is would be difficult to estimate and I
would actually run a test but let me do some really crude estimations here so the top AWS instances networked
optimized instances can handle uh 400 gbits per second and so then we also
talked about that each of our Pages were 2 megabytes per page that was our average so that's what we have out of
the gate so if we had 400 gigabits per second divided by 8 bits per
bite per bite um and then we had our 2 megabytes
per page then that's 25,000 pages per second and so that's a
lot 25,000 pages per second is insane it's unrealistically insane actually
you'd be able to do that on a single crawler in under five days um now the reality is you can never Max use 100% of
the available band with it's unrealistic it's not just unrealistic it's impossible and so for our specific use
case this doesn't make sense because we have a lot of other things that are going to happen DNS rate limiting uh
delayed response times from web pages we have the rate limit ourselves we have the craw delay we have retries we have
all of these things which make it impossible for us to maximize the total bandwidth so here's where we get really
hand wavy and we're going to make just some estimate and I'm going to say to my interviewer because of all of those things I think that I'm only going to be
able to use maybe 50% of available bandwidth or maybe even 30% of available
bandwidth um and so if we have 30% of available bandwidth then we have 25,000
pages per second time. 3 and this is around
10K um you know maybe we make that 25% it's around 10K handwavy math and so now we have our
10 billion Pages that's 10 10th divided by 10 4th um where 10 to the 4th is that
10K and that gives us 10 the 6 or a million total seconds that's how long it
would take us to scrape on one machine uh assuming that we can only use 30% of the bandwidth and so then if we have
that million seconds divided by how many seconds are in a day about 10 5th this
would take us 10 days okay takes us about 10 days on a single machine so in order to do this on
just two machines uh it would be since this scales linearly we could introduce
two machines and this would be 5 days total um we want to give ourselves a little leeway for things to go wrong and
for any errors that might happen in our parsing worker so maybe we end up instead of two machines we do that
time 2 and that equals four machines so we have four of the Superduty Network
optimized AWS instances that we're going to need here to achieve crawling
and so we can update that here crawler we'll have four machines emphasizing
again that that's hand wavy what about our parsing worker well our bottleneck is actually here on scraping and so
everything Downstream of it just needs to be able to scale scale dynamically so what we can say here is that this scales
dynamically based on the Q so we don't want our Q to get too large if our Q has some backlog then we can pull up more
workers here these can be ec2 instances uh these can be lambdas kind of any
containerized configurable compute resource here that we can just scale dynamically based on the size of the quebe so you might need to implement
some logic in order to be able to do that but that's the general concept here this is Downstream of our bottleneck so
it just needs to be able to keep up now another potential bottleneck
that's often overlooked in this system is DNS itself so if we're using a third
party DNS provider we'll want to make sure that we can handle this heavy load most third party providers they have
rate limits and these rate limits can typically be increased by just throwing money at it and so given our constraint
was that we're Super Rich then yeah that's what we could do that's totally a valid option however it's worth considering what other optimizations
here might be so the first thing that we can do is is introduce some DNS caching so we already had this reddis instance
here uh so this was our reddis wow why the text get so big uh we already had reddis here which
handled our rate limiting and we can just have that same cluster also do some DNS caching so for any given domain we
only need to hit the DNS server once and then we can cache those results and just use that cache moving forward so this is
great this is going to significantly cut down on the amount of requests that we me to make to any third party DNS provider and then another thing that we
could do which is interesting is that we can actually just use multiple DNS providers and Round Robin between them
so this could help us distribute the load across multiple providers and would also not only reduce the risk of hitting the rate limit but reduce the risk of
any of those DNS providers having issue so we could have multiple DNS providers here and so this approach actually was
suggested by a staff candidate that I was interviewing just the other week uh and I really liked this idea when they suggested it it's it's super simple but
I love how practical it is so it breaks out of that like traditional academic answer and shows that the candidates
actually thinking practically about real world constraints and real world Solutions the reality is if that staff
candidate was sitting in a room with other Engineers trying to design um trying to resolve this problem after
they ran into DNS issues that's probably the first thing they would suggest let's just get other providers in there and let's Round Rob them between them so
it's those sort of real practical solutions that often times separate more
Junior candidates from more senior candidates because it shows you're not just Reg daating something you read in a book but instead you're applying a
practical approach that either you've done in the past or it just generally shows your practical
thinking now focusing back on efficiency in order for us to be as efficient as possible we want to ensure that we don't
waste our time crawling pages that have already been crawled and so this means two things the simple case is that we
don't want to crawl the same URL twice that one's pretty obvious and then the second one which is a little less
obvious is that we don't want to parse a web page that has duplicate content of that of a page that we've already parsed
so this is the case where you have two different URLs maybe even on different domains that have the exact same content
and you might be surprised this actually happens way more than you would expect on the Internet it's maybe a depressing fact of the lack of diversity of content
on the internet um but nonetheless those are the two things that we want to handle so number one don't crawl a URL
that's already been crawled let me actually instead of you guys watching me try to stumble over typing that let me
copy and paste that here so
efficiency we want to not craw eall that's already been crawled that's the one that we're going to start with so
this one's the straightforward one we're bound to have a lot of duplicates in this parser when we extract URLs so
we're going to take some web page we're going to pull all the URLs off of it and the chances are we've probably already put those URLs on our Frontier queue or
we've already processed them right and so the simple thing that we can do here
is when we get a new URL we're just going to check do we already have it do we already have
the URL is the URL already here and this should be simple maybe actually we make the URL our primary key we don't need
some ID there and so we just check if it exists now you'll note that in our current setup URLs are only added here
uh after they've successfully been parsed then we add the URL so as it stands right now we may add a bunch of
UR duplicate URLs to our Frontier queue actually so you could add another check here in the crawler maybe or what might
be best best is that we actually just in our parser worker when we put a new URL on the Queue we also put it here um
directly into the metadata DBS DB and we maybe have like a last crawl time and so your last crawl time would be undefined
when you get a new URL you'll put it on here it'll be undefined and then when we actually parse it we'll update this with
the real last craw time and with the S3 link which also would have been undefined so that would handle that
um make that the primary key that's easy you're going to have have what 10 billion of these so that's a lot we're
probably going to want to Shard this it'll be sharded on the primary key um easy still a quick look up log in no
problem this isn't our bottleneck anyway so that should work relatively easy now that second one of don't parse a web
page with duplicate content that's already been parsed um in order to do this we're going to make sure that our
crawler doesn't put something on our parsing queue that we've already parsed from a Content perspective so this is
going to need a new Step which is to Hash the HTML and so it's going to Hash
that HTML and then put that hash here and so it's going to put that hash there
and then we'll want to check we'll hash that URL look in our URL metadata does
that hash already exist if it does don't put it on the worker if it doesn't do put it on the worker and now the real
question becomes how how do we do that check and how do we make that check be efficient enough and so one thing that
we can do and I think this is probably the best answer is that you can add just a global secondary index I think we said
we were using Dynamo DB here anything would work but just to make this all tie together I'm going to say we're using
Dynamo DB and so I'm going to add a global secondary index on this hash and
so this should make this quick up pretty efficient this is going to be log in now it should be more than good enough and
us to be able to check for that inclusivity um especially since you know we're
bottlenecked mostly on this IO not on this IO these are going to be collocated within the same uh virtual private Cloud
right that's what they're called um so that's going to be quick enough now the other option is that we have kind of an
auxiliary inmemory hash set um and so this could be that we have reddis here
and then we use a reddis set and we have a Redd set with those hashes and so we
just need to check then reddis to see if the hash exists store them there as opposed to in the secondary index now we
have some issues where if reddis goes down maybe you want be writing to Persistence of course there's some things that could show up there we also
have the fact that this could be a lot of data so another place where we could do math we have our 10 it doesn't let me
type in there okay we have our 10 to the 10 10 pages each hash is going to be
maybe something like 20 bytes or so and so this ends up being 200 gigabytes of
data which is a lot but you're going to have a single rdus instance that's 250
56 GB of data so this could still fit in a single rdus instance um given that we weren't money constrained like this is
great this would work whether it's the global secondary index or this they're both totally fine trade-offs of course to discuss in your interview is that
this is additional Hardware additional cost and additional thing to make sure that we maintain fault tolerance if it
goes down this is slower it's n log n or excuse me log n this one is O of one um
and given that this is in memory nothing goes to diss this is tens of milliseconds so that's a good tradeoff to discuss now something I I see
candidates do all the times in interviews and usually Unfortunately they don't justify it but they say oh
I'm going to use a bloom filter I'm going to use a bloom filter right here and so first of all what's a bloom filter a bloom filter is a space
efficient that's the important part space efficient probabilistic data structure that's used to check for set
inclusion just like a hash set so you can basically say is this thing in a set just like we're doing here um but in a
space efficient way so you basically trade accuracy for space efficiency see so it'll be far less than 200 GB but now
false positive matches are possible and false negative matches are not so in
other words to say that more clearly a query could return either possibly in the set or definitely not in the set and
so in our case we're checking we're saying is this thing in the set and it'll return well it possibly is and
that's going to have some error margin and so this means that we could have those false positives where it tells us
that something is in the set even though it's not basically telling us we've already parsed content even though we haven't uh and then we won't put it on
our parsing queue and we'll lose that content and so maybe when we're talking about 10 billion URLs that's not a big deal there's not going to be a ton of
false positives so who cares maybe or maybe it really matters that we get all
the text on the internet of which that's a bad option this is a trade-off something to discuss with your interviewer but all in all given the
size uh and the lack of constraints here unless my interviewer told me that I need to have a really small rdus
instance I wouldn't even consider the bloom filter I don't consider it actually to be a very good option uh I
bring it up here only because it's something that so many candidates when I ask this question talk about and frankly
I see it almost as a bad sign when they do because they don't set up the problem they don't say that I'm memory
constrained here in redis and as a result this is my solution they basically just say I need to check for
set inclusion of a hash so I'm immediately just going to use a bloom filter they don't consider the global secondary index they don't consider just
keeping it in redus and it's clear to me that the reason they're doing this is because my guess is that this Bloom
filter is kind of prominence in literature maybe in Alex shu's books or some of these other things that's my
guess grocking whatever um so people are kind of just used to regurgitating that and it shows that you know sure they've
read some things but they're not really thinking thoroughly about what the best option here so I personally would go for the global secondary index but this is
also totally fine now the last thing to round out efficiency that we just want to be aware
of something called crawler traps so these are pages that are designed to keep Crawlers on any given site
indefinitely they can be created by either having a page that links to itself many times of course we've talked about how we just handled that um but it
can also just link to different pages in that same domain over and over and over and over and over and over and over and
over over again nearly indefinitely maybe hundreds of thousands of times or something all with basically no content on that page so if we're not careful we
could end up just crawling and crawling cing and crawling and crawling and crawling on a single domain not getting any useful information so fortunately
the solution to something like this is pretty straightforward and we can just Implement some max depth for crawlers so
we can say like our our max depth is 20 or something like this and then we can add a depth field here to Any Given URL
in our metadata um and so every time we follow a new Link Link we can increment
this depth field by one if the depth exceeds our threshold our threshold then we're stop crawling so this will all be
done by the part worker the parse worker when it adds a new URL will check the the the depth of the URL that it's
currently parsing and then add for the new URL that old depth plus one if that
depth depth is exceeded I don't know why that's a hard word for me to say right now if that depth is exceeded then we
won't put it back on our Q so that should be relatively straightforward um okay so let's let's
take a look we handled fault tolerance politeness scale and efficiency and at this point there is our semi- beautiful
design this thing covers all of your functional requirements it covers all of your non-functional requirements and this would certainly pass an interview
at senior this is far more than you would need to do to pass an interview at midlevel if you were able to have that
initial highle design that we talked about and then you were able to kind of competently answer some of my my
follow-up interview questions about retries or about things going down here or about how to handle efficiency of not
re uh uh you know reparsing the same URLs or or content if you were able to
do that then great um You probably pass as a mid-level candidate if you arrived
at something like this but without kind of the deep depth that we showed here or the Deep depth that we showed here um
maybe you didn't talk about DNS or you know there could have been things that you left out that's probably passing at
senior and then for staff you maybe don't need all of this but you needed to show depth in some places so we showed
some opportunities this could have been a place for depth we just talked about that the different types of message cues was a place for depth um talking about
DNS some solutions there of course was a place for depth so lots of opportunities there's no strict rule on where those
places are you'll want to find them and make sure that they make the most sense to you and they're the places where you have your
expertise now I before I close off here I want to mention what some other deep Dives could be I'm going to paste some
of these in here actually uh maybe I'll just paste this directly off of our
website so oh shoot that looks like trash so
instead I'm going to write them um so some additional deep Dives one is how to
handle Dynamic content this is something you might have wanted to ask your interviewer directly up front so many
websites are built nowadays of course with JavaScript or Frameworks like react angular Etc and this means that the
content on the page is not just HTML um but instead it's loaded dynamically with JavaScript and so to handle something
like this we would actually need to have a headless browser like Puppeteer or something um in this crawler which is
able to render that JavaScript um before we can extract the page and so that's going to make this way slower way more
errone and way more expensive but that's something to note there another one is how to monitor the health of the system
that's something that you might want to talk about of course splitting it into different phases helped but you can have
monitoring Services data dog New Relic whatever to monitor where URLs are in each of the phases respectively and what
your main errors are um how to handle large gosh how to handle large files or
large web pages maybe I'll just say that large web pages um so some web pages might be huge
maybe we want them maybe we don't um they could cause some issues to our system we can use something like a Content length header on the requests to
just skip downloading large files that's one option something you could talk to your interviewer with uh about and then
how to handle continual Updates this one's more common particularly if you were told to design a web crawler for
like a Google or an indexer or maybe we're told that we want to retrain this model every couple of months or so so we
want this crawler to continually run um and in this case I think that best solution is we had talked about that URL
scheduler that you might add here as opposed to just adding things back on the que and so I think that's the right
solution you have some smart URL scheduler again it periodically queries your url metad
database here to determine what we put on the frontier que as opposed to putting it directly here and then we would probably have that last crawled
time uh to just check some logic if we haven't crawled something in you know in minutes days hours whatever put it back
on the Queue so some additional deep Dives I'll leave with you guys additional deep Dives of course those
aren't the only ones as well um but those are some good ones so hopefully you're feeling good hopefully this was
clear enough and that it made sense we've SA all of our functional requirements all of our non-functional requirements we're leaving the interview
excited happy knowing that we just crushed it and we're about to land that new job so Kudos thanks for following
along just five days so thank you very much again
Conclusion
everybody for watching um really L the reception to these videos going to continue to do it I know I'm a little
I'm a week late on this one I was traveling so apologies um but of course
if you have an interview coming up particularly at a big Fang and you want to get this Hands-On practice I'm biased
I know that um but bias aside I really think the best thing that you can do is practice with an interviewer who works
at some of these big companies and has asked these questions before and they'll be able to show you exactly what they're looking for so head over to hello
interview.com see if it makes sense for you to schedule a mock interview um I'll be looking at the comments as I always
do so please follow up with questions anything that you think I did stupid let
me know uh always happy to hear that feedback and most importantly best of
luck with your upcoming interviews you guys are going to do great

