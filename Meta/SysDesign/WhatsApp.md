Intro
hey everyone and welcome back to the channel today we've got another problem breakdown for you we're going to be
doing design WhatsApp or design messenger this is a really common
question and one that people are constantly asking us uh for a YouTube
video so here I am before the end of the year giving you uh that YouTube video uh
for you those of you who are new to the channel we are hello interview we're here to help you prepare for your
software engineering interviews this channel is loaded with guides deep Dives
uh and problem breakdowns that will hopefully help you prepare for system design we also have a ton of content on
the site talking about behavioral interviews we've got animated coding Solutions and patterns uh lots of stuff
that we think will be very helpful for you um for me I'm Stefan I am one of the
co-founders of hello interview I have also worked as a senior manager at meta
and then at Amazon uh where I conducted north of 20 interviews so I am very
familiar with the process and hoping to share some insights as we walk through
but I don't want to spend too much time if you like content like this please like the video subscribe and let's go
ahead and dive in before we dive in I wanted to introduce our delivery framework this is
The Approach
just basically a series of steps that you'll follow in order to conduct your system design interview now for midlevel
and Senior candidates I highly recommend that you follow this as closely as you can if you're a staff level candidate
you've got 20 years of experience and you want to color outside the line great but the purpose of the delivery framework is to make sure that you cover
the important bits of the design and also to help you to think about the problem as you work through it what we
find is that candidates who follow this framework tend to on average and there's
certainly exceptions uh perform better uh in interviews than than candidates
who don't now I'm going to actually try to follow this as closely as possible for this video so you can get an idea of
what that looks like and then I'll earmark those places where I'm diverging or giving you some additional detail
that may not actually be part of your interview but the first step is requirements and that's where we're going
Requirements
next is a place where we can have a conversation with our interviewer to really understand the scope of the
question and sometimes we can even debate what's in and out of scope in the ideal case once we've set our functional
requirements we can actually use those as stepping stones for our high level design and for a lot of candidates who
get lost or have difficulty managing their time it usually comes back to them not setting good and actionable
requirements so do spend time here we generally recommend candidates spend about five minutes and what that gives
you enough time to do is to think through all of the different product edge cases to come up with a concise set
of functionalities that you need as well as the non-functional or constraints on
your system so for WhatsApp the easiest way for me to come up with functional requirements is to put my myself in the
shoes of the end user so I open up the WhatsApp app what do I see well the first thing that I see is a list of all
the chats that I have with other people or other groups but in order for those chats to exist I have to have created
them so let's go ahead and assume that one of my functional requirements is to
start group chats I'm going to use group here as like a general case if I've got
a group of two that's a one one to one message now once I've got those those
chats in place the next natural requirement is for me to send and receive messages between different users
um my expectation is that if I send a message it goes to all of the members of that chat and if anybody sends a message
to a chat that I'm a member of I'm going to receive that now it's a natural question here to ask are there
constraints on these messages do we want to support video audio and maybe my
inter viewer says yeah we should definitely do that so we add media attachments to what we're going to
design another thing that we should probably think through as the candidate
is what happens when our clients go offline if you're designing um a product
that has a mobile app those mobile apps are going to disconnect periodically
maybe I turn off my phone before I go to bed and in that case for WhatsApp I
would expect that when I wake up and turn my phone on on that I'm actually going to get all the messages that I
received when I was offline so I'd like to be able to access the messages after
I've been offline I can go into additional detail here I can ask my interviewer about
whether we should support video and audio calling whether I need to be able to see whether my friends are online or
offline but generally speaking we should try to keep our requirements pretty short and there's no
actual need for me to go ahead and say I need below the line uh audio video
calling if I don't have time now in this case I've spent about 2 minutes getting
the base functional requirements I have some additional time here where I can discuss with my interviewer some
additional functionality they might be planning but be careful about expanding the scope to be too uh extensive if you
do you're going to create problems for yourself if you're low on time and you didn't just rattle off those
requirements I've obviously thought about this problem before then don't bother wasting your time trying to
enumerate things that you're not going to include it's a good idea to ask your interviewer hey do you have anything
else that's in mind then move on next I'm going to move over to my non-functional requirements and here I'm
going to try to describe how the system performs these aren't nuser functionalities these are things that my
system ought to do while while I'm making those functional requirements real so the first thing that most people
are going to think of when they think of a chat app is low latency I'd like to be able to get my
messages um in a short amount of time now a lot of candidates will stop here
and they'll say oh it should be low latency but I would actually encourage you to quantify these non-functional
requirements where possible in this case let's think what would be an appropriate
latency for a chat application well it turns out that most people aren't going to have two phones sitting in front of
them looking to see if I send it from this one how quickly do I receive it so we've got to figure out what would be
perceivable well if you were sitting across from me and I sent a message and it I had to wait a few beats before I
got a message that would seem slow but the difference between 100 milliseconds
and 500 milliseconds is not really all that noticable so we want to give ourselves a bit of room here in our
design and we don't need to necessarily make this uh low latency so let's go
ahead and assume that it's 500 milliseconds of latency this is going to come back later on in our design because
we'll be able to use that 500 milliseconds and ask whether we have budget to do different things the next
thing that we might think through is that we want to make sure these messages actually get to their recipient uh it
would be weird if I sent a message and they were like well I never actually got that so we'd like to be able to guarant
that the delivery of messages actually happens the next thing that we're going to think through is what's the scale of
this system and often times candidates will try to make assumptions here about
the size of the system for most of the web scale systems it's usually a decent
assumption to assume 100 million or a billion users and in whatsapp's case I
think it's actually a couple uh billion users so let's just go ahead say billions of users so we need high
throughput for our system we're going to have to handle lots of messages I'm going to defer here in trying to come up
with the actual number of messages that the system needs to uh receive and send
because I'll be able to make more informed estimates of that later on when I know more about my system I don't need
to jump into uh back of the envelope calculations just yet the next thing is
specific to what's out I don't want to store messages unnecessarily so ideally
I'd like to keep the messages on the server just long enough to be able to perform my functional requirements and
then I'd like to get rid of them if you think about privacy and WhatsApp is a very private app then data is like toxic
sludge it's something that you don't want to keep around that ideally you're either actually deleting it or you're
encrypting it in a way that even you can't access it so that way you don't have the liability on your hands the
last thing that an app like what app probably needs is to be able to tolerate
faults this is a gigantic system we're going to have things that are failing all the time ideally these individual
components aren't going to take down our app this is generally true of most apps but it's especially true of what's out
and so we're going to include this in our non-functional requirements now we might talk about additional things here like should we be
able to prevent spam and security issues should we have to deal with scraping or
people trying to get contact information from all WhatsApp users I'm not going to
go into those but if I had additional time I'd Mark those below the line uh and move
Core Entities
on now that we've got our functional requirements our next stop in the delivery framework is our core entities
core entities are not an explicitly evaluated part of the interview you're not going to have interviewers who are
writing in their notes hey they got the core entities wrong generally speaking what they're evaluating is that final
design and kind of the process through which you came up with it but core entities are really important in that
it's easy to make mistakes in your design if you don't get the entities right this is also a place where you can
have some discussion with the interviewer about the identities of various items especially in product
style interviews being able to think deeply about the identities of entities
in your system is going to make a world of difference in in your data model in your API and so forth and so for some
interviews like meta's product architecture interview being able to reason about these entities is really
important now for this problem we first want to talk about the actors of our
system who is involved and uh in this case all users are kind of on equal
footing uh we have uh anybody can send messages between peers on our Network we
don't really have any privileged actors if we were designing Uber we have writers and drivers if we were designing
YouTube we have creators and viewers but for WhatsApp all users are peers and so
we can leave it at that once I've got the actors I can work through my functional requirements and make sure
that I've got nouns that reflect all of the things that I need to do so the first thing that I need to do is set up
a chat and inside my chat I can send and receive messages now when I want to access
messages after I've been offline I think it's important to recognize that a
person isn't offline a device is offline I turned off my phone and now it's back
on but my laptop's been on the entire time and so I need an entity to reflect
my clients or maybe my devices so that way I can keep track of where have
message has been delivered I want to know that all of the messages have been delivered to my phone and my laptop
eventually I've got a pretty good set of entities here that cover my functional requirements so I'm going to keep moving
I'm not going to spend additional time here but I've given some good discussion that tells my interviewer I'm thinking
deeply about the nouns and the entities in my problem our next step in the delivery framework is for us to talk
about our API or system interface and before we go there we need to First
think about how we actually make connections between our app and the backend servers
API
on our website on hello interview we have some premium content one of those deep Dives as part of the premium
content is our real-time updates Deep dive where we talk a lot about connectivity and the various options for
making connections between clients and and servers and you've got a lot of
options here uh you can use long polling ssse we can use websockets or web RTC
one of the ways that we talk about how you can kind of Reason through whether
you're going to need to use one of these Technologies is based on a whether you are very latency sensitive if not you
should definitely use polling in this case we need to deliver all our messages in 500 milliseconds so that doesn't
apply the next thing is whether There Is frequent biral communication uh between
the client and the server in this case yeah messages can be coming back and forth uh for our chat app quite
frequently so we can't use ssse in this case because we also need to be able to
send messages quite rapidly the last consideration for us is whether we have peer-to-peer or need audio and video
support we don't actually need that for WhatsApp with the requirements that we're given so the natural conclusion
for us here is to use websockets I think in WhatsApp uh the the real app they're
just using a simple TLS connection they're not using the overhead of websockets but the same principle
applies here we need a persistent connection between the client and the server that we can Ferry messages back
and forth so a restful API for WhatsApp probably doesn't make as much sense
because it doesn't give us a way for us to send those messages back uh from server to client so now that we know
that we're going to be using websockets for the connection between client and server we can talk about what our API
looks like and this isn't going to be a tradition restful API there really is no standard for describing a websocket API
but I think an easy way to talk about this is commands that are being sent from the client to the server as well as
commands that are going to be received uh by the uh client from the the server
in terms of commands that are going to be sent well we can go back to our functional requirements to reason through this first of all we need a way
to create a chat we also need a way way to send a message we may need a way to create an
attachment we'll think about this as we go into our actual design how this might work and then we might need a way to
modify the participants that are existing in a chat maybe to add a user or remove a user we could clearly think
of lots of other functionalities but we're going to stop here to make sure that we cover our functional
requirements in terms of commands that are going to be received well we need to get a notification to our client
Whenever there is a new message we we need to be able to send and receive messages we also need to get updates
when new chats are created that I'm um added to or maybe when participants
change so that way I'll know that you know Sandra is no longer part of the group chat uh you know maybe she's on
the outs uh with our our social group now I can obviously go into detail about
the body and content of each of these but I'm not going to do that here in
part because the rest of the design is going to take a lot of time so what I'm going to do is I'm going to tell my
interviewer hey I think this is the rough scaffolding but I'm going to come back to this as I get more clarity on
the details it's very common in system design interviews to be somewhat
iterative and especially for the API and highle design there usually is a bit of
a back and forth and most interviewers understand that this is what what's going on so my recommendation is that
you tell them hey this is just the the start and I'm going to come back to this as we have time you may not have time
but at least they recognize that you know that this is a not not a complete
description the trick is you don't want to leave your interviewer in a Lurch so
what you don't want to do is make an obvious mistake or do something that looks Incorrect and then make it seem as
though you don't know that you've made a mistake what happens then is your interviewer stews on that they might
make a note in their um interview notes and the base assumption is that you
missed that even if you had it in the back of your head so communicating proactively about where you're going to
stop short or where you're making an obvious mistake is really important to making sure that you land that
High-Level Design
interview now that we've got our API we can move on to the next step we don't
have a data flow requirement here this isn't a particularly um data heavy infra
system so we can move straight into everyone's favorite the highle design I've actually moved the functional
requirements up here so that we can refer to them for the highle design our recommendation is that you actually work
through your functional requirements and try to satisfy them as simply as possible now it can be tempting to try
to jump ahead and build a highly optimized scalable system out of the gate we don't recommend that you do do
that for certain candidates who are very experienced go ahead skip a step if
you've got a staff level interview and you don't want to go through all of the basics I think that's completely
acceptable but for most candidates it can actually be useful for you to build the basic system and then progressively
and organically evolve why well two reasons one this is how systems are actually designed in the real world
people aren't just jumping to Optimal system they're organically evolving them over time and secondly it's very easy if
you try to jump to optimality to both leave gaps and holes but also to have
instances where you kind of lose track of where you are and what you needed to do if I'm getting lost in some scaling
consideration I may not build out all of my functional requirements and the system isn't working it's hard for my
interviewer to give me credit in those instances so get really good at banging
out a system that satisfies the base functional requirements and then layer on some of the scalability and
non-functional aspects of the system so with that in mind let's go ahead and start with our first functional
requirement to be able to start group chats for this I'm obviously going to
need a client and that client is going to make a connection to a chat server
I'm going to assume that this is a single node chat server I just have one instance and that's going to simplify
things dramatically and then create problems that I'm going to go ahead and solve later that chat server needs to
communicate with a database I will go ahead and use Dynamo DB here but we
could realistically use any key value store we could also use a relational
database I think a lot of people get hung up on relational databases thinking they don't scale I think Shopify just
released some of their numbers for Black Friday saying there my SQL instance was doing some number of millions of
transaction per second the idea that relational databases somehow can't satisfy these high scale situations is
is just simply not true although some interviewers might mistakenly perceive that to be the case in which case you
know go ahead and try to adapt for you know in some cases their their ignorance or or out ofd ideas about what's
possible in this case we'll go ahead and use Dynamo DB so our clients are going to make websocket connections to our
chat server and our chat server is going to connect to our database then our
client can send that create chat message to the chat server and then the chat server can create a record in our
database well what tables do we need in our database well first of all we need a
chat table uh that's going to be really important for us to be able to store metadata about the chat maybe we have
the ID uh the name of the chat potentially some additional metadata
that we might need and then we we also want to know who is in the chat so we'll
include a chat participant table and that will have a foreign key or a
reference to the uh chat ID as well as a participant ID now the interesting thing
about this is that when we create a chat we typically want to do two things one
is we want to be able to find all of the participants in a given chat and then
the next thing is we want to be able to find all the chats in which we are participant so for the first style of
query we can go ahead and use a composite primary key on this chat ID
that basically allows us to look up all of the participants given a chat ID we can uh use the participant ID as a sort
key for the latter query where we want to find all of the chats that I'm a participant on we can use a global
secondary index or GSI and basically this is a functionality in Dynamo that
allows us to create an index which enables these rapid lookups without having to organize our data in a
specific way and so with that Global secondary index we'll be able to query all of the chats that I'm a participant
of and that gives me a basic system that allows me to start group chats now that
we've got our chat set up we can start to think about how to send and receive messages this is a little bit easier in
this degenerate case where we have a single chat server I'll tell you why all of our clients are connecting to the
chat server via websockets so we might have a thousand connections for clients
to the chat server when we want to send a message the client will send a send
message request to the chat server with the chat ID that it wants to send it to
the chat server will then query the chat participant table to go and find all of the participant IDs that it needs to
send that message on on to now we need to go and send those messages back to
the client how can we do that well the nice thing is this this chat server maintains connection for all of the
clients that are currently connected so what we would do is we would have a simple hash table and it would say
client a is connected to websocket one and client B is connected to websocket
2 and now once we have all of the participant IDs we look up the the
client ID in that hashmap and then we find the associated websocket connection
and we send that new message command back to the client so that they can receive it so in this case we don't have
durability the messages aren't stored anywhere we can only send and receive messages to people that are currently
connected to the chat server but being able to have kind of a live chat room is
fairly straightforward and the messages get sent we look up the participants
based on the participants we find the associated websocket connections and we send them back to the client now that I
can send in receive messages let's talk about how I can send and receive media the idea here is pretty simple I have a
baby picture or a video of my kids and I want to send it to Grandma and the rest of the family how can I do that well the
most naive thing that we could probably do here is we could create an attachments table in Dynamo DB and then
what we could do is when users want to send those videos they could send a message in that existing websocket
channel to our chat server which can then write that data to our attachments
table in Dynamo DB then when we need to receive those messages we would load all
that data and send it back to the client this is broken for two reasons the first
reason is that Dynamo really isn't intended for large blob storage especially if you're talking about
videos which could be hundreds of of megabytes this is really not a good use case for Dynamo TB and the second thing
is we're using our already exhausted chat servers for this very intensive
high bandwidth use case of uploading media if you can imagine we've got this
disparity between these gigabyte payloads that are happening when I upload the video of my kids for Grandma
and then the OMW messages that I'm sending to other users to let them know I'm on my way to the movie theater and
that disparity is usually a sign that something is wrong so a lot of candidates will rightfully reach to a
blob storage here since we're already using AWS why don't we go ahead and use
S3 instead of having this attachments data what we can do is have our chat server write those binary blobs to blob
storage and we solved half the problem here S3 is made for multi-gigabyte payloads it has all the guarantees that
we need in terms of availability and then in terms of throughput we should be able to store things here but the
problem remains that we are still passing a lot of data through our chat server that really doesn't map to the
very small messages sent rapidly that we previously had been using the chat server for so a simple solution for this
is for us to use pre-signed URL so you might have heard these in some of our other designs and the idea is pretty
straightforward when our client want to make an upload it's going to make a request to the chat server to say give
me an upload Target or an upload URL the chat server is going to use its
authentication to go and ask S3 for an pre-signed URL which is basically a URL
that has embedded authentication usually with a TTL so it'll say you can upload
to this URL in the next hour the client will then make a direct request to that
blob storage and then upload load the media and then it will have a URL that's
addressable inside that blob storage uh that it can then send inside the message
that it was already sending so now instead of sending hey here is a message
that includes the entire video I'm going to send a message to that chat ID that
includes the URL to the payload that I've already updated finally when users need to receive the message they're
going to receive that URL and they're going to make a request back to that blob storage to go and grab that payload
uh and send it onto their client now there are some additional problems here we need to be able to expire this media
after it's been sent to all of its recipient maybe we only keep it around for 30 days uh we want to manage the
storage space so that users aren't unnecessarily uploading data to our S3
bucket so they're not using us like a Google Drive uh but generally speaking this pre-signed URL regime is going to
work quite well for our purposes and it allows us to reuse the existing messaging infrastructure that we set up
for our SE second uh functional requirement all right we're moving quickly here and uh we're on to our
fourth functional requirement this is where things are going to start to get a little bit more complicated because up until this point we've been assuming
that our transient connections to the chat server were sufficient for delivering messages but if I want to
access messages after I've been offline then I don't have that connection to the chat server that I can use to send those
messages so we're going to need to evolve this solution a bit so let's go ahead and give ourselves some space
first of all I need to be able to store my messages so I'm going to need a messages table let's just assume that
messages have an ID they' got some contents maybe they have a Creator ID or a sender ID and then a Tim stamp we'll
assume the chat server is the one responsible for the timestamp so we can keep it reasonably consistent so now
we've got the messages stored on our server but how do we assume or how do we ensure that they actually get to the end
user well one way to solve this is for us to create a separate inbox table and we'll have a recipient ID and we'll have
a message ID and the idea here is when messages need to be sent we'll create an
entry in the inbox for all of the recipients so what would the flow look like here well first of all when we want
to send a message a client goes to the chat server and says send message to a given chat ID here's the contents the
chat server is going to go and look up the chat participants so that way it knows who to send a message to so it's
going to make a query to the uh GSI for this table actually I don't think it needs to use the GSI it can use the
primary key then we're going to create a transaction to write to the messages and
inbox channel so the messages uh table will have one record which is the
message contents and its Tim stamp and then the inbox table we will create records for every participant in that
chat now note that Dynamo DB transactions support up to 100 records
so we need to make sure that our group chats are no larger than 100 participants so we can make this
transaction I guess 99 once we've created the recipients now we can try to
go and send messages to our clients in the chat server we maintain the map of
the client IDs to the currently connected webs sockets and then for each participant where we can address them
we're going to go ahead and send the message to that client now we want to
keep track of delivery we want to make sure that those messages actually got to the client so a natural thing for us to
do is when the client receives a message it's going to send an act or an acknowledgement back to the chat server
so when it receives a certain message ID the chat server is going to receive the app and then at that point the chat
server delete that entry from the inbox so that way we don't need to send it
again now when clients connect to the chat server for the first time the chat
server can then unload all of the messages in the inbox that the client
hasn't received we will go and look up all of the message IDs for that recipient ID and then for those message
IDs we'll grab their content and we will send messages to the client which will
will then act each of those messages and remove them from the inbox so what we're guaranteeing here is that messages will
be eventually delivered to clients that clients as long as they are periodically connecting to the chat server will
receive those messages and if they are already online on the chat server
they've got a websocket connection then we'll already be able to send the message over that pre-existing
Deep Dives
Channel all right so we finally got a design that satisfies follow of our functional requirements but it does so
in a degenerate way and we're going to be reminding our interviewer throughout this process that we understand that
this design doesn't scale that we know about the problems because we don't want them to jump to the conclusion that hey
this guy doesn't understand or this gal doesn't understand scaling the next step
for us is to jump into our deep Dives and this is the place where we're going to start to satisfy our non-functional
requirements deal with any questions that our interviewer might add on to the list they might throw additional
requirements and then constantly look for places where we can refine our design uh this is kind of an iterative
process where we're looking for issues resolving those issues and then moving forward so I'm going to go ahead and
delete our framework to leave space for our non-functional requirements which I'll drop on the screen now now despite
being a degenerate solution we're actually not off to a terrible start so first of all this non-functional
requirement of delivering with low latency is already satisfied ified when clients are connecting to our chat
server they're going to send messages we'll write those messages to the database but since we already have all
the websocket connections we can deliver those messages immediately for anybody who's currently connected so that one is
satisfied we can also guarantee delivery of messages because we're writing them on the server side to our database so we
write the messages to this uh messages table into the inbox clients are going
to get those messages if they're connected and if they're not not then when they connect again to our server we
can go and find all the messages that haven't been delivered and deliver them great but the next requirement is really
going to throw us for a loop in terms of billions of users we're probably not going to satisfy those with a single
chat server and we really wouldn't want to because of the availability problems WhatsApp famously served 2 million users
per server 2 million connections per server which is actually pretty high and they're right to be proud of that I I
think you could probably get those numbers even higher on Modern Hardware but still as an order of magnitude we're
going to have to have hundreds if not maybe a thousand chat servers in order to support the operations that we have
here so to get to a th000 chat servers we're going to have to make some changes me rearrange this diagram a
bit so first visually let's include some additional chat servers when the clients
are trying to connect to our chat servers they need to know which one to go to the natural thing to do here is
insert a load balancer but we'll note that the load
balancer here needs to be a little bit different with a web server our web
servers are stateless and what that means is that the load balancer can basically terminate requests at the at
the layer seven at the HTTP level and then forward those requests to an
arbitrary server so if I get an HTTP request to a layer 7 load balancer I can
forward that HTTP request to any of my stateless web servers get the response
and return it back to my client it doesn't need to go to a specific server but with websockets it's a connection
oriented protocol and so I need to retain the connection between client and
server and as such I need a different style of load balancer this this is known as a layer 4 load balancer and the
way that it works is when a client connects to the load balancer it creates a TCP connection it's going to go and
send messages over that TCP connection and the load balancer is going to create a symmetric connection to my chat
servers so whenever the client creates a new connection a new connection is created and when the client disconnects
the load balancer also disconnects and what this is going to do is effectively it's going to make this load balancer
invisible to my chat servers it's as if the client was connecting directly to a
chat server now the load balancer can decide which connections are made to
which servers and the most natural way to do this for this setup is to use the
lease connections so when the client connects to the load balancer it's going to
choose the chat server that currently has the least open connections the load balancer knows how many connections it's
already made and it's going to choose the one with the least and the reason this is useful is because the chat
server's primary resource the thing that it's consuming is that connection now we can go up to 2 million connections but
probably not larger and what this allows us to do is when we scale we add new chat servers into the rotation those
will be saturated quickly because the load balancer will recognize that this new server has zero or one connections
whereas my other chat server has millions I'm going to start to Route inbound connections to that chat server
until it's approximately equal with others Now setting it up like this does
give us that horizontal scalability but it doesn't actually solve our problem in fact it makes this first requirement
break let's talk a little bit about what that looks like so the client connects to the load balancer to the chat server
they want to send a message they send a message uh they are user a and they want to send a message to user B so normally
what we do is the chat server looks up all the participants it would find user b as the participant in whatever chat
that we were talking about it would write the message into the messages and inbox and then it would look at its
local websocket connections and try to pass the message back down via the
websocket that the other user is connected through but we have a problem here user a might be connected to chat
server one and user B might be connected to chat server 2 so so user a isn't able
to send that message to the websocket that user B is connected through because
they're connected to completely different servers so fundamentally we have a routing problem here we need our
chat servers to be able to talk to one another to pass messages so that they eventually arrive at the clients that we
care about like all good system design problems there are a bunch of ways that we can potentially solve this the thing
that I think a lot of candidates grab gravitate toward is to try to use kofka here and the idea would be we're going
to set up C kofka topics for each user when clients connect to a chat server
we're going to subscribe to the topic for that user and then when we want to send a message to a user we'll write to
the kofka topic for that user and so the idea would be if I need to send a message to a chat I'll look up all the
participants I'll write to those kofka topics and then these chat servers will be reading from those topics and they
will grab the message and then send it to the associated websocket connection back to the client now unfortunately
this isn't a very good solution in part because kofka really isn't architected for billions of topics another problem
is that kofka topics are really heavy they're somewhere between 50 and 100 kilobytes per topic which when we talk
about billions of users is terabytes of data just to get the setup for both the
part partitions and the topics finally kovat doesn't really support this rapid
connect and disconnect for many topics it's not built for these very shortlived
small topics micro topics that we're trying to set up here so ultimately kfka
probably not the best solution a better option for us is to use a consistent
hash ring and the idea here is if we can predictably know that a specific user is
always going to be owned or connected to a specific server then whenever we need
to send messages to that user we can just send them to that server and know that it can pass them along so how might
this work well first of all we'll dump our load balancer and expose our chat servers to the web via DNS that way
clients can connect directly to a chat server but they may not know which chat server to connect to so let's go
introduce a chat registry and the idea with this chat registry is it's just a
way for clients to find out which chat server they need to connect to and then finally we're going to need some way to
store our configuration we can use zookeeper or uh
ETD but any storage that we can sync of between all of the nodes uh in our
cluster so that they can be aware of where a particular user is
assigned and so the steps now to send a message when a client first wants to
connect they're going to go to the chat registry and say I'm user a uh tell me which server and the chat registry might
say you're connected to server one now when they want to send a message to user
B they're going to write their message to server one which they're connected to
they're going to do the same set of processes to write their message and create it in the Inbox and now that they
know that they want to send a message to user B they're going to use the information that's in Zookeeper to find
out which chat server user B might be connected to and then make a direct connection the chat servers are going to
write to one another so uh server one is going to write to if B is assigned the
server to a message that says I've got a new message for user B and and then
server 2 is going to check its internal hashmap to see if user B is indeed
connected uh to the server and if it is it's going to pass that message through so we've got two hops instead of just
going through that singular server now this isn't without its problems the the biggest issue with this consistent hash
approach is scaling becomes a bit of a an orchestration so imagine we have four
servers and we want to move to five the consistent hashing approach is going
to guarantee that most of those users are going to stay on their existing host but some of the users on the edge about
20% are going to get moved to a different host the way that that typically happens is we signal into
zookeeper or into etcd that this event is happening and then chat servers are
going to slowly disconnect the users who are misassigned if user a is connected
to server one and it needs to moveed to two we'll disconnect them the client will reconnect via the registry and then
they'll be connected to server two we need to do this slowly so that a lot of connections and disconnections aren't
happening simultaneously and while this scaling event is happening when we want to send
a message to user B who might be on server two or might be on server three
depending upon where we're at in the process we may need to send messages to both of the servers so that that we can
eventually get that message to user B which is both additional overhead and stress on our service but also this
additional orchestration that we need to run now your interviewer may or may not
require you to go into that detail but it's important to understand what is actually happening during scaling events
for a consistently hash Service uh in order to make this work now while the
consistent hash approach is good it does force us to contend with this orchestration problem for scaling and
there is potential that chat servers might get hot that the connections on
one chat server uh might be more than on other chat servers we basically have uneven load so the idea behind the kofka
instance where we had kind of externalized that inter server communication was good in spite of the
fact that from a technical perspective kofka is probably not the right technology to imp mement this so can we
get a bit of both well yes I I think we can and the solution here that I think
is a pretty good one is to use redis pubsub the way that redis pubsub works
is you tell redus I would like to listen to a particular topic which is a string
uh redis creates an internal hashmap much like our chat servers do and then
when you publish messages to that topic um reddis will look up in that hashmap
which sockets are listening on that topic and then pass them the message it is a very dumb uh socket server in some
sense and the guarantees of reddis pubsub are pretty low what redis pubsub
offers is at most once delivery of messages which is to say I might deliver
it or I might not um that would normally be pretty bad except for the fact that
we do already have ways to guarantee the delivery of our messages remember that we're writing them to our durable
storage when clients connect they're able to retrieve any messages that
haven't been received yet we can even have our clients periodically PLL or
receive some other notification that there might be messages that are waiting for them and that they need to go and
get them so we have a way to deliver those messages in a reliable way redis
pubsub gives us a really lightweight way of having the real time or under 500 MC
delivery of messages so what does that look like well when our users connect to
a chat server they can connect to anyone will use the leas connections that chat
server will register a subscription to redis pubsub for that particular user ID
and then when we send a message and we get to that point where we we want to go and notify all of the connected users
that a message is waiting the chat servers will then publish a notification
to that topic given the user ID and reddis will pass that over to the server
that's responsible for that user ID and then that server will pass that over the web socket that's also associated with
that particular user ID so fundamentally we have a way of bouncing through redus
to get to the right server and get the messages uh to the right client now this isn't Panacea and
fundamentally we have many of the same problems that we had with the consistent hashing approach in that if for some
reason we need to scale the reddis cluster then we have to go through the same orchestration problem of moving
topics and moving connections you have to understand for redis what we basically have is the
topics are going to be spread amongst nodes in the cluster and so each chat
server is going to need to maintain a connection to each of the nodes of the redus cluster now fortunately this redus
cluster isn't doing much it it really doesn't have much responsibility aside from basically echoing requests across
sockets and so we don't need a giant cluster to be able to support the throughput that we have but we are going
to require an n * m number of connections here which if the system
were to scale to trillions of of accounts might become a problem for us
so now that we've satisfied billions of users we've got one more requirement of messages not being stored
unnecessarily this gives us a bit of time the idea for WhatsApp is that after 30 days uh if you haven't received your
message you aren't going to get it and uh like I mentioned in the beginning we
don't want to keep messages around that we don't need to they end up being a privacy liability which for meta is
incredibly important and very expensive when they get wrong so what we can do is add a cleanup service which is going to
do this work our messages table remember has a timestamp so if we add a secondary
index on that Tim stamp we can go find all the messages that are older than 30 days and we can delete them the inbox
remember is going to have a record for every undelivered message and it's going
to be deleted as soon as the clients receive it if we add an addition timestamp field here then we can use the
same sort of cleanup process when messages are received by all clients we may also want to delete
the message here so when we are about to go and delete from the inbox we can
check to see if that is the last message in the Inbox and if so we can remove the
message there may be some race conditions here but remember we've got these guard rails of 30 days so even if
we might miss a message we're not going to miss miss it for long uh it's going to disappear now this gives us a chance
to really estimate the storage requirement of the system and if we assume we've got a billion users and
they do 100 messages per day then we're going to have a 100
billion messages per day if each of those messages is capped
let's just assume that the contents can be no long no larger than a kilobyte then we're going to have a kilobyte per
message so we have 100 billion kilobytes or 100 trillion
bytes and if you recall Mega is a million Giga is a billion Terra is
trillion so this is uh 100 terabytes that's per day and we'd
multiply that by 30 days if we assume that all message me we're going to wait
indefinitely but the reality is most messages are going to get delivered immediately and get removed by our other
process so our database is going to need on the order of a few hundred terabytes
this is a lot of of data but not a a unheard of amount and certainly
achievable by modern systems our interviewer might ask us a few
extensions to this problem so one extension would be be to allow users to
have multiple devices how does our design need to change now all of our tables currently
are keyed off the idea that the recipient is a user ID that basically a
user would get one message there's kind of a onetoone relationship but if they might have
multiple devices then we're going to need to add a new notion and what we can
do is add a client with a user ID and then maybe a
client ID now we need to go and update our design such that everything we are
referring to a user we need to refer to the client so our inbox for instance
would have a recipient client ID and our Pub subtopics would now be
clients now when a client wants to send a message they're going to look up all
of the participants and then for each participant we're going to look up all of their clients and then send messages
to each of them now this would greatly increase the number of rows that you
would need to insert into the inbox table in the instance where for instance
you've got a hundred people and they've got five devices each so we would
probably want to put some limits on the number of active clients that a user could have maybe they can have two or
three devices and then we would need to go and percolate that restriction through to the group size to make sure
that we're not running a foul of that Dynamo DB transaction limit where we can only insert a 100 records at a time a
final extension that you might get asked is about presence indicators or whether
someone is available and the idea for this is you open up your app and you see
your contact list and you'd like to see little green orbs next to those people who are online and then maybe no orb or
a Red Orb for those people who aren't this requires some product design we
really need to specify the requirements of the feature because we need to know which users care about the presence of
other users you could do this in a very simple polling fashion by keeping a
table which has whether a user is connected or not and then querying that
that table whenever you want to see whether that user is currently active
and so what this would look like is when a connection is established to the chat server it would write to a new table
maybe this is available user ID and status and then
when a connection happened it would write a status of available and then when you disconnected when the websocket
connection was terminated then that status would be set to unavailable now
in a lot of cases people want to get notifications about when that's happening if you had the screen open
you'd want to see things that are changing and we would probably use the existing Pub sub infrastructure for this
so we would need some way for users to indicate their interest in the
availability of a particular user they would have to subscribe to that somehow
and then whenever those disconnect events happened we would publish to that topic and then pass those events down to
the clients that are concerned with it a big challenge here is deciding which users I care about watching because
there's obviously some immense fan out that could happen here what we probably don't want is when a user to get
disconnected for us to have to send out thousands or tens of thousands of notifications so we need to figure out
how we can constrain the number of users who can be watching a particular user at
a certain time but those would be the types of things that you might go into uh with additional time in this
interview okay so we touched on a lot of information in this problem you might be
Conclusion
asking yourself all right how much of this do I actually need to know for an interview and this of course is going to
vary depending upon how grumpy your interviewer is and the companies that you're you're interviewing for but
generally speaking for midlevel candidates the expectation is that you're relatively new to system design
and so we we touch on things like webs socket management consistent hashing and
Pub sub database design the expectation is that you're not going to be particularly deep in any of these areas
now you should be roughly familiar and being able to call out various uh challenges that you're going to run into
is definitely a bonus but the interviewer is not expecting you to come up with a perfect design out of the gate
for more senior candidates they are expecting you are going to be familiar with all of these Core Concepts that you
have an idea about how load balance ERS work and how websockets work and you have an idea about how consistent
hashing might enable scaling of stateful services you are going to make mistakes
everybody does your interviewer isn't expecting any specialist knowledge but they're going to expect that you do a
pretty good job in putting together a system that scales and satisfies the requirements for a staff level candidate
you're going to really zoom in on the interesting parts of this problem so your interviewer wants to see that you
really understand that the statefulness of these chat servers is pretty interesting and that the data model is
in service of really rapid querying and then also very fast rights to be able to
support the throughput that we're talking about and so what they want to see from you is that you're able to zoom
in on the hard or important parts of the problem and then generalize your knowledge and your experience to be able
to come up with solutions that are going to work for a particular instance it's not the case that staff level candidates
are like senior candidates but just even better they're going to focus on qualitatively different pieces but
they're also going to be able to bring in a much larger toolkit of approaches
and experience that their interviewer is going to be able to see Managers
generally speaking are usually held to about a senior level uh of standard
across most companies there are some exceptions to this where managers are held to a staff level uh standard uh but
they are very much the exception rather than the rule that's usually not the case anyway I hope that this breakdown
was useful for you um we have the writeup available on our website so if
you've got questions feel free to comment below or comment on our guide which walks into some of these things in
Greater detail and then highly encourage if you've got questions around ssse or
websockets or about consistent hashing to read up on their realtime updates Deep dive which goes into a lot more
detail and spells out some of these Concepts um so that you're able to use them in an interview thanks for spending
time with us uh love your your likes and subscription uh if you found value here
and otherwise until next time I'll talk to you later
