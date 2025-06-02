Intro
all right hello everyone welcome back to the channel I am back with another breakdown of a common system design
interview question this time Love Is in the Air uh we're going to be designing
Tinder um so if you like our content you want more of it make sure you like subscribe you know all those things that
I have to say uh but really the increasing number of subscribers is motivating to us and it's motivating us
to keep pumping out more and more content for all of you so if you're enjoying it go ahead and take a moment
to do that uh quickly for those who are new to the channel I'm Evan I'm a former meta staff
engineer and interviewer conducted many hundreds of interviews uh and nowadays I'm the co-founder of hello interview
and hello interview is a site that helps software Engineers prepare for their upcoming interviews both via free
educational resources uh as well as paid mock interviews with senior interviewers from your target
company um if videos aren't your thing I'm going to link in the description a written guide um that has all of the
same that covers all of the same topics that I'm going to discuss in this video so let me show you what that looks like that's over here you can see on hello
interview.com we have a lot of common problems at this point Tinder being one of them this was actually written by one
of our top coaches Joe Joe was a former staff engineer at meta he's currently uh
an engineer at notion Joe and I actually went to college together uh he's a super super bright guy so this is a fantastic
write up he also wrote the Cassandra write up here as well as YouTube so give this content a a a read um I'm going to
put his LinkedIn as well as my LinkedIn in the description so if you want to connect with either of us you can find those there last thing um before we get
started we've been working really hard this last couple months on what we call guided practice and so if you want to
practice this problem or really any of those problems that we have here on the leftand side um you can use guided
practice and this walks you through each of the steps in our delivery framework the requirements the Coreen the apis uh
deep Dives highle design and gives you instant feedback on each of the
questions so this was a deep dive question I just answered we'll talk about this in the video I nailed it um
but you can see kind of all of the questions here going all the way back to when you did API routes that wasn't a very good answer core entities the
non-functional requirements Etc so take a look at this uh you can do Ticket Master for free right now um the other
ones do cost money they're 60% off through the end of September it's just a thank you that any early users so give
that a look but enough of the upsells let's Jump Right In I know what you're here for let's show you how to design
The Approach
Tinder all right so what the heck is Tinder in the first place well Tinder is a mobile dating app uh it was
revolutionary when it came out the way that it works is it shows you a stack of profiles that match your preferences and
are close to you in location and then you can swipe left or right really quickly in order to indicate swiping
right if you like someone and left if you don't like them or if you're passing on their profile and then if two users
end up swiping right on each other then they match and you're allowed to dm with each other and chat so that's what
Tinder as an app is now as we walk through this call it a system design
interview of course this isn't uh a exact replica of a system design interview because it's me an interviewer
walking you through kind of in more detail than you would provide in an actual interview how I would answer some
of these questions and how I've seen candidates answer them in the many times I've asked uh candidates to design
Tinder but we're going to follow the hello interview recommended delivery framework and if you've watched any of
our other videos then you know this framework really well by now but I'll go over it just briefly the first thing
that we're going to do is that we're going to lay out the requirements of the system this is both the functional requirements or the features of the
system as well as the non functional requirements or the qualities of the system qualities are those things like
the latency the scalability ETC you'll see when we get there we're going to define the core entities of the system
these are basically like the tables that you're going to have in your data model the entities uh we won't go into the
fields just yet that'll happen later on in the high level design but we'll get a a basic overview of what entities are
exchanged uh and persisted in our system and then we'll move on to the API design
so we'll document the apis the user facing apis of our system basically the contract between our users and our
backend data flow is not relevant to this problem that's only relevant for non user-facing system design questions
for which this is user-facing nonuser facing are are things like you know designed distributed uh job scheduler or
rate limiter or a message CU you know some of those deeper backend components so not relevant here you can check out
the videos on adclick aggregate or WebCrawler if you want to see examp examp of data flow uh then we're going
to sketch out a simple highle design of the system now crucially the goal of our highle design is to just satisfy our
core functional requirements we're not worried about the non-functional requirements yet we're not worried about scalability or uh ensuring our
availability consistency guarantees or any of that stuff yet we're just getting down something simple that's going to
work and satisfy our functional requirements and then we get to the fun part which is the Deep Dives this is
where we take that simple highle design and we layer on all of the nonfunctional
requirements by going one by one through them and going deep to ensure that we can satisfy each of them so this is the
the general framework that we're going to follow let's get
Requirements
started as promised we're going to go ahead and start with those functional requirements and so so you guys don't
have to watch me type I'm actually going to paste in the functional requirements here and we'll go through them and so
when the interview first starts this is a time where you can ask some questions like you may not be fully familiar with how Tinder works that's fine spend some
time asking your interviewer not only how Tinder works but which parts of Tinder are most interesting to them and
so this is where you might list out some of the features like you can see on the screen here and then prioritize them say
like these are the ones that I think matter in this 35 to 45 minute interview and here are some of the ones that I think fall below the line so in this
case and when I ask this question this is is the set of functional requirements that I usually land on with the candidates and that's that first users
can set their preferences and so this is like the type of people they want to match with so the age range the gender
that they're interested in things of this nature any preferences uh maybe and
then importantly this doesn't include like creating a profile I usually put
that as out of scope and so we can do that here actually so out of scope o like creating a full profile we will
create a profile only because it's important to set the preferences but in terms of like linking all of your images
as a user and you know your description and your funny witty prompts and all of that we're going to consider that out of
scope now once a user has set their preferences then we're going to need to be able to or they're going to need to
be able to view that stack of potential matches and so the user can view a stack of potential matches and this is going
to be based on those preferences that they set so we should only show them people that are in their age range and gender preference Etc and importantly
they need to be close to their current location so this needs to be users who are only you know n miles and one of
their preferences set can be the distance that they're okay with um and so it'll be n miles from their current
location is the only matches that we'll show them and then from there users can swipe left or right no or yes
respectively on each profile and if two users swipe right then they should get a match notification that they've matched
so those are the core functional requirements that we're going to go with now I'll often times when asking this
question introduce a constraint which makes this problem more interesting as well and that constraint is that we want
to avoid showing repeat profiles so if somebody's already seen a profile then
we don't want to show it to them again this makes sense and this is how Tinder Works you've already decided if you like or don't like someone there's no reason
for us to show them to you again so that's our functional requirements of
course uh functional requirements these are the core features of the system they're usually phrased in this like users can
users should be able to users whatever that's that's the framing of these functional requirements and that's how
you should be thinking about them in your head now when it comes to the nonfunctional requirements let's write
that out here non-functional requirements this is where you worry about the qualities of the system and so
this is where you're going to consider things like cap theorem this is where you're going to consider the scalability
the latency the fault tolerance the durability all of those ility statements that you've heard and know so well
there's actually a list of these things that should be considered on the Hello interview website if you go to the delivery framework and then go down to
non-functional requirements uh I've kind of documented the list of things that you might want to consider here um and
so the key is that like all systems are usually all these things all systems try to be fault tolerant and scalable and
low latency and of course they do but with non functional requirements you're specifically trying to identify the
qualities that are uniquely challenging and interesting for this particular system that's the goal and so step one
identify which of these qualities are relevant to this system step two put them in the context of this system and
then step three if possible quantify them so let's do that together here the
first thing I would consider is Cap theorem so should this system prioritize consistency or availability and you
don't know about cap theorem go give it a read it basically states that in distributed systems you have to choose two of three consistency availability
and partition tolerance partition tolerance is a guarantee in a distributed system so we decide between
prioritizing consistency or availability in making this Choice the question is really does every single read of the
system need to read the latest right or else it will fail if so we need strong
consistency if not then we'll probably prioritize High availability and so in the case of this system we actually want
to prioritize consistency specifically in the context of the system swipes so
we want consistency for swipes and the reason for this is because the way Tinder works is that when the second
person swipes right on a profile for whom that other person already liked them then they instantly get a uh you
know match notification that shows up on their screen notification might not be the right word but the second they swipe
then bang it goes you match and it gives them a little celebration thing um and so in order for us to ensure that we get
that match right when we swipe right well we need to have the most accurate
view uh of the latest rights when we read to know that somebody else had already swiped on us even if it happened
only moments before and so I'll talk later on in the Deep dive some caveats here uh there is a way to satisfy this
problem without consistency for swipes but um I'll go into more detail on that later for now we're going to prioritize
consistency over availability specifically as it pertains to swipes for all other parts of our system we'll prioritize High
availability um other things that we want to consider here is when a user opens up their app they want to get
their stack of potential matches shown to them immediately so they don't want to have to be waiting and this is a long
operation potentially um as it pertains to to Tinder because we're having to
filter all of the profiles based on location which can be expensive and then based on on your set of preferences and
without careful consideration here during our design this could take a while and so I'm going to explicitly
call it out as a non-functional requirement I want low latency feed SL
maybe we'll we'll stick to that same terminology stack loading and I'm going to quantify it I want it to be under 300
milliseconds and so for quantification here what you should think about is 200 milliseconds is perceived by humans as
real time this is like a blink 200 milliseconds and so when we have results
and things we usually want to be between that 200 and 500 millisecond range and so I'm just putting 300 here 500 maybe
would be okay to half a second um but I'm going to go with 300 and then the next thing to call out
here is that there's going to be a lot of of Rights particularly from swipes
like swipes are so easy and because they're so easy users can just swipe left right left right left right A ton
and so maybe in the interviewer in the interview I would ask my interviewer what's the scale of this system or I would make a prediction and I'll tell
you it's about 10 million daily active users and so we can write you know maybe
somewhere around here let me move things around to the scale is 10 million daily
active users and so um if we have 10 million daily active users and each of
them swipe on say 100 profiles or whatever each day then this is a lot of Rights and so what I'm going to add to
my non-functional requirements is scale to handle the high right through
throughput of 10 million time 100 swipes a day and of course they'll be Peaks
associated with that too so those are my non-functional requirements and now of course we're going to use these when we
get later in our deep Dives um to inform what we need to satisfy in our system
where we should go deep and what we need to satisfy so let me stop here and let's move on to the core entities in the
Entities & API
API with the requirements in place we're going to move on to the core entities
and then the API and so core entities this is where we simply
document uh kind of the core entities that are persisted and exchanged in our system we don't need to do the full data
model the full schema here but I would communicate that with my interviewer so I would say explicitly like I'm going to
document the core entities these are going to be the tables that I'm going to have in my database uh I'm not going to
go into the full schema or data model yet because it's a little early in the design I don't know all of the columns
just yet so instead I'm going to do that when I get to the highle design and so for here I'm just going to call out what
are these main entities well we're going to have a profile this profile is going to be responsible for storing the
preferences of the users uh we're also going to have a swipe when user swipes
left or right we'll persist that and then we're also going to have a match if two people match then we'll create a new
match entity to to identify that this was a match so these are the core entities of my system easy
enough we're going to go from there onto the API and so these are just the user-facing apis needed to satisfy our
functional requirements and so the way to build up your apis is to look at your functional requirements and go one by
one through them often times there's a one toone mapping between a functional requirement and an API this isn't always
the case we'll actually see an example of that here and sometimes there's maybe two apis required to satis by a single
functional requirement but this is the the general uh process that you should
follow to come up with these apis so let's do that here the first one users can set their preferences so this is
essentially creating a profile with their preferences of course we talked about how out of scope is creating a
profile with their images and all of those things but we do need to create a profile that at least just has those
preferences because that'll be important to creating the recommendation stack and so we're going to use rest here we're
going to make sure that we have proper rest vers so I'm going to post my resource is going to be profiles and the body of this request is
going to be those preferences so maybe the Min age maybe the max the max age
the gender that I'm interested in matching with the radius how far away they can be from me and maybe there's
some other things here uh in terms of preferences as well and this could either just return a success 200 or
error otherwise or maybe it Returns the actual profile back to the user either way now the next one that we need to do
is that users can view that stack of potential matches this is going to be based on those preferences that we just said as well as their current
location and so this is going to be a git request and this is going to be on the resource stack or you know some
people are very particular about the plural of their resources so we can call it Stacks I don't have a strong
preference there um now the server is going to take into consideration those preferences that we stored in our
database in the profile entity um but it also needs to know the user's current location and this isn't something that
we're going to store cuz it's something that's going to change so we're going to require the user to pass this into us
via the API specifically via a query pram here so they're going to let us know where they are the latitude and
longitude uh and then this is going to return a list of profiles and so this is one of the nicest things about following
this framework of doing core entities and then API because our API can just reference these core entities we don't
need to document all the fields and columns and and you know I did do the post body here didn't necessarily even
need to but this is going to streamline our API writing I don't need to again write everything that's in a profile
it's just a profile I'm referencing that core entity that I defined now we also
need to know what user we're getting a stack for of course and so some people might think to put the user ID up here
as either a path parameter or a query pram maybe even put it in the body as uncommon that is in get requests um but
these would all be security concerns you know this if you've watched some of the other videos we don't want to put put the user ID into the request itself at
least not into the the body or the query or path progams because it can be easily manipulated uh so I could just make a
request with somebody else's ID and I could get their stack and see their preferences um that wouldn't be very
good or their matches based on their preferences that wouldn't be good so instead uh we're going to use proper API
security here and we're going to use either JWT or a session token in the header and this is what we're going to
use then server side to validate who the user is making this request okay now the
next one that we have here is that users can swipe left no or right yes and so this is again going to be a post request
because it's going to create a new row in our database in our swipes table create a new swipes entity and so we'll
have swipes here we'll need to know who we're swiping on uh notably this isn't you this is the other user that you're
swiping on um so as a path parameter here we're going to have that user ID
because it's required that's why we use it here um and then the post body will
be something like maybe the decision of either yes or no this could also be left
or right or anything like that so we have these three core apis and then then
this again could just return uh you know I guess it's going to return did they match yes or no so it might return a
match object um but that'll be optional it could also return just undefined in the
200 so looking at our last functional requirement here two users swipe right they get a match uh and there's a
notification and so in this cases we'll talk about more later on and we already alluded to it the second person to swipe
is going to get that instant match that shows up on their screen right for the swipe the other one's going to need to get a push notification and so that push
notification part well that's not an an a user facing API our server is going to
in uh initiate that so we're not going to write an API for it uh instead these
are our Three core user facing API and now as we move on to the highle
design we're going to use these to go one by one and ensure that our design is
able to satisfy each of these requests both the inputs and outputs of these
High Level Design
requests okay so we' got the requirements in place we've outlined our core entities we've also documented our
API at this point we're sort of like done with the setup we have a really clear understanding now of the problem
what what it takes to solve it what our contract is is with our back end and now it's time to start sketching that out so
we're going to head to the Whiteboard and we're going to draw out our highle design and our our highle design again
the goal is to meet these functional requirements and we're going to just start simple and so what we're going to
do is we're going to go one by one through these requirements or put another way one by one through our apis
and we're just going to make sure that our system can handle each of these so let's start with that users can set
their preferences so we have this post API on profile this is going to need to store some profile information for the
user so how can we do that well I'm going to introduce here first a client
this is just going to be the user's mobile device since this is only mobile applications this is going to interact
with I'm going to put an API Gateway in here potentially early uh you could hold off and do this later but I'm going to
opt for microservice architecture it's by far the most common architecture in the system design interview so if you're
not sure it's probably the right thing to go with but when you introduce a microservice architecture then you want
an API Gateway here and the main thing that it's going to handle is routing so it's going to Route each of the API requests to the appropriate service it
can also do some additional middleware like authentication or uh
authorization things like rate limiting potentially whatever slightly less important I wouldn't spend a lot of time
there in the interview the main thing is that the API Gateway is going to route to the appropriate microservice and so the first
microservice that we're going to introduce is what we'll call this profile service and so we'll call it the
profile service and the profile service is going to be responsible for taking that set
profile API request so it's going to take that set profile request and it's
going to construct a SQL query in order to add a row to our database uh in the
profile table and so I'm going to have a profile database here database excuse my
typing and we are going to create a new row in that and now when we documented the core
entities we told our interviewer hey we're going to hold off on the data modeler schema for now because we don't necessarily know it yet we'll do it
during the highle design this is my recommendation I want to be clear this isn't the only way to conduct a system
design interview you could do it earlier if you want to and if you know the columns feel free uh I like doing it
this way because now when I'm actually um really focused on the flow of data through my system I I have a really good
understanding of what needs to be persisted here and so when that API request comes in I have this profile um
table and it's going to have the name of the user probably of course we need that but then it's going to have all their
preferences so this is like their Min age preference their max age preference
uh their gender preference gender preference um maybe like the the max
distance from them that they want to see people and of course it'll have other things but those other things are out of
scope for this interview so I'm just going to dot dot dot them so now just next to my database I know exactly
what's in this and as we continue to build the highle design if there's more columns that kind of come to mind it's
easy for me to just add them here um since via proximity they're they're close to my database so a user uh has
that post API request with some profile information it hits our API Gateway it's routed to the profile service and the
profile service uh formulates a SQL query in this case maybe I'm making the assumption that this is a SQL database
that may not be the case there's there's no right or wrong answer here um there's not going to be a ton of data
um there's not a ton of relationships so it really doesn't matter choose your database of choice um I'll paste this in
here you would never do this in an interview but I know that we have some maybe more Junior folks who watch these
and this might be interesting to them that's the SQL query that's an example of it so you'd insert into the profile
table with these values so pretty straightforward but that's what would be run from the profile service sweet okay
let's move over to our second one then users can view a stack of potential matches so this should take into consideration the preferences and it
should be close to the current users and so that's this API this G Stacks lat long
API so when that g stack API request comes in we're going to have it also hit
our profile service certainly at least for now as we're staying simple and it's just going to have a simple I'm going to
delete that it's just going to have a simple SQL query in order to get the preferences of the user and then a
second SQL query in order to get all the profiles that meet those preferences
right and so that query might look something like this you're going to have a first query that just says fetch me
all of the profile information for this user in my case user Evan and then using that user information we're going to do
a second SQL query that says well Evan wants between 25 and 35 females a little weird to say um but nonetheless you guys
get the point in the context of the system design inter of you and then we're going to do this to handle distances so we know my latitude and
longitude because it was passed in um by the API request and so we can filter um
using my max distance and the distance of wherever that that user currently is
um and so in writing this out I'll call out maybe I slightly misspoke earlier I said that we weren't going to need to
persist users locations certainly we will have to do that I'm going to abstract it away just because it's not
the most important part of the problem but maybe every time user sends their git stack with their current location
we'll save latest location and this is what we're going to use in order to
compare their current location at time of requesting the stack to the latest location of all the other profiles that
they could potentially match with That's How we'll handle that so that's what's going to happen it's going to return the
stack back to the user now really importantly um this is inefficient we
know this is inefficient we know that this part in particular of the query is super inefficient even if you built
indexes on ladin Long here uh you're using indexes that are built for
onedimensional data in order to query two-dimensional data and it's requiring a pretty significant scan of the
database and so this isn't good and it's something that we're going to optimize in our deep Dives but it's good enough
for now now a question that I often get while I'm conducting interviews is or
conducting mock interviews at least um is do I need to start start simple like what if I know the answer what if at
this point I know that I need some geospatial index or something should I just mention it and the answer is of
course you can if you know the answer then go ahead and talk about it um the reason that we start simple in the high
level design is two things one it may be a problem for which you don't know the answers and so by building up the basics
it's helping uh build things sequentially and linearly in your mind such that you're going to be able to do
those deep Dives more efficiently later on like you might not know the answer yet to put that in another way um the
other thing is that we don't want you to go too deep in a certain place early in the interview and then spend all your
time there and all of a sudden you haven't satisfied the core requirements of the system and so that's a common
mistake I see candidates make they get to this point in the interview and now they just start talking all about geospatial indexes they burn 20 minutes
or something and they never satisfied all the other requirements and then it's hard for me to pass them in the
interview because they've designed a system that didn't meet the requirement that we agreed upon early on and so if
you know the answer maybe you mention it maybe you just call it out maybe you write it down if it's quick just don't
let yourself get too bogged down here um because the negative case is like I said
that you don't get to to meet the functional requirements of the system so little bit of a rant there but hopefully
that makes sense for our purposes we'll start simple like this and at this point we've satisfied two of the main uh
functional requirements and we have two more now let's move on on to our third functional requirement users can swipe
left no or right yes and we have that post swipe
API and so what we're going to do here is that I'm actually going to add an additional micros service for this so
I'm going to move this down and I'm going to add a swipe service and so the
justification here as to why I would create an additional micros service is because the traffic patterns of these
two services are very distinct they're very different from one another in that the profile service is not going to have
nearly as many rights only when users are creating or setting their preferences and in terms of reads it's
only when we get the stack which is not going to be all that often the swipe service on the other hand for every one
of these is going to have maybe a hundred swipes because it's user swiping on a stack and so we want to be able to
scale these two Services independently basically I can have more of these as I
need to scale up since a lot is happening here while keeping fewer of these so that's the justification here
for separating them and so now when a swipe comes in we'll say that this is a
swipe with either a yes or a no and I'm also going to add a separate swipe
database and so I'll create my swipe database here I'll call it just the swipe DB
um and this is interesting and something that I get a lot from candidates as well
which is do I need separate databases um do I need a database per
microservice can I have microservices communicate with different databases and there's a lot of misunderstanding I
would even say out there in the industry there are microservice zealots who will tell you that every single microservice
needs its own database and it can't communicate with other databases it has to communicate through servers and the
reality is that's not true that information is a combination of both outdated and just like overly pedantic
that's not how systems work in the real world it's totally fine for multiple microservices to write to the same
database in case in many cases it's optimal of course there's trade-offs here um by separating out the databases
you have better fault tolerance one can go down and the app doesn't necessarily go down if another stays up this all
depends on the circumstances of your actual application um but in this case my
justification for separating out the two databases is because the requirements of
the data base are different we talked about how it didn't really matter here there's not a ton of Rights there's not
necessarily a ton of reads there's not much relational things going on here you can you can choose whatever database you
want but for this one we have a lot of Rights uh and I can actually prove that
right we can prove that because we have 10 million profiles and about 100 swipes per day on average I think we said and
so that ends up being 1 billion swipes swipes per day on average there's
100,000 swipes in a or 100,000 seconds in a day that's rounding up um and so that gets
us to 100,000 per second 100,000 swipes per second oh bad math 10,000 swipes per
second um but then we can take that 10,000 swipes per second we can call that the average and we can maybe multiply it by 10 maybe most people
swipe while they're laying in bed late at night or at a certain part of the day and so I'm sure there's some some Peaks
here maybe even some seasonality until we get to 100,000 swipes per second I
think this is straightforward enough math I'm doing it on the spot you guys will let me know in the comments if I messed it up but the point here is that
that's a lot of Rights and a good thing to understand is some of kind of the
limits of modern databases as their as it pertains to their read and write through put and so like a postgress
database hosted in AWS if you get a large instance uh and you're writing not
a ton of data how much data are we writing here right we're probably writing like 1 kilobyte of data uh we
just have two IDs maybe let's document that so we have a swipe we have the user
one we have the user two we have kind of whether or not it was a like so yes or
no uh and then maybe like some cre created ad or something so this is 32 by or 16 bytes 16 bytes a couple bytes uh
you know another what is this 12 16 bytes or so so it's less than than 100
bytes um so even less than that 100 bytes of data and we're writing that
100,000 times Peaks per second okay and so as I was saying uh postgress in AWS
you're looking at like so postgress AWS Max instance you're looking anywhere
between like 5,000 and 20,000 rights per second why the range here because it
totally depends on what data you're writing how large is the data how big is the instance in AWS like there's a lot
of there's a lot of factors here so this is just roughly rubbing it and so like we can kind of think about this as 10K
rights per second when we're dealing with a relational database like postgress notably this is per node right
we can always scale to more nodes um but this would mean that we need anywhere from like 5 to 20 nodes totally possible
for what it's worth it's not crazy um and we'll talk about in the Deep dibs maybe more about these tradeoffs but
this is totally realistic but there also exists Cassandra and Cassandra is
optimized for rights uh and so with fewer nodes we can handle the same right
through put and so maybe it makes sense then for that reason to separate this into a separate database and to have it
as a different database technology you mean Cassandra and so again trade-offs here the team needs to learn two
technologies now if we just both made these postgress that would be easier on the team but it would cost us a bit more money potentially cuz we have more
postrest nodes these are the Fun Trade us to discuss in an interview um I'm going to go with this option for now we
might change it later on but uh Cassandra it's right optimized so it can handle this peak of 100,000 rights per
second better than a postgress database for example could uh I'll link actually
in the description there's a Netflix Tech blog that's pretty great it talks about how Cassandra scales linearly with more nodes um and how they were able to
get it to 1 million rights per second for Netflix so pretty interesting read
I'm worried a bit about taking too long in this interview but it may be worth me just briefly explaining why Cassandra is
better at rights than something like postgress so I think on the spot here
I'm actually going to do that um this is going to be maybe a little handwavy obviously this would require a video
itself so I'm not going to go into too much detail on our website we have a deep dive on Cassandra so feel free to
read that but the real Essence here is that Cassandra is doing two things that
postgress isn't the first is that it's batching its rights so it's keeping all
of its rights in memory and then only when that memory kind of gets full or a
certain amount of time passes does it actually flush and then write into do an iot to disk so this makes it fast um and
then additionally that that flush to disk is just appending to the end of a file and so let me sort of briefly go
over how that works and compare the two so Cassandra what happens when a write
happens well the first thing that we're going to do is we're going to write to a log so we're going to write to a log file this is so that we can persist that
that write in case anything goes down and then two we're going to write to a mem table and so this is just writing to
memory this is just writing to memory so not to disk this one is to disk so you have one dis right and then you have one
memory right and then you can return to the user acknowledge so three act the right all done at this point and then
the fourth thing that happens is periodically we flush that memory that
mem table uh we flush memory to disk and when we do flush it to disk uh we flush
it to disk in a way that's just appending to the end of a file so right
is just in aend um there's a bit more information there I'm being a little hand wavy but like this is the Crux of
what's happening now let's compare that to postgress and so with postgress we also write to a log and call it a write
ahead log and postgress case so again that's dis but in this case now we
actually do the DB WR to disk too so this first log one again is just in case
something goes down we want to get that write down as soon as possible in case the database goes down we can recover um
but then we're almost immediately going to do the DB right now there's some caching and there are some optimizations in postgress that makes this not always
true I can hear you guys yelling at me in the comments but this is mostly true we do the DB right and then importantly
the ZB R and postgress isn't just a pending to the end of a file it's actually seeking to find the right page
where this data exists finding the data that exists in that page and then actually updating it so seeking to write
spot and changing or adding row I guess is how I'll call that um and so if you
were doing like an update to a row in postgress you need to go find that row and then update it if you're doing it in
Cassandra you're just going to add a new line at the end of the file that says I want to update this row and then
compaction is run periodically which basically takes all of these different rows and compacts them into just a
single one in order to save space so I might have gone too deep here but hopefully that helps at least a little
bit understand why Cassandra is is more right optimized it's because it both batches the rights and the rights are
quicker there is to the end of a file and so I'm going to go with uh Cassandra here for my swipe database a last
functional requirement to handle is the matching so when two users swipe right or yes on each other they match and they
get a notification so the client's going to swipe get the swipe surface um we're
going to add that swipe to the database and then we can also check is there an inverse swipe and then if there is we're
going to want to create a match first and so we could create that match in this database we create it in this
database or we could create a new database and I don't want us to spend too much time thinking about this
there's a lot of trade-offs here but it's not the Crux of this problem so I'm going to do something that might seem slightly surprising um but I'm going to
do the following and I'm going to create the match in this database down here and
so it's going to be user one oh user one user two uh you know probably a created
at time or something whatever and and the reason that I'm going to do that is just because I'm foreseeing even though
this is out of scope and not important to this problem that we're going to want to load users profiles and all of their
matches and so there's maybe a slight relation there and I can put them in the same table um it's not a big deal could
potentially put them here too we maybe want to reconsider Cassandra though it's also fine um anyway don't think too much
about this it's not the important part of design Tinder but we're going to store that match and then more importantly when we store that match
we're then going to call uh the native notification services and so the native
notification services are APN stands for apple push notifications or FC CM which
is Firebase Cloud messaging which is used by Android um and so they both
provide sdks or apis that allow us to send push notifications to users Oh
wrong one that allow us to send push notifications to users so the second person that swipes is going to
immediately get a congrats right on the client back from our response but the
first person that swiped swiped who knows how long ago and so we're going to send them a p push
Deep Dives
notification all right now it's time for the Deep Dives this is the fun stuff so we have our basic design down and now
we're going to go one by one through our functional requirements and for each of them we're going to go deep to explain how our system satisfies those
non-functional requirements now a quick note about deep Dives particularly as it pertains to your level um the amount of
depth that you go into and the amount of which you proactively lead these conversations is entirely determined by
the that you're interviewing for so if you're a mid-level candidate then there's not a lot of expectations to do
a ton in terms of deep Dives in fact it's more likely that you're not going to really lead the conversation here
your interviewer might take over they'll ask you some questions like for example how are you going to guarantee
consistency in swipes and they'll explain to you a scenario for which things might get inconsistent and then
ask for you to problem solve and try to figure out a good solution there's no expectation that you know these things
or have done these things before when you're a mid-level candidate instead we're really evaluating as the interviewer your problem solving skills
given a question giving a prompt given us highlighting what could go wrong how are you going to problem solve and
determine a solution now with a senior candidate our expectation is that you do a bit more leading here so you're
leading the conversation to at least one or two deep Dives of appropriate depth um maybe we jump in as the interviewer
and point you in the direction of a couple of things that's no problem that's totally natural um but you should be largely leading IT staff candidates
this is is where you're able to fully proactively identify where the issues are lead the conversation and go really
deep in a handful of places maybe at least two or three places like we're going to do um in this video here today
now last thing I'll say there caveat for the staff candidates the biggest mistake I see is that I think candidates hear me
give that advice or they read it elsewhere or see it in our blog posts and I do a mock interview with them and
they just ramod through the interview they're just talking fast like they're really trying to not let me the
interviewer speak because they have the misconception that if I speak as the interviewer then that's a knock against
them leading the interview and that is not true so while you're a staff candidate you want to lead the
conversation sure but it's still a conversation and a conversation by definition includes two people so leave
space for your interviewer to guide you do things like here are the three priorities that I'm going to go deep on
do you agree would you re prioritize I'm going to start with consistency I think it's interesting for this reason stuff
like that it's really important that you give your interviewer room to push you in certain directions because they
likely came into the interview with a couple key things that they really want to see and so by not giving them the opportunity to lead you there you're
shooting yourself in the foot okay so enough about that rant aside um let's get into our deep Dives and so our first
one here if we look at our non-functional requirements is we need consistency for swipes this is a really
interesting one so let me explain what the problem is here the problem is that we want to ensure that the the second
person who swipes immediately gets that Jing match on their screen that they get
the dopamine hit and feel really excited the second person will get that asynchronous notification right we've
mentioned that and so this means that if two users write or swipe at about the same time uh then if we're not
consistent we might not know that the other one swiped so let me give you a scenario we have Cassandra here astute
viewers of this video might have thought to themselves wait he's choosing Cassandra sure has white right through put but by default it's eventually
consistent so he's going to screw himself later on when he needs to talk about strong consistency and swipes to
the people who are watching that Kudos very very key observation so let's talk about what the problem is there you can
have two users swipe it about the same time and let's say that they both swipe they come to the swipe service and they
both write to the swipe DB to write their swipe then they check for the inverse swipe so maybe they just switch
their user ID and the other user's ID and look to see if that entry is in the table uh given that this is eventually
consistent it very well might not be yet basically the node that they're reading hasn't had that right propagated to it
yet and so they're going to incorrectly think that there's no inverse swipe and this is going to happen for both person
a and person B and what it will result in is both of them not getting a match
notification and both both synchronous match notification and neither of them are going to get an asyn match
notification basically we just like lost the swipe or the match forever uh because of the eventual consistent
nature we lost this match we have two people who swiped on each other and the world may never know right they're not
going to be able to find that love that they've been seeking so that's our problem and that's our problem that we
need to fix now there's three main options or three main Solutions here and
let's go through them one by one the first and this might sound like a copout but the first is let's just not be
consistent I kind of alluded to this in the nonfunction requirements that there's a world in which we're not consistent we instead prioritize
availability and the argument here and this is actually an argument I hear many staff candidates make is that if your
person B so the person who or person a excuse me the person who swiped first
you're going to get an asynchronous notification and you don't know when that other person actually swiped you
you assume when you get that asynchronous notification that they had just matched you um but we can kind of
be loose there so in that situation I just described we could have some like
reconciliation workflow which just checks the table every hour or so for
any matches that we missed and in that case send both users an asynchronous notification and they're not any the
wiser they don't know that this match actually happened an hour ago and they think that the other person just swiped
right on them and they had swiped right on them an hour earlier right so they're n little wiser and this would simplify
things a ton uh it would mean that we can stick with Cassandra we can stick with eventual consistency we can reduce
our costs we just have some reconciliation workflow so you can imagine some Kon job here that just like
runs hourly and looks from missing matches um so that's option one and it's
a valid option it's a really interesting thing to discuss with your interviewer for what it's worth now often times when
this question is brought up in an interview it's in the context of you figuring out how to handle this
consistency challenge so many interviewers might be like that's very astute that's very interesting but I'm
going to force you to handle the consistency problem right so you can't do that cop out so tactically suggestion
to you if you ever got this question in an interview I would raise that it's a valid option it's an interesting option
be prepared for your interview to push back on you and tell you that you need to handle something else so let's see
what other options we have option two we can stick with Cassandra here um but we need to get around this eventual
consistency issue and so Cassandra does have some configurations that enforce slightly stronger consistency guarantees
ultimately without going into too much detail there you're probably still leaving gaps and it might not be the
most effective solution and it's kind of you know neutering Cassandra a bit maybe that's not the right word choice but uh
you're not taking advantage of the right throughput that you wanted to take advantage of in the first place so another option that I'll see candidates
do often and is a totally valid great option is that they introduce some cash
and we can say that that cash here is reddis and now every time a swipe happens we're going to write to this
cash and our key is going to be user one colon user 2 and the value can be
anything it doesn't matter because this is essentially functioning as a hashmap so let me make this clear key value can
be anything maybe just true right and so the ordering here matters this says user one swiped on user two they swipe to the
right on user two they want to match with user two right and so now what happens is that anytime a swipe occurs
we'll write that to reddis and then we'll also check if the inverse exists so does user 2 swiping on user one exist
if it does we know that we have a match and we can trigger our match workflow and we can respond synchronously with
the match uh and then after we write to redus we'll then go still update our swipe in either case in
Cassandra and so why does this work importantly this works because reddis is
single threaded and redis has support for Atomic operations so this right in
this read can be done atomic basically they're both happening via the
same single thread and this forces serialization because what we wouldn't want to have happen is that like one
person person a reads person a reads let
me not write that out but person a reads uh person B reads person a writes person
B writes and then by kind of intertwining these read and write operations the read came up empty and
there was no match right so we need to group The read and WR so that they happen atomically and this way the the
the ordering doesn't matter whichever comes first or second is is largely irrelevant but we can't miss anything
because they're happening together if you guys could see my hands right now I'm demonstrating this well with my hands a bit harder to draw on the
escalador Whiteboard but hopefully that makes some sense here so redus single-threaded things can't happen
concurrently at least not via multiple threads and then we can have an atomic operation to user one liked user two and
read did user two like user one and if it did report back now there's one issue
that this introduced and that's that you could write to the cash and then failed to write to the database and now you
have like an incons inconsistent state by introducing rdus we have a distributed transaction now we want this
right and this right to always happen for things to remain consistent they both have to occur and so we made things
a little challenging for us eles um because we need to enforce a transaction in a distributed system and this is fine
there are solutions for this The Saga pattern let me write that down Saga pattern is a common one to enforce
consistency in distributed system in distributed system so maybe I should say
consistent transactions so I'm not going to go into detail on that here that itself would be
a whole video but take a look at that that would need to be the solution here tactically in your interview I would
want to point out that I understand the single-threaded nature and the need for an atomic right in reddis and then that
I understand that I've just introduced some issues here as it pertains to uh a distributed transaction and that I know
solutions for that maybe even just dropping the word Saga pattern would be significant enough there so that's
option two if you want to keep Cassandra the benefit here is that you still have your cheap high right through put this
is wicked fast and it's in memory It's relatively expensive it could certainly grow in size uh and we could do the math
to see how large it's going to grow but that would just result in US partitioning here probably by user one's
ID um and notably if you ended up partitioning and these two things showed
up on a different node then it would become a little more difficult to do that Atomic operation so you'd want some
partition that ensures that the reciprocals show up on the same node um so maybe you sort them first partitioned
by the sorted value anyway nonetheless so this is the this is the the solution two totally valid let's talk about what
a what a solution three would be a solution three would be that you drop Cassandra all together we talked about
in our high level design how postgress could actually work here it would just be more expensive that was our downside
right so we talked about 5 to 10,000 we probably have it here 5 to 10,000 rights per second 5 to 20,000 rights per second
it would take like 10 nodes 5 to 20 nodes or so um to satisfy our right
through put that's totally fine but the nice thing is that post postgress actually
supports um you know acid properties in transactions natively so if we did
switch this to postgress uh should I do overwrite this
yeah I'm going to overwrite this uh and then I might just control Z out so if we did switch this to postgress then we
could do something really interesting we could change a single swipe row to
instead of having two rows for each for each reciprocal swipe right we have this row Row in our cassander database if
user one swipes on two and we'd have the inverse of this if user two swipes on one we could have a row that looked like
this it could be a swipe it could be gosh it could be user one user two and
then like user one decision and user two decision right and so now the reciprocal
swipe and the you know first swipe the first swipe and its inverse are kept in the same row and so why is this
important well this means that when a swipe comes in we're going to either create this R if it doesn't exist or
just update it and both the swipe and the inverse swipe are writing to the same row and so postgress will lock the
row on concurrent rights this is something that's going to happen um automatically for you and so this is
going to cons uh simplify the consistency management a ton and ensure that post's acid properties handle the
concurrency in the the updates accordingly we're going to come in here we're going to lock this row we're going to write our value the next guy if they
came in at the same time is just going to be waiting he's going to come in after on the same row see that somebody else already liked him and Trigger the
match flow right so by updating the same row we avoid the complexities of merging records and we can easily trigger that
match flow just using post's acid properties natively pretty nice um now
we're not going to be able to handle as high of a right through put we'll need more nodes it'll be more expensive we'll not need redus anymore more so that's
great um tradeoffs here in my opinion either the Cassandra option which I'm
going to go back to here um just to make sure that we're kind of all alined
either the Cassandra option or that postrest option that I just documented are both great Solutions five out of
five if you read our answer keys um so either one works I love this conversation and the tradeoff and really
what I'm looking for in the interview is that candidates can show this depth particularly at the staff level at the
senior level I would just want you to land on one of those two options and be able to explain it fairly clearly at the
midlevel option I wouldn't expect any of this depth uh you just introducing a cash and telling me that you're going to
do the lookup in the cash not understanding the complic uh uh you know the complication that you introduce with
the distributed transaction totally fine I don't expect that you have that level of understanding at mid-level so that's
deep dive number one all right now it's time for deep dive number two so we come back over to our non-functional
requirements and we see that we want low latency stack loading so just just as a reminder so that we're clear on what the
problem is right now with our highle design when we want to load a stack of profiles that are recommended to us for
us to swipe on we call that the stack we're going to query the profile service and the profile service is going to
query the profile database for our preferences and then query the database
again to find all profiles that match our preferences right and so this is a
expensive query and it's going to take a long time to run particularly because it needs to filter by Loc
and so filtering by latitude and longitude is a two-dimensional query that normal indexes aren't going to be
able to serve well and it's going to result in US scanning a lot of rows of data doing comparison checks before
we're able to return the stack to users and so consequentially to the users that means that they're sitting there with a
little loading spinner when they're trying to find love and they want that stack ASAP but we got them just seeing a
loading spinner and that stinks so we're going to try to fix that and so again
there's a handful of options options here as well the first option that I hear candidates propose is can we just
do geo sharding can we Shard this database based on users locations and
then we'll have far less data to search over and it'll make that expensive query faster because there's less rows to look
at and this isn't a terrible intuition and in combination with some other Solutions might be sufficient but in
isolation it comes up short and the reason being is what about users who change locations as they do often you
know people go on vacation and then they're swiping on their Tinder account for that new location or what about
people who are on the boundaries then of different partitions uh you know we cut the boundary maybe at the New York state
line or something and people in New Jersey uh are still five miles from me
uh if I'm on the edge there but I'm not going to match with them at least it's not going to be efficient to match with
them cuz I'm going to need to go look at another Shard and what about highly populated areas like New York City there still tons of profiles in New York city
so it's still going to be a really slow query so moral story is in isolation Geo sharding or Geo partitionings not going
to be sufficient here what we really need to do is fix the root problem and
the root problem actually but before I go there let me propose another solution a a solution is that we can do similar
to what we do in like Tinder or or excuse me uh Instagram or Twitter feeds
and we can precompute so what we can do is every night we can do that expensive query and
we can cash it and then we can have a stack there ready for users to go so let
me propose that here I'm going to have like a uh come on I'm going to have a stat
cache and so I'm going to have a stat cache and then I'm maybe going to have
some Cron job some oops some Chron job I'm
actually going to do it here cuz I'm going to want to introduce something later so I'm going to do it like this so
I'm going to have some Cron job that's going to run every night it's going to grab all of our users it's going to run that expensive query and pre-compute
their cash and then it's going to go like this when a user wants their stack
we're just going to pull right off the cache and it's already been pre-computed so this should be like an O of one
lookup time we only have the latency associated with transferring the the size of the stack Over The Wire
so this should be super super quick this is the pre-computation approach this Crown job like I said can run every
night can run every midday uh can run you know every 6 hours whatever you want
it to be you have pre-computation now what's the issue with this approach the issue with this approach is that what happens if
something has changed that something that changed could have been somebody who's in your stat cach deleted their
profile they don't want to be seen anymore they're no longer on Tinder they already found love it could be that you've changed locations I'm no longer
in Seattle I'm in Los Angeles now and so if that's the case I was in Seattle when
you calculated my stack cash now I'm in Los Angeles and I check my stack and it's all people in Seattle what the heck is this that's not what I wanted right
or I changed my preferences I now want you know people that are slightly older
for example and I still have all those younger matches in my stack cache that would not be good and so what we can do
is we can handle the invalidation there and this is fairly straightforward and that anytime one of those conditions is
met like a user changes location or another user changes their preferences or whatever then we have to invalidate
the appropriate stat caches and there's going to be some like fairly complex is application logic to realize which
thatat caches those are that we have to invalidate and then for these users who got invalidated we can either trigger a
workflow in order to refresh them or we can just have them invalidated and then they're going to have a slow stack
loading time so basically take a hit on only a subset of users now even if we didn't have to worry about invalidation
if a user swipes through their full stack cach like let's say their stat cash is 100 people and they swipe
through all of them now they're going to have that long load time again in order to get their new profile and that
expensive query and so it's still not optimal for that reason if they're invalidated again low low load time so
in any of the backup cases we still have that inefficient query that we need to run so let's focus now on solving maybe
that root that root cause of the problem and what we can do is that we need to realize that it's the the latitude and
longitude query that's so inefficient and so we need a geospatial index and so
I've talked about this in a handful of other videos if you want to watch The Uber video you'll learn more about geospatial indexes I won't go into
detail about them here but what they are is a special type of in-memory index that's going to allow you to search on
geospatial information latitude and longitude much more efficiently and and there's different
ways to do this option one is that like this could be postgress and we could have What's called the postgis extension
and so postgress has a bunch of extensions that you can enable one of them is called postgis and it supports
geospatial indexing and so we could just enable it here and it's going to make things really quick at least for the the
the lookup on location so that's option one now there are some complaints that
this doesn't scale as well I think we're well within the scalability limits of it frankly if I was designing the system
I'd probably go that route but that's one option another option which I'll put
down here is to introduce a search optimized database or some external data
source that's optimized for these sorts of expensive queries particularly geospatial queries and so elastic search
has native support for geospatial queries built in and so we could just do
this and so now all of our data is also in elastics search and so we can go like
that all the data that's in our profile database will show up in elastic search at least the fields that we need to search on we can use what's called
change data capture here uh what this basically means and this arrow is an abstraction I want to be clear about
that but any change that's made to your database you have an event stream and it basically puts on a stream like Kafka
for example if you're using postgress Dynamo DB has Dynamo DB streams out of the box but it's going to put those
events on a stream and then we can have some consumer here that that for every change in our postgress database or
whatever database we chose here we're going to also make those updates in elastic search and it's going to make sure that the data between these two
things remains in sync and so this way when we search um to get our new stack
it's a pretty quick query in elastic search and so whether you do elastic search or a different search optimized
database or you do postgis extension both of them work both of them are great Solutions I would lean towards postgis
extension only because it doesn't introduce anent irely new data store that the team has to learn and manage
and all of those things but either option works and now the best solution here is that we combine these two
approaches and so this Cron job now can be running against elastic
search nightly or whatever to cach the stack and then anytime that we invalidate the stack or that a user gets
to the end of the stack we can just query elastic search instead of doing the expensive thing so this is our right
path we'll WR directly the profile database CDC will propagate it to elastic search but our git stack path
either hits the cache if it's there if it's not there it just queries directly from elastic search and given the
geospatial index on elastic search this search is going to be a lot faster than if we searched our database directly the
only last thing I'll say here is that there are other optimizations like while a user is swiping on their stack if there's aund thing people in their stack
and they get to the 90th person then we can proactive ly trigger this caching flow right we can proactively load up
their next set from elastic search cash it and that way to them the scrolling feels infinite they never need to stop
so that's deep dive number two okay we're almost there so kudos to anyone that's made it this far you're doing
great I know I'm throwing a decent amount of stuff at you um but really appreciate you continuing to watch and
hopefully you're finding it useful the last non-functional requirement here is that we need to scale so I'm actually
going to kind of hand wve past this one this one we've been talking about scale for all of the deep Dives so all of our
horizontal or all of our services they're going to scale horizontally we're going to scale up our databases and our caches as needed partitioning
elastic search true manage scales and clusters cash can be partitioned so all
of the normal stuff here horizontally scale Shard our databases load balancers
I think you guys know this stuff pretty well by now there's lots of resources online that can go into that I'm not going to spend as much time there
instead to to wrap up this video I want to talk about the constraint which we haven't discussed yet which is the need
to avoid showing repeat profiles and so how are we going to do this essentially
what needs to happen is that as our profile service is generating or our KRON job whichever one is generating our
stack we need to compare it to people that they've already swiped on and so one like the simplest thing we could
possibly do of course is just this so load the stack or the cach stack from elastic search or from the cach into the
profile service query for for everyone they've ever swiped on and then compare them in memory remove the ones they've
swiped on and return back to the client for a mid-level interview this is great it works no no worries it's not very
efficient so we're going to talk about things that we could do better for those staff and or senior and staff interviews
um but that is the viable simple option that you should certainly always raise in the interview now the other thing that you
could do is that we already have this cash here um so we could use this this
cache we'd probably need a different key value pair because the this isn't going
to be efficient for us to be able to get everyone that user one has swiped on because the key is user one Co and user
2 right so that's not going to be an efficient lookup because this is like a hashmap style lookup so maybe within
this cache we introduce a set uh where the key is the user and the value is
everyone that they've swiped on and so the value is this set of other people
getting a little tight on Space here but hopefully you guys are following that and so instead of quering that database
which would have been slow we can query the cache and do the same thing that was mentioned there this can either be an
arrow oh I just had something pop up on my screen I don't know if you guys could see that or not uh but I'll keep going
here um so we could have this arrow to the profile service also to the Cron job
when it does the pre-computation either way but we hit this cache now what's the potential limitation here
so if we have this cash um we have 10 million daily active users we said that
they swipe so I'm going to come down here we have 10 million daily active users we said that they swipe on an average of 100 a day um we said it was
100 bytes so 100 bytes per entry there or in this case um each entry is just an
additional 16 bytes but anyway I'm still going to round up 100 bytes let's say 365 days that's 30 36 36.5
terabytes uh yearly right so every year we're going to add 36 36.5 terabytes to
this cache caches a huge cash is like 128 gigabyte
cach most AWS caches are smaller than this right 32 64 gigabytes or something
respectively so this is going to take a ton of instances of this cash and that's going to be pretty expensive uh it'll be
fast because it'll be partitioned by the user ID so that's not a problem but it's just going to require a lot of hardware
and a lot of caches so can we do something better well we can and there's
two things that we can do better either we speed up the query to the database or we reduce the amount of space needed in
the cache to speed up the query on the database we could of course just
introduce a index and so uh whether postgress Cassandra we can have an index
on user one and that'll make it at least a lot quicker for us to do this query
and so that's good and is a totally viable approach probably the simplest option maybe even the best option to be
honest so that's one thing we can do the other thing we can do is try to make this use less space and so the option
there is that this 3 36.5 tabes is too much so maybe we introduce a bloom
filter and so Bloom filters I'm not going to go into too much detail but go ahead and Google it on your own they're
space efficient data structures and they're used to quickly check if an element is possibly in a set so just
like how sets have dot contains that are o one similar here in a bloom filter the difference is that it's a probabilistic
data structure so we reduced the space tremendously and in doing so uh we
introduced or we reduced the accuracy or the Precision so with a bloom filter it's just like a set but it takes far
less space but now when you check if something is in a set there's a small chance of a false positive but you
cannot have a false negative and so what this means is that it might return to you yes something is in the set and it
might be lying to you and so in our case that might be fine because most of our checks are going to be no that thing's
not in the set right uh and in the case that it is yes it's in the set then we can just confirm that it actually is by
quering our primary database right we need to double check since there's that option of false positives now in my
opinion this is like slightly over engineering um I probably wouldn't go
for this approach I think the index approach is fine especially since we're mostly handling everything pre fetching
so even though this introduces some additional time uh it's not horrible or the end of the world and I'd rather
avoid the bloom filter which itself still is going to be that large it's still going to be really large here um
that's my personal opinion either option works in the interview these trade-offs are which great the last thing I'll say
is that staff candidates often times will have the confidence to propose that we just adjust the constraint and so the
constraint if you remember was avoid showing repeat profiles but many staff candidates I interview will say something like this they'll say well
actually wouldn't it make sense if we show repeat profiles again after say a month and what this will afford US is
that we can clear out our cash after 30 days basically get over this 36.5
terabyte issue because now we're going to have far less data in the cash we only need to keep the last 30 days and from a user experience it's probably
better anyway things might have changed in 30 days your opinion of somebody might has changed their profile might
have been updated or otherwise maybe it's not 30 days maybe it's 60 90 whatever but this is a fantastic
proposal and it's the sort of thing that you would do at work a PM comes down
with some constraint or some requirement and you as the engineer can push back on them and say actually I think this make
might make more sense both for our user and and from a cost efficiency perspective it's a great option so
that's another thing that could be discussed here but ultimately with this deep dive you're trading off the space requirements and the efficiency in order
to do those check and that's what we would want to hear
Conclusion
about all right there we go at this point I think that we have designed a pretty good implementation of Tinder um
and if you follow the leveling guidance that I gave throughout you'll know what exactly would have been required at each level if you're somebody who just fast
forward to the of this video and you're looking at it and you're thinking I'm a mid-level candidate this is a lot watch the full video this this this isn't
expect at all from a mid-level or even senior candidate we we went into depth um in all the places that we could or at
least a number of them um anyway Kudos if you made it this far this ended up being a long one let me know how you
feel about the length I think this is 15 minutes longer than the previous ones I usually try to keep them an hour I know
that I went on some spur the- moment tangents throughout in this one let me know if those were good useful if they
were bad ultimately I just want these videos to be as useful as possible to you all so uh let me know in the
comments also leave any questions call out anything I did wrong as always I'll be trying to respond to comments as best
I can um lastly again check out our guided practices uh where you can try
this question on your own or consider booking a mock interview with us at hello.com but until next time good luck
with your preparation and thanks everyone for watching
