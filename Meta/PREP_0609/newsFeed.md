Intro
hey folks today we're going to do
another problem breakdown this time for
newsfeed for those new to the channel
we're Hello Interview and we help
squeeze and em to nail their interviews
i'm Stefan i've been an interviewer and
bar raiser at Meta and Amazon and have
conducted north of 2,000 interviews at
this stage for all levels up to senior
staff and managers newsfeed is a fun
question because it requires careful
attention to data modeling details and
plays with concepts like fanout that end
up being very important across system
design problems
for this problem we'll focus on a now
dated variant of Facebook where users
could follow one another
unidirectionally and view a
chronological feed of posts a more
modern newsfeed architecture would lean
heavily into MLbased ranking while we
haven't yet covered news feeds in
particular our video recommendation
breakdown is a great start if you're a
machine learning engineer and not
familiar with ranking and recommendation
systems i'll link it somewhere for the
rest of you who are strict software
engineers preparing for system design
interviews let's get into it if you'd
like to follow along with a written
version of this breakdown I'll include a
link in the description and also
somewhere on screen for all of the
The Approach
problems we break down on this channel
we'll be following the Hello Interview
delivery framework this is just a simple
structure for solving problems that
keeps you focused on the things that
interviewers are looking for what we
find in practice through tens of
thousands of mocks is that candidates
who have a system make more progress and
get stuck less often so we highly
recommend it the setup is pretty simple
first we'll discuss requirements with
the interviewer both to nail down the
constraints of the problem and clarify
any uncertainties we might have this is
a good place to figure out the crux of
the problem or the hardest part more on
that in a second next we'll outline the
core entities or the nouns involved this
is key to designing a good data model
and API and it helps to orient you for
the next pieces of the problem after
that we'll build out an API for our
system these are the stubs for our
design once we've credibly designed a
system which can implement these APIs
we're halfway done for some data
processing design problems the next step
is to build out a data flow this helps
to clarify each step in the system like
a web crawler needs to grab URLs parse
HTML extract URLs etc etc in this
problem we won't need to cover this with
our API in place we can start on our
highle design our goal with the initial
highle design is to satisfy our
functional requirements as simply as
possible this usually means building a
system that doesn't scale and has some
warts and issues that's okay we'll make
note of those and come back to them
later finally we'll move to our deep
dives here's where we'll proactively
identify bottlenecks of the system
satisfy any lingering non-functional
requirements and follow the
interviewer's lead if they want to talk
about something specific and hopefully
by that point you've had time to
whiteboard a working system in 35
minutes easy enough let's get into
it we'll start with the requirements for
Requirements
newsfeed for functional requirements we
need a system which is going to allow us
to create posts follow users and view
the resulting feed so let's go ahead and
add those to our list while you're
building out functional requirements it
can be helpful to put yourself in the
shoes of a client of the system imagine
you have the app open what data is
displayed what options are available to
you with newsfeed we might note that
users are typically scrolling we want
them to be able to consume a page full
of information and then keep going so
we're going to include that as a
functional requirement as well if you've
done a good job of putting yourself in
the shoes of the user you might be
thinking of additional functionality as
an example users should be able to like
and comment or post can have privacy
settings i'd recommend you keep things
simple to start and if requirements are
getting large beyond say three or four
items mark extra things as below the
line or bonus put bonus here that way
it's clear what's in scope for your
system note here that you don't
necessarily need to list these below the
line items if you were starting from
scratch and running out of time I'd
actually suggest just moving on to your
non-functional requirements rather than
talking about things that you're not
going to talk about keep in mind you do
have a fixed time available to you so
don't rush the requirements but don't
spend more than a few minutes here next
we'll talk about non-functional
requirements here it's helpful to have a
discussion with your interviewer about
typical scaling trade-offs common
prompts you might ask yourself are
things like cap theorem do we require
consistency or can we favor availability
often times this will vary based on
different functionalities or parts of
the design in this system it makes sense
for us to utilize eventual consistency
when users create posts they don't
expect that they're available they're
immediately available in users feeds but
they will be looking for them to appear
quickly we can put some numbers here
both to make this concrete and to help
us with design choices we'll make later
let's assume we have 1 minute before a
post is available in users
feeds next let's talk about latency
users expect responsive UIs which means
we have a few hundred milliseconds to
respond to requests before they start to
get annoyed let's use 500 milliseconds
as a roundtarget latency for both
posting and viewing
now let's think about scale knowing the
scale of a system will give us more
bounds on size and throughput we can use
later facebook is big billions of users
we don't need to know exactly so let's
just assume two billion
users and move
on
API & Core Entities
our next stop is core entities remember
these are the nouns we'll use in the
design depending on the problem there
can be more or less discussion here for
a newsfeed our entities are pretty
simple we have a
user we have a post and there is a
follow relationship fundamentally news
feeds are about finding the post from
users you follow we don't need to build
out a full-blown data model here so I'm
going to avoid attaching properties or
attributes to these entities we'll get
to that as we start to fill out our
highle design and that's it for our
entities now let's move on to our API
design the easiest way for us to build
out our APIs is to refer back to our
functional requirements and make sure we
have coverage of them it's not always
the case that your API is onetoone with
your requirements that's totally okay
but we do need to ensure that our APIs
satisfy our requirements once we're done
we'll know that our highle design is
complete when it implements all of our
APIs for this problem we'll need three
APIs first we need a way to create a
post let's keep this simple with a
restful post endpoint so we'll post to
/posts and we might pass along the
content of the post let's assume that
we'll return a 2011 when it's successful
and maybe we'll pass back the post ID
great our requirements don't have
anything more here so we can move on for
our next API we need a way for users to
follow each other we don't have an
explicit requirement for unfollow
although that makes for a sensible
extension that some interviewers might
ask let's use REST conventions to create
a follower edge by putting to the user's
followers so we will put /users ID
followers we don't necessarily need a
body here just because there's really no
metadata that's associated with this
finally we need a way for users to
access their feeds moreover we need a
way for them to gradually pageionate
through their feeds for this let's
create a get endpoint for a virtual
resource feed that has both a page size
and a cursor so we'll get /feed we'll
pass in a page size which might be 25
and a cursor and this will return a set
of posts and a next cursor cursors are a
very common approach to pageionation in
this case our cursor could be a start at
time stamp which tells us how deep into
the feed the user has traveled when a
user loads a feed they'll be able to
view a set of items from the present
time to some point x in the past which
is the time of the last item in that
response when they request their feed
again they'll pass in that time and
retrieve the next set of n items all
which are older than that timestamp this
way we can ensure that the user is able
to see every item that's been published
even as they query deeper into their
feed with that we have our three APIs
that satisfy all of our functional
requirements sometimes people will ask
do I need to use REST here and the
answer is not necessarily if you
controlled all the clients you could use
gRPC for instance you could even write
these endpoints as function signatures
verse REST endpoints but if you haven't
been doing it that way for a while I'd
recommend instead you just learn REST as
it's very standard across the industry
and you'll likely avoid any yellow flags
from REST zealot interviewers no reason
to go non-standard if you don't need to
so that's our API the next step is our
highle design here's where we're going
to try to implement a system which
minimally satisfies our requirements
while it's not strictly necessary we
recommend to try to build out the most
basic system that satisfies the
requirements before you start to
optimize the reason for this is simple
candidates often lose themselves in
micro optimizations that aren't actually
important before they get a working
system on the whiteboard this can be a
major problem especially if you run out
of time so let's get a working system
and then we can take a step back and
figure out where to optimize
High Level Design
our first requirement is to enable users
to create posts this is pretty simple we
need a service which is going to accept
our post requests and store them in a
database for each post we need to keep
track of who created it its content and
when it was posted in this problem I'm
going to use DynamoB as the backing
store but you're free to substitute in
Cassandra or any other scalable wide
column store we'll put our post service
behind an API gateway and load balancer
we aren't getting into the details just
yet but as posting volume increases we
can scale in more post services to
handle the incoming requests provided we
don't blow up Dynamo DB this is actually
pretty scalable so great our first
requirement is out of the
way next we need to allow users to
follow each other some candidates look
at this and immediately assume we need a
graph database but this isn't the case
for this problem graph databases like
Neo Forj are really useful when you need
to do comprehensions like find all the
users who are followed by at least two
men who also follow each other these can
be tricky queries to answer or execute
and often require specialized query
languages like cipher to even ask but in
this problem we only need to answer
queries like tell me all the users who
are following this user so we're going
to keep things simple as a quick aside
in interviews I highly recommend you
start with simple approaches that are
tightly fit to your specific needs
versus adding a ton of complexity
earlier on there's plenty of time in the
interview to layer on new complexity as
you need it but if you tie yourself in a
knot early on you're going to have a
hard time getting untangled in time the
simplicity of a solution is a hallmark
differentiator for junior candidates
versus more senior ones here we're going
to follow the same model we did for post
creation we'll have a follow service
which accepts requests from our clients
and writes to a follow table in the
follow table we need to support two
obvious types of queries first tell me
all of the users followed by A and then
tell me all of the users who A is
following the way we're going to do this
is putting a partition key on user
following and a sort key on user
followed this will allow us to list for
a given user all the users that they are
following to support the reverse we can
create what's known as a global
secondary index or gsi in Cassandra
world this is just a secondary index you
can think of the global secondary index
like another table but one that's
managed internally and consistently by
Dynamob on our gsi we can choose a
different partition and sort key and for
this we'll choose the reverse our
partition key will be user followed and
our sort key will be user following when
we want to query all the users who are
following a given user we can query this
gsi at a particular partition key and
pull out all of the users who are
following a given user for the record
DynamoB puts a limit on these range
requests you can return no more than one
megabyte of data you can then page into
the results since our user ID and
metadata are on the order of 10 bytes we
can retrieve a bit less than 100,000
entries per requests this will be a
problem for our most followed accounts
but a non-issue for everyone else great
we're almost there let's talk about the
feed
next our third requirement is to be able
to view a chronological feed for a user
we'll create a new service for this
because unlike the post and follow
services this is a readheavy service
which will bear the full brunt of our
traffic we'd expect far more people to
pull feeds than to create posts for
instance also generating the feed may be
computationally heavy depending upon how
many posts need to be merged together
the feed service can interact directly
with the post and follow tables to
satisfy the requests a micros service
fan will tell me I need to wrap these
tables behind APIs so that these
services aren't querying the same data
but that's a huge waste here the
decoupling benefits are dwarfed by the
overhead we introduce but if you feel
like your interviewer is going to be a
stickler for microser best practices go
for it in the ideal state the feed
service will take in a user ID and query
the follow table for all the users
they're following then we'll take that
list of users and query the post table
for each one of them to grab all the
recent posts for that user finally we'll
merge all of these lists together before
returning them to the requesttor as our
feed if this sounds problematic it is
there's a few big problems here but
let's address the most costly ones first
when we want to query our post table we
need to be able to look up the posts
created by a specific user we can't do
that currently with our primary key
being the ID of the post which is useful
for pulling a specific post but not much
else so we'll again create a gsi sorted
by creation time to do that cool we're
halfway there but alarm bells should
still be ringing for you what about if
the user is following a ton of other
users what if the creators have a ton of
posts at this stage in the interview
we're going to acknowledge there are
still problems verbally to our
interviewer and commit to solving them
in a few minutes when we get into the
deep dive we want to keep traction so
that we can solve our core functional
requirements before we enter our
optimization loop our final requirement
is to support pageionation so we can
have a clean infinite scroll experience
for end users to do this we need a way
of grabbing pages of the user's fee
remember how earlier we added a cursor
argument to our API design that cursor
indicated the oldest timestamp the user
had seen in their feed we can use that
timestamp as a filter as we go retrieve
posts so when we query the post gsi for
each user the requester is following
we're going to retrieve no more than the
page size number of elements and we're
going to query with a created at that is
less than the cursor basically we're
going to grab the most recent posts
before this date that allows us to page
back
infinitely and that concludes our highle
design we have a system which satisfies
our functional requirements and will
work with a lot of users but not for
users who follow or are followed by a
lot of
Deep Dives
people we'll start our deep dives by
addressing the problem headon how can we
deal with accounts that follow a lot of
people in our current design if you were
following 10,000 people then our feed
service needs to make 10,000 requests to
the postgsi returning maybe 10 million
aggregate posts all of which need to be
merged and sorted in almost real time
before returning to the end user that's
a lot of work network calls etc and we
haven't even talked about failures or
tail latency yuck so what can we do
instead your instinct here should be to
think about ways that we can compute the
feed results when the post is created
rather than at the time the user wants
to read their feed and in fact this is a
pretty good line of thinking let's add a
new table premputed feed to our database
we could put this in a separate cache
but I'll put it in Dynamo just to make
things easy when posts are created we
can read all the users who are following
that creator out of the follow gsi and
store the resulting post ids into this
table then when we want to query our
feed our feed service can read posts
directly from the premputed feed table
super fast we'll want to keep this table
manageable in size so we may only store
the latest 200 posts in there if we
assume each post ID is 10 bytes to store
200 posts per user we'd need about two
kilobytes per user just as a gut check 2
kilobytes is almost nothing and Facebook
earns about $100 per user annually in
the US so this is a pretty reasonable
cost for us to bear if we have 2 billion
users million mega billion giga we need
2,000 gab or 2 terab of storage for all
these feeds this is quite reasonable for
a modern system so that sounds great
what's the catch while this dramatically
improved read performance it creates a
new problem for us a pattern which will
repeat until the end of time when a user
who has 10,000 or more followers creates
a new post we suddenly need to write
tens of thousands of premputed feed
records this is tough while the biggest
accounts are rare and aren't posting
often they create a thunderstorm of
activity that we need to handle for
starters we probably do not want to do
this synchronously in the post service
where we create the initial post the
worst case is the hello interview
Facebook page needs to wait 60 seconds
to fire off its latest status update
just because we need to write to a bunch
of feeds so let's use an async worker
pool we'll put together a set of workers
that are reading from a centralized
queue of post updates whenever a post is
created we'll add an entry to the queue
workers who pick up this job will read
from the follow gsi to grab all of the
users who we need to write to their
feeds if this is a large number we might
break it into smaller sub jobs which are
put back on the queue so we can spread
the load across many feed workers once
they have a list of follows followers to
work from they'll create entries in the
premputed feed for those users for the
post ID in question with this solution
in place we've kind of solved the
problem by spreading out the rights but
what about the truly mega accounts the
Justin Bieber who have hundreds of
millions of followers is broadcasting
rights for them even appropriate i'd say
probably not we even talked about some
of the limitations in pulling these
followers out of Dynamob earlier well
we'll need to page through the results
we can refine our design slightly by
adding an extra column to the follow
table which indicates whether the feed
is premputed for that relationship we'll
set this flag when the account being
followed has a ton of followers maybe
100,000 or more if it's set we'll use
the async worker path when a post is
created by that user our feed workers
will write the resulting post ID into
the premputed feed table if it's not set
the feed workers will simply ignore that
follow when the feed service receives an
inbound feed request it will list out
all of the follows which are not
premputed we'll grab the latest entries
from the post list from those accounts
like we did before the premputed feed
table finally we'll merge the two lists
at runtime from the preconmputed feed
table we'll pull out the posts and the
latest end posts from all the follows
that weren't premputed and we'll return
those back to the user this hybrid
approach gives us a nice blend of both
worlds we can cap the number of writes
we'll need to do when a post is created
and limit the number of reads we need to
do when the feed is queried i'll note
here that this rabbit hole keeps going
deeper what if a user is following a
large number of huge accounts what
happens when a user unfollows another
user does the premputed flag ever
reverse i'll leave some of these as an
exercise for the reader but these
questions are nearly infinite and good
followup do note that many platforms
will enforce enforce product limits
rather than engineer to infinity google
does not let you get to page a thousand
linkedin caps the number of connections
you can have sometimes it's just not
worth engineering around the
0001% of users at some place you throw
in the
tow let's touch on one more deep dive
before we wrap things up so far we've
been focused on getting the list of post
IDs that make up a given feed but when a
popular account publishes a new post
that means that post will be at the top
of the feed for a large number of users
a huge number of accounts will suddenly
be querying for a singular post ID in
the post table this is a recipe for a
big class of problems usually called
hotkey or hot shard the problem is
systems like DynamoB while theoretically
scalable are only scalable as long as
you design your system within certain
parameters one of DynamoB's assumptions
is that you need relatively even load
across all your keys the reason for this
is pretty straightforward the partitions
we've been talking about are eventually
physical hosts at some level and those
physical hosts have real performance
limits if all of your requests go to
host A it doesn't matter if there's a
thousand other hosts ready to handle
different requests you'll get throttled
or
fail so our problem is that we're
getting a tidal wave of requests for
Justin's latest post and Dynamo DB is
throwing throttling exceptions what can
we do well the first option for us is to
shield that particular partition with a
distributed cache with a least
frequently used eviction policy and time
to live ttl posts don't change often so
keeping them around for a short period
should be okay and we don't need a ton
of memory we're only going to use this
for the most viral posts or those with
the most reach this cache will keep our
hottest posts in memory diverting
requests away from the sensitive Dynamo
DB partitions instead of a million
requests hitting Dynamo DB only one
request does which sounds like a great
idea and this is a solution that many
mid-level and even senior candidates
propose except it has the same problem
if we have a distributed post cache
where we use the post ID to shard the
cache the cache also has a hotkey since
Reddus is in memory the throughput of
this cache might be enough to absorb the
load but the same fundamental problem
exists a simple solution for this second
problem is to have multiple cache
instances rather than sharding our cache
our feed service will then randomly
choose amongst the instances that are
available we don't even need these
instances to be replicas of one another
or to coordinate in any way now instead
of limiting ourselves to one request
making its way through to Dynamo we'll
instead have n requests where n is the
number of instances that we have in our
cache but since that n the number of
cache instances that we've set up is
dramatically smaller than the millions
of requests that we were expecting this
is a great trade-off and allows us to
solve the problem there's a lot of
subtlety here especially around how you
shard data and interviewers will pick
and choose where they expect you to go
deeper it's very common for them to take
control of the interview at this stage
and choose specific weak points in your
design that they want to probe more
deeply even if you've already
acknowledged them for what it's worth
this is not necessarily a sign that
you've gotten something wrong it's just
a way for them to drive to the level of
depth that they need to get the signal
they need remember that interviews are
not just about you reciting a correct
answer to a problem it's about observing
your process for solution design a lot
of signal the interviewer is gathering
to make a hiring determination is
implicit it doesn't actually show up on
your whiteboard i'm going to stop deep
dives here for reasons of time but all
of these types of deep dive questions
are why this particular problem is so
popular with interviewers and the
answers generally follow the same
pattern identify a bottleneck think
about solutions and then identify the
bottlenecks in those solutions and keep
going the more comfortable you are with
the process of identifying and proposing
solutions the more effectively you can
get to a workable design in an interview
Conclusion
setting we've covered a lot in this
problem async worker pools fan out
hotkey problem sharding and more well
you're unlikely to encounter this
specific problem in your next interview
the concepts we've covered should be
common to many more problems you'll see
both in interviews and as a practicing
software engineer i hope this has been
helpful and until next time see you
