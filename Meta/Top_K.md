howdy everyone and welcome to another system design breakdown today I'm going to be talking to you about topk YouTube
videos this really uh online you might see this as Heavy Hitters or topk anything it's a pretty general question
that touches on a lot of Core Concepts that are going to be relevant across system design interviews this session is
going to be a little bit different than what we might previously have seen on some of our videos where you're ask to design an entire app and marshalling
together a bunch of services in order to uh build out all of the functionality
this is more akin to an infr style interview where we're designing a specific subsystem and as such it's
going to allow us to go deeper into some of the core principles about how these systems operate so I'm really excited to
be able to get into detail with you now just a quick plug this material is available on our website I'll include a
link in the description where you can read this as well as any of the other common problems that we have we've also
got material that break down down what our recommended delivery framework so if you've got a system design interview
coming up you should absolutely check it out now who am I I'm stepen I was formerly a senior manager at meta
Facebook I also worked at Amazon I've primarily worked on uh machine learning systems for most of my career uh but I
did spend a lot of time as an engineer working on deeply scalable backend systems and so I'm really excited to
share some of that experience and knowledge with you I've also conducted north of 2,000 interviews at this stage
so so I'm very familiar with both the interview process and what people tend to be looking for and I'm hoping to
earmark some of those as we walk through this problem together so without further
Ado let's go ahead and dive in now in order to solve this problem
The Approach
we're going to take an approach that's outlined in our delivery framework which is basically a set of steps that you can
follow in order to solve system design problems and the core main idea here is
that we're first going to as basically as possible satisfy the functional requirements of the system can it
actually perform its job and then we're going to progressively through a sequence of deep Dives solve for some of
the nonfunctional aspects and bottlenecks in the system the intent here is to keep you from getting lost in
the middle of a session I work with a lot of senior and staff level Engineers who see problems and know a lot about
how to solve them but either because of the stress of the interview or because of the open-ended nature of the problem
solving and then getting lost and not sure where to go next the framework here is going to help to make sure that you
cover the right things and that you don't get stuck you always have a clear next
step your interview is going to start with your interviewer giving you a prompt this is going to be ambiguous uh
Requirements
but it's going to roughly describe what they're looking for from your system so in this case let's pretend that they
asked me to design a service for YouTube which when queried will tell me the top
K most viewed videos on the site let's also pretend that the interviewer asked
me that this service should be able to take in a time period like hour or day
or month and I should be able to surface all of the videos or the the topk most
viewed videos in that time period so the first step for me is I'm going to try to put this on the Whiteboard and the
intent here is that I want to make sure that my understanding and the interviewer's understanding is
consistent and this will also give me something to refer back to uh later on in the session some interviewers will
put some of these requirements actually on the board many won't so it's a good practice for you to go ahead and and uh
practice of of actually enumerating this but fortunately the functional requirements are pretty simple in this
case I want to query the topk most viewed videos and I want to be able to
accept a parameter which is the time period now this kind of opens the door
for a bunch of questions that we might want to ask the interviewer the first question is related to this top K
whenever you're given a service which accepts a parameter you usually want to establish some bounds on the parameter
and generally speaking K as an abbreviation mean some restricted number
in this case if I ask the interviewer they might tell me hey it's a th000 uh videos Max for k um they may also ask me
what do I think and if I was you I would put some constraints on this a thousand seems like a good number we'll keep
going the next thing is the time period has a lot of um potential so they had
given me that this might be a minute or an hour or a day do I need all time yes
the interviewer says we need all time let's talk about this window is this a
um sliding window or is this a tumbling window a tumbling window would be like 5
to 6 and 6 to 7 a sliding window might be 5:15 to 6:15 our interviewer is going
to tell us that this is actually a sliding window I might also ask whether I can support arbitrary time periods can
I get the hour between 5 and 6:00 p.m. on April 1st when I'm in June the
interviewer is going to tell me no you can't support arbitrary starting points uh this is only going to be anchored on
the current time and it's going to be a sliding window I might also ask them are there
additional time periods or are the uh periods that they've given me fixed and in this case they're going to tell me no
those ones that you have listed seem good enough great for functional requirements I probably don't need to
put a ton of detail here for infr style questions it's important that you're
clarifying but they're not going to be nearly as exhaustive as they might be for a product style question like design
Uber the meat of infrastruct infrastructure style questions is the
non-functional requirements and in the non-functional requirements we're going to be specifying some of the constraints
that our system needs to operate under which are ultimately going to influence some of our design decisions so at this
stage we kind of have to have a general idea of what the system looks like I know I'm going to be taking in uh views
from the user and I know I'm going to be reading them out so that immediately gives me a few questions that I can ask
the first is around what you might term as consistency but I'll talk about in terms of staleness which is how long
between when a video view comes in does it need to be tabulated in my top K
calculation and my interviewer might say well I'll give you a minute 60 seconds uh for that
to be available this is really important because our consistency requirements are
going to dictate things like caching or any pre-computation knowing about the end to
end latency especially if for writes uh into an index or something that we're going to read about is going to
constrain our design quite dramatically the next thing that's
obvious to most people is about reads and I might ask all right the topk
service how fast does it need to be and my interviewer might say I don't know you tell me or they might say hey this
is going to be on the front page of YouTube so it needs to return very quickly uh so that way we don't uh
bottleneck the latency so we're going to record that requirement it's also useful in our
non-functional requirements to get some assessment of scale and some of this might actually require some calculations
from but I'd actually prefer that we defer those until we need to make decisions I'm going to assume for my
interviewer that we want to support a massive amount of views and a massive
amount of videos but I'm going to earmark these for calculations at a later time when I need to make decisions
that concern them finally I'm going to add a constraint onto this system to say that
I will not support approximations uh this would be a little bit unused usual I think most
interviewers aren't going to add this constraint but some might and the idea here is that there are a lot of systems
that look like this where you might accept an approximately correct answer
if that's the case then using things like Bloom filters or count Min sketch are entirely appropriate you might use
uh approximate nearest neighbor search inor indexes knowing whether you need
precise answers is really important and for a lot of massive scale systems
actually that Precision isn't that important I'm going to pretend my interviewer in particular is going to
tell me that they want this to be precise because I think it makes for an interesting question but I will have
some follow-ups at the end of this video where I talk about what happens if we relax this constraint there are some
alternative solutions to this problem that I think you'll see more commonly online uh that are interesting to go
through so with that I've wrapped up my requirements section um note that your
probably going to be spending four or 5 minutes here uh don't overdo it it's easy to burn a lot of time in your
interview but don't over uh or don't skip through this if you don't have the requ right requirements your system is
going to be very hard for you to design the next step in our process is
Core Entities & API
to come up with our entities and apis for the problem now fortunately for this
problem in particular these are pretty basic and I wouldn't recommend you spend excessive amount of time on things that
aren't going to be differentiating but it can be really helpful for you to know what are the inputs and outputs of my
system and approximately how are they shaped these are going to be the anchor points for the rest of your design in
some sense you're connecting the inputs to the outputs it's just drawing a line on a diagram so really good to have the
edges defined carefully let's talk about the entities for this problem The chorde
Entity is a view I have a view on a video and ultimately I want to go and
get some sort of top K responses uh for it for that top K it's going to be
parameterized by some sort of window a Time window and these are actually like an enum uh we talked about them earlier
minute hour day all time there aren't other entities
in this system I actually don't need to be concerned about users I don't need to be concerned about video categories and
I can move on the next thing that I want to think through is what are the uh the
apis that I want to support well when a view comes in I'm expecting that there
is a stream that I can connect to either somebody is going to make me an API call
or maybe I already have something like a Kafka topic or something else that represents this but I'm expecting on
that stream I'm basically just getting video IDs the next that I want to talk about
is how my users or clients are actually pulling this and for that I probably want to expose an API to them I can make
it a rest API I can basically say get uh views video and I need some parameters
for this API so I certainly need what my K is and I'm also going to need to
specify my window what is this return well I think there's a lot of different ways that I could frame this but
probably I'm going to want some sort of sorted list uh I need a video ID and
let's pretend I'm going to make it convenient for my consumers and also include the views in case they want to
display the number of views over that period uh next to the videos I don't need anything else and honestly for this
service I probably don't even want to include metadata about the uh video and assume that either I'm going to have a
downstream aggregator that's going to read from me and then augment this video ID uh with those video names or that my
clients are actually going to make those calls separately it's a great separation of concerns and it makes things dead
simple for me from the design perspective so I'm going to keep moving now that we've got the housekeeping out
of the way we can start to talk about how we actually solve the problem uh the fun part and I think the Temptation here
for many candidates is to Jump Right In Without Really any plan for how they're going to approach this and so I highly
recommend you take a breather and you think through the problem there's really two classes of mistakes that I see
people make here the first is that some candidates will try to have an optimal
solution from a a scalability perspective out of the gate and then work backwards into a system that
actually functions and this is almost always the wrong decision both in the real world and in a system design
scenario because it's very difficult to take an optimized solution and make it
work as opposed to taking a working solution and make it optimal so I highly recommend that you focus on solving the
functionality first before you think about the primary scaling questions the
next problem that uh candidates typically have is they try to take all of the functionality together some
problems may actually allow you to take a giant leap all the way to the end and if you know the answer by all means you
don't need to go and break it down but for many problems especially if you haven't seen it before there's a bunch
of dragons along the way and actually taking a stepwise and incremental approach will enable you to continue to
make forward progress especially when you get overwhelmed it's not uncommon for me to see staff level candidates
struggle because they tried to swall the entire problem at the outside and then when they realized they weren't going to
be able to pull it off they didn't know where to go and they didn't have anywhere to retreat to so for this
problem we're going to try to break it down and solve it in Mally now how might we break this problem down there's kind
of two ways of thinking about this one is this problem is clearly comprised of
counters and sorting where I I get the top K maybe I can solve the counters in
a scalable way and I can solve the Sorting in a scalable way and pair them together that would be one option and a
potential way for you to solve this problem another way to solve this problem is to say can I solve the
alltime problem first basically having a top case service that solves all time
and then use that in some way for me to solve this problem of windowed queries
where I want to retrieve the last hour that's actually the approach that we're going to use here but I think both will
lend you to the same spot in either case I'm going to start and try to come up
with a simple base before I go and optimize for
High-Level Design
scalability for our basic solution we're going to take the approach that we talked about earlier in the API design
and try to bound this by the inputs and outputs of our system so for starters we
have our
client and our client is going to be making that top K call to us on the
input side or the right side we've got our view stream and let's pretend that
this is a uh Kafka topic but you could use anything here theoretically your
users could be calling you through a rest API uh you could have this as a
reddish stream whatever makes sense for you and our challenge here is functionally just to solve this middle
we need to connect the two dots so let's go ahead and toss a service in here we'll call it our top Cas service for
now and our top Cas service really has to do two things the first thing it needs to do is it needs to I guess the
the it needs to do three things the first thing that it needs to do is accept the the views off the
stream it needs to tabulate those views into a
count and then we need to calculate on an ongoing basis the top K most viewed
videos we'll probably use a heap for this as kind of a natural dat structure for getting the top K elements in a list
in a in an optimal fashion so what happens is our topk service is going to
read off of our kofka topic and it's going to increment the counts for a
given view ID then based on that count if that count exceeds the smallest
amount in the Heap then we're going to update the Heap and heapify when our
clients call us we're going to basically directly make the call into that Heap and return that value to our client uh
which is functionally that top K as long as this Heap is larger than the K and we can set it to the Thousand which we set
as our Max we'll always be able to answer the client's requests now this is
a workable solution but it is far from great there's a bunch of different
deficiencies that your interviewer is going to expect that you're calling attention to it's best for you to
earmark these problems S as you're working through the solution so that they know that you're thinking about
them the worst case scenario is they feel compelled to reach in and remind you that this isn't scalable or this
isn't reliable and as such it makes it seem like you didn't know about that that can be a really frustrating
interviewing experience so I'm probably going to earmark a few things first of all this view stream is probably very
high volume I've got a lot of views um I may have my clients making lots of
requests the count is going to be quite large depending upon how many videos I
have and this isn't particularly fault tolerant or available so let's try to
address some of those issues before we can talk about the
views and the the counts that are coming in we need to get some idea of what's the scale here and so we might ask our
interviewer how many views are happening on the platform and they might give us a round number like 100 billion views it's
a lot we'll take 100,000 seconds in a
day and then we can calculate that there would be approximately 1 million views
per second this is a large volume most Services uh would struggle uh with this
volume and you might even hit bandwidth concerns if the payloads were especially large they aren't in this instance uh
but it's worth considering another thing that we need to think through is this counts we might
might ask our interviewer how many videos are created and they might give us a number 1 million videos per day now
obviously we need to maintain counts all time so we need to figure out how many
uh videos were being created over a period maybe there's 365 days 10 years
so we get something like 3.6 billion videos but what does that mean in terms of storage well billion is giga million
is Mega so if these were a BTE a piece this would be 3.6 GB obviously not a BTE
a piece our hashtable is probably going to contain an ID let's call it 10 bytes
and a count maybe 4 8 bytes let round it up to 20 so overall this entire quantity
is on the order of 100 GB uh that's small enough to keep in memory on any
reasonable server uh that that you might be running and as such it something that
we can mostly ignore for the rest of this interviewer or rest of this interview the other thing that we talked
about briefly was the uh the service and its availability and so a natural thing
to do when we consider availability is just to replicate my service now I can't
just replicate my service now I am forced to have something like a load balancer this might be a time where we
talk about whether I need an API Gateway if we wanted to deal with rate limiting
or we wanted some sort of authentication but I'm going to ignore that for now and
the idea is that now if one of my services fails my load balancer takes it
out and I my clients are keeping that availability now when I need to bring
back that service I have a problem because this is a stateful service and for the most part we should try to
manage the state in our service such that it's not spread across our entire design statefulness is not a bad thing
especially for problems like this it's inherent to it but we really want to contain and manage that state in this
case the top Cas service is going to be stateful but we need to figure out how to deal with it an obvious thing for us
to do if we lost one of these instances is to boot it back up and reread from
our topic or stream if we have retention enabled in Kafka we can reread those messages and then repopulate the counts
and our heat the obvious problem with that is we have to start from scratch and if we assume our service is already
at its its bottleneck in terms of the throughput of of views that it's
ingesting then we're going to have a hard time catching up the way to think about this is if my service is 80%
utilized on the steady state where it doesn't actually need to catch up then
that means I have 20% that's available uh for me to actually uh work through
the backlog now that 80% utilization means that I functionally am only going
to be working through a quarter of a second 20% over 80% each second that
passes so if it's been a week uh since my service was initially booted then
that means it's going to take me 4 weeks to catch up most Services don't have a
bunch of excess capacity to go rework old jobs and so in this case what we
probably want to do is employ some sort of checkpointing the checkpointing for this
can be very simple and this is a great benefit of using cofa we can basically
write out our counts our Heap and the ID of the last view that we processed to
some sort of blob storage call it S3 or Azure blob or whatever you want to use
and and then when our service starts up we read from the checkpoint we restore all of that state and then we resume
reading from the stream from that latest time point we can do these checkpoints
on an hourly basis or a minutely basis but this is going to help us to recover
it's also going to help us to scale if we need the service to add a new instance it doesn't take a week for that
instance to become available theoretically we can catch up quite quickly provided we have a modest amount
of Headroom and our checkpoints aren't that far behind now you may feel some questions from your interviewer if you
bring up this idea of checkpointing about how you keep consistency of counts and your HEAP you obviously don't want
to stop reading views for too long while you're doing that checkpointing so there's a bunch of potential
considerations that I'm not going to go into here now the last thing about this service that is worth talking about is
how we handle this right volume and like I said said most Services aren't going to be able to handle a million TPS it's
just a lot and so a natural thing to do here is to try to spread this in the same way that our load balancer does
from the read side across many different shards or partitions so let me move my
checkpoints out of the way and then pretend that we're going to have multiple shards of this top K service
now how will these shards be organized an idea here is based on the
video view or the video ID we can assign that video to one topk service and that
means that for a given service it knows about a certain population of use um the
the easy way to do this is to take modulo of the number of shards and your
uh video IDs are then going to be distributed in a semi- random fashion the challenge that we might have
with this this is we now have to aggregate these heaps on the read side
so let me move this guy out of the way we're going to change the name of our top K service and call these guys
counters uh which is probably not super precise we'll move our topk service over
here and then the what will happen when we want to get the topk views is our
topk service will then need to query for from each Shard and
aggregate remember that we need the top K most viewed videos so we're going to have in our Heap the top 1,000 views to
be able to accept an arbitrary K between zero and a th000 if that's the case then
we can guarantee across all of these shards that the global a th000 most
viewed videos are definitely going to appear in at least one of these heaps
and the topk service only needs to grab from these heaps and then merge their lists and functionally discard uh
everything from the bottom that's past that a thousand there's really fast algorithms for merging sorted lists this
can run very quickly and functionally we only need to iterate over each of these items uh once so if there's a th items
the number of shards that's the number of of items that we're going to be iterating through if this is slow we can
obviously employ some sort of cashing and we'll talk about that potentially later but this solution provides us a
way to Shard out the rights so that we can reduce this to a reasonable value
now of course we wanted to make this economical so maybe we don't want this to be excessively large but if we needed
say 100 hosts not only have we reduced the memory requirements by functionally
100 uh for our system but we've also reduced the right volume to each Shard
you might feel some questions around how this would work with respect to Kofa and a very obvious idea would be to make
sure that this view stream was partitioned in the same way that your counters were another question that you
might feel is how you can make this more elastic so if we know about the number of shards in advance then we can address
these all independently you could assign each Shard a DNS you can actually round robin the DNS for each replica um and
you know functionally DNS can handle the load balancing and the addressing of
each of your counters or if you need to be able to add additional shards then
you'll probably need something like zookeeper where you can keep track of
the number of shards that are out there alongside the ranges or the available um
videos in each Shard so a an orchestration problem that you'll need
to be able to deal with is if I add a new Shard then I'm going to need to functionally remove remove some videos
from some of the shards and I'm going to need to hydrate them into a new one I'll
leave it as an exercise for the reader or the viewer uh how that might happen
but you can functionally use some of these checkpoints as well as the retention on your kofus stream to pull
this off and that might be a discussion point for you in the interview um but
that is one potential solution for it so now we've got a solution that works in a
reasonably scalable way for all time but obviously that's not the full problem we
need to figure out how we're going to handle the time
Deep Dives
window now that we've solved the basic solution of alltime counts we need to
get to the Crux of the problem which is how to handle these time windows and
this is actually a pretty challenging um aspect and it probably will take a a
considerable portion of the interview so if you feel like you can't just spout out a solution that's okay your
interviewer is in some sense trying to get a flavor for how you think I'm going to walk through a few different
approaches and then kind of walk through my mindset for what's going on so that you can see a little bit about how you
might take this on so generally speaking there's one way to look at these time Windows which is as producing some
arbitrary aggregation of of basically minutes or some fine granularity of time
so a solution for us might be to store these very low-level counts by minute so
let's say this is video a and this is 2:00 this is 2011 this is
202 When My Views come in I'm going to increment the count that's associated with the video ID and that minute and
then whenever I write a view I'm going to add agregate all of the minutes in my
windows and insert that into my Heap then when my clients need to read
off my Heap they can do so and everything is is fully pre-computed um this sounds attractive
because anyone who's dealt with time series data has has seen uh issues like
this but it has a number of of challenges and and difficulties the
first problem is these one minute slices per video start to explode in terms of
storage space so if we have 60 Minutes that means that if in the limit every
video had one view every minute that we take our earlier estimate of I think it
was 100 gab and multiply that by 60 now we have 6 terab of data uh that's
considerably more expensive the next problem that we have is this Heap can be stale if we're only
updating the Heap when we write then we're potentially missing out on those instances where the minute that we care
about is actually outside the window that basically if we are querying at
6:05 we no longer care about the minute of 50:4 and as such if the last view that
came in happened at 604 this top K Heap might be stale
these aren't insurmountable problems and in fact like time series databases end up having to deal with some of them so
one idea and it's a good one is to provide aggregations so maybe every time we
increment the counter for the minute we can also increment a counter for the
hour and the day and so forth we'll have many granularities of pre-aggregation
that we have given that the cardinality of these pre- aggregations is low this increases our right volume but not
dramatically and then theoretically what we can do is we can start to expire or get rid of some of these lower
granularity entries as time passes so maybe we can make an assumption for
instance that we're not going to care about the old time because it's represented by this day
here now this takes some liberties with the accuracy of the calculation as an
example if I was trying to get a week then I probably have a half day that's
immediately uh buting up against the current time and I may also have a half
day 6 days ago that I have to add up in order to make my full week this half day
is no longer being represented at the lower grains so I'm not accurate there
anymore the other problem is this still increases space and I don't think
there's any ways around this aside from relying on the sparsity of view data for
the vast majority of videos they aren't going to have a view every minute some
of them aren't going to have uh views at all after the first day or so of their
publishing and so potentially we could lean on this to make the case that the
space utilization uh from our application isn't large but generally speaking these
pre-aggregation and hierarchical aggregation approaches work really well in those cases where we need to make
queries of arbitrary time periods and we can sacrifice some of our Fidelity or we
can snap those time periods to the granularity that we want so if for
example I could take some Liberty and say well it's not necessarily over the last 7 days it's over the last seven and
1/2 days uh or 6 and 1/2 days then suddenly I don't care about this data
that's back here and I can return to my users um you know something consistent
with their expectation now I don't think this is necessarily the best approach but given
that there's a lot of candidates who uh recognize this pattern and are able to
implement it and cover some of its deficiencies you might get a passible interview by by looking at the problem
this way but I think there's a more elegant Solution that's at play here and for this let me just walk through a
little bit about what's happening when I get a view at the very instant that that
view happens we need to go and increment a bunch of counters that part's obvious
that's what we do with the alltime solution and that's what we need to do for every other uh time
granularity the challenge is that at some time after time has passed we
actually need to start decrementing those counters we basically would love to have an event for a particular view
that happens an hour later or a day later and if we had that event the
solution is pretty straightforward when the view first
comes in we can increase its count in buckets or or maps that are time grain
specific so we we can have hour counters and then for that video ID we'll
increase the hour count and then when that hour expires we can then decrement
that count on those events we can also update our Heap we can uh basically just
determine whether we need to add the item to the Heap uh when it's incremented and then when it's decremented we can update it and it
might potentially fall out I'll talk about an edge case here that you need to consider but this potentially solves our
problem so how can we do this in practice well remember we have our Kafka
uh streams and topics and they have retention enabled primarily to enable us to uh facilitate checkpointing what this
means is that we can read from our Kafka topic given any sort of lag so what
we'll do in this case is we'll read from the topic starting from more than an hour ago and we'll stop reading as soon
as the items start to pass that 1 hour ago Mark that functionally gives us what
is essentially a lagged Kafka topic that we are going to get those same events
happening 1 hour later and this when we apply it to our accounts is going to
give us the correct value the other issue that I just
briefly mentioned is these heaps and how we deal with uh items that are uh
decreasing in count you could imagine there's an item in the top
1,000 it decreases in count and theoretically the item at 1,00 And1 is
now part of that top 1,000 uh but we don't have it available it's not sitting in the Heap and what that means is that
the Heap is inaccurate it's not reflective of those top 1,000 items the solution for this is actually
pretty straightforward we can just fudge the size the Heap a bit so that we can
make sure those runnerup entries are available for us to rank against and I
know what a lot of you are saying you're saying Hey There is potentially an edge case here what if we had a video that
was getting 1,000 views per second and suddenly it goes to zero and we have a
thousand videos that are like that how are we going to handle that case and I'm
here to tell you that this just doesn't happen in practice that generally speaking most uh video viewership is
fairly smooth and fairly regular they're actually getting views on a a high frequency Cadence and as a result a bit
of a fudge in our system is actually going to be 100% precise unless we hit
these Black Swan events of you know title levels of um of outages and in
those cases I would submit that our system is probably still going to behave
uh well enough so assuming we we choose the solution where we're using some lagged entries in
the kofka topic or stream we're going to have a solution that looks like this where each of our counters instead of
maintaining one set of counts and one Heap are going to maintain counts for
each time window that we might potentially query and heaps for each time window and then we're going to have
basically kofka consumers for each of those heaps that are going to be lagged by that time period so I'll have one
consumer which is reading off the stream as fast as it can and incrementing each of these counts and then I will have
other consumers which will consume from this stream at a delay of an hour or a
day and then decrement and subsequently update the
heaps that functionally gives us a solution to our problem and it's very scalable in this case the big problem is
just how do we manage the large size of the kofka entries because now we need to
keep around the data for each of the views as they happen uh scaling kofka is
probably not going to be the core focus of your interview but it's worthwhile talking about the fact that functionally
keeping all this data is not going to be a completely trivial exercise another question that your
interviewer might have is about the read volume so so far we have a load balance
top case service which queries across all of the counter shards and then Aggregates them and this while not slow
is certainly not fast it also suffers from this fan out problem that the larger the number of shards we have the
more quer more services this needs to hit when you see fan out you should also expect that there are going to be
latency implications of this the problem with making a 100 different requests to
100 shards is if one of those shards happens to respond slow the entire
request is going to be delayed so we'd ideally like to be able to handle both the volume and the bulk of the latency
concerns and the answer here is pretty obvious like let's go and create a cache
and our cach here functionally is going to be our first protocol before we
return to users if the cash entry exists then we can go ahead and return back to
the client if it doesn't we need to go to each of our counter shards Aggregate
and then store that back in our cash now fortunately earlier on in the session we
Define the degree of staleness that we can tolerate in our system we said up to a minute and so in as much as the data
is being read off the stream and consumed into these counts very quickly probably in under a second that means we
have 59 seconds left where we can be stale and that functionally defines the
time to live or TTL of our c if you've got an instance where you can
tolerate some inconsistency or you can tolerate some staleness then your cash
is a great way for you to improve the performance of your system without sacrificing any of your requirements and
in that case that's what we would do we would set a 45 second or a 50-second TTL on our cache and that would guarantee
that as long as we're consuming quickly enough that we can um functionally answer questions uh the correct way so
earlier I talked about how in this problem we were going to require an exact solution and the justification for
this is simple that generally speaking if we bring in approximate or probabilistic data structures that some
candidates just simply won't know about them but they could probably read on Wikipedia and learn about it very
quickly and as such there's no real reason to disadvantage them but if you're thinking about how to design the
optimal system they might be a good thing to pull out of your back pocket and so it's worthwhile for us to talk here it would also relevant for this
particular problem if the cardinality of the items that you were going to be counting against was very very large so
for example if we were doing Facebook posts you might have trillions of posts verus billions of videos and then my
earlier estimate of there being 100 gbt to store the dictionary of all the
counts might be dramatically smaller than what you would actually need in which case we might need a different
approach so let's talk about how that might get pulled off before I do that I need to introduce you quickly this
concept or this data structure called count Min sketch if you're familiar with Bloom filters this is actually not too
far off and hopefully we'll put together either a video or a write up about some of these probabilistic data structures
they can be useful in a number of cases the way that this works is we have a number a fixed number of hash functions
and in this um in this visual I have the hash functions here and then I have the
bits of each of those hashes uh Down Below in cman sketch this uh bottom
record or bottom row is referred to as the width or the hash width and then the height is the number of hash functions
you basically have a 2d array of integers or counts that you're keeping
uh in this setup so what happens well when I first see a video what I'm going
to do is I'm going to take the hash of its video ID and for all positive bits
in the hash I'm going to increment the value at that respective index so if for
instance the first and third bit of the hash of my very first video ID was one
then I'm going to increment the values at that first and third uh place now if
I see that video ID again I'm going to increment again and you can see in this
case I've basically updated to two all the places where that initi hash was positive now moving along if I see a
different video ID I'm going to do the same behavior um if in this case let's
assume that my second video ID had positive bits at the second and third
position for hash one you'll note in this case that I've actually incremented
uh this value to three this constitutes a collision we basically shared bits
amongst those uh first two hashes and this is okay uh for our purposes because
uh we're accepting that there is going to be some degree of collisions now what this cman sketch allows me to do is
given an arbitrary ID I can query and get an upper bound on the number of
times that I have seen it before so how would I do that let's pretend I take that first video again where all of the
places where I had previously incremented a bit I'm going to then pull the value at that index so I've got twos
and threes basically I don't have any ones and I'm going to take the lowest value I'm going to I can't take the
highest value because I could have collisions and the lowest value is going to be an upper bound on the number of
views that I have seen for that item very much like a bloom filter will tell
me whether or not I have seen something before but it won't tell me whether I
have uh not seen it and in this way I can go and update my solution so instead
of maintaining the counts I can have a very big count Min sketch that I include
here and then when I record or increment
my counts I'm going to update the count Min sketch and then query it so that way
I have its final count and then insert that value into my Heap when I decrement
I'm going to do the exact same operation and what this is going to do is those
accounts aren't going to be precise they will be again an upper bound but they'll probably be close enough for my purposes
and I'll save a considerable amount of memory in the process so that's how you
would use count Min sketch here you may see other Solutions online that involve
some batch processing in an offline system I find that that's actually a little less popular to cover in this
particular problem in part because it is possible to solve this in a near realtime fashion
and Hadoop style disc based computations aren't nearly as popular as they once
were with the Advent of spark and a lot of data infrastructure uh moving in that
direction but your role may be different and your industry may be different so hit us up in the comments if I'm wrong M
can be all righty well that's it for this
Conclusion
question I hope that you've learned a lot we covered a ton of ground here from talking about how to use a consistent
hash to manage shards in a service how to use probabilistic data structures like count Min sketch and clever
solutions for handling sliding Windows using lagged offsets in a kofka
topic if you want to learn more our guide is in the comments or in the
description uh this guide actually covers a lot of the ground that we covered in the session today sometimes
in more detail sometimes and less but happy to answer any questions that you might have in the comments here or on
the guide on our website and I wish you all the best with your system design interviews thanks for watching
