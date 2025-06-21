```java


Intro
hey everybody welcome back to the channel uh I'm Evan co-founder of hello interview and a former meta staff
engineer and in this series we've been breaking down common system design interview questions together and today
we got a new one for you so today we're going to work through designing Facebook live comments of course this isn't
limited to Facebook uh it's any live streaming platform but the live comments feature so the the comments that come in
under the video This is actually the second most popular question asked in meta system design interviews uh and
it's really popular across all of the major fangs so it's a good one to know uh if you like this content you want more of course I'm obligated to say it
please like And subscribe it really helps us and the increasing number of subscribers is really motivating for us to continue to make these videos Stephan
and I want to make a lot more of these in 2025 particularly in the beginning of the year so uh subscribe you'll get the
notification when those come out if videos aren't your thing head over to hello interview.com I have a written
guide for this exact problem that you can read through um there's also dozens of others on the site we also have
guided practice which is a tool that allows you to try this problem and about 20 others you get to draw on the
Whiteboard you get personalized feedback as you go candidates really really love it so check it out um and there's tons
of other free content on h.com that's going to help you prepare for interviews including maybe most importantly mock
interviews with senior plus Engineers or Managers from your target company people just like me who are going to sit down
for an hour with you um and kind of let you know where your gaps are and give you everything you need to to to know to
make sure that you're successful in your interview so without further Ado let's get into it

The Approach

so as always before we jump into the actual design let's take a moment to go over the road map or the framework that
we're going to use throughout this video and it's the framework that I recommend that you use in your real system design
interviews and so if you've watched any of our other videos you've seen me do this a 100 times you're tired of it feel
free to fast forward um but for anybody who's new we're going to go through these six steps uh first off we're going
to outline the requirements of the system and so this is your opportunity to ensure that you are on the same page
with your interviewer about the system that you're going to build this includes what we call the functional requirements or the core features of the system as
well as the non-functional requirements or the qualities of the system after that we're going to outline
a very basic list of core entities and so this can be thought of the nouns of your system often times this correlates

almost one to one with the tables in your database but we're going to stop short of outlining the full data schema
or modeling any relationships the justification being that we just don't know it yet it's too early in our design
but we do want to outline the nouns because they're going to give us the context necessary to understand our API
and then move into our high level design and so once we have those core entities down as I said we go into the API uh
this is where we'll outline the core user-facing apis and we'll exchange those core entities um that we outlined
in step two now from here data flow this is for infrastructure heavy system design interviews um you'll need to to
decide on the Fly whether or not it applies in this case uh it won't and so we're going to jump right into set five
which is the highle design the high level design is when we head over to the Whiteboard we start drawing boxes and
arrows in order to outline a very simple system where the goal is to satisfy our
core functional requirements so in this case we're not going to satisfy the non-functional yet our system might not be able to scale it might not be low
latency it's very basic um but it's the minimum required system in order to
satisfy the those core functional requirements so we'll get that down and then we'll move on to step six the Deep
Dives and so this is where things get interesting this is where senior and particularly staff candidates uh show
their worth and this is where we're going to go one by one through those non-functional requirements that we outlined in order to expand upon our
design um our original highle design um in order to make sure that we satisfy
the non-functional requirements so this is where we'll handle the scaling the latency concerns security concerns
anything like that that comes up so that's the outline that we're going to follow let's do that
Requirements
now before we jump into our first step which will be the functional requirements let's just take a really
brief moment to at a high level explain what FB live comments are so you're probably familiar with Facebook live
Facebook live is a feature within the Facebook app which allows users to live stream videos to their
audiences now what we're going to be designing is what happens under that live stream this is going to be the comments that get streamed in in real
time so as users are watching a video they can be posting comments and reacting to the video as it's happening
those comments get streamed to all other users as I said in near real time and so
of course this is not exclusive to Facebook this is true of Tik Tok live this is true of Instagram live this is
true of twitch YouTube live any streaming platform uh so the solution
that we're going to have here applies to any of those awesome okay so let's get
started with our our functional requirements as I had mentioned the functional requirements are the core features of the system this is where you're going to
agree with your interviewer on what you are designing now in our case our our core features are relatively
straightforward I'm going to paste them in because it's going to be better than you guys watching me struggle through
typing here in the live video but the core functional requirements of Facebook live comments are first most obviously
users or viewers need to be able to post a comment that's crucial Fant CLC the
second is that viewers can see all comments posted in near real time and so
as new comments are coming in we're appending those comments to the bottom of the list or the log so that users can
see them importantly without having to refresh their page or anything and then
third is that you should be able to see all the comments that were posted before you joined and so maybe uh in the case
of Facebook live Tik Tok live this means that you can scroll up on your feed of comments and it'll load or older
comments that you can still view so those are going to be our core functional requirements now I put some things below the line here these are
things that would be reasonable in an interview like this but are going to be out of scope for us that's the ability
to reply to comments and the ability to react to comments or even just react to the video in general and so one thing to
note about this below the line thing don't feel obligated to do this in your interview my suggestion would be to use
this technique of below the line or out of scope only if you're in the proc process of brainstorming and something
comes to you that you discuss out loud and then agree with the interviewer that it's out of scope so if you're thinking
in brainstorming about the functional requirements and you say something to the interviewer like well should users be able to reply to other comments and
they say no let's consider that out of scope then that's something that you can specify is below the line basically a
contract between you and your interviewer of these are the things that I'm going to focus on these things are
not next up are those non-functional requirements and so non-functional requirements are statements about the
system's qualities that are important to the user and so they can be phrased like the system should be able to or the
system should be statements so for example if you're designing something like Twitter it's like the system should
be highly available prioritizing availability or consistency the system should be able to scale to XYZ right
some things you want to talk about here cap theorem uh scalability latency durability security fault tolerance
compliance these are all the things you want to consider but crucially you don't want to just list those out the reality
is that most systems nowadays need to do all those things but what you're doing in your non-functional requirements is
calling out to your interviewer the set of qualities that are uniquely relevant and interesting to this problem and the
things that you're going to prioritize when discussing the interview so let me paste in a list here of non-functional
requirements that we can discuss so for non-functional requirements here are some things I want us to discuss so
first off is scale at this point in the interview I would ask my interviewer what's the scale that we're talking about here they might ask you to
estimate it or they might tell you often times when I'm the interviewer I'll just tell you here and in this case we want
to scale to millions of concurrent videos and up to thousands of comments
per second per video uh so this is going to be a lot this is going to be huge scale actually there's a there's a fun
fact here that I think I put in the write up and that's that the most popular Facebook live video was called Chewbacca's mom funnily enough uh and it
featured a mom thoroughly enjoying some plastic you know Chewbacca mask and it been viewed over 180 million times and
so that's tons of concurrent viewers we can estimate some portion of them were commenters um and that that would get us
to you know these thousands of comments per second no problem and so the second thing that we're going to consider here
is Cap theorem we've considered scale now we're going to consider cap theorem now cap theorem you want to consider in
almost any system design interview it goes far as to say any system design interview and the question here is do we
prioritize availability or consistency and so uh the way to think
about this and we have a video specifically on this tradeoff but do you need strong consistency put in that
another way is does every single right or does every single read of your system need to be reading the latest right and
so in the case of our comment creation does everybody need to see the latest comment immediately when it comes in and
the answer is clearly no like we want real time low latency broadcasting that's what we'll get to next but
it's not an error if that doesn't happen right we would rather be highly available we'd rather you get comments
than see no comments just because we can't show you the very latest comment hopefully that makes sense and so in our
system we're going to prioritize availability over consistency as it pertains to creating comments and thus
reading those comments and then the third thing we want to consider here is around
latency and so we do despite our eventual consistency want to be as quick
as possible possible to broadcast new comments to users right it wouldn't make too much sense if you're watching a
World Cup broadcast Messi scores a goal and then five minutes later people are
commenting oh Messi what a goal right you want to see those comments come in almost immediately and so we're going to
actually quantify this and we're going to shoot for about 200 milliseconds another fun fact 200 milliseconds is
what we as humans perceive to be real time and so if you're an interview if you're in an interview that needs real
time 200 milliseconds is what what you're striving for anything lower than that frankly it doesn't matter humans
won't perceive the uh the difference anyway and so last thing that I'll say about these non-functional requirements
is that aim to quantify them where possible like we did here uh and always put them in the context of the system so
availability greater than consistency me not that interesting but for comment creation okay I understand why same just
low latency me of course but what specifically in our case Comet broadcasting and then we quantify it
same comment about out of scope or below the line security and integrity are two things that are often important to live
comments making sure people aren't saying bad things um it's not something that we're going to focus on in this
particular interview zooming back out we can see
API & Core Entities
our next steps are to define the core entities and then the API so we can do that now uh the reality is that these
two parts of the interview should move pretty quickly and particularly in this interview they're not overly interesting
or difficult and so we should be able to get them down pretty quickly let's start with those core entities let me zoom in
to make this as easy as possible on you guys what are the core entities of the system what are the nouns of the system
what are the tables that we're going to have these are all ways to think about this well most importantly we're going to have comments certainly we're also
going to have a live video now the actual data model for the live video where it's stored this is out of scope
this is another team that will handle this but it's important to recognize as an entity because we're going to have
relations to it so I'll write it down anyway and then we're of course going to have a user or a viewer so those are our
core entities and we can then move on to our API and use those core entities to
shorthand our API a little bit uh so when you get to the API the easiest
step-by-step formula here is to just go back to your functional requirements and go one by one through your functional
requirements making sure that you have an API to satisfy each of these now this isn't 100% foolproof uh for non not non-
user-facing system design interviews something like a designer web crawler you know this doesn't make as much sense
but if it's a product if it's a user-facing product as live comments is then this is a nearly fullprof way to do
this and so some uh functional requirements may require more than one endpoint but the process Remains the
Same go one by one through your requirements and create the endpoints necessary for each so the first thing is viewers can post a comment okay great
we're going to use a rest endpoint and we need viewers to post a comment so
what could that endpoint look like well it's going to be a post because we're creating a new resource what is our resource name it's comments uh some of
you have have picked on me in the comments ironically um for not
pluralizing my resource names so the reality is to me as an interviewer and to most people like who cares um but
proper restful semantics say to pluralize your resource name so I've done that here for you um and then we
need to know which live video we're posting this on and so I'm going to use a path parameter here and pass in the
live video ID now why not put this in the body well you absolutely could um but given that it is required you cannot
possibly create a comment uh without a live video ID it's common here to put it in the path parameters and so that's
what I've done here now what does this return it can either return the comment or 200 what's the body well the body is
the comment itself and notice how I'm not getting caught up in the details of like what is a comment at this point of
course a comment is going to need to have some content uh you know if there were extensions here then maybe it would
have a um media attachments which we're not going to handle but I'm just abstracting this for now and it's just a
comment it's the core entity that we've defined as a comment is what is the the post body there so we checked off one of
those functional requirements let's go back up and look at what our next one is viewers can see all comments p uh posted
in near real time um um so astute viewers are thinking to themselves wait
a minute this is going to be a websocket or some persistent connection you're right and if you know that this early in
the interview go ahead and write it down that's fantastic I'm going to take the approach of assuming that we don't know
that or even if we do we're just going to build things up simply and so the simple way to do this would be that
we're just going to have some get endpoint we're going to have some get
get comments endpoint sheesh this is why I don't type in front of you guys like this get comments endpoint which takes
in again that live video ID and maybe it's just going to take in a cursor so this is basic cursor based
pagination um and we we'll be able to pass in the last comment ID that we saw and this is going to return to us any
new comments that have come in since that last comment with some page size here maybe like 50 okay and so if you
don't know about cursor based page donation fairly straightforward you're just going to pass in a cursor which is the ID of something in your database
some Row in your database and then we're going to get everything after that and so that's what we're doing here we're
going to get the 50 comments after this and so we can just be calling this over and over again in order to simulate some
sort of real time we'll talk about that more in the high Lev design and of course this is not the optimal solution
it's not efficient we'll do something better but at the early phases of your interview even if you are a staff
candidate or something it's okay to put this down for now uh and you can just acknowledge you know this is going to
expand this is probably going to use some bidirectional communication or unidirectional communication but
something persistent later on and so the next one uh viewers can see all comments
posted before they joined well this is essentially the same thing right we want to get all the comments for a live video
but instead of anything after the live comment ID we want it before the live comment ID and similarly we want a page
size like maybe we want the 50 before this point in time and then if we want 50 more then our last comment ID would
be updated to the uh last of that 50 that we just got and we'll get the next
50 you kind of see how that's happening recursively but the difference here is there's a direction in one case we're going past comments and another we're
going future comments and so what we could do is we just add that direction pretty simply to our API endpoint do we
want after or do we want before that's a way that we can that we can model
that so there you go two basic rest end endpoints one to post a comment the
other two to get comments I'm using basic query parameters here denoted by the question mark for the first variable
and then the and sign uh for for the remaining variables posts gets all
pretty straightforward thus far so zooming back out we've done our
High Level Design
requirements our core entities and our API this is kind of the general setup of the problem at this point we've agreed
with our interviewer what we need to do we've set our parameters our found Foundation we know the general apis that
users are going to use to interface with our product and now we need to move on to that highle Design This is where
things get fun they get interesting we start actually drawing those boxes um on the Whiteboard and so just like with the
API with the highle design we are going to just satisfy our functional requirements and we can do that by going
one by one through our apis and so if we go one by one through our apis we'll subsequently be going one by one through
our functional requirements and we're essentially saying when this request is made what happens in our system what
happens in the back end of our system and what components are necessary in order to effectively fulfill that
request and so I'm going to move a little bit quickly through this highle design the reality is the highle design
for this system is is really straightforward and I want us have adequate time to go into deep um to go
deep on the things that are interesting bya deep Dives um but let's talk about what it might look like so the first
thing is that users want to be able to post the comment we have an API for that a post comments to a live video ID cool
let's model that what's that going to look like for us well the first thing is that you're going to have a client I'm
going to introduce an API Gateway it's not strictly necessary here uh it's a
single client server database relationship you'll find so we don't need routing but I'm going to take
advantage of the middleware and I'm going to introduce it uh I'm also going to have a comment service and so this
comment service is going to be responsible for com comment crud oper ation let me just move it down a little
bit and then I need some way to persist these comments and so there is my
comments theb great and so what's going to happen is the user is going to make
that post request in order to create a new comment our API Gateway is going to forward that onto our comment service
our comment service is going to craft and then initiate a query to our comment
CB in order to create that new comment and so we talked about earlier in our core entities how we weren't going to
talk about the data model or the schema just yet now is the time where we do it when we get into our high level design
you can see how it's really linear at this point I've just told my interviewer this is going to save a comment and naturally now I can say well what is a
comment right a comment's going to have some comment ID that's going to be important it's going to have the video
ID that this comment was placed on it's going to have the author ID um and then
it's going to have the contents of the comment the text of the comment probably some created at field is going to be
necess necessary and so in terms of our query pattern we're going to be querying by video ID a lot so we'll want an index
on that we're also going to um be sorting by the created at column so
that'll be important as well and I'm not going to make any decision about the type of database yet uh in your
interview it could go either way you could talk about it now that would be totally fine I'm going to choose to talk
about it when we talk about scale because I think it's going to be more interesting the reality is for a simple highle design here any database is going
to work SQL database is fine here MySQL postrest Etc key value stores document stores
they're all going to get the job done um so I'll go into more detail on that a little bit later but important to know
where your indexes would be what your primary Keys would be of course comment ID in this case so that's the thing for
us to to handle but very simple client initiates a request we save that comment in the database and we return with our
200 check we now have viewers can post comments it's a simple crud service
next up is that viewers can see all comments posted in near real time now of course as we alluded to earlier this is
going to require some persistent connection you'd be wise to let your interviewer know that hey I know that
this is going to require some persistent connection but let me start with the simplest thing that we could do the simplest thing that we could do is that
basic polling with that API that we outlined here so get comments for a live video ID that have happened since some
given last comment ID that we have this could also be a time right different ways to handle this time might even be
more natural um for this direction of the query anyway but in any case what we
can do is then just have a simple client that is going to every two to 5 Seconds
query our gateway to ask our comment service if there are any new comments since a given comment ID if no comment
ID is given well then there's no comments since that point right
um that quer is simple that query is simple regardless of what database you chose so if it was a SQL database this
is simply you know select all comments um where video ID equals the given video
ID and created at is greater than the created at time of the cursor fine um
and then similar query if this is a document store or key value store this query is pretty straightforward
regardless of what database you choose so if you chose a SQL database then it's just select all comments where the video
ID is the given video ID and the created at time is greater than the created at time of the Cur CS or the last Red
comment nothing to it uh similarly easy on a document store or similar awesome
so again we're just expanding this basic crud service we can create things we can read things nothing to it we're going to
use polling in order to just get new comments every couple seconds and those will be maybe not quite the near real
time we're looking for yet again persistence uh connections will be important later but it's a good start
for now the next thing that we needed to do is viewers can see all comments posted before they joined and so we had
the same API endpoint we just specified a direction and it's the same concept here so when a user first joins the live
video they have no comments they have no past comments uh or they have no kind of new comments yet we're going to probably
first load up that live video alongside the last 50 comments or so from the video and in order to do this we'll use
that same API endpoint we're just going to switch the direction and in our query that's just going to switch the greater
than or equal to on the created at sign so now we want the last 50 comments that are less than the current comment and
obviously we're not going to necessarily have a current comment right out of the gate and so if that's the case we'll just start from the end of all existing
comments right similar concept there now one thing that I'll note just for fun um
but this wouldn't necessarily be the most important thing in this interview but there's different ways to handle
this concept of a user continuing to scroll up so you've probably done this on Instagram or on Facebook live what
whatever it may be where you scroll up and it fetches the last 50 and you keep scrolling up and you want to just scroll
up and up and up and up and up maybe you want to go all the way to the beginning uh for whatever reason you you continue to scroll up and read comments and
there's different ways to optimize this one really popular thing to do with pagination is to introduce a cache and
this is going to be a cache for a specific user ID and in our case live video or just video ID so that would be
the key and then it's going to be the comment as a list here and so when a
user fetches comments past comments we might show them the last 50 but we're going to cash
the last 1,000 this is going to have a really tight TTL and so maybe it just has a TT of 5 minutes because that's
what we anticipate being the narrow window with which they might still be scrolling up and so now if they scroll
up above that 50 instead of having to to issue the query we can just go grab it from their cash and give them the next
50 now what you might be thinking is it why don't we just give them more than 50 we can do that as well of course we can
give them thousands uh and then let the client just show them the ones that matter at that point there's different
optimizations here and this really would only matter for super popular videos where comments are coming in like crazy
and somebody may want to be scrolling up really quick in order to fetch the next the next group of thousands of comments
or so another pattern that we could do again just because it's interesting and related to pagination here not specific
only to this problem is that we can have it be such that we send the client over maybe the 500 last comments and then
once the user Scrolls up to about the 400th then the client is going to know let me go optimistically fetch the next
500 because I have a feeling they might finish this list right finish this stack something similar to what we do in
Tinder uh if you've read that breakdown or seen that video so I'm not going to include this because it's not the focal
point here in design FB live comments if anything I would just briefly comment on
that um but I wouldn't let myself get distracted because despite how simple this highle design is and it is quite
simple basic crud service it satisfies all of our main functional requirements and it's left me plenty of time in the
interview now to talk about the things that are going to be interesting which are going to be these non-functional requirements around how to scale and how
to ensure this low latency and eventual
Deep Dives
consistency all right with the highle design be behind us it's time for everybody's favorite part which is the
Deep Dives and so again in the Deep Dives we're just going to go one by one through our non-functional requirements and expand on this simple high level
design in order to make sure that we met all of these requirements at the end we're going to be able to look back and
say okay I met all my functional requirements I met all my non-functional requirements I acce this interview give
me the offer and Life's good right so that's our goal here uh so first off one
thing that I want to mention is the level to which you're proactive in the Deep Dives is a function of your seniority and so if you're a junior or
mid-level candidate this might actually shift now to where you're less leading the interview and it's more of a question answering so the interviewer
might be asking you questions you know this polling approach isn't going to give us the low latency requirements
we're looking for what else could you do right for example but if you're senior especially if you're staff the
expectation is that you identify where the issues are and you drive the conversation towards these things and
again the best way that you can do this is just by going one by one through those non-functional requirements so let's do that now um I'm actually going
to go in reverse order here maybe I'm going to start with low latency comment broadcasting so this is the case where a new comment came in it should show up on
everybody's client quickly as you remember we're using polling right now so we just have the client every 2 to 5
Seconds asking if there are any more comments of course this means that our latency is 2 to 5 Seconds as opposed to
the 200 milliseconds that we were looking for so we're going to want to find a way to speed that up the key
Insight is that instead of using HTTP request responses here where the client is saying are there any new comments and
the comment service is responding after quering the database we need some sort of a persistent connection here so we
need a way that we don't have to ask every single time but instead the comment service can just tell us as soon
as a new comment comes around and so there's two popular Technologies to
handle this persistent connection the first is websockets and the second is
ssse and so let's talk a little bit about each of them I'm actually going to paste in some notes Here Again to
prevent you guys from watching me struggle while typing starting with websockets websockets are bidirectional
and so you create a connection like this and now at any point the client can say something to the comment service but the
comment service can also say anything to the client at any point this is great and so in our use case you can imagine a
new comment gets created or saved by somebody else and we just push over that websocket right so push instead of pull
back to the client to say there's a new comment and we can do this quickly so this is great and it's a viable option
but websockets also have some downsides so websockets use their own protocol they're not over HTTP or https and this
just means that they're a little heavier weight what happens is that they initiate an HTTP handshake first then
they need to upgrade to a websocket connection and you need to have all of your infra in between all of these
places support this upgrade and so for example the client's going to go to the API Gateway try to do a handshake
establish a websocket connection here right and then likewise it's going to go create a websocket connection here so
that it can sort of be a pass through but in the case where you have low balancers proxies firewalls or any of
these things uh that don't support websockets things are going to break and this happens more than you would expect
actually so often times if you're putting websockets into production uh things are working in your test environment everything's great you put
it into prod and you realize that either it's not working at all or it's not working for some users and this might be because some users are Reed to corporate
firewall that's not going to allow for these these websocket persistent connections um it could be that you have
some production API Gateway or otherwise which isn't going to support them and so there are plenty of API gateways that
supported out of the box AWS managed uh API Gateway is an example um I think
like engine X has configurations for it right so this is by no means a a task
that cannot be achieved but it comes with overhead and it's a bit more complex and the main kind of interesting
bit here and maybe I'll write this down oh I already have it there right so websocket is perfect for when it's bir
directional there are as many reads as there are writes so the client needs to get as many things as it needs to send
or post and so in the case of a messaging app this was the last video we did check that one out with Stefan we
did WhatsApp if you haven't seen it already but in the case of a messenger app this is perfect because there's likely a pretty close relationship
between the amount of messages you're sending and the amount of messages you're receiving but that's not the case here with live comments the overwhelming
majority of our users are going to be in a live video watching the live video and and the comments are just streaming in
like the average here might be 1 to a thousand or so you can have some users who are active commenters but the
majority are passive they're just watching and so it's not bidirectional we can still post a comment periodically
with our restful API that we have with this you know SL comments post request that was right here on this https
endpoint um but we can receive comments via that persistent connection and so
websockets seem to be a little bit of Overkill so what else can we do do the other thing that we have is that pastes
it up here ssse or this stands for Server sent events send events and this is actually
perfect for our use case in live comments because it's similar to websockets and then it it opens up this
persistent connection uh but it's unidirectional and so in this case it's just the uh it's it's just the case that
the comment service can push changes to the client but the client can't say
anything to the comment service over this and so instead of having its own protocol like websockets do it's just
over HTTP and https and so it uses uh it uses HTTP headers in order to specify
that hey I'm going to be sending this over over chunks so keep this open uh and it basically just looks like a long
running HTTP request the other nice thing about this is that it doesn't require anything too fancy like browsers
have built in support to handle the reconnections and everything that go on here if for some reason you were to get
disconnected and so so it makes it a much more lightweight and then given that we only need unir unidirectional
communication it's the right choice for us of course you can still post a comment you're just going to post the
comment over the HTTP request response via our post endpoint which was this guy
up here all right so hopefully that that all makes sense now not all API gateways
similarly support ssse out of the box um so there are still challenges here um
many of them will like close your connection after predefined period of time and you need to go in there and update their configurations in order to
elongate that or specify different headers to make it clear to the Gateway that it shouldn't separ the connection after say 30 seconds or 60 seconds so by
adding ssse it doesn't solve all of your infrastructural challenges but it definitely makes things easier
lightweight and we get the unidirectional communication that we're looking for so let's let's tie that together I'm going to just by way of
abstraction draw a line through here technically as you saw it was to the API Gateway and then the API Gateway
forwarding to the comment server um but I'm going to choose ssse and I
would say as much in my interview I would weigh the trade-offs between websockets and S as we just did and I would come to the conclusion that SSE is
best um and so when a client now creates a comment we are then going to look for
all other users who are listening or watching that live video and we're going
to push over ssse that new comment so that they get it and so you may be thinking okay but once a new comment
comes in how does the comment service know which users to push this to do we need to update our database do we need
to store this state somewhere and it's a great question but it's actually really straightforward and so all we need to do
is have an in-memory mapping in this comment service and so a new s
connection is established the first thing that can happen when this is this connection is established is that we're
letting it know maybe via the headers which live video we're watching and so we're saying this SEC connection is
associated with video id1 and we can just store that mapping in memory so here's an example of what that could
look like so these connections these are just pointers to the respective connections and now if a new comment
comes in for video id1 I'll look in that mapping in memory and say who all is connected to video one oh well I have SS
connection 1 4 and 7 so let me send it to them and I can just do a for Loop and do something like connection 1. send
that new comment that came in and then it's going to show up uh to the client for them to be able to render
as needed so this is how we're going to enable that sub 200 millisecond latency
because a new request is going to come in our comment service is then over ssse going to maintain this persistent
connection that it can just push over uh that new comment uh but you might notice
that this doesn't scale very well uh what happens when we need to horizontally scale our comment service
and now we have multiple of these and it might be the case that a new comment comes in and it lands on this server but
the people who are watching this live video are on a completely different server and so this one doesn't have SS
connections right it needs to somehow communicate with this one to send it over to them and so that's one of the
things that we'll talk about next as we get into scaling so before we get there we're going to look back at our
non-functional requirements we just talked about low latency and now we're going to jump around and we're going to talk about
scale and so let's come back we had talked about what that issue is if the comment service horizontally scales then
we don't know which user is connected to which service and which live video they're watching and so we don't know
how to forward that onto them so let's break this up a little bit I'm going to move some things around I'll keep them
on the Whiteboard so you guys have them later um but the first thing I'm going
to do is I'm going to do a little bit of math now and you might have noticed I didn't do math up front this seems kind of like a faux paw system design any
you're supposed to do math up front I disagree uh I find that most candidates do math for the sake of doing math they do some estimates on scale some
bandwidth they look at me they go so it's like pretty big and then they they go design the same system they were going to design that's not useful math
is very important though but math should inform your decisions and so my concrete suggestion to you is to do math in your
interview at the point where you have a decision that you need to make and so in this case the decision that I want to
make is scaling here and so I want to think about my my bottleneck we said that we were going to have a million so
1 two 3 one two three we said that we were going to have a million uh active live streams at any given moment and
then we would have like a th000 viewers we said right and so what I'm trying to
figure out is how many ssse connections am I going to have at any given moment because an ssse connection is probably
going to be my limiting factor here uh boxes high powered boxes they can handle
give or take like a million ssse connections and so we'll use that as a rough number and then our division
becomes easy here because we have a million concurrent videos a th000 viewers of each and so that means that
we're going to need a thousand services in order to handle just the number of ss connections and so we don't probably
need a th Services when it comes to writing posts um because the amount of memory that we have here the network
needed to write to the database will scale this out later it would turn out that that's probably less and so this is
our limiting factor and so what I'm going to do right away actually is I'm going to do the following I'm going to
separate out a separate service and I'm going to call this like the real time comment service um and what's going to
happen is that this service is still going to be responsible for what it was before of this HTTP post request in
order to get old comments uh post request in order to create comments and then get requests to get old comments um
but instead we're going to create the SS connections to this guy and so let me model that in a way that looks a little
bit easier maybe can I make that transparent
there you go so obviously this is going to be horizontally scaled too but what I'm trying to get across here is that there are a thousand of these servers
right and I separated them so that I can scale them horizontally differently and so I might only need a hundred of these
but a thousand of these and that's why I've separated them out right so every time an S connection gets established a
user started watching a live video we are going to connect them to one of these realtime comment services and now
you can see the issue hopefully a new comment just came came in our comment service got that comment and saved it to
our database and now it needs to tell every single one of these 1,000 let's
say to make this concrete let's say that new comment for video one just came in
and so it needs to tell every one of these comment Services these real-time comment services that is connected over
s to somebody who is watching video one that it got a new comment and so somehow
we like need an arrow here uh it would be a unidirectional Arrow right so
somehow we need to tell one of these servers but how do we know which server that's the big question that comes up
and so there's two ways to handle this let me show you the first here and the first would be that you would introduce
a central dispatcher is maybe the way to think about this and so you'd have something for coordination zookeeper is
a great technology to handle this coordination and so zookeeper is going to keep a mapping a registration of
where all of these servers live and the live videos that they're responsible for
okay and so then what's going to happen is that when a new client wants to connect over ssse here it's going to
make a request either to our comment service or realtime comment service either way and we're going to go over to
zookeeper and say hey a new person needs to connect they're watching live video One which real-time comment service
should I subscribe them to and it's going to give us a host IP address that we should end up connecting them to so
that we can establish this SSE connection and so let me show you here what that might look like I'll put this
over here maybe even I'll make it a different color right so that's what that's what exists here in Zookeeper
it's this active mapping of all of the different servers and the videos that they're subscribed to and maybe how many
users they have from each of those respectively and so now the process would be that when a new comment comes
in the comment service let me go back to black the comment service is going to
ask zookeeper hey I have a video for live video 123 uh which server should I
message that to and it's going to tell you oh it's This Server so all good and then we're going to come down here we're going to draw an arrow to these guys
we're going to let them know that we have a new message or a new comment that came in and they can push it over to
their friends over SS again via that inmemory mapping and so really quickly what actually happens here is that we
don't ask zookeeper every time that's slow uh we have a cache and so in memory on the comment service we've cached this
mapping this Json blob so when a new comment service comes up it asks zookeeper the source of Truth hey what's
the registration what's the mapping let me cat that on my server and then I'm going to subscribe to any updates and so
any updates to zookeeper are going to get pushed now and my comment service is going to accept that incoming update and
update its cash respectively but tying This Together comment comes in comment
service says either by looking at its cash or asking zookeeper directly I had a new comment for live video video one
which servers have ssse connections to everybody viewing live video One it's
going to tell me it might be one it might be multiple I'm then going to make a request to that server with the
comment and then that comment is going to look up in its inmemory mapping which connections it has for that live video
and it's going to push them over ssse of course this should be unidirectional as well uh over ssse
to the client so the client can render that new live comment so that's option
one that's the the central dispat dispatcher approach there's some
downsides to this approach the first and most obvious one is that we have an extra hop here every time that we come
in we need to ask zookeeper and so we largely got rid of that hop here but we
didn't on the connection when a new thing is connected it needs to ask zookeeper which should I connect to and
so again the cach is helping us a lot here but there are some potential downsides there I'm going to hold my
hands up and say this is hand waving honestly the cash is probably fine um but you have an extra component to
manage uh potentially an extra hop here more importantly is that there's complexity in handling changes to the
real-time comment services so these are going to go up and down respectively they might die for some reason we might
need to scale horizontally and add more and zookeeper needs to maintain visibility of all of that state and so
when new servers come up they have to be registered within zookeeper zookeeper needs to be pinging heartbeats to each
of these to know who is still up and who isn't and so it's not just that these servers need to know who they're
connected to or at least the number of people they're connected to but that needs to remain consistent with what
zookeeper sees and so we've introduced a little bit of a consistency issue here that has the potential or capability to
get out of sync and so zookeeper has a lot of great tooling to make this problem not much of a problem but these
are the potential downsides here so that's that approach let me copy this
and show you what the other of the two approaches would be so alternatively we
don't have zookeeper instead of having a single source of truth that we go ask like an all- knowing Oracle hey where
should I send this to instead what we can do is we can just broadcast so think about the comment service just like
yelling out into the ether maybe with a megaphone it just says hey I just got a new comment for live video One and then
all of these real-time comment Services have their ears open their ears to the street if you will and they're listening
and if they hear oh live video One I have live video One then they'll take that new comments and they'll do something with it and if they hear it
and they're like oh I don't have live video One I don't care about that they won't do anything with it right and so
in this case we would introduce Pub sub which is perfect for
this sort of broadcasting and subscribing and so the comment service is going to get a new comment it's going
to those arrows of the wrong way that's getting annoying um it's going going to put that
new comment on pubsub probably after committing to the database so first for durability uh sake commit that new
comment to the database then broadcast it by a pubsub so put it on pubsub this
is just a channel right it's just like a message bus um that we're going to put
this on and then all of these guys all three of them and you know when uh in
production all up to a thousand of them or more are subscribed to this message bus right they're subscribed to this Pub
sub they are subscribers so this is the publisher these are the subscribers and so a new video comes in it's going to
yell via Pub sub new video came in and then all of these are listening and only those that hear one for which they know
that they have an active user who is connected is going to take it and then again run that connection one. send with
that new comment right so that's the the pubsub approach the nice thing here is that you don't have a consistency issue
anymore more and you don't because you don't have two things that need to know their own State these real-time comment services are the only thing that need to
know their state and it makes uh failures in the comment realtime comment service a lot more graceful you can
imagine that one of these goes down well then those users just lost their s connection no big deal right and so
they're going to need to reconnect they're going to reconnect to a different one of these we probably pulled another one up as well but
they're going to reconnect to a different one of these the inmemory mapping is going to be updated and then
because because we're still going over pubsub we're just still subscribed we're listening and we're going to send it over to them um so these guys know what
they need to care about basically there's no other thing that needs to be in the picture so between these two
options there is no right or wrong answer both of these options are great I tend to think that this Pub sub solution
is a little bit simpler um I think actually that FB live comments in
production went with they don't use keeper to my knowledge but went with a single dispatcher approach it's actually
for slightly different reasons around scaling in collocation which we probably won't get into in this video but both of
these approaches are absolutely valid in an interview if you're a mid-level candidate you're probably not going to
get into this much detail if you're a mid-level candidate you'll say I'm going to use Pub sub to broadcast from the comment service to a real-time comment
service which is connected over SS your websocket and you're golden if you're senior it would make sense for you to
weigh these tradeoffs a little bit um and then certainly if you're staff you should be able to articulate the pros and cons of each of these go into
details about them and then even furthermore as we'll do here in just a moment talk about how each of these May
scale respectively so now the problem that's worth discussing briefly and this would probably just be something that a
staff or really great senior candidate talked about would be that all of our or
all of our real-time comment services are subscribed to every single new comment right now and so you look you
can look at this as like drinking through a fire hose this is a pretty CPU intens task now because every single
comment that comes in they're checking in their mapping they're determining if it's right for them if it is they're sending but there's a lot of wasted
resources here because the overwhelming majority of the time it's not going to be a comment that is something that they
have an active ssse connection to for a client right and so we want to wait for them to just listen what to what matters
for them and so what we can do is that we can partition our Pub sub and so if
you're using like red is Pub sub these are called topics if you're using Kafka they're called channels but they're all the same thing they're just partitions
of our Pub sub you can think of them as just like maybe oh kind of multiplying these out there's not a lot of space
here but you get the picture uh kind of like a stack of different message buses here and so what you can end up doing is
just separating using something like the hash of the video ID modul the number of channels that you want or the number of
topics that you want so something like that and that's how you can determine which one of these it should go on and
then each of these real-time comment Services don't need to subscribe to every single topic or every single
Channel they only need to subscribe to the sub set that they have an active
client connected to them with right so you might only subscribe to a couple of these and this way you're only listening
to messages that come in that are either your live video ID or something else that's in this hash grouping so it's not
perfect it's not like it's only your videos uh someone might be tempted and I hear this in interviews they're like I'm
going to partition based on um having a topic for each live video ID
this just wouldn't work um it certainly wouldn't work in Kafka I don't know red is is limit off the top of my head but
it probably wouldn't work as well there's limits reasonable feasible limits the number of topics or channels
that you have and so that's why you want to do this hash modulo end thing so you can just group them together and go from
one big channel to end channels where that end channels might be a thousand it might be a million uh whatever is needed
for scale that's something that can always be tweaked but then we're only listening to the ones that matter now
the last thing that I'll mention here and I'm going to go over this just really briefly is that you don't want to
have let's say that there's three people watching video one you don't want them like randomly assigned cuz then maybe
they'll all show up on a different server here and now three different servers need to subscribe to the channel for video one when we could put all
those on the same server we could collocate those ideally you have every single viewer of a single live video on
a single real-time comment service now if you have a popular video with 160 million concurrent viewers or something
like the Chewbacca mom or a World Cup final then that's not going to work you're going to need to allocate that over 160 of these but at least it's 160
and not 500,000 right um so that's one optim
optimization that you can handle in the case of Zookeeper approach this actually makes this easier uh because when a new
request comes in we're going to look at where everybody else with that video ideas and we're just going to tell you to connect to that same box so this is
great for that approach it's a little harder here the way that this works and it's a it's a bit complex
so again not going to go into too much detail but you can actually have a zookeeper or
another um another service similar that sits here and then your API Gateway via
a layer 7 low balancer can have in the header what the live video ID is and then ask this guy where should I route
him and then route it to the correct one and so it's similar to the dispatcher approach we're just only using the dispatcher uh to do Cod location you
could make the argument at that point then like why not just come up here and do the dispatcher approach um like I
said both work no Pros or no no right or wrong answer there it's just a matter of
weighing trade-offs the last thing I'll touch on um is that if you're a staff candidate
maybe a fantastic senior candidate there's more you can talk about here like for example what is the difference between using redis or Kafka um you
actually probably don't want to use Kafka here because Kafka has a lot of overhead to subscribe and unsubscribe
from channels and you can imagine that when users are scrolling through their feed they're subscribing and unsubscribing really quickly if they're
not clicking into a live video they're just scrolling through their feed and so pubsub uh with reddis being in memory
makes this a lot easier so maybe it's a better approach there right that's the sort of thing that you can talk about to show staff level signal um I guess we
should talk about the database I I I mentioned that we would come back to that and I think now is an appropriate time as it pertains to scale so we said
that we would have the the 1 million videos um let's just estimate and say there's about 100 comments per video I
think that's fair if anything it's probably even high the overwhelming majority of videos probably get no comments um this is concurrent so
loosely let's say each video is about 30 minutes that's probably too long but in any case that would mean that if they
were fully sequential this is like 48 um
is I guess a day right so this is how many we're having a day um
it's going to grow quickly there's a lot of Rights here and this is decent scale 480 million right is that math wrong 480
million I think I'm off by one order of magnitude there so 4 billion um I don't
know Mental Math while you're on the spot in a video for everybody who's watching is difficult so forgive me but
regardless I can get a sense here that this is a lot it's also high right through put so we're going to want a database that can support that high
right right through put but realistically a postgress database if sharded and scaled correctly can do this
SQL databases would work fine but there are databases that are optimized for this sort of thing and given that we
really have no relations in our data we probably have a user and a live video ID column uh in our query is pretty simple
it's just going to be able to query a primary or not a primary key uh but query an index here for for video ID and
then you know we can use the created ad as our sort key so Cassandra is going to work well here um it's going to be
really easy to Shard based on video ID so we can scale this horizontally like I
said sort key on created at the query is simple it's just to get it for a given video ID and it's great at handling the
high right through puts um so that's what i' probably do
there and of course this is going to result in eventual consistency in places which is fine so this goes back to our
nonfunctional requirement if we're going to prioritize availability over eventual consistency so if we go and we try to
read and we have replicas here and we're hitting a read replica or something it might not have the latest comment that just came in yet that's okay we're going
to show it to the user anyway without that latest comment no big deal and if anything we have the pub sub or the dispatcher um real time flow to make up
for things there okay uh let's take a look back we met our functional requirements we met
our non-functional requirements we went through the full flow we nailed the interview we're hired we're excited hopefully this made sense the things
about this interview just to recap is when to use websocket versus ssse websocket is heavier weight but
necessary for bidirectional communication we have a one to one in the read to writes SS is unidirectional
lighter weight but this means that we can only push from server to client um so it's great when you have a lot more
uh Communication in that direction right and the balance isn't even there uh we
talked about how to scale up whether it's pubsub or a central dispatcher in
order to make sure that we can locate the correct real time server for which the persistent connection is on this is
a common problem this is similar to what you're going to do in something like a real-time messenging app for example
talk a little bit about scaling databases um the inmemory mapping I think we've done a good job
Conclusion
here all right well done if you made it this far hopefully everything made sense and you have a pretty good understanding
of how to design a live comment feature for Facebook or any other live streaming platform if you like the video give us a
like give us a subscribe if there were questions if I did something stupid wrong you disagree with leave a comment
let's chat about it I'd love to to respond to as many comments as I can um and like I said keep an eye out more
videos coming to start 2025 but all in all hope you guys enjoyed and best of luck with your interviews talk soon



```
