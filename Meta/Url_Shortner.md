Intro
hello everyone welcome back to the channel uh I'm Evan co-founder of hello interview and a former meta staff
engineer and today I actually wanted to take a step back and make a more beginner friendly video for you all
today so many of you have seen our system design video breakdowns uh we're going to do a new one of those today and
it's going to be for the classic question design a URL shortener which is everybody's first system design question
and in this video as I mentioned I'm going to slow things down a bit I'm going to teach Concepts that we otherwise take for granted in some of
our other videos so if you're new to system design or you're dusting off the cot webs this is the place to start uh
if you like our content you want more of it please make sure that you like and subscribe uh the increasing number of
subscribers is really motivating to us it makes us want to create more content for you so make sure you smash those
buttons if you haven't already lastly if videos aren't your thing I've linked the written resources in the description as
well so if you don't want to watch this whole video you can just come here and read the written form there's also tons
of other common problem break Downs over a dozen now on the left hand side you can also try all of these yourself with
guided practice and so guided practice is a tool that quickly just lets you walk through designing systems on your
own and then you get this personalized feedback for each step along the process this feedback was tuned by myself and my
co-founder Stefan so give that a go and then the last thing here is that if you're looking uh or if you're preparing
for interviews the best thing that you can do is mock interviews and that's our specialty here at hello interview so
come on over do a mock interview with a senior plus engineer manager from your target company and they'll tell you
exactly where your gaps are and how you can improve all right let's get into
The Approach
it before we start designing our URL shortener let me take a brief moment to just explain the framework or the steps
that we're going to follow both in this interview and this is also the framework or steps that I suggest you follow for
any of your system design interviews so the first thing that we're going to do is we're going to Define the requirements of our system this is both
the functional requirements or the core features as well as the non-functional requirements or the qualities of the
system things like scale durability fault tolerance after we do that we'll Define
or outline the core entities this is really simple highlevel list of the core
entities that are going to be persisted and exchanged in our system another way to think of this is like the names of
the tables or collections that you would have in your data model once we do that we're going to move on to the API this
is the user facing API it's the contract between your client and your users and your backend service from here we're
going to skip data flow this is only applicable to infra heavy system design questions so like designer rate limiter
design a message CU stuff like that so not applicable to a user facing product like a URL shortener so instead we're
going to go right to high Lev Design This is where we're going to head to the Whiteboard we're going to start drawing boxes in arrows in order to outline a
system where the primary goal is to satisfy the functional requirements ments that we outlined in one and so at
this point our system is going to be really simple it's not going to be able to scale it's not going to be able to do anything too fancy it's just going to be
able to satisfy those core features that we outlined but from there we're going to move on to our deep Dives where
things are going to get fun and we're going to go one by one through those non-functional requirements in order to
evolve our highle design in a way such that it ends up satisfying each of those non-functional requirements and at the
end we're going to have a system that satisfies all of our functional requirements and all of our non-functional requirements and we're
going to feel really good like we pass the
Requirements
interview as promised we're going to start our design with the requirements of the system and so the first thing that we do
is we start with the functional requirements the functional requirements are the core features of the system this
is where you're going to try to identify the top two to three features that are necessary and that you will have time to
design in your 35 to 45 minute interview now if you were told to design a system
that you already know well then this should be pretty easy but you might also be asked to design a system that you've maybe never heard of in this case you're
going to want to ask a lot of questions this is the time where you would pepper your interviewer with questions in order to better understand the system that
you're required to build in our case what is a URL shortener well a URL shortener is a service that converts
long URLs into short ones and then those short URLs will redirect you to the original URL so you can take this long
URL give it to the URL shortener it returns this Returns the short thing you can put the short thing in your browser
and it's going to redirect you here pretty simple so in our case functional
requirements can always be thought of as like these users should be able to users can you know users will statements and
so what are ours well that first one is that users can create a short URL from a
long URL or an original URL perfect that's our first thing what's the second thing well users can be read directed to
the original URL from the short URL easy right those are the two core
features of a URL shortener now I'm going to add a little bit of flavor that's often added in these questions and that I'll uh have candidates address
if I'm conducting this interview and that's that I want to optionally support a custom Alias and so this is that users
could come to us with their own short Alias maybe instead of us generating this random thing they give us for
example Evan and then their short URL becomes SL Evan assuming it doesn't already exist so we'll support that
optionally if they want to provide it we'll also optionally support an expiration time and so maybe somebody's
creating a short URL for a conference or something and they only want it to be valid for the week then we'll expire it
after that week if they give us that expiration time this means that if somebody tries to navigate to that short URL after the expiration they'll just
get an error or something telling them that it's already expired so these are the core functional requirements of the
system um the next thing that you would do is that you would go into the nonfunctional
what we refer to as the non-functional requirements of the system now the non-functional requirements are instead
of being features and like they are the qualities of the system and so the
quality of the system are all of those words you've heard these are like these Iles these ilities words these things like the scalability the latency the
durability security fault tolerance is your system compliant this is where you talk about cap their
all of those things what qualities does the system need to uphold in order to ensure a good user experience and that
we're meeting user expectations and so what you typically want to do when you get to non-functional requirements and and
these are hard often times especially for more Junior candidates to think of is that you should go one by one through
those Illy statements maybe you have a list of them um kind of readily on your on your table as you're going into the
interview and you think about which one of them are uniquely interesting and relevant to this system
and so for example the first one that we could look at is latency how is latency important in our system well it's really
important that that redirection is low latency and so one system requirement and these are instead of user should be
able to this is the system should be statements so the system should be low
latency on redirects so if we give it a short URL
we should automatically go to that original URL so not only did did we choose the non-functional requirement
but we put it in the context of our system it's not just low latency it's specifically low latency on
redirects and we want to quantify it too we're going to say about 200 milliseconds 200 milliseconds is a good
number here because it's what is uh the humans perceive as real time so anything
under 200 milliseconds you wouldn't even notice the difference uh 200 milliseconds is like this snap of a finger it's real time so it's a good
lower Bound for us here so we have one non-functional requirement lower latency low latency on
redirects another thing that we can think about is the scale of the system and this is a time when I would ask my
interviewer I would say how large of a system are we designing how many users what's the scale of this system and they
might tell you to estimate it uh or they might just give you kind of a sense of what the scale is I typically would do
the latter and I would tell a candidate that they should expect 100 million daily active users and around 1 billion
URLs that gets shortened kind of in totality over over over over all time and so that would turn into a functional
requirement of the system should be able to scale to support to support 100
million daily active users and 1 billion URLs fantastic
making good progress on the non-functional requirements another one that's interesting here which is a little bit
handwavy whether it fits in non-function requirements but I want to call it out because of how important it is it's that
each of these short URLs or each of these short codes they need to be unique so the system needs to ensure sure
uniqueness of short codes these short codes are these kind of things that we're pending to the end of the URL
right we need to ensure uniqueness of short codes so that there's no collisions so that people don't end up getting redirected to a site they
weren't expecting to go to so those always need to be unique that's definitely going to be a core system
requirement and then the last one here that I'm going to do which typically you might do first but it's always going to
be considered and that's cap theorem so really quickly what is Cap theorem well cap theorem is a theorem that states
that from um when considering consistency availability and partition tolerance you can only ever have two of
those three things now partition tolerance in distributed systems like we're almost always designing in system
design interviews this is a guarantee you have to have partition tolerance because you're going to have partitions
you're going to have different instances for example of your database you're going to horizontally scale your servers
and so the decision really becomes is it consistency or availability does my
system need strong consistency or does my system need High availability and
what I want you to think about as you're in an interview is do I need strong read
after write consistency the way to think about this is does every single read of my system
have to read the latest right or else the system breaks or fails in some way
so common examples of systems that need this read after write strong consistency are like a banking application or a
ticket booking system the the example being in the ticket booking system case if somebody went and booked the last ticket to the
Taylor Swift concert in Germany and then I in America went to book that same ticket and I went and read the database
and it told me it was still available because I didn't have strong read after write consistency I would book that ticket and now we would both show up and
we would be fighting for the same seed that would be bad this would be like a fatal error to our system we we can't
have that same to in a banking app somebody else trades a stock especially if it's a low float I no matter where I
am in the world need to know that that stock was traded because it might impact the price before I buy or sell respectively
right um in the case of a URL shorten or do we need that strong read after write consistency well you can imagine that
somebody gives us a long URL we shorten it we give them the short URL back does anybody who then hits that short URL
immediately need to be able to be redirected we could say no and the
reason we could say no is because first of all there's some time that it takes for a user to share a short URL with
other users and for to start being used and that gives us time to be eventually consistent if for some reason somebody
was wicked quick a there are ways that we can handle that by making sure they're redirected to that same original node but B if they didn't get redirected
in that first couple seconds up to even a minute who cares right like we can show them a little error that just says
like we're still saving this in the system try again in a minute and no big deal things would the world wouldn't end
two people wouldn't show up to the Taylor Swift show fighting for the same seat right so because that's the case
because we we don't need strong consistency we're instead going to go for availability and so we're going to say high
availability uh and we don't need strong consistency wow I don't know how to spell that we don't need strong consistency instead uh we can handle
eventual consistency so event eventual eventual
consistency for URL shortening right
cool okay um so that's our non-functional require the last thing that I'm going to say here is that many
guides will instruct you at this point into go to back of the envelope estimations so you come in here you do back of the envelope estimations you
would end up talking about things like scale estimations latency estimations like total storage estimations whatever
this is fine you can do it but I'm going to suggest that it's useless um estimations and calculations
while doing system design is very important but doing it upfront like this
I find as an interviewer is almost always useless candidates will do some basic math About Storage latency Etc and
then they'll look at me and they'll go okay yeah so it's going to be a big distributed system and it's like we kind of knew that already didn't we there was
100 million daily active users and a billion URLs you're not you're not telling them anything new and you're not going to change your design based on
that information you are always going to do a distributed system and so what I argue is that doing
math for the sake of doing math is not useful instead you should tell your interviewer I'd rather not do math up
front and I'm going to do it during my high level design or my deep Dives if I need it to make a decision and so the
key here is that you're going to do calculations when the result of those calculations will directly inform a
direction or decision that you're going to take in your design and doing it up front like this in my experience does
not satisfy that next up we go into the core
API & Core Entities
entities of the system now the core entities as I mentioned these can be thought of as basically the tables that
you're going to have in your database this is the entities that your system is persisting storing in the database and
exchanging via the apis right and so core entities as I suggest as we
suggested hello interview you start by just listing off these entities don't worry about the full data model yet
you're going to get into that later I would communicate this proactively with your interviewer I would say I'm not going to do the full data model just yet
instead I'm going to list off these core entities and as I get into my high level design I'll be more explicit about the fields or columns for each of them
but in our case what do we know that we have we have an original URL we have a short URL and then like we have a user
who creates them these are the entities in our system pretty straightforward and the reality is that this system is so
simple that you could outline the data model here if you wanted to you probably know it at this point the reason that we
don't yet is because for more complicated systems it's often times too early and we haven't had a chance to
think through our API and all of the requirements that that would have us understand what the full data model
would be but in this case it might be fine I'm going to go with this and and uh this is a good enough core entities
for now which takes us then to our API the API is where again we Define that
contract between our client or our users and our system and the way that I
suggest you go after the API is very methodically you're just going to come up here to your functional requirements
and in most cases it's a one toone mapping between a functional requirement and an API not always sometimes you have
like two or three API endpoints for each requirements or maybe uh you don't even have an API endpoint for a requirement
but you should come up to this list and you should say the first thing I need to do is users should be able to create a short URL from a long URL okay let me
make sure that I have an API that supports that so in doing so the first API that we need is to be able to
shorten a URL and so this can be a post Endo to some URLs resource and it's
going to return a short URL we're just going to reference here our core entity
right it's going to return a short URL and the body here is going to be what
namely it'll have that original URL again referencing that core entity uh it could have that optional custom Alias
I'm going to use question mark in order to uh indicate the optionality there and
then we can also have optionally that expiration time so that expiration time right and so there's our first URL our
first API endpoint which is going to allow us to take an original URL and return a short
URL uh when you're doing these system design interviews you often times will use rest apis though not always uh when
you are using rest apis a couple things to think about you want to make sure that you get your verb correct here you
have post put patch get delete Etc most often you're just going to use post when
you're creating a new resource put or patch when you're updating a resource delete of course if you're deleting a
resource and then get if you are quite obviously getting or fetching a resource
so make sure you have those down and then when it comes to these paths you you typically are going for a plural
noun and so to be honest with you as an interviewer I don't care about all of this I think this is like kind of silly
semantics that are easy to to change figure out they're not the most interesting part of any design but
especially at the lower levels you'll have like what I'll call restful API zealots interviewers who really care
about this and so I just want you to be aware and considering things appropriately okay so that's that first
API endpoint right we just satisfied that first functional requirement the second one is user should be able to be
redirected to the original URL from the short code okay so we need to handle an API endpoint for redirection and so how
is this going to work well we're going to have some get endpoint and it's going to go to slash like our short code or to
use our uh our core entities it's just going to go to our short URL and then it's going to return
a redirect to our original URL right so that's pretty straightforward
now in case this isn't obvious the way that these systems work of course is that when you run this git and we'll get
into this in a in a moment when you run this git you're hitting our server the server that we own our URL shortener
with that short URL and that short code uh and then we can take that code figure out what we need to do with it we'll get
into that later and then and then issue the redirection but that's how this ends up working so here are our API endpoints
super simple we double check we have an API endpoint for each of our functional requirements these fully satisfy those
requirements we feel like we're in a good spot and we're ready to move on to the next
High Level Design
section so at this point we've done all the setup work we have a really clear understanding of the system that we need
to design we know the core entities that are persisted and exchanged and we've defined our contract with our back end
between our client and our server and so the next step is to come over here and do our highle Design This is where
things are more fun we get to go to the Wi board we get to draw and our primary goal again is to just satisfy these core
functional requirements so we're not going to worry about scale or meeting latency or uring uniqueness or availability or any of these things yet
we're going to do that later we're just going to get a simple design down that works and by following this framework our mind is just working linearly so
that even if we've uh if we're g excuse me if we're given a problem that we haven't seen before we can just build
the design up step by step by step okay so when it comes to the high level design here's how I recommend you do it
you come over to each of the apis and you start with the API and you draw out the system that's necessary in order to
satisfy that API this is equivalent to going step by step through each of the functional requirements as your note but
by doing it uh for the for the apis you can be really clear about the data flow and about what needs uh to be the input
and the output of each request and how the system of transforms those appropriately if you will so let's come
over here and let's let's draw this out I'm going to start simple and I I have a given client this client here is just
maybe like the website right pretty simple um and then I also have a primary
server so this is going to be the primary compute resource in my back
end and then I'm also going to add a database I'm going to add a database and
so this is a very classic design pattern just a client server database
relationship the client is going to make a request to your backend server your back in server or your server is going
to do something persist it in your database and then return it back to a client and so in our case what we're
considering right now is what happens when a user tries to shorten a URL they're going to make a post request to/
URLs and then we're going to return to them a short URL well how are we going to do that we're going to do that
because they're going to make that API request here that API request is going to be you know get short
URL it's going to hit our primary server our Prim primary server is going to have some magic black box that creates short
URL we'll talk about how it does that later we'll stay abstract for now so it's going to generate that short code
and then it's going to come over here and it's going to save it to the database I'll make that a two-way Arrow this one should be
too cool so it's going to come over here it's going to save it to our database and then return it back to the client
well what is it saving to our database well we probably now Define some data models instead of having separate
entities or separate table for the short URL and the long URL which we could do I'm instead going to combine them in
this case into one because of how simple it is and this is going to make more sense so I'm going to have a URL table
and this URL table is going to have the short URL and it's going to have the long or original URL it's probably going
to have the creation time and the user ID a forwarding key to the user that ended up creating this and then
subsequently I'm going to have a user with a user ID I'm not going to outline anything more of course a you user table
will have a uh an email a password hash uh salt all of these different things
who cares I see so many candidates get distracted by those things in an interview we're focus on the core functionality here all of that is
auxiliary and so maybe I just do this you know of course all the additional metadata cool and so we take a look at
that first API endpoint that we had post to URLs return a short URL here's how it's going to work the client is going
to post to our primary server it'll create a short URL it'll store that in the database as a mapping between the
short the long UR URL at the creation time and with the user ID and it'll return that short URL back to the client
easy we got it first one down now the second one is that the user needs to get
that short URL and be redirected to the original URL and so how are we going to do that well now we have an additional
thing here we have this like uh you know redirect which takes in the short this
one took in the long and so that's going to come from our client it's going to hit our par Ary
server our primary server is going to look up long from short all right so
it's going to go over to our database it's going to query it based on that short URL I'm probably going to want to
make that our primary key it's going to query based on the short URL and then it's going to return the long URL back
to the user and it's going to return this back to the user with importantly a
302 redirect and so a 302 redirect is just
the http status code which tells the browser I want you to take this URL and
automatically navigate to it I want you to automatically navigate to this URL
and when it comes to redirects we have two options we have a 302 redirect and
we have a 301 redirect these are both different https status codes and so in
the case of a 301 redirect this is a permanent redirect and what it basically
means is that the C uh the your clients your browser DNS servers potentially
they can cash this redirect and in the future they might not even need to go to your service they're just going to
redirect it immediately based on the cach in the 302 case this is temporary
and so it's never going to be cashed they're always going to come to us first we're going to look it up and then we're
going to send it back and so there's a conversation that you would have with your interviewer at this point potentially about whether 302 or 301
makes more sense now it depends on your requirements I suppose in our case we
don't care about analytics which is what would make the 302 the right answer here because in the case where you have
analytics you can show users how often their short URL is being queried um you
would want to make sure that it always comes to your server because then you can log and you have an understanding that this redirect was was requested in
the 301 case you're not going to get that you're not going to be afforded that ability it's not going to hit your server so you're not going to be able to
log anything for future analytics now this per redirect would be better if we were worried about compute cost if we
were worried potentially about not having to scale this server in the future then uh by having it be permanent
it's handled by caches elsewhere and may never even hit our backend service in the first place that's pretty nice and
so there's pros and cons here typically speaking you want to go with the 302 even the cost to uh you know how many
servers you may need because it allows you to understand if things are working
even if you're not showing users analytics even if that's not a core requirement you would be tracking that
internally as a as a platform as a product and if you saw things drop off a cliff there well you would know
something broke probably broke on the client and we're not getting these requests anymore and so by making it a 301 you lose that visibility and this is
the argument that I would make in an interview uh and why I would decide on a 302 redirect here and so the server will
respond with a 302 redirect with the uh original URL and the client will then navigate that original URL and they'll
be viewing that original website awesome so super simple we went through each of
our apis we now have a really high level design that satisfies both of our core
functional requirements I suppose with that being said as I just went back here and checked as you should do too I noted
that we actually didn't discuss two parts of that functional requirement and that's the custom Alias the expiration so let me come back and amend
appropriately uh we're going to add here you know that short URL slash custom
Alias this could be either of those things if they provided a custom Alias and then we're also going to add that
optional expiration time so an expiration time here and so now what a
user would do if they gave us a short uh if they wanted to get a short URL and they gave us a long URL and then they also gave us a custom Alias we would
need to First Look up in the database does that custom Alias already exist if no add a new row where the short URL is
the custom Alias and return that back to the user easy and then in the case of expiration time being provided we'll
make sure that we add it here and then on the redirect call when we come to look up our long URL based on the short
URL we'll also check the expiration time is the current time greater than the expiration time if so return an error
instead of a 302 redirect okay with that being said now we have a highle design that satisfies
each of our functional requirements and it's time to go deep in order to expand this design to support each of our
non-functional requirements so as we move on to the Deep Dives we're
Deep Dives
going to come over to our non-functional requirements and we're just going to go one by one through them evolving the simple highle design such that it meets
each of these non-functional requirements as well as the functional requirements that are already satisfies and now if you all will allow
me I'm actually going to take some Liberties here and I'm going to start off with the third one Ure uniqueness of short codes and the reason I'm going to
start off with that one is because you'll realize that in our highle design we intentionally overlooked kind of the
core of this problem we black booxed this create a short URL that's the hard
part that's the interesting part of a URL shortener and we just handwaved it now we did that intentionally the reason
we did it intentionally is that a common mistake I see candidates make is that they go too deep On Any Given part of
the design too early and then all of a sudden time runs out and they didn't even get a chance to satisfy all of the
functional requirements that features their system this is a mistake and so you want to remain pretty high level
make sure that you have the base down make sure you satisfy those functional requirements and then come back and go deeper and that's exactly what we're
doing here so I would have told my interviewer I would have said to my interviewer I'm blackboxing this for now but I'm going to come back to it and now
let's do exactly that so what do we need we need two things when it comes to creating a short URL well maybe we need
a couple of things we need the creation to be fast that's reasonable we need it to be unique and we need it to be short
those are the three things that we care about how short well we could ask our interviewer or we could guess but
typically we're talking in like this 5 to 7ish character range right so 5 to
seven characters maybe is short enough and so let's talk about some options
that we have here and in interview you do do exactly this you'd kind of work your way up building from the most
simple solution to something more complex certainly if time allows so the first thing that we could do is that we
could just take a prefix of the long URL or the input URL so any given long UR
that comes in let's just chop off the first five to seven characters stick that then as our short URL or our short
Alias or excuse me our short code uh and then append that to the end of our wwwb
bitly.com that prefix right now this is obviously bad why is it obviously bad
well because there are tons of URLs that share the same prefix what about every single URL at www twitter.com or wwwf
facebook.com or any of these different common URLs they're all going to share the same prefix and now we don't have a
one to one mapping between short and long URL we have a one to many mapping this means that if you give us one of
those prefixed short URLs we have no idea which one of the thousands hundreds of thousands of long URLs it actually
maps to so it's a terrible idea don't do it the second thing that we could do is
we could use a random number generator this is a much better idea so a random
oop so this is a random number generator and so we ask oursel like how
large can can this number be how large should this number be how large would this number need to be well if we come
back over here we're reminded of our scale that we're going to have a billion URLs and so this means that this random
number needs to be at least between one and a billion of course if it's just between one and a billion our Collision
rate is going to be really high so we might want it to be higher than that but it needs to be at least that 1 billion
is 10 to the N or 10 characters right 10 characters that's
more than our 5 to S that's too many characters and so we'll need to do something a little bit more
sophisticated in order to compact that we can't just depend 10 characters to the end of this thing and we need at
least 10 remember we probably need 11 12 13 in order to make sure they Collision rate is lower but here's what we can do
we can do something called base 62 encoding and so base 62 encoding is basically can be thought of like a
numbering system like zero all the way to to you know 1 2 3 4 5 6 7 eight and all the way up but instead we're going
to incorporate the alphabet and so the way that the numbering works is that we go from 0 to 9 and then we go from A to
Z and then we go from A to Z lowercase and so what this means is that 10 is actually a 11 is actually
uppercase B and it means that any given character can now encode uh 62 options
as opposed to just n or 10 like in the traditional base 10 encoding
right so we can take a large number and then base 62 and code it and so now how
large would we want this to be well if we had for example a code that was
length six let's go right between r five and R seven then it would be 62 to the 6
possible combinations 62 to the 6 is 56
billion about and so that's pretty good we have like a decent amount of space there we can randomly choose a number
between 0 and 56 billion we can base 62 encode it and it's going to be a short code it'll be of length six in base 62
encoding uh but what about our chance of collision what is the chance that a random number between 0 and 56 billion
when calculated a billion times ends up colliding well you might be surprised by
this but the Collision probability is actually really high uh this is often times referred to as something called
the birthday Paradox I'll write that down in case anybody's interested in reading about it so this is the birthday
Paradox and it's this counterintuitive probability problem that states that there's actually a 50% chance that two
people in a group of only 23 people have the same birthday I'll say that again
you can see why that's so counterintuitive if you have 23 people in a room there's a greater than 50% chance that at least two of them share a
birthday despite there being 365 days in a year now the formula that is used to
calculate that can be used to calculate um the the probability of a collision
on 56 billion uh randomly generated things as well and you wouldn't need to
know this in a system design interview but just because I thought it was interesting I went about and I did this and it turns out that out of 8 billion
or excuse me 1 billion random Generations there's an estimated 880k
collisions that would happen here so that's a lot that's like a decent number
of of collisions right it's depending on how you define a lot 880k over billion
might not be that many but it's it's certainly a large enough number that we would end up with more than a one to one mapping and so how do we address this
well one thing that we can certainly do is that we can take this approach we can random number generator base 62 encode
um yes there might be a collision but what we'll do is before saving it to the database we'll come over to our database
and we'll read the short URL see if any exists like this already and only if they don't exist write to it update it
so we just int roduced another read instead of calculate the short URL and save to the database it's calculate the short URL check and then save to the
database right so that's totally possible so basically we just need to
check for Collision first is that a big deal not really it's an extra read uh there's
some consequences to that but no it's not a big deal that's one option another
option is that we could hash the long URL this is a a common one that I see a lot online and the candidates often
raise so they can take that long URL and they can call some hash function and so maybe that hash function is like md5
something cheaper like murmur hash something like shot 256 cryptographically secure whatever but
you get a long URL and then you would end up getting some thing some output
right some hash some hash and you would take that hash and you would base 62 and
code that hash again right and then you would slice it to take just those first six characters so that would be the
operation that you would do there now what you end up with is six characters
of Base 62 encoded so you end up with the same thing that we ended up with the random number generator and because of
how hash functions work right a hash function despite it being deterministic
has that waterfall effect such that if you change just one bit on the input the whole hash should change significantly
basically increasing the randomness of the hash that's generated and that property means that the the output is
actually just exactly the same as the random number generator it is literally the same thing there sure there's 56
billion chance uh 56 billion possible combinations the chance of collision is exactly the same so same as above again
this would totally work it would work exactly the same we just need to make sure that we check the database first
can we avoid checking the database is the question the answer is yes is it a better approach the answer is maybe yes
um but what we could do is we could use a count like why introduce this Randomness in the first place why doesn't the first
person who comes to us just have short code one the second person have short code two the third person have short
code three and so on and so we can just have incrementing a counter we can just
increment counter for each new short URL or each new long URL that needs to be turned into a short code and then again
we'll base 62 encoder we'll always do that so we can kind of make this space more Compact and so this allows us to
get up to that 56 billion with six things but we're guaranteed to never
have a collision because we're always just linearly increasing there a sequential nature to it right we're
going to go zero all the way to 9 and then to capital A and then to capital B all the way through until you know
eventually we have six characters of that base 62 encoding and so this is great and maybe what we can do here just
to visualize this is I'm going to expand this guy up like
this and we can add in here like some counter so there's some counter in here
which we're just always going to go grab the next count what's next right grabbing a count is fast it guarantees
that it's Unique and by base 62 encoding it we guarantee that it's short it's not without its flaws though so there's a
predictability which is bad for security and so what this basically
means is that anyone who wants to know our short URLs can uh they can easily
know how to count and they can easily know how to base 62 encode and so not
only could our competitors know how many URLs we've shortened by just continuing to call our service until they end up
not getting a short URL that converts to a long URL anymore um but they also can just like scrape all of the long URLs
that we have right by just calling the short URL with that new incremented code each time and so maybe this is a problem
maybe it's not like this is a product decision we could say when users go to create a short URL like a warning
warning like they these are not don't don't uh don't shorten private URLs right like
we're not responsible for this that's one option there we can of course have rate limiting so that our competitors can't just come and like scrape and grab
all of these URLs if they want to but we also could do something more sophisticated and that's just not let
this become a problem in the first place by introducing something that's oftentimes called a by junctive function
and so you don't need to know this again in a system design interview I think this is just interesting if you brought brought out these facts they'd probably
be impressed but you don't need to know this bjective functions are functions that just issue a Ono one mapping and so
there are libraries one of the most popular ones is squids dog you can look that up if you're interested and it
takes a number and then it returns to a hash that looks exactly or a base 62 encoded string that looks exactly like
the short URLs you see on bit.ly and it can take that uh that number that you provided it and then one to one map it
via some off obfuscation um so that you can no longer incrementally uh you know know how to
get the next URL if you're if you're a competitor a hacker or anything like this so these bjective functions exist
it's worth you looking up on your own I'm not going to go into more detail but that's one option there now the nice thing about this counter approach of
course is that we don't need to do the read right we know that every single one of these is unique so now we get the counter we run our bjective function if
we want to and then we go store that short code in the UR uh the short code in the URL table and we're to
go um the last thing that I'll say here is that you're probably thinking to yourself oh no this isn't great why do
you have a counter on a single server you're right we'll talk about it when we get to scale but for now here are your options in order to create a short code
both two and three are totally realistic and you could provide these in an interview and it should totally be passing you'll just need to call out the
need for that Collision check four is an option I think that I like in this case because it doesn't require that
additional check but ultimately there's very small differences between them
let's come back over and look at what non-functional requirement we should go into next so I'm going to go back in
order now and I'm going to jump into low latency on redirects and so how can we make this redirect as low latency as
possible right now what is it that we have to do while the client has to make a request to the primary server the
primary server needs to look up that short URL in our URL table return the long URL and then that long URL needs to
be returned to the client now the expensive part of all of this is this database lookup that's what's going to
take the most time and now without any indexing and I'll explain indexing here in a moment but we would have 1 billion
rows here and you would need to look at every single one of these rows and try
to find the short URL that you're interested in so that you could return the long URL that it maps to that would
obviously be like prohibitively expensive it would take a really long time to do and so the common thing that
we do in databases in order to make these queries and these lookups more efficient is that we use something
called index and so each URL table you can define a primary key this is true of most
database systems now this primary key does a couple things one it enforces uniqueness which is good in our case
certainly but it also ensures that an index is automatically built on that um
on that column right on that primary key in the table and this index is typically
kept in memory not always but you can think of it as this thing that's kept in memory that is a pointer to a location
in disk and so so instead of us having to go to disk and seek and look for through all of the records in order to
find the short URL we go to memory we look at this index and we ask it hey where is short URL 123 and it's going to
tell us where in disk it is and we can just seek to disk or we can just go exactly to that place in disk find the
long URL and return it makes it much much faster now when you add a primary key to something like postgress let's
say that our database here was postgress then it uses a b tree as the index a b tree is like a self it is a
self-balancing tree not like it is a s balancing tree and if you've been studying for your coding interviews you
know plenty about trees um and so it's going to make this log in often times
actually much quicker than that there are quite a few optimizations that exist in modern databases nowadays but that's
what's going to happen and it's going to make this look up a lot faster now you do have an option of additionally
creating a a a further index basically a second index on this short URL which can be a hash index and this would be 0 of
one it would hash the short URL and and point directly to where the the the row is for us to get the long URL you could
totally do this realistically you don't need to uh these be trees in postgress for example and all these modern data
databases are so well optimized for these like equivalency lookups um that
it would effectively be the same so not something to actually worry about um now
we're still going to disk like we solved one part we don't have to go to disk and then read all the records in disk we're
going to go to memory uh we're going to use that index to find where we need to go in disc but we still need to go to dis and then back realistically ssds are
really fast nowadays uh so this this wouldn't probably be a problem but we could certainly make it faster by never
having to go to dis in the first place and only ever going to memory and so while we're going to index first that
was our first option we added that here index our second option is that we're going to add a cach and so we can use
something like redis we could use MC D we can use any any inmemory cach here and what this cash is is it's just
another server it's just another computer somewhere a separate instance a separate computer running and we're just
going to utilize its memory we're going to utilize its Ram in order to be really quick here and so we're going to make
this be a read through least recently used so read through least recently used
cache what the heck does that mean right it means that any time that we want a short URL or we want a long URL for a
short URL we're going to look in the cash and if there's a cash Miss then we're going to get it from the
database update our cash and then return it that's the read through nature the least recently used is just saying if
this cash gets full then our eviction policy is that anything that hasn't been touched lately kick it because the
reality of a system like a URL shortener is that there are going to be some URLs that are really hot that they're getting called all the time but after a couple
weeks months no one's going to use the old URLs anymore and so there's no reason for us to have them cash their
lookup might take a little bit longer the first time who cares and so caches like this uh are oftentimes just key
value pairs that's at least most common that's why I say oftentimes and so in our case the key is just going to be
that short code or that short URL and then the value is just going to be the long URL and so this is going to be a
really quick in memory of one lookup if we have a hit if we have a Miss then we have to come to our database look it up
by the index re uh place it in the cache and then return it but the subsequent call will be over one again so that's
what we can do there great option now there is one thing that we could do further I would actually stop here and
argue that this is best for some of the reasons the arguments that I made when it pertains to the 302 versus 301 but we
could also cash in a CDN a Content delivery Network what these are is like they're little Edge servers that are
geographically located all over the world so you can imagine that our primary service maybe is sitting there in California and you're trying to
request a short URL from China uh well there's a lot of latency required in
making that request all the way from China over to California and so CDN are these servers that are all over the
world and the user then would hit that server in China and we would have cashed
on that CDN any responses to any of our for example um you know API requests to
to to to redirect to a longer URL from a short URL there it is right uh so we
could do that but the problem is it's going to hit that um CDN and then just redirect the user and it's never going
to come to our primary server so there's the same issues we mentioned with the 302 301 redirect which is that in the
case of a 301 redirect it's a permanent redirect so it never hits our primary server and we don't know if our servic is well like working and so if we care
about knowing if our service is working and logging and analytics then we wouldn't use a CDN if we don't care
about that then we could use a CDN but we could also use a 301 redirect and then we'll just have less things come to
our primary server and we have more caching at the edge both the users browsers dns's and CDN respectively so
good discussion to have with your interview this is kind of the essence of these system design interviews there's no right or wrong answer it's trade-offs
it's discussions it's weighing different uh priorities and so something important to note heading back over to our
non-functional requirements we can head to our next one which is scale to support 100 million daily active users and 1 billion URLs and so when we talk
about scale we want to work our way typically left to right of our system and see where all the bottlenecks would
be all of our services here all of our components how do they need to scale so
I'm going to move some things around a little little bit just so that we have room but the first thing that we're going to look at here is our primary
server and so does our primary server even need to scale well we said that we had 100 million daily active users now
let's just say that each one of those daily active users does one redirect this seems normal maybe it could be two maybe it could be three change your
estimate but I'm going to say that the average is about one redirect and so 100 million is the same as 10 to the 8th
when you're doing math in a system design interview I suggest you use exponents like this this uh because it
makes the math a lot easier watch this so we have 10 to 8 and then there's a 100,000 on average not on average but
round it up excuse me seconds in a day right so that's 10 the 5 and so 10 8
divided by 10 5 is just sub subtraction on the exponents so 10 the 3 in other
words 1,000 so we have 1,000 requests per second okay uh that's if it's evenly
distributed but we want to handle some Peaks so maybe we multiply by 10 or maybe we multiply by 100 in either case
we're somewhere between 10 to 100K request per second being our Peak here
so we did that math pretty quickly it's kind of a handy Tool uh using the exponents in that way and so then you
start to build up some intuition about what is a lot and so an ec2 average
instance like a T3 medium can handle around a th000 requests at a time uh I
say around this is intentionally handwavy like this depends on a how computationally expensive these requests
are how much memory is being used how much CPU is being used how large the payloads are how much bandwidth is being
used like these numbers are very rough but in an interview you can use that roughly like a thousand requests
concurrently is reasonable enough and so we would we can't handle this in one
instance here if this was just one server and it could handle a th requests per second and we have 10K or 100K we
obviously uh need to do something different here and so we have two two options to us you probably read about
these the first is what we call vertically scaling and this is just making this box bigger so like box Plus+
basically uh and when I say box of course this is the server just some terminology there and so we can go to a
bigger instance instead of a T3 medium we can pump it up to something that has more CPU more memory can handle more
bandwidth like a bigger box that's one option it's more expensive another option and this one's the most common
one certainly in system design interviews is that we scale horizontally and that means that we just have more of
these and that each request that comes in goes to one of them right and so
that's a that's a really good option and the option that we're going to take here we're going to scale this horizontally but one thing that's
interesting to note is that there are a lot of reads in our system 100K rights per second for that redirect but this
get short URL we could imagine that there's far fewer of those like there are very few people who are trying to actually create a short URL every day
maybe it's a thousandth of the amount of people here so just like one Quest per second it's not a lot and so that
doesn't need to scale a lot the reads need to scale a lot and so as a result what we can do here is something uh kind
of interesting which is that we can evolve our design to be a microservice
architecture and in doing so we're going to have two separate Services both of which are scaling horizontally we're
going to have one here which is our read Service this one's going to be responsible for the redirection and one
which is our WR service this one's going to be responsible for creating the short
URLs and then in doing so we're going to introduce a new component here that we call an API Gateway and it's responsible
for being the entry point so the API Gateway gets a request for one of those API endpoints that we Define and then
it's going to determine based on that API endpoint which one of these services do I go to which one should I route this
request to the read service or the right service respectively and then the right service
of course we're going to do this let's just tie everything together here we have this is only on the read
service and then this still goes through here right or maybe you can make this
abstraction like this if you want to since it's a read through but in any case kind of the same thing just a little bit of a layer of abstraction
there okay and so now we've split this up and what this means is that this read Service we're going to scale this one
horizontally we're going to have a lot of them bang bang bang and we might have far fewer of these right services and it
affords us the ability to do so now let me just note that this is like this is
true and it would be a good thing to say in your system design interview but there's like a very little bit of code
happening on both of these boxes and the reality is like splitting this up into two means that you have two different services to maintain and it's probably
Overkill there's no right or wrong answer but I just want to call that out you very well could just keep these in the same box and scale them the same but
uh you know it's a trade-off to way this is totally a valid option too so feel free to discuss it in your interview um
now which each of these Services when it comes to their scaling nowadays this is like all handled for you on the modern
Cloud infrastructure whether it's uh you know Google cloud or AWS or Azure or otherwise and there's just autoscale it
and so you can have these ec2 instances or you know in the AWS world and you configure memory in CPU limits so you
basically say if 75% of my clusters memory is used or if 75% of my CPUs use
throw up a new box and then if less than 20% is being used take a box down and these things will just scale
automatically and yes technically of course there's a load balancer here in front of them that is taking these
requests and then just routing them either with round robin or however else you configure it within your um you know
your your Cloud dashboard and it's routing it to each of the boxes but that's how it works in practice nowadays
like you don't actually control the up and down uh it's just all autoscaling so
something that's worthwhile to know um okay so that's how we we scaled our services now with that right service
though we have an issue remember we had that Global counter here or we had that counter here now this counter if we have
multiple of these right Services we can't have two different counters they're not in sync like they both start
at zero and then they go to one and now there's two ones there's two twos you get the picture right so this isn't going to work and instead we need all of
these right services to agree on the same current count and so what we need
to do is we need to pull this counter off of the instances basically that counter can't be in memory anymore on
these particular servers we need what we can call like a global counter and so we can have a global counter here um and
This Global counter again could be reddis for what it's worth it could be the same instance too I'm just drawing this separately uh to make it easy to
see and now they're both going to ask this Global counter for what's the next
count and it just keeps a single count here that goes from one to two to three you get the picture all the way up right
and so in Reedus's world reddis has an incor um which is a command that's just
going to increment a counter you can have that counter here in memory and because redus is single threaded you don't have to worry about any
concurrency it's single threaded so we're going to do one incur at a time and it's wicked fast because it's in memory and then we're just going to do
the next one so the count is always increasing now one thing I'll mention just quickly is that this means now that
uh in order to get the count you got to go somewhere else make a network call get the count come back do your
calculation send it to the database you added a step here and so one thing that we could do which is kind of cute is
that when a server comes online we can request like the next 1,000 counts for example and then keep all of those in
our internal memory and then just be using those until we need to request the next 1,000 counts and if this server
goes down before we used all 1,000 no big deal like those are lost forever those counts but it's fine right we had
up until what it was like 3.5 trillion until we needed to add the the seventh
character there so we can afford to lose some there's no big deal um but this is how this would work I'm going to remove
that and you guys can just remember that these are both horizontally scaled respectively okay and then what about
the database so let's head over this way now how does this guy need to scale well again let's let's do a little bit of
math here maybe I'll I'll do it right here um so we have a short code that's like 8 bytes we have a long URL maybe
that's like 100 bytes we have a creation time those are always 8 bytes uh we have an optional custom Alias
maybe that's up to 100 bytes that'd be crazy though cuz it should be small so that's on the high end an expiration time 8 bytes you know this is 216 bytes
232 bytes let's just round up because maybe we want to throw more stuff in there let's say 500 bytes and so we have
500 bytes times 1 billion rows and so that ends up just being 500 gigabytes
500 GB isn't a lot modern ssds are in like the hundreds of terabytes like 5
gab is nothing so we can just have a single instance of our database it's no big deal the only other thing we'd be
concerned about is the read throughput like can our database handle the read throughput and we put most of the reads on reddis anyway in our cache so our
database is chilling it's good to go now if we did need to scale the database then we would Shard probably by our
short short Ur short URL and that would mean that we would just have multiple instances of our database uh and where
the data was stored would be based on like take your short URL modulo 3 and store it on one of those databases it's
kind of how that works but in this case we didn't need to we did the math and we proved that it doesn't matter and so at
this point our system is is fully scaled coming back over the last thing that we had was high availability now
most of what we've done by having the auto scaling by separating these and scaling them independently horizontal
scaling uh we're at this point largely available there are some things that we
want to consider like reddis here uh we would want to make sure that we probably have honestly I don't care actually if
redus goes down it's fine because it's read through so we'll load it back up by just hitting the database we'll be slow for a little bit no big deal if the
global counter goes down that would be a problem so we'd want to have some high availability modes here which basically means that we would have some redundancy
uh we can also periodically snapshot the count and save it to disk um if you want to look up reddis high availability mode
it'll it'll uh explain to you more about how all of that works but that's a configuration here in the database too
um we can have some some replicas so maybe we have a single replica we
frankly probably don't even I don't know having a single replica would be good in case the database went down um but we're
also just going to take snapshots every hour or so so a snapshot of the current state of the database stored in
something like S3 a big cheap blob storage and that way if the database ever goes down we just pull it back up
having that replica there means that if one database goes down we can just point to the replica and it can be in charge for a while until we get our Snapchat
back up Snapshot back up um but that should satisfy our high availability in this case no
problem so at this point we take a look back at our requirements and we've
satisfied all of our functional requirements when we did the high level design we've now satisfied all of our non-functional requirements and we look
at ourselves and we say I nailed it like I've passed this interview I've crushed it and I know I've crushed it because me
and my interviewer agreed on the requirements and I have now completed my design satisfying all of those
requirements and so I'm feeling really good you should be feeling really good hopefully you learned a lot as
well so there you have it I hope you all learned something today especially if you're new to system design I really
Conclusion
hope you found this useful uh we're going to get back to our regularly scheduled programming don't worry with some of those more complex problems and
breakdowns coming out in the near future uh as always if you have questions feedbacks things that you think I did
wrong please go ahead and leave a comment I'd love to hear from you uh and I get to as many of those as I can so
don't hesitate there and of course don't forget to like And subscribe all right good luck in your upcoming interviews
I'll see youall soon
