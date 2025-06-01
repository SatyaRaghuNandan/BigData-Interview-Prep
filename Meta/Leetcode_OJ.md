hi everyone welcome back to the channel uh I'm back with another breakdown of a common system design interview question
this time we're going to go over how to design leak code or it's often times referred to online as online judge
online coding competition or Live Leaderboard you'll see any variation of these that pop up uh now if you like our
content and you want more please make sure that you like and subscribe I got to say the obligatory kind of YouTube intro there but truthfully the the
increasing number of subscribers is really motivating to us uh and encourage us to pump out more content for you all
on this channel so if you like what we're doing make sure you subscribe Now quickly for those of you who may be new
to the channel uh by way of introduction I'm Evan I'm a former meta staff engineer and interviewer I've conducted
thousands of interviews now uh nowadays I'm the co-founder of a site called hello interview and we help software
Engineers prepare for their upcoming interviews both via free educational resources like these videos and the the
uh you know the content that's on our site as well as paid mock interviews with senior interviewers from your target
company so for example if you're interviewing at Google uh you can meet with a Google engineer or manager spend
an hour with them practicing and they'll be able to point out exactly what your gaps are uh to help you kind of land
that role at Google uh lastly if videos aren't your thing I've linked a written
guide in the description below that you'll see and I go into all the same topics as this video just in written form so I'll show you what that looks
like over here uh the written form we got all the diagrams the breakdowns things that make this bad good great as
well as I think now we're up to 15 other common problem breakdowns some deep Dives introductions lots of good content
over here so go ahead and check it out uh but without further Ado let's go ahead and and get
The Approach
started all right before we jump into solving the problem as we do in every video Let's just break down the
framework that we're going to use in order to answer this system design question of of course this is the framework that we recommend that you use
for all of your system design interviews if you've watched any of our past videos you know this well by now you can skip
ahead but let me just walk through it very quickly we're going to start by going over the requirements this is both
the functional requirements or the core features of the system as well as the non-functional requirements or the
qualities of the system so qualities like how scalable how low latency things of that nature and then we're going to
go into the core entities this is basically the dat data that our system persists and exchanges via its apis
which will transition us nicely to go over the apis of the system this is the contract we have with our user of course
we're not going to do data flow it's less relevant for these sorts of product D style questions uh so we're going to
jump right to high level design where we're going to get to the Whiteboard and we're going to sketch out some components and boxes in order to have a
highle design that strictly satisfies our functional requirements so it's going to be really simple at this point
point it's not going to worry about scale or any of those non-functional requirements but then we're going to move on to deep Dives and this is where
we're going to go deep so this is where we're going to satisfy each of our non-functional requirements one by one
by adding to our system additional complexity to ensure that it meets all of those qualities which we defined
during the non-fun functional
Requirements
requirements so as promised we're going to start with those functional requirements and this is how you should start any of your interviews you want to
get a clear understanding of what the features are or the requirements of the system and so if it's a system that you
don't know well then you probably ask your interviewer a number of questions here in order to understand what this think thing is and what the constraints
are now I'm going to make the I think not too crazy assumption and assume that we all know what leak code is because if
you're watching this video you're probably preparing for interviews and you're probably spending a lot of time on leak code right now um so what I'm
going to do is instead of you guys watching me type I'm going to paste in the functional requirements here the
features of the system and we can chat about them so the way you can think of the functional requirements is these are
usually like users should be able to statements I didn't put that prefix here to save myself the typing and I
recommend you do the same in the interview but we want users to be able to view a list of problems so when they
come to the site the first thing that they'll see is maybe all of the problems that we have available to them they should be able to click on one of those
and then view a specific problem as well as of course code the solution there on their client once they've done that they
should be able to submit that solution and then get the feedback as to how they did if they passed all the test cases or
not and then lastly a feature that some of you might not know about within leak code is that we want to support
competitions and specifically competitions with a live leaderboard and so I'll Define more precisely what a
competition is a little later on when we get to it um but for all intents and
purposes this is basically everybody starting at the same time they have a number of questions to answer they try to answer them as quickly as possible
and then we have a live leaderboard that shows who's currently in the lead at any given point so those are going to be the
features or the functional requirements of our system now the next thing that we do is we talk about the nonfunctional
requirements and so non-functional requirements again are the qualities of the system some things that you really want to consider here are like cap
theorem so we want to prioritize consistency over availability or the other way around any environment
constraints things like scalability latency durability security fault tolerance maybe even compliance those
are all things that are relevant again I'll paste in a couple key ones that that I've identified here for the
non-functional requirements for leak code and note that in any system you can
go off that long list that I just said every system should be durable and low latency and have security and all of
these things but that's not interesting in an interview in an interview what you want to do is identify like what's
uniquely relevant and interesting to this particular question that's probably a better way to even frame
non-functional requirements in the first place he's like what makes this system uniquely challenging and so you'll
answer those questions starting with cap theorem um are we going to prioritize availability or consistency in our case
we want to prioritize availability over consistency and the reason being here is you can think about any place where we
make an edit doesn't matter that people see it immediately basically does every
single write or excuse me does every single read need to read the latest right and in our case no you could
update a problem definition and maybe people still see the stale one for a couple seconds afterwards or somebody
could submit their solution and somebody might not see it update in the leaderboard within that exact second
that's okay we'd rather that be the case but the site always be up and available to our users so we're going to offer
availability over consistency an important one that's unique to uh to to
code is the security and isolation when running user code we'll talk more about why this is important but of course like
we're taking in a user's uh input and specifically code that we're executing
on our own machines we certainly want to make sure that that's not malicious um so that's going to be something that's
important there we want to be able to scale but you'll note not just scale generally we're putting this in the
context of our system and we're quantifying it wherever possible so we want to scale to support these
competitions and we'll say that competitions can have up to 100,000 users that's probably something I would
have asked the interviewer and and then the last thing here is we want like a fresh or near realtime leaderboard um so
people should be able to look at the leaderboard and you know see it updating maybe in near real time to know who the
current leaders are uh ideally without having to even refresh their page so
here are some of the interesting non-functional requirements these are going to guide our deep Dives later on
now before I move out of the requirements um while if you've watched my earlier videos you know my opinion
about back of the envelope estimations I don't recommend you do that up front here because I don't think they influence Your Design yet if you know a
reason why you should because you're trying to make a decision feel free to do them at this point but otherwise what
I typically recommend is that you tell your interviewer hey I know some candidates do estimations here uh I'm
going to save my estimations for sometime maybe later in the design if I need them in order to influence a
decision so if the results of my calculations will influence a decision I'll do them then but for now I'm going to foro but what I do recommend that you
do is that you just ask your interviewer about scalability or excuse me about the scale of the system um so I would ask
the my interviewer you know how many daily active users uh how many problems maybe I I guess and make my own
estimations but you can probably just ask them and so in our case we're going to have up to 100,000 daily active users
that'll be that Peak that comes from competition so those two numbers are the same and then I looked at leak code just before this it has about
3200 3,200 problems so we'll say there's 3,000 total problems um so these are the
the requirements of the system this is the foundation that we're going to build upon and our goal for the rest of the interview is to now design a system that
strictly satisfies these requirements and we want to stay focused importantly to these requirements so we don't want
to go design something that's different than this we're going to build up those functional requirements on our high Lev
design and then we'll make sure we satisfy the non-functional requirements in our Deep
Entities & API
dive so the next thing that we're going to do is we're going to go over the core entities of the system and now
importantly what I do when I'm interviewing and the suggestion that I give to all of the many candidates that I work with is that I recommend they
don't document the entire data model here yet uh and the reason for this is that there's a good chance you don't
know it yet if this is a problem you haven't seen before or a system you're unfamiliar then documenting all of the
fields or columns this early in the interview can be daunting and the reality is it's not necessary like give
yourself time to think of that later on during the highle design as you'll see that we do but what is
important at this point is that you have a clear understanding of just the entities the objects or the tables um
that are going to be needed in your data model and so for example some of the things that are going to be particularly
important here let me maybe scroll up a bit or obviously we're going to have a user that one's pretty obvious we're
going to have problems uh when you submit a submission to a problem we'll save it as like a submission record
we'll probably have some compet comption objects this is going to have information about the competition when it starts stops Etc and then this one
sort of depends on how you design your system and is a bit more handwavy but like maybe you have a leaderboard maybe you just query submissions and Aggregate
and that is your leaderboard but I'll put it here for now and so in a real interview I would be clear with my
interviewer and I would communicate I would say I'm just going to list out some of the core entities so I can get my mind around the sorts of objects that
are going to be exchanged in the API that we're going to do next but I'll detail the full schema for these later
on in the interview so I'd make sure I communicate that with them uh and 99 out of 100 times I'll say that sounds
great so once you've done that you're going to scroll down to our next step maybe if I scroll up to show you we've
done the core entities next we're going to go on to the API so we can come back down here and these are the user-facing
apis this is basically what do we expose to the user and the key thing here is
that the apis are going to satisfy our functional requirements and they're
going to exchange our core entities and so you can lean on that shorthand as
you'll see me do here in a second and instead of kind of thinking about what are all the many API endpoints I might
need for a system like this just scroll back up to your functional requirements and go one by one through these there's
a good chance that often times it's a one toone mapping for every functional requirement there's one API endpoint
that's not always the case sometimes it's one to two you'll need to be kind of a little flexible in an interview of course but for the most part come up
here and start with what API endpoint is needed for users to view a list of problems okay so I can come down to my
API and I'm going to say view a list of problems what is that going to
require um this is going to be a git endpoint it's going to hit some problems
resource of course I can put my API version whatever I know some folks like to do that it's it's not the most
important thing in my opinion um and this right here is probably good enough and that I'm getting a list of problems
I'm gonna add some some extra stuff here which is that you know I can probably filter on things like a category or
maybe a difficulty uh difficulty and then I probably want some pagination
here so I can just do page based pagination I'm going to do the general page there as well as the page size uh
there you go so that's my basic get problems and what does it return well
well it returns a list of problems but maybe importantly and this is fairly
minor but what I would call that in my interview just cuz it takes no time is that problems are going to be probably
pretty large entities they're going to have test cases and you know the code
stub and all this stuff and I don't need that at this point so I really just need like a partial problem I'm deriving this
from typescript this term partial you can use whatever you want but the point is I'm telling my interviewer that I recognize that I want this thing to be
fast and it can be fast by minimizing the payload size and I can minimize the payload size by just sending over the
wire the things that are interesting here like the ID the name of the problem and the difficulty and maybe the category right so that satisfies viewing
a list of problems the next one is view a given problem and code a solution and
so for view a problem the code a solution happens client side so we're going to say view a problem this is also
going to be a get probably that same problems resource and then I'm just going to use a path parameter here
instead of a query parameter and it's going to be the problem ID and so just quickly the distinction here is this
notation that I did where it's a question mark followed by all of the ERS stand uh these are called query parameters and they're useful for when
things are optional and then path parameter so this is just going to be problem slash and then the problem ID or
the problem name um these are for when things are required basically you need a problem ID in order to view a problem
otherwise there would be nothing to view right and this is just going to return that problem so there's our first to API
endpoints uh the next one is that we want to be able to submit a solution and that'll of course give us feedback and
so we can have our submit solution and on submission here we're
going to have some post endpoint because now we're creating a resource we're creating an entity we're creating a row
in our table a submission row so we're going to post um and then you know the
name of the resource here this could be submissions this could be problems still some people care a lot about this most
interviewers don't and I certainly don't I don't think this is the most important part of the interview um so I'm still
going to do something like this I'll probably just post to that same endpoint um maybe you can put like a SLS submit
there but I know people get all kind of upset about verbs and things to I've read your comments um but the important
thing is it's a post endpoint here I'm going to post to the problem ID that I'm solving for and then I'm going to maybe
get in response the submission object that was created but I need a post body here and so I'm going to say what code
uh that I'm sending that's going to be important of course the language uh that I'm I coded in because I can choose from
different languages so maybe it's python something like this and then maybe optionally I have a competition ID and
so this is if this was part of a competition I would send over the competition ID as well so that we could associate this submission with the
competition that I'm a part of so this is probably good enough one thing that I
will note is like if the code was really large maybe you want to up upload it separately like to S3 first get back
that S3 URL and then just pass in here the S3 URL instead of all the code the reality is I'm not too worried about
that here and I'm going to put the constraint that you know user Solutions can only be up to a couple uh you know
maybe tens of kilobytes at most so I think it's still fine for us to put in the body but that's something to note
and then the last requirement that we have here is that live leader leaderboard so we want to be able to get
that leaderboard uh and I'm going to say you know get leaderboard and that API endpoint of
course it's going to be a G again well maybe say there's a leaderboard resource and then we'll need that path pram
because it's mandatory of the competition ID and then because this could return up to 100,000 participants
we'll want pagination here as well so again I'm going to do simple page based P pagination um cursor based is the other
option but I'm going to do this uh and that is going to return we'll say that leaderboard object uh so there's my apis
again the key here is that I have an API or at least one API for each of my functional requirements basically I've
satisfied my functional requirements with my apis these are user facing I paid attention to some some relatively
important things like if it's going to return a lot of items then having pagination is smart some filtering here
query prams for when it's optional path prams for when it's required ired when we're posting can of course use the post
body in order to post more information um but now with these in place we can use these in order to now
build our highle
High Level Design
design so as a reminder the goal of our highle design is to satisfy those functional requirements and so we're
basically just going to again go one by one through these functional requirements or one by one through our API since they were derived by the
functional requirements and build up a really simple system we're not focused on scale or anything yet that's going to
come later we're just going to focus on satisfying each of those requirements and by working linearly here it's going
to help us stay super focused on the task at hand and not ultimately get distracted and so one common Pitfall
that I see when I'm interviewing candidates is that they start to get distracted by all these additional things that can happen you know maybe
they're designing something like a Yelp and they need to introduce reviews and they start talking about replies to
reviews or comments or admins coming back and and emailing the the person or replying to a review it's like this is
all the distraction we agreed on what the functional requirements of the system were upfront there was a reason for that and so let's make sure that we
stay focused and adhere to them cuz ultimately we only have 35 to 50 minutes
depending on the length of the system design interview from the company that you're interviewing at so I'm going to
start with this view a list of problems or satisfying this endpoint here what is the simple thing that we can do in order
to satisfy that I'm going to start drawing over here the first thing is that we have a clients of course this is
the the client that's interacting with our website and then I know in many of the other videos we opt for
microservices right up front this is generally a good strategy in this case looking at the functional requirements
things look relatively simple and straightforward to me so I'm going to start by just having a simple server
client server relationship no microservices if we need to break the up later as we keep going maybe we will but
I'm going to start simple and I'm just going to call this the primary server to start and then I'm going to introduce a
database this database is of course is going to for now to satisfy this requirement store our problem entity so
we got that problem entity there this is our database and so we talked about in our core entities how we would come back and
Define some of those data models this is the time to do it so when you're actually in your design and you've introduced something you know what you
need there so what's going to happen when a user requests to see the problem list well they're going to want to see problems
and these problems will have something like an ID probably a name uh a difficulty we said they would have as
well as a category and so that's all they have for now we're going to add things probably later as we fulfill more of the high level design and more of the
requirements but let's start with that for now and so when a user goes to view the list of problems the client's going
to make that API request here to our primary server our primary server is then going to query for all of our
problems and return it back and of course we had some pagination here we had some filtering so this is just going
to be simple uh kind of wear Clauses if we're using a SQL database or filtering
uh depending on the database that we're using now the choice of database here one we could punt on this decision until
later I'm going to say that for this problem it doesn't really matter we're not doing anything fancy there's very
few number of users we only have 100 100,000 daily active users that's not a lot at all there aren't a ton of Rights
uh and there aren't as a result of that daily active user there's a ton of reads so go with your favorite database here postgress is fine if you want to go the
SQL route if you like a Dynamo DB that's great here too don't overthink this decision it's not the most important
thing given there are no kind of key insights like you know really high right through put or something that's going to
dictate us making a different decision so viewing a list of problems super
simple now what about the next one view a given problem and code a solution this is equally simple so maybe I'll label my
endpoints here just to be clear the first one that we have here is get problems and then now we're doing get
problem these are all coming in here you can label these in your interview if you want or not doesn't make a ton of
difference but I just want to be clear in this video and so this next one very similar process the client asked to get
the problem we're going to go to our database query by our problem ID this is probably going to be our primary key so
that it's easy for us to query by it's nice and fast great and we'll return that problem ID no problem easy we'll
render it to the user now when a user clicks on a problem they expect to see some more stuff than just this though at this point they're going to need a code
stub and I'm going to say code stubs because we're probably going to have some object there which has the different code stubs per language
there's test cases here uh you know there's going to be some description of the problem of course in leak code maybe
there's Solutions there sorts of all all sorts of other stuff but that's the main things that are relevant so you can see
so I'm adapting my data model as we go great so so now you have viewed a
problem in order to answer that problem well you're going to just do that on your client this is kind of a small thing uh Monaco there's different
editors or idees that are open source uh mon
mono is one of them and so you can basically just have that have that editor have that IDE that light simple
IDE directly in your browser so users can uh write the code directly there for the problem that they're
viewing next up we're going to look at what happens when you submit a solution and you want to get feedback how are we
going to implement that how are we going to implement this submit API endpoint and so the simplest thing that
you could do is that you could run the User submitted code directly in your primary server in your API server here
so this basically means saving the code to a file and the local file system running it and then capturing the output
saving it into the database um this is a terrible idea don't do it this really
sucks because if a user submits malicious code code that we don't trust and they absolutely could do this then
it could do all sorts of naughty things it could take down our server compromise our system they could delete data since
we're connected to the database they could DS us they could how they could mine crypto I don't know they could do
all sorts of naughty stuff in here and we don't want to let them do that um so anytime that you have user code where
you don't know what it could be it could be anything running it on a primary server that's connected to your other
services is a bad idea you need isolation isolation is the key key word
here and so for our highle design where we're doing something simple maybe it's fine to just say that you're going to do
this I know that typically that's the pattern that we follow do something simple and highle design and then layer
it on later in the non-functional requirements now because this one is so naughty uh I would probably recommend
just kind of like upfront addressing it I would feel pretty uneasy as the interviewer if a candidate just proposed
that they were going to do this and moved on now you could say I'm going to run it in the primary server for now cuz just the high level design I'm going to
come back to this and I'm going to improve this cuz I know that this is a big security concern that would be okay if you want to proactively communicate
that um but if you know it's an issue and you know some solutions then even though it's the highle design maybe you
just jump in and solve the problem and I'm going to do that here because I don't want anybody to you know only watch up until this point in the video
think that this is an okay solution and then go do it in an interview um so let's talk about what some other options
are of course as I said the issue was that we need some isolation we can't let them run in the same place as the file
system and the database Etc of our primary server and so we could satisfy
this isolation by running a VM or a virtual machine on the privary server here so let me just kind of draw that
this could be a a VM to run code uh and VMS provide a fully isolated environment
on top of the server and so this way if there are any crashes or any malicious code or anything bad that happens
they're totally confined to this box here they're totally confined to the virtual machine machine and they can't
impact the primary server at all and so there's there's still some issues here the main issues with the VM is that
they're a decent amount of overhead they run an entire operating system they run a full OS so they're really resource
intensive and this basically means that you're going to need more of these primary servers you're going need a bunch more Hardware in order to support
all of the different VMS in order to run user code because of course in the future we're going to need to scale this
um and the VMS because they're so intensive they also lead to some some slow startup and as I mentioned that
inefficiency of resource utilization us needing more Hardware so they're not a great option now we can get around both
of those issues kind of that slow startup the resource intensive Nature by instead making this a container and so
what we can do is that we can use something like Docker containers where unlike a virtual machines containers
share the host operating system and they only package up the application code and the dependent
so they're much more lightweight they're much more efficient and allows us to run more instances of this container on the
same hardware and thus of course spend less money so what we can do I'm
actually going to copy this again because this will be a little bit more to draw uh but we can have all these
containers down here uh so we can have a container for each runtime that we support this is basically all of the
different code Java python Etc and so what the containers are going going to do is that they're going to install the
necessary dependencies so you know uh all the necessary dependencies to run
JavaScript Java python uh Etc and then they're going to run that
code in these sandbox environments in each of these containers and then they can respond to the primary server which
with whatever the result was and update the database and so but before I kind of
talk more about that flow I want to throw out one other great option here this I think is the one that I'm going to go with
but another great option here is to use what are called serverless functions and so a good example of this is like AWS
Lambda you may have heard of that great thing to to look up if you haven't but these serverless functions are just
small stateless event driven functions it kind of sounds fancy uh that run in response to triggers so just like an
HTTP request like a rest request um and they're managed by Cloud providers like AWS and they automatically scale up or
down based on demand basically instead of having a server a container that's always sitting here cuz these exist on
servers of course you basically just make an HTTP request the telling AWS
Lambda for example that you need some resources it pops up uh you know a little resource uh which is the Lambda
which can then be configured with the runtime environment support Etc in order to run the code and do the same thing
and so these are always here sitting waiting we can hit them run the code in the case of the lambdas there's nothing
here we have a request to run some code code we tell AWS I need to run some Java code it pops up a machine or a part
portion of a machine they handle that internally that needs to run that code takes your code runs it and gives you
the response and so that's also a great option candidates can absolutely use lambdas or other serverless functions
here uh works great the problem with lambdas is that they have an issue with
cold start so when you go and you request it and you want it then it's got to be pulled up and it's got to download the dependencies and get itself into a
state where it's ready to run whatever code it needs to run and so there's been a lot of work in the AWS team and
strategies in order to avoid this cold start problems you can warm them up have them already there of which case you
sort of just have the containers here so anyway any option works I'm going to opt
for this so we have kind of an additional server here or handful of servers that are running each of these
different containers for our different runtime environments or Docker containers and so now what happens is
that the primary server is going to pass the code down to these guys they're going to run it
there's going to be some response maybe there's errors that happen success failure of course they're running test
cases give that back to the primary server and then the primary server is going to update that by saving it to
some submission and that submission again we talked uh a little bit about
the fields that are going to be needed here it's going to have you know probably the the test case results uh
pass or fail so maybe I'll I'll just call it past and we can make that a Boolean uh errors if they existed how
long it took to run some of that sort of stuff is going to come back from our containers and we can store it here as a
submission all right we're almost done with our highle design here if we come back the last thing that we need to do
is support these competitions in a live leaderboard and so the first thing is we
should Define a competition over here we're going to have some competition it's going to have some ID and it's
probably going to have a start time and an end time maybe there's some restrictions or things like this it's
also going to have some problems I guess what I should probably do forgive me here I maybe should have stated this
earlier is what the heck is a competition we sort of need to Define it so in an interview maybe earlier on
hopefully or at this point you're going to ask your interviewer what is a competition and so let me Define that up
here what is a competition we're going to Define it as follows so we're going to Define it as
this competitions have some start time they last 90 minutes and there's 10
problems that uh you know the folks competing need to try to solve we can
have up to 100,000 users per competition and the way that we determine a winner
is who solves the most problems in those 90 minutes and in the case that people have solved the same amount of problems
then it's whoever solved them faster okay so that's what a competition is so when we we come back down here and we
Define our competition object we have the ID start time end time and that list of problems this of course is just going
to be the problem IDs um but the list of problems the 10 problems that are
involved in this competition okay and so now when a user
comes and they submit something or they try to run their code then they're also going to have the competition ID that
they're involved in so there are some things that we need to add to our submission here the competition ID I
guess we forgot this originally I forgot this originally the problem ID the user ID and then it's kind of obvious but I'm
just going to add our user entity ID being the only relevant field of course there's other things but you and the
interviewer both know what they are so we don't need to put them um but so now we have this submission it's got the
competition ID the problem and all sorts of information and so as far as the high Lev design goes when we want to get the
leaderboard uh I guess I should have had that post submit here too what did we have that as problem SL ID and then now
we're going to have that git leaderboard right and so that's going to be the ID of the competition and so when
we want to get the get the leaderboard um what we could do in the
simple way is just have our primary server query our database for all of the submissions for a given competition ID
so we' make that the primary key and then we would Group by user ID so how many are completed there where past
equals true and then we would would further sort in case of Tai by the completion time um so we should probably
have completion time or creation time here as well and so that would be what I
would do for the highle design just super simple we'd have a query there what the heck would that query look like
I don't know if it's the most interesting thing in the world but I just wrote it out and can paste it here so we'll select the user ID the counter
the count of uh those past submissions um and then the maximum of the submit time
uh or submit it at I guess this should probably be the Min one because we want the shortest there submissions filter by
that competition ID and past equals true so that may or may not be perfect I wrote that fairly quick just before this
but it's not the most important thing and you wouldn't write this query in your interview you would just explain to your interviewer that you could very
simply query the submission table grouping by user ID and then using completion time or the submitted at time
in order to do that ranking in case of ties what I would also do at this point is I would call out to my interviewer
that like I recognize that this is inefficient I recognize that it would work but it would be a pretty expensive
query especially if we have a lot of people trying to hit our leaderboard and so I would let them know that that's one
thing that I'm going to call attention to that I'm going to go try and fix in my deep Dives but for now if you look at
our design here what we have is a design that successfully satisfies our core
functional requirements the core features of the system users can view VI a list of problems by making a request
to the primary server and then we'll return all of the problems back to the user to be shown allowing filtering on
difficulty category Etc they can view a given Problem by providing that ID to
the problem that they're interested in we'll fetch it based on primary key and return to them the relevant code stubs
test cases etc for them to be able to code their Solution on the Monaco IDE here and then when they submit the
solution we'll take their code we'll pass it to one of our containers here based on the appropriate runtime we'll
run their code we'll take the result of the output stored in our database as a submission entity and then pass the
result back to the client letting them know if they passed or failed and then for competitions we have this
competition object that an admin or whomever would create ahead of time slightly out of scope for this interview
but more importantly when a user submits they'll also provide that competition ID in the case that they're competing uh in
a competition as we see down here in our API we'll then attach that to their submission um and then when we want to
see the leaderboard we'll just query this submission table grouping by or selecting only those within a
competition ID grouping by the number that have passed by user and then sorting by the speed that it took them
to complete that latest question and then we can return that back to our
Deep Dives
client all right so now it's deep dive time we have our highle design in place which satisfies those functional
requirements and now we're going to add upon that highle design in order to make
sure that we can satisfy those non-functional requirements and we'll go deep in a couple of areas to make sure that we satisfy these additional
requirements so we can go one by one through these again we'll start with security and isolation when running
users code so we talked about how we already satisfied a good amount of this by using these Docker containers here
this satisfied the isolation components and largely the security component as well because we're separate from the
primary server and we can't access any of the resources like our database or our primary file system or anything over
here but there's a couple other things that we want to consider so despite the fact that they're running in the container there are a couple things that
could still go wrong now what if a candidate just had in their code an infinite Loop they just had a while true
or something well we would end up giving them to one of our runtime Services one of our Docker containers and it would just run it infinitely and that Docker
container would be forever pre occupied and we' need to spin up another container uh and waste the resources
indefinitely on that one container that has that while loop and so what we can do there is that kind of the most
obvious thing is we can have an explicit timeout per execution and so we can say
that code can only run for something like 5 seconds for example and if code runs for longer than 5 seconds then
we're going to kill it and return an error back to the user and then similarly we don't want a user who just
does a bunch of fork bombs or kind of excessively uses memory or excessively uses CPU on any of these given
containers um so for that we can add CPU and memory bound so these containers can
be configured such that they have a really tight limit on their memory and CPU and if that limit is exceeded then
the whole container just gets teared down and we'll pull up a new one of course returning the error back to the
user maybe not being explicit so that they don't try to like kind of reverse engineer how they can take advantage of
us but these are really the two main things we want to ensure users can't abuse the resources and make run up our
bill and to satisfy that we can have those timeouts and uh and CPU and memory bounds um some other things that I'll
just mention here which are less important but also interesting is like we'll probably have a f a readon file system on these Docker containers so we
won't let people kind of mess with the file system at all for the code we'll just write to the temp directory that'll
handle some issues that could potentially come up there we probably want Network isolation like they they definitely shouldn't be able to read our
database or access our primary server or anything um so we can have some basic
Network isolation stuff in place this is like VPC controls and the AWS ecosystem I'm not going to talk too much about
that uh because it's not the most important thing you can do some additional research if that's something that's interesting to you and then some
stuff like you know we can enable it such that it doesn't allow system calls on the box so you know you can't mess
with the underlying system or operating system next let's end up doing the fresh
and near realtime leaderboard I know that we're going a little out of order the order here doesn't particularly matter we just want to make sure that
all of these are fulfilled um but as you remember in the high level design we talked about the limitation with
fetching the leaderboard being that this query specifically over here was going to be super expensive um so that's the
first problem that we want to solve and then the second bit is this near real time portion and freshness we want users
to be able to have their leaderboard open and then just kind of have it updating without them needing to refresh their page and so we want it to update
every you know couple of seconds nearish real time whatever it may be so that they can see any changes that might have
happened to the leaderboard and so in our current implementation we're going to run this big expensive query which if
we're aggregating over 100,000 things here this might take several seconds to run additionally it's going to cost a
decent amount of money if this is 100,000 entries each entry that it needs to aggregate over it's a couple hundreds
of bytes um like if this was Dynamo DB and I think that we've determined maybe
it's postgress but it doesn't really matter as an estimate this is like on the order of 50 bucks per query uh you
can see a breakdown of how you would calculate that on our Dynamo DB write up on the website using right capacity
units but the thing that's important here is that this is expensive it's going to take too long and it's going to cost too much money so we need to first
start by solving that and so the most obvious thing that you could do is you could introduce a cache and so by
introducing that cash cash maybe we'll say it's reddis uh redis cash what you would do
is that you would query the database you'd run this expensive query and then you would cash the result and then
everybody else who tries to fetch the leaderboard is just going to hit the cash but of course we don't want them to
hit the cach forever because very quickly this leaderboard is going to become stale so we would need to
introduce a TTL here so there would be a TTL of maybe 10 seconds or something and
so some somebody would request uh the leaderboard from the database we'd run our expensive query we would cash it
with a time of of 10 seconds for the next 10 seconds everybody is going to hit that but then when 10 seconds
elapses this is going to get removed from the cash and it's going to be a cash Miss so they're going to go run the
expensive query again and again repopulate the cash and so you probably see what the issue is here both that
first user and every unlucky user who hits us at the 10sec Mark is going to have a cash Miss and they're going to
have to run the query which we've cut down on the amount of times we need to run the query significantly we've saved ourselves tons
of money um but we led to a pretty bad experience for that unlucky uh user that
hits us at at the boundaries here so how can we solve that now what we can do is
we can update the cache uh on every single right that's one solution here
actually before I do that let me propose a different solution first so another solution is that we can have a Cron job
or some you know scheduled worker here whose job it is to refresh the cash and
so this Cron job might run instead every 10 seconds or so and now it's going to
every 10 seconds query the database for that expensive query and then update the cache those arrows should be single not
double but I'm going to delete that in a second so it doesn't matter and now we don't need a TTL here every 10 seconds
this guy's going to go run the new query and then save the fresher data in the cache now every single user hits the
cach this is great right there's never anyone hitting the database other than this Cron job which runs once every 10
seconds in order to make sure things are fresh so that's fine this is still kind of expensive but on the order of things
not really who cares and it doesn't matter if it takes a ton of time uh it's having a slight impact on freshness but
at least all of our users are always hitting the cach so they're always getting kind of this o of one here and
well what's in the cach the cash value is just a string uh as a reminder redis is just key value pairs so the key here
is probably something like a string leaderboard colon the competition ID and then the value is
just some Json blob which is basically the result of this expensive query and
so it'll have you know the rank list of users as well as each of their scores whatever it is that we need to ultimately send back the client for them
to be able to render the leaderboard right so that's what we have here now the main issue with this approach if
it's run every 10 seconds is that this cach is pretty stale us users are going to be requesting the leaderboard they're
going to be maybe polling kind of calling every couple of seconds to see if there have been any updates and
nothing's going to change except for on the 10sec is boundary and so this might be fine uh it's probably too long
obviously you can just lower this make it 5 seconds maybe even less if you start to go below that then you know
you're running the Cron job uh you know pretty frequently maybe at a rate that's even more frequent than
the amount of time it takes for this query to return like if this query takes 4 seconds to return and we're running this every 3 seconds then we're going to
be overlapping with our previous query and need more cron jobs um and that might be too much to manage so my point
is this solution could work it's not terrible you're going to have a little bit of staleness you're going to want this Cron job to run more frequently
than less frequently but it's maybe not perfect you could get away with this uh
the thing that I don't love about it is that you've introduced kind of an additional dependency here this Cron job
that's going to have to run if it has issues like maybe it goes down or somebody pushes bad code to it then the
cach is never going to get updated and we're going to all of a sudden have some you know call it a Thundering Herd on
our database to do this expensive query and that could really cost us um so for
that reason I'm going to opt to not go with it but just know it's an okay option especially if you did that in a
mid-level interview I think that's totally great even in a senior interview it's not a terrible suggestion um I
wouldn't necessarily count it against you though it's certainly not the best now the other thing that you could do is you could just update this on each right
and so what you could do is you have your result come in you update the database instead of doing this query you
would do a cheaper query like for this user how many submissions have they had and what's the time of their last
submission and then go update just those values in this Json blob and so this would mean you'd have to read this
entire thing into memory parse the Json blob update it and then resave it to
reddis and so that's sounded like a lot of work it kind of is it's not great especially cuz you can have some races
here like everybody's having sub Missions at the same time and fortunately redus is single threaded so
this would still work uh especially since users can't like submit two solutions back to back they're going to
always be different users this is again it's an okay solution um but you're reading a largish amount of data
especially if you have 100,000 users it's not just largish it's like actually large into memory in order to do some
kind of updates and then writing it back to cash and then how are you going to make sure that these remain consistent
it's a little bit more difficult and so that solution also works again
everybody's just hitting the cache and we never have to run this query that's pretty nice um but I want to introduce
something that might be even better and that's that in reddis it's just key value pairs it's an in-memory data store
we have a fantastic write up written by my co-founder Stefan uh on our on the Hello interview website click on learn
at the top system some design and then reddis and you'll see it and it explains how reddis works I'll give just a slight
overview reddis is made up of key value pairs where the value can be any data structure or most data structures it
could be something like a string or a basic type like it is here or it could be one of those data structures that you
know well from all of your studying of DSA and so one such data structure that exists is something called a sorted set
and so sorted sets are just collections of unique elements where each element is associated with a score that defines the
order of the element in that set so it's a ranked set essentially all these
elements then are ordered by that score and this is going to allow us to do efficient range queries like retrieving
the elements within a specific score range or ranking so if we go back to our pagination here on our leaderboard if we
want say the second page 100 things then we want just the leaderboard or the rankings between 100 and 200 we can do
that really easily with sorted sets and the time complexity it's in memory so it's wicked fast we don't have to do any
querying um and the time complexity is Ol l in so pretty quick there but now
what we would end up doing is that within our sorted Set uh the element
would be like the user ID and then kind of the thing that it's ranking on ranking on the score that we would have
with it would be its computed score which is going to be based on the number
of submissions and then maybe we add some decimals uh for the submitted time time to make that the the tiebreaker but
for Simplicity the score here is the number of completed or pass submissions that they've had right and so now we can
always just query this in order to get the latest leaderboard walking through that a user submits their code we run it
we then uh update our database you know write the additional submission to our
database and then go to reddis and for that user in the sorted set if they passed we update their score and do what
whatever calculations their score are necessary based on that last submitted time and so now it's a little bit easier
to keep these consistent we're writing and reading just a little bit of data from the red uh to and from reddis as
opposed to that huge blog and we still maintain that all of our users end up hitting the cash and they never have to
run an expensive query so that's a fantastic option now in order to keep things like near real time here I would
first ask my interviewer what is near real time and I would maybe make a proposal and I would argue that in this
case near real time is like three to five two to five seconds the reality is
submissions aren't coming in that quick and so if we just refresh every couple seconds it's probably more than good
enough I'd make sure that I get a consensus with my interviewer on that but if that was the case then what I
would do here is I would still just pull I would pull every 3 seconds to get the new leaderboard for whatever page I'm on
um and then I would fetch you know the scores just from within that start and end offset and then I would update it on
the client now every time I ask this question in an interiew interview candidates naturally want to introduce
websockets or server sent events some sort of persistent Connection in order to truly do this in real time and I
think it's an interesting thing to bring up I would bring it up in an interview um but I would actually point out that I think it's over engineering for this
case and the reason is introducing websockets or SS comes with some meaningful drawbacks it's a lot of
additional infrastructure to maintain you need some sort of a websocket manager you need to now not have
stateless servers but servers that are maintaining state which has some consequence to fault tolerance and
durability and so the added over the the engineering overhead that's introduced
by bringing in websockets or S uh I don't think is worth that couple of seconds of more real time in a
submission and in an interview these are the exact conversations to bring up like that's an interesting trade-off to
discuss with your interviewer I recognize that this solution exists but given the constraints of this problem I
think it's over engineering and polling despite how simple it sounds I think would actually be the optimal solution
and that's why that's what I'm going to go for you know this is what I would say to my interviewer hopefully that makes
sense one additional thing that I failed to mention is that now that you're writing to both of these kind of
databases the database and the cache at the same time you'll generally have the concern about consistency like what
happens if you wrote to this one and then your primary Service uh server went down before you wrote to your cash now
your leaderboards always out of date there are a lot of different ways to handle this uh I'm not going to go into
all all of them one potential solution is that you use change data capture
something that we've talked about in a number of other videos and so off of your primary database here if it was Dynamo DB this is Dynam DB streams if
this is postgress I think they call it something different logical replication or something um but what effectively
would happen then is instead of an arrow there you would just write it to your database and then CDC captures an event
stream of all of the changes that have happened to that database and puts them in a queue you would configure this and
so like you could put Kafka here for example um but you know there's going to
be some we're going to the the change dat a capture excuse me the event stream
is going to be put onto some Q or some stream like a CFA will have some worker that pulls off of Kafka and then writes
it to the reddest cach I'm going to extract that all away with just the CDC Edge but that's one way that we can make
sure that if something is written to the database it's also written to the redest cach and then if our cash ever went down
well we could catch up um by just reading the latest things off the stream more likely we would probably just read
from the database and load back up and start from where we were but you have some options there okay now the other
one that we're going to talk about is going to be the last one that we're going to talk about availability versus consistency is a little less interesting
in our implementation we've already implemented something that prioritizes availability we don't have you know asset properties paramounts in our
database with transactions or any consequences to locking or consistency here so kind of uh by by the lack of
that or the absence of that this is prioritizing High availability of course we'd have the basic stuff like load
balancers between uh in front of each of our servers the score scale horizontally all of those things I'm not even going
to mention them necessarily um maybe worth mentioning in a mid-level interview for all other interviews it's
kind of obvious and inferred so not the most important thing but we need to talk about the scale to support competitions
with 100,000 users and that'll be kind of similar to the availability stuff here um so as I said horizontally scale
this sure whatever um but more importantly what are we going to do down here so the consequence to this is that
we could drop a submission and that would be pretty bad especially if a user gets to the end of the of the
competition they submit their last thing we come in here we have a bunch of people who are submitting towards the end and we don't have enough containers
up and so we can't do anything we just end up dropping their request and maybe sending them an error and now they're
disappointed because it impacts Ed their result and their score and now their profile doesn't look as good and they're
in our email and all sorts of bad things happen right so we don't want to drop those requests we want to be able to scale to this big surge of 100,000
things so what are some things that we could do well we can proactively just horizontally scale these a ton we have a
bunch more Docker containers these of course are running on servers we can have beefier servers we can have more of them and as a result we can kind of
buffer any big um you know amount of submissions that come in at any given time that's expensive because we're
going to load up on all of these servers prior to a competition we're not going to need any of them until potentially at the end and maybe we didn't guess right
so maybe we still Dro things so it's not perfect another thing that we can do uh and that we would call that pre-scaling
to put a word on it another thing that we can do is something we can call Dynamic scaling and so if these
containers are running in uh you know AWS or any other Cloud environment um
then you can use cloud services that have some sort of Auto scaling so maybe this is like WS fargate with ECS
containers um and what you can do is you can specify a memory um or a CPU limit for which we
need to pull up more containers so if your containers hit some limit in their CPU or memory consumption we automatically pull new ones up if they
go below some lower limit we'll automatically tear them down this way we can dynamically scale and so this option
is not bad but the reality is it probably can't be dynamic enough if we get to the end of the competition and we
all of a sudden get like 100,000 submissions then we're not going to be able to Auto scale fast enough to be able to handle that so instead what we
can do and what we should do is introduce some buffering here so I'm going to move things around a little bit
and when a submission comes in what we're going to do is we're going to put it first on a que and so this is going
to be some message Q it could be CFA it could be AWS sqs either works here we're just using it as a very simple message
cue so the choice there isn't that important and we're going to put the uh the
submission on AWS on that message CU and then we'll have some worker that pulls
it pulls those uh you know code run requests or those submissions off this arrow is just
one sided and then that worker is going to go over to our Docker containers and
say run that stuff and it's going to get its response and now when it gets its response it'll go to our primary server
and say you know write write this submission data and then we'll do that
same flow that we did a moment ago where we write to the database CDC updates the cache so by doing this we've introduced
this Q importantly as a buffer so that if we have a huge influx of things that are coming they'll just get queued up
we'll be dynamically scaling this as fast as we can and then the workers can horizontally scale as well they'll be
pulling things off of the queue and then so long as there's enough capacity here they'll hand them to each of these these
guys in order to run the code and if anything failed for some other reason maybe we can add retries some other
durability properties there now that we have the queue um but I'm not going to go into as much detail for this
particular interview um so this is a good approach but one thing that's interesting here is now we've just made
submissions fully asynchronous and so how does a user know whether their submission passed or
failed this gets a little interesting because now we have a primary server that's putting it on a queue it couldn't
Theory wait here on the queue for a couple of seconds runtime could take up to 5 seconds and then the worker comes
back to the primary server maybe after 10 or so seconds this is too long traditionally to have a single rest
request open um and so we need another way to notify our user that their
submission either passed or failed and so the way that we can do this again is
just with polling you could open up a websocket or an ssse connection I'm going to make the same argument I made
for the leaderboard and say that polling is totally sufficient here and so I would introduce like another API
endpoint let me move things around here that is something like this uh checks
problem uh you know maybe it's the problem ID and then like a submission
and then a submission ID or something like this um and this is going to be
what Returns the actual submission this is now just going to be a 200 or failure whatever Arrow code error code and so a
user is going to kick off their submission or it's going to post here go through all of this run come back update
the database and then meanwhile they're going to be running that get check call which is going to go to our primary
service and look in the database for that submission ID to see if it already if it exists and if it does pass or fail
if it doesn't return you know it doesn't exist yet and the client side logic will know to keep trying that at least for up
to 5 seconds before it shows an error to the user and so interestingly this might
sound not that sophisticated I guess to some Watchers of this video but I want you to go over to leak code and submit
your code at leak code and open up uh you know your inspect element console and the network tab there on the right
if you're using Chrome and you'll see that every 3 seconds there's a request to a slash check endpoint and so they do
exactly this they pull and it makes sense it's a simple solution why over engineers if you don't need to um so
that's how we would scale we would introduce the que um and then maybe one thing that I'll I'll I'll say here I
don't want this video to get too long and I don't want to get distracted by things that aren't the primary focus
here but of course when you introduce a queue you don't want to store large amounts of data on that queue and so if
our problem Solutions end up being pretty large kind of similar what I talked about in the beginning then what
you're likely going to do is introduce S3 here and store the solution or the code solution itself oh store the
code solution itself in S3 and then we don't need to put the code in AWS we
would download it again from S3 in the worker before passing it to each of these guys but that's small and minor I
just want to make sure people you know might notice that and comment in the comments so I'm just not going to focus on it here but that is how you would
handle that all right just like that we have a
Conclusion
a design here that crucially meets all of our functional requirements and our non-functional requirements and this is
really the moment in the interview when you know you've done a good job if you can look at your system here and you can go back through your functional and
nonfunctional and say check check check I've met all of those then you should be leaving the interview feeling pretty
confident and so quickly let me just give an overview maybe of what I'd be looking for at each level here I know I
went into a bit less of that than I do in in in kind of the normal interviews I don't ask this question typically of
Staff candidates though I have seen it be asked some of the major fangs of Staff candidates um but I think it's a
little on the easier side and so as a result I usually ask it for mid-level and Senior candidates for mid-level
candidates kind of the main thing is that you realize the importance of the code isolation usually just running this
in Docker uh or in some Lambda is a great first step there I wouldn't expect that you're able to enumerate maybe all
of these things are important but usually having some explicit timeout uh is really important that's good so
Docker container and some timeout would satisfy all of this I I want you to recognize that this query to fetch the
leaderboard is super slow and not optimal so maybe that caching solution with the cron uh Cron job to constantly
refresh the cash that would be great that would be passing uh I'd want you to kind of recognize or at least I might
bring up the question to say something like uh how are you going to handle that that scale that influx at the end of
competitions and you should be able to brainstorm some good ideas there whether it's kind of pre-scaling autoscaling or
ultimately this que for senior candidates we we we want to be able to land uh probably closer to this Q
solution or at least have some good justification for the Lambda and how you're going to pre-warm it uh so that
we don't have that cold start problem I'd like you to get uh the the Cron job at least maybe you come to something
closer to this not necessarily with the reddish sorted set that's great to see but there are other variations that
would work all the well but likewise you should know that this this query is suboptimal um you should recognize all
the same things about security maybe you bring up one or two additional ones here like the CPU and memory bounds was an
important one but if you do all of these things in either the mid-level or senior interview respectively it's likely going
to be a hire um okay so that that wraps things up for us thank you everybody if you
made it this far congratulations I think this ended up being over an hour so apologies it's a little longer than I
usually aim for um one thing that I will actually mention before you sign off is
that we've been working on something new over at hello interview I'll link this in the description but we've been
working on these things called guided practices and they allow you to try the problems that I have YouTube videos for
here yourself you basically answer a question step by step the functional the non-functional core entities API all the
way to high Lev design and deep Dives drawing them on a whiteboard and then you're able to get some instant feedback
on your solution so I think it's a really opportune way to practice Hands-On as opposed to just reading or
watching content now as you're seeing at the the time of this recording we just have Ticket Master up on the site you
can try that now um by this time next week you'll also see uh at least four
additional other ones including leak code which I I've just finished locally here so uh try that out I think that'll
be interesting for folks and a great opportunity to practice like I said Hands-On with these problems um lastly
comment uh like And subscribe of course let me know what I did wrong as always let me know if you liked it uh I'd love
to hear from you and I try to respond to as many comments as possible possible so we we'll have another another interview
breakdown here in the coming two to 3 weeks I'll see you guys then
