welcome back everyone today we're going to be designing an ad click aggregator so just as a reminder I'm Evan I'm a
former meta staff engineer and interviewer uh and I'm currently actually the co-founder of hello interview.com and so hello interview is
a site where we help software engineering candidates prepare for their upcoming interviews and we do a lot of
things to do this but one way is via mock interviews with current and former Fang Engineers just like me uh we also
have a lot of free written resources AI Tools in any case I highly recommend you all check it out but I won't blab on too
much about that um ad click aggregator is a super common question it's one that's asked a lot at many of the top
companies I'm sure you guys have heard this or seen it come up uh as you're searching for common questions it's one that I've asked myself plenty of times
so we're going to go through it exactly as if this was a real interview I'll interject with tips from an
interviewer's perspective talk about what I'm looking for at each level respectively uh as well as kind of the
common Frameworks and and general strategies for approaching a problem like this now of course as always if
videos aren't your thing and you would prefer I've also written up a detailed answer key to this question over here at
hello interview.com so you can scan through this uh you'll be able to see breakdowns of what are bad good great
answers Etc if you also want to have a say in which questions we break down next you
can see this list is growing I think up to 10 then you can click on that suggest a question and vote for the question
question you want to see next I'm working on design a distribut a WebCrawler right now since that's the the one that's voted most highly last
bit of housekeeping you'll get this whiteboard in the description below there's also links to the previous
questions or the previous videos as well as my LinkedIn if you want to connect and chat feel free to do so but without
further Ado let's jump into it all right before we dive into solving
The Approach
the problem let's take a moment to just talk about what our general approach is going to be what's the road map that we're going to follow to try to answer
this problem so up here I have the road map that we followed for the previous
three videos If folks have watched those was were Ticket Master Uber and Dropbox
and this is the road map that I suggest candidates follow for product design
questions these are the questions where you're designing a user facing application like Ticket Master or Uber
so we go over those the API uh and the core entities before getting into the highle design now ad click aggregator is
a little different this is what we at hello interview refer to as an infrastructure design question as opposed to a product design question and
so with these questions you take a slightly different flow through the interview you'll still Define your
requirements these are the functional and non-functional requirements of the system uh you'll still do a high level
design and we'll still go into deep Dives that satisfy uh those non-functional requirements but instead
of core entities and API which make less sense in the context of a system that is
not as user facing we instead do system interface and data flow so you'll see
this later on we'll do it together but we're going to clearly outline what data the system receives and what it outputs
this is going to establish a clear boundary of the system's functionality and then we're also going to just describe we list out at a high level the
sequence of actions or processes that the systems going to need to perform uh on that input in order to produce the
desired outputs so so a slight modification here um but only slight so
just to recap that we're going to start with requirements both functional and non-functional requirements
non-functional being really critical these are the qualities of the system and then we'll do that system interface
and data flow I just described we'll sketch out a highle design this will be us going over to the Whiteboard and drawing the components with arrows for
the main goal of the highle design is to satisfy our functional requirements of our system so it'll be relatively simple
at this point and then we're going to end with our deep Dives and our deep Dives are going to be where we go deep
to satisfy the nonfunctional requirements of the system so all of the qualities of the system that we end up
defining so let's get started and and walk through this flow
Requirements
together all right before we even jump into the requirements let's just take a moment to discuss what the heck is an ad
click aggregator this isn't as straight forward as being told design Yelp or design Ticket Master which are systems
that that you've probably used directly you may may not know what an ad click aggregator is so as a brief overview an
ad click aggregator is a system that collects and Aggregates data on ad clicks so when ads show up on websites
users click them those users get redirected to the ad and we log that click and then we're able to show
advertisers metrics how effective is their ad how many users are clicking on it over what time periods Etc um so
that's kind of a high level what a n click aggregator does it actually leads us really nicely into our functional requirements where we're going to go
next so when you start any interview you're going to outline the functional and the non-functional requirements the
functional requirements are like the features of the system uh this is the highlevel you know users what do users
expect from this system and users might be external users internal users they may even be machines or apis but what's
the expectation for this system uh I'm actually going to paste in the requirements so you all don't have to
watch me type like in some of the previous videos and we'll go over them together so the first one is that users
click on an ad and the expectation is that they get directed to that advertiser's website you click on a Nike ad you go to nike.com pretty easy we'll
talk about how to accomplish that and there's a little bit of nuance there the second functional requirement maybe the
more interesting one is that advertisers expect to be able to query for click metrics over time so they might have a
query to say for my Nike campaign I want to see how many clicks we've had over the last week maybe with a granularity
of an hour and then they zoom in to the last day and they want to see with a granularity of 1 minute and so that 1
minute is the minimum granularity that we're going to support now in an interview it's often
times useful to be on the same page with your interviewer about what's out of scope so it's not necessarily a
requirement that you write this don't feel like you have to some candidates kind of really pressed to try to get
something here it's only if it comes naturally that you have some questions for your interviewer that are clearly or
that you want to get kind of agreement that they're out of scope then you could do this some things that I might want to
clarify out of scope is AD targeting and serving basically that decision of which ad shows up on the page for me we'll
call that out of scope we'll abstract that away we're not going to worry about cross device tracking we're not going to worry about integration with offline
channels so we're worried about just on our website like you could imagine we run Facebook or some other site just the
ads that show up on our site not us having some ad platform that allows you to show our ads on other
sites great so those are our functional requirements of the system next up is we
do the nonfunctional requirements and so the non-functional requirements are the qualities of the system what qualities
does this system need to have in order to provide a good user experience and
that user experience again might be an external user an internal user whatever it may be in our case it's our users and
our advertisers and so before we get into the non-functional requirements
particularly for these like infrastructure design questions it'd be good for us to get a sense of scale
first so I might ask my interviewer uh what's the scale of the system specifically how many ads are we going
to support at any given time and they might tell me in our case we're going to go with 10 million ads at any given time
on the platform and then we'll do 10,000 ad clicks per second at Peak so at our
Peak we'll have 10K ad clicks per second that's important we want to know that because that's going to have some influence on our design particularly
around scalability so now as we go into those non-functional requirements this is
where you think through those ility statements I just mentioned one scalability there's also low latency
there's the Integrity security item potency like these are some of the terms that you start thinking about with
non-functional requirements but instead of just writing those down plainly and many candidates do this for what it's
worth they just write down those words and it's it's wholly uninteresting instead identify which of
those are uniquely relevant to this system and then do two things put them in the context of this system
and then quantify them where appropriate so again let me let me paste in the non-functional requirements that I
sketched out here and we can talk through them so here we are so some
non-functional requirements we just talked about the scale of the system it's a lot 10 million ads and 10,000 ad CPS per second is is pretty decent scale
so we're going to need scalability but not just scalability scalability to support a peak of 10,000 clicks per
second we also want low latency but but again not just low latency we want low latency analytics queries and we want to
bound that to be less than 1 seconds so we put it in the context of the system what needs to be low latency the queries
from advertisers and then what's the quantification less than one second uh
we want the system to be fault tolerant and have high data Integrity frankly I actually could have put these in the
context of the system a little bit better but this basically means that we don't want to lose clicks um this often
times influen is even how much we pay out advertisers or how much they need to pay excuse me um so we want to make sure
that these click data is accurate and then we want to make things as real time as possible so on the analytics queries
that data should be as up to dat as quickly as we possibly can at least within that one minute gr
granularity and then lastly something that'll be important is this item potency of add clicks so this goes
towards the security of the system people often times want to spam uh systems like this in order to make it
look like an ad is getting clicked on maybe more than it is and so if a user goes to an advertisement and click click
click click click click click click click click click or they have some bot do that we should only count that as one click so any given user should only be
able to click on one particular instance of an ad or ad placement uh once some
things out of scope I'll just mention we're not going to worry about spam detection beyond the item potency concern you know real systems have
complex machine learning models that handle that we're not going to be able to filter by additional things in our
analytics like demographic profiling or or setup conversion tracking or anything like that we're going to keep it
relatively simple so at this point we have a pretty good understanding of the requirements of our system and what we
need to build um we're going to take this and move on to the next
System Interface & Data Flow
section now that we have the functional and the non-functional requirements down
the next step for us is to do that system interface and data flow and so what does this mean again this means
clearly outlining what data the system receives and what it outputs so we're establishing that clear boundary of the
systems functionality we can start by doing that so for example the input to
our system is going to be click data that's coming in from our users and then
also you know uh Advertiser queries so Advertiser queries those are coming in on the other side from the advertisers
those are the two inputs the outputs respectively then are from the users the
output's like a redirection and then from the advertisers the output is the aggregated
click metrics right so those are the inputs and the outputs of our system now in the actual interview if this is
useful to you do it if it's not don't for this question it was pretty straightforward so maybe we could have
skipped it um but I think it's still a good step to follow it really kind of helps build things linearly in your mind
and makes it a lot easier for when we now go into data flow and in this data flow section we're just going to jot out
a simple linear list of the steps that are necessary to transform our input to
our output so this could be as simple as something like this first is that we
have click data comes into the system cool that part is pretty straightforward next we know that user
is redirected Okay the third thing is that we probably want to validate uh that
click data make sure that we hand that item potency concern that we talked about in our non-functional
requirement and then the next thing that we would do is we would log that click log that raw click data so click data
logged the next thing is that we need to aggregate it click data aggregated so
data comes in we validate it we log it and now we run some aggregation process over it in order to make sure that we
can put it in a format that's eventually read optimized and so that we can have
the aggregated data queried by advertisers all right this is kind of the highle flow of how our systems going
to work and importantly this highle flow should meet all of your functional requirements that you outlined earlier
as it does here users click and get redirected advertisers can query those steps are one two and six
respectively um and then you know it should take advantage or take note of your inputs and outputs that you define
so the goal here is that you have a really clear understanding albeit incredibly high level of the steps that
are necessary and you're going to use these steps to inform Your highlevel Design which is where we end up going
next so the key with these interviews is that each of the sections before in this
road map fuel or inform the subsequent sections so the functional requirements
and in part the non-functional requirements but largely the functional requirements informed our inputs and outputs in data flow here and our data
flow is going to inform our high level design and then we're going to go from there so here's our high level data flow
now let's get into that high level design all right here's where the
High Level Design
interview starts to get a little bit more fun we've set the foundation we've laid the landscape we know what it is we
need to build but now it's time to actually build it so we have the Whiteboard we use our squares circles Etc arrows and we start to sketch out a
high Lev design of the system and as a reminder the goal of this highle design is to satisfy our two core functional
requirements that's the main goal here and the way that we're going to do that is by ensuring that we have a high level design that kind of follows and supports
this clear data flow that we outlined which itself was derived from those functional requirements right so again
everything's building on one another so just a note to say that if you are a
midlevel candidate this is like E4 L4 Etc um then you probably getting to this
highle design within 15 minutes that should be what you shoot for if you're a senior or staff candidate ideally you
moved a little bit quicker you got about 10 minutes until you got here so there's plenty of time for you to do the highle
design and deep Dives so as we get started let's first just focus on this
kind of a user clicks on an ad and they're redirected to the advertiser's website it's the very first thing that
we're going to be focused on here so we can have our browser don't know why it's
audit there we go we can have our browser and what our browser is going to do is our browser is going to click on
an ad and when we click on an ad we'll hit our service which is going to
be some click processor service we'll call it so click processor service and
then just to kind of round things out for clarity we mentioned this was out of scope and I'm going to keep it abstracted but it's going to be
necessary because there's some data that we might talk about here that's going to be relevant you'll see this here in a second I have some ad placement service
first so the browser reaches out to the ad placement service says give me some ads we send it over some ads it gets the
ads from some ads DB which again it's not the focus of this interview but it's
necessary for us to know what data is going to be entering our system so this is going to have the data of advertise I
spelled that wrong didn't I I'm just going to say ads save myself the trouble this is is going to have some ad ID it's
going to have the redirect URL and then it's going to have some additional metadata that you know we don't care about this will be the actual ad the
image the text all that stuff right not that important for our purposes so the browser is going to get some ads they're
going to get rendered here a user is going to click on the ad and then that click is going to go to our click processor at which point of course
according to our functional requirements that user is expecting to go off over here to the ads website ny.com was the
example that we used earlier so there's two ways that we could do this the first way is that we send the redirect URL
here and when the user clicks on this they have the uh the redirect URL and they just navigate to the redirect URL
and then immediately after or in parallel we send the click event so that's the first way super simple super
straightforward now the downside with that approach is that whether they're sophisticated users who hate advertisers
or more likely somebody uh who who has an ad blocker what they would end up doing is that they would just extract
that redirect URL U from the Dom here and they would just redirect to it kind
of directly without ever sending this post request to our click processor so they would get what they want what they
want is to be able to go to the ad and then you know not care about the big bad advertisers getting their metrics and
being able to to to click on it and count it so they can just take that redirect URL which would be in the Dom here and navigate directly to it while
kind of subverting the process of actually loog bling that click so that's what what what could happen there um and
obviously that wouldn't be ideal another thing that we could do is that the ad placement service could only send over
the ad ID and this is actually what we'll choose to do in this case so then
when we click on it we send a click event with that ad ID and then this guy is going to have to ask the ad
DB ask the ad DB you know what is the redirect URL maybe I'll make this clear
and just say get redirect URL given the ad ID and then we'll return uh we'll log or
click we'll talk about that in a second and then we'll return a 302 to redirect 302 redirect response with the redirect
to that URL so this way they can't subvert us they have to come through us they have to get their click logged and
it's only once their click is logged by The Click processor that we can return with our 302 using the redirect URL so
they end up going where they need to go this is also nice for what it's worth because we to pend additional things to the query parameter some additional
metad data to talk about where the click happened Etc that's out of scope for our design um but gives us more control by
making them first have to come to our server and then we'll respond with that redirect HTTP response so this is the
way to kind of easily satisfy that first functional requirement now for the second functional requirement we want to make
sure that advertisers can query click metrics over time so that's where we would go next let me take a step back
quickly to just say that maybe in a real interview what you would do is you would work through your data flow here sequentially noting that we've done one
and two you'd satisfy three through six um but I'm going to kind of detour just
a bit if you all will let me because I try to make these videos show you uh kind of what would be required or what
are the expectations of a range of levels from mid-level all the way up to staff so I'm going to start with
something kind of crappy here that a lot of mid-level candidates reasonably kind of do and then we'll talk about why it's
crappy and we'll build up to something better note though if you're a senior or staff candidate you know you won't start with the crappy solution you'll you'll
start a little bit further on um towards the better solution but I'll call each
of those out as I go bear with me so again we want advertisers to be able to query click metrics so the first thing
that we need to do is we need to make sure that we store click metrics so to orient oursel again the browser has just
clicked on something there was a post request to our click processor service and now we need to persist that click
dat data so what I'm going to do is I am going to add an arrow here and I'm going to add a new database this is going to
be our click DB and our click DB is going to store that click data and so these are going to be click events those
click events are going to be things like they'll have an event ID they'll have the the ID of the ad that was clicked
they'll have the user ID if they're logged in we'll talk more about that later and then they'll also have the Tim
stamp so this is a simple click event again in reality at Google Etc ET
there's actually a lot more information that's stored with the click there's information about the user's browser demographics you know kind of this large
blob of additional metadata but as this is usually asked in an interview as I typically ask it in an interview that's
not required we keep it pretty simple so it's it's just this data so we stored The Click data in our click DB and then
the simplest thing that you could possibly do is you could have up here some query service so I'm going to call
this the query service SVC for short and then I'm going to have my advertisers browser so
Advertiser browser so my Advertiser decides that they want to see all of the
clicks from the last week or so the query service then constructs a query to query our click DB to get them that data
this is the simplest thing that you could possibly do and especially for mid-level candidates like this is this is a great start it's not going to be
passing in an interview but it's a great start a couple things that we'll know is that this event database has to be
optimized for a lot of Rights so for whatever reason in in most of like the system design especially interview
Literature Like Cassandra is the main choice here um frankly there there are plenty of databases that work well here
um but let's let's go with Cassandra for now Cassandra is a fine choice and Cassandra uses a sword structure that
resembles lsms so what it does is it it inserts and updates into a log like
structure which is known as a mem table and importantly this mem table is in memory which allows these rights to be
so fast and then periodically we'll flush those mem tables to disk into a
file that's called an SS table I won't go into too much detail there feel free to look that up on your own if you're interested it's not strictly necessary
to know these sorts of things in an interview the extent would be that you know Cassandra is optimized for rights
ideally if the interviewer were asked you why is it optimizes for right you could say a little bit more um but
frankly that's not a question that's asked all that often um but importantly
while these SS tables are optimized for reading a specific r so for example if I want a specific row
based on an event ID that's that's easy and fast in Cassandra they're not optimized for range queries or
aggregations which is exactly what we need here right so we're going to end up
having some query and actually let me maybe come up here and copy and paste what one of those queries would look like so that you guys can see it I'm
going to pull this right off of the document from our written resources that we have um so the query might look
something like that right I want to get all of the the total clicks um or I want
to count the number of total clicks and from event unique users Group by a given
ad ID over some period of time and so this aggregation query is going to be super super super slow it's going to be
super slow on Cassandra in particular but the reality is it would actually still be really slow on post grass
Dynamo DB Etc especially as you open up these time Windows realizing that there's 10,000 of these clicks per
second that's a lot of rows to munge Aggregate and count so for that reason
when when an Advertiser goes to hit the query service this isn't going to satisfy those non-functional requirements which require that this be
pretty fast right less than one second this will be certainly longer than one second so it's bad um now often times I
say get down something simple that works for the functional requirements and then move on to the Deep Dives and satisfy the non-functional requirements and the
Deep Dives and that's true I stand by that but for some things it's like you
can't have something that is so bad in your eye Lev design you should have it be a little bit better than this right
so I'm going to say this would not this would not pass as a high level design at any level of interview including
mid-level um so let's do something better right the key here is that this query is slow so instead we're going to
need to aggregate the data and then put it into some database in a way that it's
read optimized so this database is write optimized it can handle lots of wrs coming in quick great but it's not read
optimized the read is super slow so we can handle that by pre- aggregating and
then putting it in some read optimized database in a format that's read optimized hopefully that makes sense and it's pretty straightforward so let's
talk about the the ways that we would do that now what we can do is we can use
spark so we can put a spark layer here spark and what spark is going to be is it's going to be a map ruce job so it's
essentially going to go over Cassandra it's going to uh go across all of the shards from Cassandra get all of the
data and then aggregate them so run some map reduce job to aggregate them at these minute intervals and so it's going
to write them at a minute interval let me move this up it's going to write these at a minute
interval to some read optimized database and so we can call this Su olap
database olap stands for online analytical processing um they're kind of the common database of choice when
you're doing query aggregations now given how simple actually our functional requirements are of just looking at ad
click data over time Windows ol op's probably not necessary like you could use anything here you could use a Dynamo
DB you could use post graphs whatever um but in a real system you would have a
lot more Dimensions that you could query by in which case olap becomes more more interesting more necessary um let me
make this Arrow be the other direction okay and then spark needs some
way to start so let me just just kind of throw that here so KRON scheduler
boom so what's going to happen here is we're going to have this Chron job and this Cron job is going to kick off spark
every say five minutes or so and so every five minutes Spark's going to run it's going to grab all of the data that
is coming from in the click DB and it's going to aggregate them using map ruce and then it's going to write those
aggregations to our read optimize database here and those optimizations might be at ID minute so this is like
the modulo minute right not second are not events anymore and then total clicks
right so that's kind of the main data that's going to be stored there let me write that in the same format with our
dashes and now when the advertiser goes to query this is going to be so much easier they're going to give us the ad
ID that's already been aggregated um and it's going to be significantly quicker
right hopefully that makes a lot of sense um now one thing you might be noting is like why two databases here
why not run spark do some aggregation and then write it back to the same database and so the first argument is as
I mentioned this is going to be optimized for wrs and not optimize for
reads even after being aggregated because of the way that we use SS tables here now you could say okay cool that's
fine don't don't use Cassandra and you'd actually be smart to say that like the reality is
10,000 uh clicks per second thus 10,000 transactions per second that's not that
much like we can handle that on a well optimized postgress instance on good Hardware we
can handle that with Dynamo DB we can handle that with most modern databases and if you have postgress then you know
we've got some indexes built and it's much easier to do range queries so that's totally possible but even with
that being said there's two main reasons why you'd want to separate out these databases so the first is that it
reduces contention so separating the right heavy and the read heavy workloads reduces contention and resource
competition which is going to you know improve the overall performance so if you have a ton of Rights uh reads coming
in or excuse me a ton of Rights coming in then your reads might be slower because they're waiting to get a
thread and then the second thing is Fault isolation so issues in the right
path don't necessarily impact issues in the read path and vice versa so if this goes down or we have some problems and
we'll talk about fault tolerance later but our analysts can still read and if this goes down and our analysts can't
read anymore well we're still logging cck and we'll be able to back fill so that's going to be that's going to be really
important um so this now is passing for
a mid-level candidate um this is actually getting pretty close to overall passing for a mid-level candidate for what it's worth but we'll still going to
get one of those non-functional requirements this is a great starting point for senior and staff candidates
but we're going to expect a bit more specifically because you'll know some of our realtime uh non-functional
requirements aren't met we haven't talked about item potency fault tolerance um we did kind of do okay to handle
these two um of the nonfunctional but that's where we we ultimately end up
going next so let me stop here and then we'll we'll take it to deep
Dives all right now it's time for us to move on to the Deep Dives so we should have satisfied our functional
Deep Dives
requirements and now we're going to move on to our deep Dives with the goal of satisfying all of these nonfunctional
requirements so let's do exactly that the first one that I want want to kind of pay attention to is the latency
issues so we want to be able to get data into our system as real time as possible
and especially this minute granularity what would happen with our system now is if we run our spark job every 5 minutes
or so then it's going to take you 5 minutes until you can see how your ad is doing and as an Advertiser maybe you
just launched an ad and you want to see right away or maybe you just really want to see what happened in that last five minutes and right now we don't show you
any of that so that's not great so we could obviously run spark more frequently we could take that down to
two and a half minutes to one minute maybe 30 seconds but eventually you reach a point where you run the spark
job so frequently there's a lot of overhead to start a spark job to run the map produced to get the rights and it's
decently computationally expensive so you you hit a limit of how frequently you can run this thing so let's talk
about what some of our other options are instead now in a real interview I would probably just you know delete components
here and build upon this but because I link these whiteboards in the in the comments or in the description of the
YouTube video I'm going to leave this here and I'm going to come down and actually just paste a new version and this is what we're going to work off of
now so this is kind of the spark solution it's okay potentially passing even for a mid-level candidate if we
could talk about some more things in depth um but now is where we're going to go a bit deeper particularly for those
senior and staff candidates so Spark's not going to cut it anymore I'm actually going to go ahead and get rid of spark
we just talked about the reasons why it's not great instead what I'm going to do is I'm going to introduce a stream
and so I'm going to introduce a stream like CFA or Kinesis I'm going to do Kinesis uh either one would work this is
going to be a click event stream and so when clicks come in our click processor
is going to put those clicks on the stream and from there instead of having
our our click DB we might actually come back to that just a quick note but I'm going to remove it for now
uh we're going to need a stream aggregator and so I'm going to put in something like
flank so I'm going to have Flink here uh spark also actually supports stream
aggregators uh kind of a different implementation of spark than the one that we had previously um but I'm going
to have Flink here and so what Flink does is it takes click Events off of the stream in real time and it Aggregates
them so in memory it keeps some inmemory data structure
that's well I'm going to get rid of those cuz that seemed too hard to write but you know is the minute maybe this is
maybe this is minute 45 um and count and the counts at 12 and it keeps this in memory and keeps
updating them and what you can do in Flink is that you specify an aggregation window and so in our case our
aggregation window would be 1 minute and so for 60 seconds it's going to say this
is minute 45 and it's going to continue to increment this as it's reading off of this stream D ding ding ding ding ding ding and it can do this for each of the
ad IDs so for add so for ad ID number
one this is minute 45 and we're going to count 12 more come in this goes to 13 14
15 16 17 whatever as the minute ticks and it becomes minute 46 then we write
this aggregated data off to our database so at this point bang we can write that
data directly here and so this guarantees that we're
at least much more real time now at this point you can read data at the minute marks exactly after a minute finishes
maybe not exactly but nearly exactly after a minute finishes you can read that minute's data because it was written directly from Flink uh which was
our stream aggregator now the aggregation window let me write that down because that's useful so the
aggregation window this is the terminology that describes the period in which data is grouped or aggregated so
that was one minute for us and then Flink actually supports something called flush intervals too and flush intervals
are super crucial for latency sensitive applications like what we have here so we could Define maybe a 10-second flush
interval what flush intervals are is they're the interval at which intermediary results are flushed from
the system so we can be counting in the minute right and keep aggregating over a
minute window but once we hit second 10 we'll write whatever we have and when we hit second 20 we'll write whatever we
have and we write hit second 30 we write whatever we have until we get to the minute and then the data is complete and
what this means is that in an ad as an Advertiser if it's 427 as it is for me
right now and it just started at 427 then after 10 seconds I can read the partial data so nearly in real time I
can know how many clicks have come in in the first 10 seconds of this minute at least right so you end up kind of seeing
a graph probably seeing these right like if you have a graph and maybe this is our data this is time at minutes this is
the number of clicks and then here's our kind of partial data and it would be dotted is the way that this usually
happens over ux right showing that it's partial it's not complete data this is where it is up until this point so we'd
be able to do that with these flush intervals in Flink which is super nice
so ultimately this system is much better because it satisfies that real time or
new realtime component now our advertisers can get the data almost immediately so this for senior and staff
candidates could be where you started many candidates that I interview for this question already know that this is
going to be a stream processing question they start with this as their high level design and that's great fantastic we'll
build on it from here some candidates don't they start with that uh kind of more simple bash processing
implementation with spark above that's okay I usually then point out to them I don't like that 5 minute um kind of
interval how can you do better and then they arrive at something like this from this we build on the the further the
further deep Dives excuse me as we'll do now the next Deep dive I want to tackle
is maybe the scaleability to support a peak of 10,000 clicks per second so
let's talk about that for a bit what can we do to make sure that we can scale well it should be relatively
straightforward so first off we can scale our click processor or AB placement Services horizontally so we're
going to have more instances of these we can do that dynamically most modern systems allow you to scale Services
dynamically based on CPU or memory thresholds that are reached so if we you know occupy 80% of the CPU here we'll
just pull another one up that's great so you end up having multiple of these uh I know that you know sometimes people will
represent this by drawing multiple boxes I typically don't horizontal scaling at this point is it's pretty obvious um but
worth just calling out verbally in your interview of course another thing that's that's rather obvious is that we can
have you know we'll need a load balancer load balancer API Gateway that can all
go here um so I'm going to say I'm going to use an AWS managed API
Gateway Gateway so that's going to be responsible for handling routing
potentially some middleware it's going to do some at least some load balancing um but each of these horizontally scaled
Services have their own load balancers that sit in front of them um but pretty
simple we've done that so far more interestingly is the stream we need to be able to allow this stream to scale so
in Kinesis for example we have a limit of 1 Megabyte per second um or 1,000
records per second so let me write that so this has a limit of 1,00
1,000 records per second um or 1 Megabyte per second whichever comes
first so we'll need some sharding here uh we can Shard by at ID that's the Natural Choice so Shard by at ID
um now with Flink it can also scale horizontally um so this will have more
tasks or jobs they're referred to in Flink and we can have a separate Flink job reading from each Shard doing the
aggregation by add ID so we're going to Shard by add ID here we're going to have multiple of these they're going to be
reading from each Shard respectively doing their aggregations great that's all fine given that we shed by ad ID
there's kind of no distributed contention issues because each Flink
instant is responsible for its own set of AD IDs and no other Flink job has that set of AD IDs that it's responsible
for S part's pretty simple and then same too with our olap database if we need to scale this by sharding we can do that as
well um this would probably be an appropriate time to do a little bit of math and determine kind of how large
this thing's going to get with its aggregations um I'm going to spare you guys that inline math here to but know
that that would be an appropriate thing to do you'd probably want to actually um shred this one by Advertiser
ID as opposed to ad ID because that's probably the most common query is that advertisers are
going to want to see like the performance of all of their ads gosh that spelling is horrible
Advertiser um so that's probably what you would do there this is all straightforward obvious stuff that you do in most interviews now where this
gets interesting is what happens if you have a new ad Nike just launched a new ad it's got LeBron James everybody's
clicking on it and now you have a hot Shard and particularly you'd have a hot Shard here in Kinesis and this could be
a problem this could you know be overwhelming it would likely result in increased latency but
in worst case it could even cause some data loss so to solve this hot Shard
problem we need a way of further partitioning the data basically one partition has far too many rights to it
we need to somehow further partition that and kind of the most popular approach for doing this uh is what's
called kind of the celebrity problem so you end up doing is that you end up adding to The Shard key to the primary
key some number between Zer and N so for hot shards we would do something like
this you would Shard on ad ID and then some number between zero and N depending on how popular it is so maybe this is z
and 10 and this basically takes that popular ad ID and then further shards it
n times right on to n different partitions on to n different shards so this is a really popular way to handle
that and so this is easy enough we can do this this kind of has to get handled in the click processor service The Click
processor service needs to know what's popular it needs to make sure that it does this additional uh kind of Z
through n on the primary key um or the partition key before it writes the Kinesis that's fine but then now I
talked about earlier how with Flink we wouldn't have any given Flink job or two Flink jobs responsible for the same set
of AD IDs where that could happen now so that's a problem but ultimately since
Flink is in memory here it can actually scale much better so what we would do is we would just have a sing single Flink
job or a single flat uh Flink task still for each ad ID even for the hot ones and
it would be responsible for aggregating over a set of shards which is possible Flink can aggregate over a set of
Kinesis shards so that's what we would end up doing that way each Flink job or task is still responsible for its own
set of AD IDs even if it's a hot Shard even if it's hot ad ID um we would have
no issues there so that's how we would handle scaling next up let's go back to our non-functional requirements and this
time let's talk about fault tolerance and data Integrity so specifically this is how can we ensure that we don't lose
any click data so if we come back down here let's start with our Stream So by
default these streams are distributed they're fault tolerant they're highly available you don't really need to worry about them going down this is actually
true with both Kafka and kenesa streams particularly if they're hosted and managed it's something that we can kind of look past you can assume that they're
always up that they're always available so with that assumption in mind no worries there but what happens if any of
these Flink jobs or tasks go down well that could be an issue so what we want to ensure is that we enable what's
called retention policies on this stream so both CFA and Kinesis allow you to
enable retention periods and so we can choose something like 7 days this is configurable and what it means is that
even after events get read from the consumer Flink in our case we keep them
in the Stream for that configurable amount of time 7 Days in our case and this is useful because then if Flint
goes down and it comes back online well it can just read from where it left off like that data is not gone it can pick
back up and start reading there again even if it had read it before no worries it has some cursor that understands
where it was prior to its last flush or its last commit and it can pick back up
and start reading so that's great we're going to enable that retention policy let me actually note that so enable
7-Day retention policy
great um now stream processors like Flink they also have a feature that's called checkpointing and so this is
where they'll periodically write their state to persistent storage something like S3 so you could imagine
particularly if we were doing an aggregation over a really large window here like let's say even over a day then
we'd be keeping this data in memory for a day if we went down say in the 23rd
hour then we would have 23 hours worth of data to reread off that stream in order to keep up and or catch up excuse
me and of course while doing that new data is coming in so we could get caught pretty far behind and this is why often
times we'll use checkpointing by defaulting I think the checkpoint is 15 minutes you run the checkpoint every 15
minutes it might be 10 but it's around there so a lot of candidates will when I
ask this question say I'm going to enable uh checkpointing on Flink and this is kind of like a common senior
engineer thing to say they've read it in a book somewhere they know that checkpointing is good for handling fault
tolerance um but unfortunately like astute candidates and some some great staff candidates in particular recognize
that this doesn't make any sense like why would we use checkpointing when our aggregation windows are so small our
aggregation window is only a minute so at most we have a minute worth of data that we need to go read off of the
stream at 10,000 clicks per second this is 10,000 * 60 it's not that many events
and checkpointing doesn't even really help us we're going to check point halfway through that at the 302 Mark uh
and this would just mean that we have all of this data that we're writing to S3 uh that's unnecessary you know S3 is
pretty cheap but it's still more expensive than it needs to be and given the small aggregation Windows it doesn't make much sense so I would argue that
you wouldn't use checkpointing here uh as a rule of thumb if the aggregation window is less than 5 minutes depending
on how kind of the rate of events in your stream probably doesn't make sense to checkpoint and so as a a staff
candidate as a great senior candidate maybe you would point that out you would say I know a lot of candidates might bring up checkpoints in here it's
something to consider but because of the small aggregation Windows I'm going to opt to actually not use checkpointing
that shows some Nuance there some sophistication that really sets apart those senior
candidates now one thing though is that click data M matters a ton of course if
we lose clicks we can lose money so despite our best efforts with these retention policies um with how we're
going to handle Flink if it goes down there can still be errors like there can be transient processing errors in Flink
there can be bad code pushes from employees out of order events in the Stream this can all lead to really
slight inaccuracies in our data and so it shouldn't happen a lot in fact it
should be relatively uncommon but any inaccuracies are an issue to us so
because we need really high data Integrity as defined in our non-functional requirements we're actually going to want to introduce
something called periodic reconciliation and this means that we're essentially going to have a job that runs maybe once
a day maybe once every hour kind of either of those work in this case but they're going to take that batch
processing solution from earlier and apply it here as well and so the way
this is going to work is that uh we can enable Kinesis to dump raw click events
to S3 and I think there's actually other connectors such that it doesn't have to be S3 S3 is the one that I'm I'm
familiar with here and I don't want to say anything that's inaccurate um in this recording but feel free to look it
up on your own time basically kis allows you it has some integration with these things that they call connectors and it
means that it'll dump those events as well as whatever consumer is hooked up it'll dump those to you know um to that
data store S3 being the one that that I know it certainly supports so you would dump it to S3 and then you would do all
of those things that we talked about before so I'm going to add here
my spark map reduce we'll have that Cron job which is
just going to be necessary for kicking it off of course every in this case now hour or day so we'll say day not too
important that we do it more frequently than than that um it would it would depend on the business needs and when we
need to have perfect accuracy um but then you're going to have some Boop maybe we'll call this our
Recon ciliation worker and so spark is as it did before
going to read those raw click events it's going to do its aggregations and then it's going to give that data to
this reconciliation worker which is going to be a server that's responsible for potentially
fixing uh incorrect records so it's going to compare the data that it has
potentially it's going to compare the data that it got from this spark job from this map Produce job to the data in
our database base which came from the flank aggregations and if anything's different we're going to trust the
reconciliation worker is correct so we're going to overwrite or we're going to fix that data we'd also probably want to event or alert the team at this point
too to let them know that there were some inconsistencies we'd probably have some um some logging some observations
over this as well if this ever started to increase then we know something's broken here that we need to fix but what
we've ultimately done is we've combined that first solution that we had up here which wasn't great um such so now we get
the both The Best of Both Worlds we get that real-time processing and then we also have the reconciliation in order to
make sure that our data Integrity is incredibly high now this this video this interview
maybe would would be incomplete if I didn't at least mention Lambda and Kappa
architectures so I don't want to go into too much detail here but some viewers May realize that this is neither a Kappa
nor a Lambda architecture and I'll come back to that in just one moment but for the uninitiated let me kind of describe
what both of these are so first Lambda and cap Kappa architectures they're data processing architectures for handling
large scale data processing systems like this one so in a Kappa architecture we
design for stream processing we treat all data as a continuous stream and we rely solely on that real time processing
layer so actually what we had here before we added the reconciliation this was a traditional Kappa architecture you
got a stream you have some stream processor you handle everything sort of in quote unquote real Time That's a cap
architecture now a Lambda architecture is similar to what we had here and that it uses batching but to satisfy that
issue of you know we had 5 minutes that we had to wait it has some real time
layer that's not guaranteed to be accurate but it's sort of you could imagine some other service or other
worker here that's handling the aggregation on 5 minute windows and kind of writing those to the database and
then they ultimately get overwritten um by the by the batch processing job and
so we make no guarantees that things are accurate within five minutes but we want to give you real- time data and then after five minutes it becomes accurate
that's more or less what a Lambda architecture is and so you'll notice here we're not Lambda or Kappa we we
kind of combined the two and so I I've had candidates kind of bring up to me they go oh what's going on here like is
this okay can we have both like does this break something and the answer is
of course it's okay and actually using a hybrid approach like combining aspects of Lambda and Kappa architectures it's
not frowned upon in fact it it's incredibly practical in many scenarios like this one um and I think it's really
important to remember that like these architectural patterns that you can read in textbooks they serve as guidelines
they're not strict rules so being able to adapt them to fit specific business
needs or operational context contexts excuse me this is super common um and
honestly it it shows seniority so it shows that you haven't just read textbooks and you have this academic
understanding but you understand the practicality of software engineering um so maybe to summarize this is applicable
outside of the context of this question it's even applicable outside of these two architectures Lambda uh and Kappa
and it's that practicality should almost always be favored over some abstract
Purity in an academic sense so I think this is pretty good evidence of that and candidates who are able ble to handle
that Nuance again are indicative of seniority so this is something that tops or that staff candidates and top senior
candidates will recognize of course there are potential solutions to this particularly with the Lambda
architecture which are passing as well pure Lambda architecture I would push back on the accuracy of those first five
minutes or n minutes until you handle the the batch processing as I think this solution is a bit more sophisticated um
but that is what that is um maybe I'm actually not going to write it here but
this next cut so that you guys have this um in the linked whiteboard I'll maybe
put a summary over here to the left of Kappa and Lambda architectures just so you all have it as a written Resource as
well okay this is exciting we're making great progress so I think we we have our last non-functional requirement to worry
Conclusion
about we handled fault tolerance and data Integrity we made it as real time as possible already our low latency
analytic queries happened by the fact that we added that olap database um to be optimized for reads and we're doing
the pre- aggregations we talked a bit about scalability um with sharding so the last
thing is this item potency of AD Clicks in other words this is how do we prevent abuse from users clicking on ads
multiple times so again what we don't want to have happen is that you have some Nike ad some bot or some user just
goes and clicks on that ad a ton and then it tricks our system into thinking some ad is really popular and getting
clicked on all the time right we don't want to do that so first off item
potency I think most people here are familiar with the term know what it means but to be complete let's go over
what item potency is this is right off the internet item potents is the property of certain operations in
mathematics and computer science whereby they can be applied multiple times without changing the result beyond the
initial application so to put this another way if something's item potent it means you can send the request as
many times as you want and the effect on the system usually the persistence layer of the database is going to be unchanged
it's going to be as if it only happened once and of course that's what we care about here so naturally most candidates
uh when I when I push them on item potency they think about user IDs they basically say let's make sure that any
given user can only Click On Any Given ad once and so they try to dup on user
ID this this actually has issues um for a number of reasons also we can assume
that our users aren't necessarily logged in you can be looking at a Facebook or something like this maybe a Twitter twiter or whatever actually I think both
of those applications require you be logged in but let's just say that the interviewer throws the curveball at you that they may not be logged in and this
will also solve some of the other issues um that come from using user ID but let's just assume that to be the case we
need to be able to S support logged out users so what do we need to be able to
do what we can do is generate what's called an ad impression ID so let me
first describe an add impression now if you've ever used your Facebook your
Instagram Etc you'll often times see the same ad multiple times you might see it on Monday and you might see that same ad
again on Thursday this is retargeting it's incredibly common in advertising
now in this case we want to track if you click on that one on Monday and that one on Thursday even though they're the same
ad they're a different ad impression so ad impression refers to like the
instance of the ad right so let me try to make that even a little bit clearer if I went to my Facebook right now and I
loaded up and I had some Nike ad I shouldn't be able to click that Nike ad a ton of times that should be one click
but come Thursday if I see that Nike ad again somewhere else on my Newsfeed that's a new ad impression I should be
able to click and count that one hopefully that makes sense so the first thing that we want to do is we're going
to generate we're going to generate an add impression ID so on our server we'll
generate some unique ID when we send over an ad and we'll have that impression ID alongside
the advertisement in the browser and then what happens is when a user clicks on an ad we're going to send that ad ID
as well as that impression ID to our click processing service and what we can do is we can add a cache
here say redis but this could be any inmemory cache mcache D is fine here as
well we're going to add reddis here and what it's going to do is that we are going to store I wish I had room to
label this but I think it's getting a little crowded so I'm just going to talk about it verbally uh we're going to store that add impression ID when we got
it we're going to store that add impression ID and potentially that user ID now we could say that we have a
unique ad impression ID for each user so we don't need to do that but store that add impression ID and then if a user
clicks on it again 2 3 four five times it'll come in here and before we put it on Kinesis we're going to look in reddis
and say is that add impression ID in our cache if it is we're just going to drop
it maybe we have some logging probably be good to keep track of that but for Simplicity I'm going to say we just toss
it that is a duplicate and we don't care about it so this is great this works um
the issue then becomes we kind of introduced the new challenge if you're a malicious user your this click is just a
post request and it's just a post request with the body of the ad ID and the impression and so if I'm a malicious
user I could just have a bot or something send that request over and over and over again with a different ad impression ID and I could just make up a
different ad impression ID every time right just change a character change a couple characters whatever it may be and
I'll check if they're in Redd and they won't be in reddis because they're new they're made up but they're not real ad
impression IDs they're not ad impression IDs that were created by our ad placement service right so there's a
couple things that we could do here a simple but not sophisticated thing that we could do is store each of the ad
impression IDs maybe in our ad database or in a cache and if we get an ad impression ID not only check if it's um
kind of redundant or already been seen but also check is it legitimate look in the ad DB and say did we actually create
an ad impression ID with this ID that's fine that's one way but it requires an additional DB call so instead what we
can do is we can just sign that impression ID and maybe with the timestamp in the ad placement service so
what the ad placement service now is going to do is going to send over the ad ID the impression ID and the signed
impression ID so we're going to sign it with some private key that we have server side and then when the browser
clicks we're going to send that ad ID that impression ID and that signed
impression ID and the first thing that we're going to do is we're going to verify that signature we're going to see
is this legit was this not tampered is this correct right that's what the signature is for and if it is then okay
we know nobody made up this impression ID it's a real one let me now check in reddis is it a duplicate and if it's not
let me carry on and put it in Kinesis so that's how we're going to handle the item potency
see all right just like that I I think that just about does it so to recap we
satisfied our functional requirements in our highle design then we went through each of our non-functional requirements
and kind of expanded our high level design through deep Dives to be something that was more sufficient now
what we have here is something that is passable for a staff candidate for a senior candidate I think you could have
left out the reconciliation that fine you might not have had time to get to the item potency I would have liked some
depth whether it was in understanding how to scale Kinesis or retention policies we definitely would have
required some knowledge there and I think I'd like to see you at least get to uh you know this Kappa architecture
though there are strong justifications for the Lambda that maybe could have passed for senior as well um for
mid-level as we discussed before even if you got here then I would have asked some follow-up question questions in
different areas kind of probed a couple of places to fill out our 35 minutes but assuming you answered all of those
pretty eloquently and had a good understanding this probably would have been passable at mid level so hopefully
this gives you a good understanding of what would be required at each level the main tradeoff there just to summarize is
that as you are more Junior then we have more depth or more breadth excuse me and less depth so for a mid-level candidate
we look for 80% breadth 20% depth at a senior candidate we now want more depth
so maybe we're looking at more 60 70 breadth 30 40 depth and then of course
at a staff candidate we want you to Breeze through the breath we know that you understand the basics get that high
level design really down really quickly and let's spend a lot of time going deep talking about the things that are
complex and interesting and more importantly with staff candidates often times you'll find some place in this
architecture that you have intimate familiarity with from your past work and you can even teach the interviewer
something about it I think usually it's a Telltale sign that a staff candidate did well when I leave the interview
Having learned something myself so that wraps it up I'm pretty happy with this design hopefully you are uh all are as
well great job if you made it this far I know these are long I've been trying to keep them short but there's a lot of things that I want to talk about uh
hopefully it was it was informative I'm going to continue to publish these once every 3 weeks that's been the Cadence thus far I've been holding myself to
that uh please continue to leave comments ask questions tell me all the things that I've done wrong I enjoy responding to those comments I try my
best to keep up to date as they're coming in and and and provide those responses also kind of the the Kudos the
praise whatnot in the comments has been super encouraging too that's really what's been motivating me to continue doing these a lot of people are finding
them incredibly useful so um thank you so much for those kind words uh
truthfully it motivates me to keep going now lastly if you want to practice with
me or somebody like me a former or current Fang uh senior plus engineer or
manager then head over to hello interview.com and schedule a a mock interview um obviously I'm biased I run
a mock interview site but I'm I'm fully bought in to this idea of mock interviews being incredibly effective
even outside of my bias I get messages from candidates every single day multiple messages a day of folks that
either I worked with directly or we've worked with through hello interview um and they express you know immense
gratitude they got the job and they're so thankful for for having worked with us and they really credit a large
portion of that success to the mock interviews so I'm bought into this being something that that really works and helps candidates prepare prepare um and
you know worth considering if it Mak sense for you so with that being said uh
thanks for watching I'll see you all again in 3 weeks and uh best of luck with your upcoming interviews you're going to do great
