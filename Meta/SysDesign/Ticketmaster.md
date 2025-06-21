welcome everyone uh welcome to what is the first of hopefully many system design breakdowns uh today we're going
to be walking through a common system design interview question that's asked at many of the top companies so we're going to be designing a ticket booking
service like Ticket Master so this question is asked a lot at meta in particular especially in what they call
their product design interview though it's also asked uh quite a bit in the regular system design interview now I
spent 5 years at meta uh I was an interviewer a staff engineer there and I'm now the co-founder of hello
interview which is a site that helps candidates prepare for upcoming interviews largely bya mocks with senior
Fang engineers and managers uh so between asking this question at meta and asking it in mock
via hello interview I probably asked it uh probably well over 50 times and I've seen exactly where candidates of all
levels do well and where they trip up so today we'll walk through this problem in the same structure as if it was a real
interview uh but I'll periodically be interjecting with tips Frameworks Etc
kind of lessons learned from those many mocks that that I've done across both meta and hello interview lastly before we get started
um if videos aren't your thing I've also written up a a detailed kind of breakdown of this question on hello
interview so you can head over there and read this I'll I'll link it below you
can see there's also a number of other uh breakdowns of common questions that you can check out as well so without
further Ado let's get into it okay before we jump immediately into
The Approach
designing the system let's talk about the suggested road map and this is the road map I suggest that you follow for
any of your system design interviews particularly those that are um designing these user facing products like design
Ticket Master is so the first thing that we're going to do is we're going to talk about the requirements this includes the
functional requirements kind of the features of the system as well as the non-functional requirements so the qualities of the system and then we'll
outline our core enti this is like what is the data that's persisted and exchanged throughout our
system we'll go over the apis and then we'll do a highle design which satisfies
our functional requirements so a simple design that satisfies the main features of the system and we'll conclude with
deep Dives and these deep Dives uh will be a conversation with the interviewer depending on your level the interviewer
might even lead this um but it's going to go deeper into satisfying those non-functional requirements mainly so
this is the plan that that we're going to follow and we'll go Section by section the first thing that we'll do is
we'll jump right into the requirements so when your interview
Requirements
starts the first thing that you're going to do is you're going to start by writing down your functional requirements these are the features of
the system and they're usually statements like users should be able to so when you get here hopefully you've
had some experience with this system in the past usually they choose really popular systems if you haven't asked the
interviewer a lot about the system what is it to do what's most important functionality where are it features how
to users use it Etc once you have that good sense then start to list what are
the core features the core meaning the ones that are most necessary to make this uh system work in function so in
the case of design Ticket Master the very first most important one is users should be able to book tickets so we'll
add book tickets there the Shand of that uh in order to book a ticket a user needs to be able to view an event so you
can imagine viewing an event page seeing a seat map choosing a seat we'll call this viewing an event so view an event
view the event details who's performing Etc and then you can ask yourself well
how do they get to we're sort of walking backwards through the user flow how do they get to viewing an event in the
first place they need some Discovery they need some search so users should be able to search for
events and so in my estimation these are the main top three functional requirements you just can search for an
event they'll see a drop- down list of events I'll click on one of them this will take them to an event page from
here they can book a ticket to that event perfect uh these are usually the functional requirements that most
candidates end up landing on and the functional requirements that I sort of like uh push them towards if they're asking questions or need any
help once you've done your functional requirements you're going to do your non-functional
requirements and so your non-functional requirements are the qualities of the system they're not
features uh but they're the qualties of the system like scalability availability reliability fault tolerance all these
things that I'm sure you've read number of times uh in the books and the resources the biggest mistake that
candidates make here though is that they just write those terms they just write availability and scalability and and
whatever it may be all of these idies um this is not always strictly
wrong but it's defeating the purpose like all systems have those qualities
the important part of non-functional requirements is to identify what makes this system unique interesting and
challenging and so you should go through those Ides in the context specifically
of this problem and we can do that here now so the first question I usually ask myself is Cap theorem in the context of
cap theorem is my system going to prioritize availability or is it going to prioritize consistency and kind of the easy right
answer here particularly for mid-level candidate is that we're going to prioritize
consistency more than availability and the reason for this is because we
need to make sure that no ticket is assigned to more than one user we can call this no double
booking sheesh typing is bad no double booking right so for any given ticket we
can only have one user sitting in that seat so consistency is really important for us there um however a more nuanced
candidate maybe a senior level candidate would actually realize that these two things can coexist and I'm being very
careful when I say that they can coexist uh but in different parts of your system in different parts of your microservice
and different parts of your system architecture so what I would amend this to is that we need strong consistency
for booking tickets but at the same
time uh we want High availability for search and viewing events that's kind of
the right more senior answer there so when users are searching and they're viewing events they should be highly
available and it doesn't really matter if an event was just added and they don't immediately see it within a couple of seconds fine but in the case of
booking a ticket if a user in Germany bought a ticket that I'm viewing while I'm here in America um I need to know
instantly uh that they booked that ticket or get an error because I can't book that ticket anymore right so strong
consistency for booking tickets High availability for searching and doing events um what else is interesting in
this system well we can ask oursel first about the read WR ratio is there anything unique there and in this case
we would recognize that reads are much greater than wrs so it's probably like 100 to one uh maybe even a th000 to one
probably 100 to one if our conversion rate for booking tickets is maybe around 1% so there's going to be a lot more
people searching and viewing events then they're all ultimately buying this is going to have consequences on our design
that we'll see later on the next is like think about how our site is used what's
our query access pattern is often how I refer to it so um what are what's the
Frequency consistency irregularity with which requests are hitting our system and what you would note is that people
don't book tickets to events all that much there kind of this regular even consistency uh until you end up having
really popular events and so when Taylor Swift's tour is about to go live or the Super Bowl or the World Cup all of a
sudden you have tens maybe even hundreds of millions of people at your front door trying to get the same ticket so in the
context of scaling this is an example where you wouldn't just write scalability but instead scalability is
important uh but it's to handle surges from popular events specifically and so we'll need to design
with that in mind scaleability
cool awesome um so there's there's a long list that you can keep going down these non-functional requirements um
obviously it's important that we don't use lose data that we remain compliant with gdpr all of these sorts of things
but if all of that comes to mind what I usually suggest is that you just note that as below the line so like out of
scope uh you know gdpr oops gdpr compliance I'm not going to write all of
these out but fight fault tolerance Etc you sort of get it and then once you've done this you can say to the
interviewer uh these are what I'm going to prioritize here's what I've considered out of scope would you like me to
reprioritize any of this is there anything from down here you'd like me to move up here anything from down here you'd like me to move down is sort of a
nice an way to make sure that you check in you're on the same page with the interviewer and it shows them that you have this larger product thinking that
you can think about all of these things that are necessary in designing a system um but you also can remain focused on on
what really matters for this particular system sweet so with that you've defined the functional and the non-functional
Core Entities & APIs
requirements so the next step is for us to Define our core entities and the API
I'll do these sort of in the same step here CU they usually come hand in hand usually you won't spend more than like 2 minutes here on core entities and up to
five on API um but the purpose of the core entities is to start to get an
understanding of what data is persisted in your system and then exchanged by the
apis so this is really going to be useful um in order to you're going to use these in order to build your apis as
well as of course your high level design so you can think here what are the core entities of a system like Ticket Master
well the first thing is we're going to have an event and so admins are going to add these events uh note that adding events is
going to be out of scope we're going to be focused just on sort of like the user flow for our system um but users can add
events events themselves need to be hosted somewhere so they're usually hosted at a venue like a stadium uh and
then there's somebody who's performing there's a performer so we'll probably have tables for each of these or
collections for each of these and then maybe most importantly you need a ticket so we're going to have
a ticket table and this is going to have all of the tickets for a given event so that we can determine whether or not
they're available who's purchased them if they've been purchased their price stuff like that so these are our core
entities um now one thing that you can do is that you know next to these you
can mark down what all of their fields would be name description Etc if you know them at this point I usually
suggest and for me if I was going and doing an interview right now I would just stick to the core entities and I would be clear to my interviewer like
I'm not going to detail the key fields and columns yet because the reality is I don't I don't quite know them yet I'm
too early in my design they're going to evolve naturally so instead I'm just going to get a clear sense of what my
core entities are and then as I move into the high level design and you'll see this when we get there we'll be more
explicit about exactly the fields that matter but for now I would stop here and
with the with the core apis defined I would move on to API and so these are
strictly speaking the user facing apis these are the API the client is going to be making in order to satisfy the
functional requirements and so the way that you do this when you get here is that you should look back at your
functional requirements and create an API or in some cases more than one API in order to satisfy each of these
requirements and they should exchange return take as input the entities or um
you know properties fields of these entities so let's run through an example of that book tickets um let's do that
one last Maybe because it's the most involved let's start with the simplest view an event so in order to view an
event I'm going to have a git call I'm use a rest API that's what you'll typically do in these interviews uh in
most cases though you should consider other options graph qall being the main other one so I'm going to have get event
and then I'm going to have this path Pam of event ID and so users can pass in an event ID and what they'll get an
exchange is an event object they'll need to get information about that venue they'll need to get information about that performance this is everything
needed for us to render a page about this event and then we'll also need a list of tickets this is going to be so
that we can render the seat map so like what tickets are available where's their seat Etc so take an event ID and return
these entities that's going to be for viewing an event very easy um now we can
look back up here and we can go next for searching for an event so if you want to search for an event you would do get
maybe we'll have a search endpoint um and this search endpoint can take in
things like maybe a search term this can be free text um so something like this
and it would also probably take in a location and so maybe this location is lat longe I'm just going to have it
abstracted as location for now maybe we have a type or a category so this is
something like uh is it a sporting event music Etc uh dot dot dot maybe there's
some other query prams that that you would care about uh date is probably a really important one too right here like
date ranges um these are all the optional fields that you can search for and what
this is going to return is that this is going to return I'm going to use this is just pseudo code here um derived or
inspired by typescript but partial event a list of partial events and the reason that I say partial here and this isn't
particularly interesting for the interview you can denote this however you want um but just so it's clear this
is because I'm going to return just just a limited amount of information from that event like the name the description the performer whatever it may be because
I just need enough to show those search results and then you'll click on those search results and and and hit this API
endpoint to get the full detail um but here's our our search endpoint so we
have a basic um endpoint to satisfy viewing events a basic endpoint to view searching for events and the last thing
that we need to do is satisfy booking a ticket so this one's more interesting
and the reason that I paused before coming back in into this one is because uh you'll notice or it's important to
notice that booking is actually a two-phase process so if you ever used a Ticket Master or if you've ever bought
an airline ticket you would know that what you usually do is you see a seat map or you see an airplane map you
choose a seat and then you go to a second phase where you're actually going to purchase that ticket and so in that
second phase you usually have a timer or a countdown maybe 10 minutes in order to
uh actually purchase that ticket and for that 10 minutes that ticket's reserved for you so you click on a ticket it ends
up being reserved you then have 10 minutes to actually book it if you don't book it that ticket goes back to available and that's the same pattern
that we'll have here so in an interview some candidates because they have experience with these sorts of things they've thought about that they know
that they know that it's two-phase and that's usually awesome to see but it's not a requirement if I see that that a
user writes a single endpoint for booking a ticket then I'll point out actually this is going to be a two-phase process and then they'll they'll amend
it accordingly so what we'll end up doing here is is we'll have some posts um and we'll maybe call it booking um
and the first endpoint is going to be just to reserve and this is going to take in in the
body just a ticket ID and so there's variations of this problem where maybe you can reserve multiple tickets you can
click on multiple seats we're going to make it simple and just say there's a single seat that you click on that seat's associated with a ticket and
you're going to get that ticket ID as the input and you're going to want to reserve it you'll notice that I don't
have user ID actually in the body here this is on purpose uh some candidates will put user ID here on it it's it's a
security concern you wouldn't past or post uh a user ID in the in the request
body because that could be altered I could come in here and then post uh a reservation on behalf of somebody else
so long as I knew that user ID so instead usually user information is kept in the header either via JWT or a
session token uh and that's usually nice to note in your interview kind of shows some technical Excellence but you don't need
to spend too much time here then the the second thing that you're going to do that's going to be your reservation this
is going to reserve a ticket for 10 minutes and the user client is going to go to a payment page and you're then
going to try to fill out that payment and so now we'll have another endpoint to confirm again our header is going to
have that JWT we're going to need the ticket ID to say which one we're confirming and then we'll have some payment details probably and so we'll
offload this to stripe thirdparty payment services stripe has things called payment intents
um which use common client libraries that you can set up either in react or or raw JavaScript whatever it may be um
in order to get this payment information and this will be posted back then to your server so we have our two endpoints
just to recap for booking a ticket the first to reserve and the second to confirm and so maybe this isn't a post
CU we're not creating a new entry here uh maybe this is just a put or a patch respectively um but but certainly not
the most important thing awesome so that satisfies our core entities and our core apis and then in the next section we're
going to use these apis in order to build up our highle
High Level Design
design all right so at this point you should be about 15 minutes into the interview um which leaves you about 20
minutes to do your high Lev design and your deep Dives um give or take depending on your level maybe it's
taking you a little bit longer to get here and that would be totally fine as well but the next step we've done our requirements qu entities and apis let's
let's get into that highle design so again the highle Design's goal is to uh create a simple design that satisfies
our three functional requirements so in order to do that zoom out a little bit
the first thing our design is going to have is the client it's going to be the user that's interfacing with our service
and then we're going to opt for a microservices architecture this is by far the most common setup in these types
of interviews if you're not sure which to go with which architecture to go with microservices is probably the right call
um so for that reason we're going to have an API Gateway the API gateway's main responsibility is to take incoming
API requests and Route them to the correct server uh the correct micros
service it also does some other things uh we can note those it does authentication it often does rate
limiting uh and then of course as we just mentioned routing is that that most important one so when we build up our
high level design what we're going to do is we're just going to go one by one through our API requests and of course
our API request mapt back to our functional requirements so we can start with this one viewing an event what
happens when the client the user ends up has having a git request to an event ID
in order to view an event well let's draw that out so what would happen is first they're going to hit our API
Gateway our API Gateway is going to Route them to the correct micros service in this case I'm going to call it the
what am I doing uh I'm going to call this the event crud Service uh so so while it's responsible
for creating reading updating and deleting events um you know most of those other crowd operations are out of
scope for this problem we're just handling that view path but that would be handled in this microservice so that request is going to
hit this service and then the service is simply going to read off of our database
so we'll have a database here and this database is going to store those core entities that we talked about
so we're going to have an event table let me zoom in uh we're going to have an event table
and that event table is going to uh have an ID it's going to have a
foreign key to a venue ID needs to be held somewhere there's going to be some performer or team uh obviously it'll
have a name description dot dot dot bunch of
different metadata uh and then additionally maybe importantly it's also going to have a on to many relationship
with all the tickets um so this isn't going to actually be the ticket information this is just
going to be uh forign keys to all of the different tickets cool so that's our event table um they're less important so
we won't spend as much time on them but we mentioned them so we'll have a venue which will have an ID it'll have some
location if it's probably going to have a seat map some stuff like that um oops and then we'll also have a performer
it'll have an ID dot dot dot who cares you know the details there cool and then while we'll we'll
probably come back to it um you know we'll also have our ticket table and
that ticket table it'll be an ID per ticket uh probably a seat price Etc
right so seat here is like the location uh and then of course it's going to have a relation back to an event so this is
everything that's stored in in this database um we can opt for you know here's where that SQL nosql conversation
comes in um uh uh I'll talk a little bit about why that's probably not relevant but at
least for this database we talked about consistency being important for tickets in particular there's obviously some
decent relationships between this data we've shown that now one to one one to many so these are the properties that matter to us I'm going to go with
postgress a SQL database under the justification that one it's it's one that I use frequently um and it
certainly satisfies our requirements here for assid properties on tickets uh
allows for the ability to do transactions and a you know it's it's good for these SQL queries where we'll
have to have some mild relationships but it's worth knowing that like a nosql database would have been fine here too
you could have chose Dynamo DB and actually in your interview no SQL versus SQL is kind of an old debate like it's
it's not that interesting um what's more interesting is the qualities of the database that you need because the reality is most of the things that a SQL
database can do a nosql database can do nowaday and most of days that is things that a SQL database can do and no SQL database can do so you can have asset
properties on DJ for example um totally fine actually in the interview it
sometimes not even sometimes it shows the candidates seniority when they understand that that's kind of not a
relevant debate like many mid-level candidates will go SQL versus no SQL and sort of try to break all of this down
whereas the more senior candidates just say here are the qualities of the database that I need either of these would have worked in this case I'm going
to go with postgress because it's the one that I'm I'm most familiar with and it'll do just fine for the job cool
great and we move on um so this is this is that appropriate time to map out the
fields uh and the columns I mentioned that we would come back to this at this point I put them right next to my
database because typically they evolve and you'll see this they'll evolve in this design too but this is what we know
for now so coming back to that get request a user is going to want to view an event so they're going to hit our
event crud service we'll get the event details the the venue and the performer from a join uh as well as you know the
tickets that are available and we'll return that back to the client so very simple that satisfies our first API
endpoint here the second one is our search endpoint um our search endpoint
for that let's do this I'm going to move these down a little bit
maybe okay and then I'm going to add a search service so I'm going to add a search
service and for now in our highle design I'm going to do this as simple as humanly possible and that that means
that I'm just going to do this so a user is going to search for something let's maybe copy this so that it's close and
and clear they're going to search for something and at least based on term type date Etc this can just be a SQL
query so it can be something like select star from our DB where type in whatever
and uh term or you know name like uh whatever our term is you kind of
get the picture here um this would work now for what it's worth this totally sucks and it's incredibly slow and the
reason it's incredibly slow is these wild cards here mean that we need to scan this entire database we need to do
an entire DB scan to see if any of the names match whatever term was inputed here um that's not going to cut it but
for now in my highle design I'm going to leave it like this and I'm going to come back to this and I might even say that
in the interview I'm going to say this isn't going to cut it uh I'm going to come back and optimize this once I've satisfied all of my functional
requirements first so that's our very simple search case um the last thing that we need to
do is we need to satisfy booking so again two-step booking flow reserve a ticket and then confirm the purchase of
that so in order to do this I am going to add a new service which is going to be my booking
service and so that first request is going to come in this is going to be that kind of
reserve request that reserve request comes in and what do we do the first
thing that we do is we update our database so this is going to be a single direction we update our database here um
such that for this ticket ID remember this Reserve came with a ticket ID so for this ticket ID we'll look up that
Row in our table and then we'll update a status column so we'll add a new column for status and this is going to be
either available reserved or booked and so we'll update it in this case to
reserve served and then our user will return to the client saying success 200
and then the next request that's going to come in is that purchase request or that confirm
request it's also going to take in a ticket ID as well as those payment details right so that guy's going to
come in now we're going to use stripe a third party payment
processor um in almost all of these cases you can abstract out away the payment unless it's an interview that's
like specific for a payment team or has specifics to do with you needing to design a payment system but we're just
going to use stripe because it's interesting the the way that this works is that you actually
call out to stripe with the payment information you're going to post to stripe and then stripe is going to handle that payment asynchronously it
needs to call out to the credit card companies determine whether or not it can be paid for it happens very quickly for what it's worth but it handles that
asynchronously and then it calls back to your system not by responding to this single request but actually via uh a web
hook that you've set up so you're going to register a call back URL and you'll have some endpoints in your booking
service Wrong Way Around um you'll have some endpoint in your booking service which is exposed
for this to call back to so just good to know but but not necessary maybe for the interview the point is we'll get the
payment information we'll call out to stripe stripe will handle that reach out to the the credit card companies Etc the bank
and then respond with what happened and it's going to respond if that response is that it was
successfully able to pay then great what we're going to do then is we're going to reach back out to our database go to the
ticket table and update this status now to booked amazing and it would probably
not only be booked but we'll also have like a user ID here who actually booked it and now this ticket is no longer
available it's assigned to that user maybe we'd send them an email all of this I'm going to consider that out of scope but that's what's going to happen
in the happy path here so this is sort of our high level design but a a stute
listeners Watchers would have realized that there's something wrong with this two-phase booking process right now and
specifically what's wrong is that if a user were to click on a seat and then go to the payment page and on the payment
page they have that 10-minute countdown what happens if that 10 minutes is exceeded what happens if they just
closed their laptop and we're done they decided they didn't actually want this ticket well in our case what would
happen is that this status would stay reserved forever and what that means is that when we show users the seat map
we'd be quering our database for tickets that are available which would exclude the reserved of course and that seat
would basically just be infinitely reserved for that user which is wrong and that doesn't meet our requirements
of it needing to expire after 10 minutes so how could we handle that the first
thing that we could do is that we can add an additional call
here with the time stamp with the time stamp of when oh my gosh with the time
stamp of when this thing was reserved so reserved timestamp and now what we can do is that
when we read the database to see what's available this query would look like select all tickets where the status is
available and or excuse me or it's reserved but the re reserved time stamp
is more than 10 minutes ago so we made this query a little bit more complicated but this would absolutely work um now
this is an okay option the the one downside of this option is that you you make your database and your data model
here a bit confusing you have a status of Reserve while things aren't actually in a reserve status and you need to keep
these two things consistent with one another that sort of sucks so there's something else that we can do and we can
introduce for example a Cron job here and this Cron job might run every 10 minutes or so
and it's responsible for querying the database for every ticket querying the database for every
ticket that's in a reserve status uh and then checking its Reserve time stamp and if it's been more than 10 minutes since
the resered time stamp then it's going to set the status back to available so that's what this Cron job would do now
this works and is totally a valid approach and in fact for mid-level candidates uh this is this is kind of a
passing approach for the interview now for senior and and certainly staff principal and Beyond this wouldn't quite
be enough and the reason it wouldn't be enough is because there's a Delta that gets introduced here we'll call it n
between the time when a ticket should have been um unreserved and the time when our Crown job Ran So if our Crown
job ran every 10 minutes or so and we had a ticket that was supposed to be unreserved at noon but our Crown job
didn't run again until 12:09 then n equals 9 we had 9 minutes where this thing was should have been available but
instead it was reserved and ultimately the ticket was reserved for 19 minutes not just 10 as was expected so we need
something that's a bit more real time and to do this we can do something a bit
more sophisticated we can get rid of the KRON drob we can actually get rid of the reserve time stamp as well as well as
this Reserve status and instead we're going to introduce a distributed lock so we'll call this our ticket lock
and we can use redus uh you can use kind of any in memory cache here but what
this is going to be used for is that when a ticket gets reserved instead of updating our ticket table at all we're
just going to keep track of that here and we're going to keep track of it with a TTL so we'll have some key value pair
of ticket ID to maybe just a Boolean of true that part doesn't doesn't matter and then a TTL of 10 minutes and so that
means that after 10 minutes this key value pair is immediately going to be deleted from our database so how would this
work when a user tries to reserve a ticket from that first API request we're not going to write to the database at
all instead we're simply going to put that ticket in our lock we're going to lock that ticket for 10 minutes by
setting the ticket ID with a TTL of 10 minutes awesome now if 10 minutes
elapses or actually maybe let me not keep my head of Myself by doing that we know now things are locked and so in our
event crud service when we want to for a given event get all of the tickets for that event and see whether or not
they're available we would need to First query our database for all tickets that have a status of available and and then
for each of those ticket IDs we would need to look them up in reddis to see if they're reserved if they are we would
remove them from that list of available tickets and send it back to our client great now in the case of that user who
closed their laptop you know before they were able to confirm their payment this
is going to expire immediately at 10 minutes so if a user at 10 minutes and 1 second 10 seconds whatever it wants is
going to be queries to get our seat map again and to get the available tickets
now when we cross reference it with a ticket lock that ticket ID is no longer going to be there and as a result that
ticket is going to be available and it's going to be shown to the client for them to be able to book it easy so this is a
super easy elegant solution um to use a distributed lock here and the reason that we use a distributed lock as
opposed to maybe just keeping this in memory in the booking service is because there's going to be multiple instances
of this booking service right this isn't a single machine this isn't a single compute resource um this is going to
horizontally scale and they all need to have the same consistent singular view of the lock and so that's why we
separate this out and have it as it uh kind of as its own um in memory cache
here hopefully that makes sense this sort of the optimal the optimal answer um I'll mention just quickly
sometimes candidates will ask or want to go into an interviewer may ask like what happens if this lock goes down well if
this lock goes down then you put have the following issue one we'd immediately
bring a new one up we would detect that this is down and we would immediately bring a new one up but that means that any users that reserved a ticket in that
last 10 minutes lost their reservation and so in theory for a 10-minute window we could have several users go to a
payment page and try to book the same ticket now because this is a um a
postest DB here and we still have the the acid properties on the right to available or booked meaning one right
needs to complete before another one could read it um whoever ends up submitting that purchase first is going
to win um and the other one's going to get an error and this is a a bad user experience it sucks for those users in
that 10-minute window they're going to have a bad user experience and this is a conversation that we would have with the product team like is this okay is it
okay that in the unlikely event we have a a disaster where our lock goes down then we'll have a small 10-minute period
where we're not going to lose our consistency guarantees but our users are going to have a bad experience and I
would probably argue that that this is fine for what it's worth okay um so this is now our highle Design
This satisfies all of our functional requirements it's not perfect it doesn't scale searches is not great but we'll
handle all of that next in our deep
Deep Dives
Dives okay now for the fun part so with the Deep Dives this is where senior and
staff in particular candidates really earn their keep if you're a mid-level candidate what you have right here on
the board already might be passing especially if you got that redest lock most mid-level candidates don't get that
far most mid-level candidates land on the um on the Cron job solution that we discussed but you're close here if
you're a mid-level candidate your interviewer might ask you a little bit more about how you would scale the system they might ask about search being slow Etc answer those questions well and
you probably have this in the back um in any case especially for senior and staff
candidates this is the place where you're going to show off your chops where you're going to show off that you can go deep and your goal should be to
find one to three places where you can show off that depth I'm going to go into detail on a couple of such places but by
no means are these the only places they're not the ones an interviewer is explicitly looking for it's really up to
you to decide where you lead the conversation from here now the process that you should take when you hit the
non-functional or excuse me when you hit the the Deep Dives is to reference your non-functional requirements
and look at them and see what's missing and that should really inform where you go next with your Deep dive so we talked
a lot about how search wasn't optimized and that's the first place that I want to start and actually you'll notice that
oh I went back and added it here already um but we originally didn't have low latency search and this was a miss so
this was something that I missed originally in the non-functional requirements I realized it as I was designing the system and it's totally
okay to go back and edit it that's something that you can do and should do in the interview that's great so what's the first one that we're going to handle
here low latency search so we come back and our current solution we know is slow the current solution is slow because we
do a full table scan on a query like this so this is our API endpoint for search I'm just going to move it out of
the way I'm going to delete that and the common solution to search problems like
this is to introduce a search optimized database and a very popular one and one
that I recommend you use in your interviews is called elastic search and so the way that elastic search works
is along with other things it builds an inverted index to make searching
documents by terms really quickly so you can imagine that we have an event an
event has some text for the name and the description and maybe all of these other things that describe the event and what
we're going to do is we're going to tokenize that string or those sets of strings and create terms from them so
you could imagine that the string might be the Philadelphia Eagles are playing in a wild card match up against the
Broncos this that and the other I guess that couldn't happen NFC versus AFC but you get my point we would turn that
into uh Philadelphia Eagles playoff Wild Card all those terms and then we can map
those in a hash map of sorts to the documents or in our case the events that
those show up in so the word playoff shows up in event one event two and event three and then maybe the word
swift like Taylor Swift shows up in event five event six six and event n you
get the point and so now you have this really quick lookup such that if somebody searches in description for
playoff then we can easily return to them all the events that mentioned playoffs and show them the relevant
events based on their search term and this can be combined not just on description not just on name we would
probably search term on each of those elastic search also has support for geospatial queries it actually uses a
combination of quad trees and geohashing if I'm not mistaken don't quote me on that um but I'm pretty sure and so you
can do these sorts of things like searching for location and terms and dates at the same time and it'll use the
the varying indexes that it's created whether these inverted indexes or geospatial indexes to make it as quick
as possible so elastic search is a really effective solution to make these
search queries as quick as possible so we can delete this line and instead we'll search using elastic search
and so then the question becomes how do we get data into elastic search and how do we make sure that that data is consistent with what's in our primary
database and so it's important to note that it's not best practice to use elastic search as your primary data
store this is usually on the back of durability concerns and it has no support for like complex transaction
management um actually we use the elastic search um as a primary data
store for for our first startup and we learned the hard way that it didn't work out very well so I know this from first and
experience um so as a result of that we need some way to make sure that if
anything changes in our primary database that change gets propagated to elastic search and so there's a couple ways that
we can do that the simplest way is that we just handle this all in our application code so in this case anytime
an event is added anytime an event is added we'll write it to our postgress DB
and we'll also write it to elastic search now this puts some complex logic kind of complex logic in your
application code here because you'll need to make sure what happens if this right fails then you don't want this right to happen What happens if this
right fails then you probably need to retry this rate right or back out um
reverse that first right so there's some things to consider there depending on your product requirements but that's definitely a viable
solution another common solution that you'll see pop up a lot is using what's called change data capture so change
data capture or CDC as it's often referred to do is a process for which changes to a primary data store uh can
be put onto a stream and then those change events can be consumed and
something can be done with them so in this case anytime something changes that change event will be put on a stream we
can consume it and then update elastic search with whatever that change was so
in interviews this is often times just abstracted to be this uh you know you can just do that
Tech technically speaking like this is a large abstraction you know this is a stream there would have to be some worker that that does the right here um
but often times this is good enough in the interview you might want to clarify that this is an abstraction but that
would work well the one thing to be aware of with CDC and particularly with rights to elastic search is that it has
a limit on the number of rights that it could take per second because it's updating these indexes right in each
right so for services that you're systems that you're going to be designing for which there are a lot of
updates to elastic search then you'll need to do something smarter here like have a queue have some batching whatever
but in our case you would note in the interview that events venues performers like these don't change a lot they
hardly ever change and not only do they not change a lot but they're hardly ever added maybe at most an admin adds tens
hundreds maybe even thousands a day but that's absolutely nothing um so we don't necessarily need the queue there we can
just update elastic search on each change to our primary database so in doing that our search is
pretty dang quick this is great the introduc of introduction of elastic search was perfect I'll spend just a
moment going into how we can make this maybe even faster your interviewer might ask you what about popular queries what
about if everybody is searching for Taylor Swift how can we make that as quick as possible um so the answer to
that is usually cashing now you need to recognize that in our system we're not doing any ranking or recommendation
for users so if two users search for the same thing they're going to get the same result that's important and that's very
important to note for caching of course um and so there's a couple ways that we
can handle this the first is that for elastic search here you might be using
and you probably are using open search AWS is open search this is like a fully
managed elastic search cluster and open search supports
something called node query caching I believe that's what it's called again maybe
don't quote me look that up but I think that's what it's called and what this is is that this is a cache on each of the
instances of your elastic search cluster each of your shards um and it caches the
top 10K queries to that shard in a least recently used cache so you can enable
that I think just via the config and that's a great option quick dirty easy
and that's going to work great so that's going to of option one another thing that you can do of course is that you
could add redis or mcache here and you could cache your search term or some
normalization of your search search term as well as the search results then that would work fine as well then you just
need to make sure that you invalidate appropriately when there are updates made things like that so that's an
option another option and the option that I would probably take here just because it's it's quick and easy is that
your system probably already has a CDN uh for the static images which was scope for us but you know most systems will
have it and so we can have a CDN here
and what the CDN is going to do is that the CDN can cash these API calls so it can cach this
API call and its results and usually when you cach an API endpoint in a CDN it's for a short period of time 30
seconds to a minute or so but that way if a lot of people are searching for the same exact search term then you can just
return those results immediately by hitting that CDN which is of course geographically located close to them so
this is wicked fast um a couple downsides to note here Pros it's super
fast great for those super popular events in particular um but this becomes less useful the more permutations you
have of your search query so like we already have a lot of things here type date location if this was lat Lae then
this would kind of take this out of the picture because it would be a user's lat La that would have too much precision um
and thus we would never have any overlap two users would never hit the same but if this was something like San Francisco
okay and then turn and so like maybe that would be small enough that you
would have enough cash hits but the more query terms that you have here the more query pams the less likely you're going
to get cash hits and the more likely that you're just wasting space in the CDN so that's definitely something to
consider and then of course as I mentioned earlier if the system evolved such that it gave personal
recommendations then this wouldn't suffice because this would mean that everybody who searched the same um uh
you know search with the same API call here they would get the same results and that wouldn't be true for our system
anymore because people should get personalized results so these are all the sorts of things that you can mention in the interview um and it's impressive
just throw some of these things out there if they're contextually relevant
okay so we talked a lot about search there that's the search deep dive looking back at our non functional requirements low latency search check we
met that okay great um I'm actually going to go out of order here just because I want to focus on maybe some of
the most fun and interesting ones and I'm going to go to scalability to handle surges from popular events so let's take
a moment to lead the conversation then in that direction so the first thing that you'll
notice is taking a step back and focusing on the user experience when user comes to our website and they click
on an event they're going to see those event details about the event venue performer and they're going to see a seat map and the seat map is going to
show them seats that are available and seats that are already booked and they can click on those that are available and so the way that this would work in
our system right now is that they would query our event cred service we would query to get our event venue and
performer and then we would query to get the tickets for that event with their available or book status and then we
would need to cross reference that available or book status with tickets that might be in our lock so anything
that's in our lock needs to be moved from available to reserved or just booked so that uh the client knows that
it can't book it so we would do all of that and give it back to the client now the issue with this is that we made that
API call we loaded that up on the client and now immediately the client sees an accurate representation but after 1 second 2
seconds 5 Seconds 5 minutes 10 minutes it's grown stale and now they can be clicking on seats that appear to be
available but they're no longer available and we're going to have to immediately give the user an error and that's a really bad
experience so particularly for these more popular events that would happen a lot like a lot of people are buying
tickets so it could go sale really quickly so the first thing that we could do here is we could try to make that map
real time and this means that anytime a ticket becomes reserved or moved to book
then we update the client to mark that seat in real time as no longer available
and we could do that a couple of ways the first thing that we could do and would probably be the most simple is we could just use long pulling um so long
pulling is the client opens up uh or sends in an HTTP request and then that
request is kept open for usually like 30 seconds to a minute or so for the server
to be able to respond um and this can happen in a while loop so you kind of just keep long
pulling keep long pulling so the server can keep sending things back and keep sending things back and in our case keep the seats updated so that's one option
it would be super cheap it's easy to implement requires no additional infrastructure um especially if users
are not on this page for a long time this is great if users are on this page for a minute to 5 minutes this is
perfect if we find from our analytics that users sit on these Pages for a really long time 5 10 20 30 minutes
hours then we may need a slightly more sophisticated approach and that sophisticated approach could be to open
up a a persistent connection so your mind might have gone to websockets and
that would be an option A websocket is a bidirectional persistent connection um
but instead we could probably go for Server sent events or ssse and so while not similar maybe in
implementation they're similar and that they are a persistent connection between the client and the server such that the
server can send information to the client um not only when the client sends
a response so in the beginning open up that connection and then the CL or the server can push information over that SS
connection kind of whenever it wants so long as the connection's still open and the difference the key difference aside
from their implementation between websockets and ssse is that websockets are fully bidirectional SS is
unidirectional so it's only server to client and that's all that we need here right we only need our server to be able
to tell our client that new seats have been taken so that's something that that you could do and you could talk about this in the interview um I'm going to
set up S connections persistent connections between my API Gateway my event cred service and my client and
every single time there's a change to either of these on the status of available or booked or on my reserved
I'm going to push that change over to my client and the implementation there is actually a bit more complex it's probably out of scope for this interview
but that's kind of the degree that you would probably go into um and that'll be fine and then your interviewer might
point out or maybe you would notice proactively that this is great but when Taylor Swift the Super Bowl the World
Cup comes around the user experience is going to be that they get to that page and it immediately goes black they'll
see all these available seats and then within you know a couple couple milliseconds it's just going to go black
because everything got booked because you had 100,000 or a million people all trying to fight for the same 10,000 to
100,000 seats and so that's not great so what can we do to fix that issue now the
solution there is that we need to introduce a choke point we basically need to protect our backend Services
introduce a choke point improve the user experience by doing so and that choke
point would be by way of what's referred to as a virtual waiting queue so what you would end up with is let's see if I
can make room for this you can move all of this over
and introduce here a virtual waiting queue and so this
virtual waiting queue could be only enabled for really popular Events maybe it's admin enabled there's some config
here and an admin determines what events we should introduce a virtual waiting queue for but at a high level in
abstraction what happens is that you have a million people or so that all try to buy the tlor Swift tickets and
instead of seeing that event detail page they enter a waiting queue and they get a message that says thanks for your
interest you're in the queue we'll let you know when you're out um and they get put in this queue and this queue could
just be redis here um that would probably be a cheap lightweight implementation you can use Aus sorted
set so that it's a priority queue based on the time that they arrived other implementations make this random so it's
a bit more fair and it's not just the users who are closest to our our company servers that maybe get in first but in
any case you'll have that set and then you'll probably have some event driven logic such that you know once we have
100 seats booked we let the first 100 people in once we have 100 seats that are booked we let the next 100 or
thousand whatever it may be and you pull those people off of the queue maybe you put their user ID or their session or
you assigned them a token and you pull that off this virtual waiting queue and then you can notify the users maybe over
that same ssse connection that you created um prior that they're ready to
go and then that user can be let in and that user can book so this is actually a
really nice example where this is a simple solution it's a simple solution
but it's a sophisticated solution and it shows that often times like the best answer isn't the most technically
complex um but instead it solves the problem in a simple and maybe creative
way so the virtual waiting Q There is great um okay those are those are some
great deep Dives we can come back and look strong consistency for booking tickets we actually already covered that
in our functional requirements when we were dealing with booking we introduced our reddest lock so we we got to that one early we covered that we have strong
consistency that's wonderful High availability for searching and viewing as well as our read uh to write ratio
being in the favor of reads significantly so this is where you might just get the normal questions of like
how would you scale the system or maybe you proactively talk about it as an interviewer I usually find these
discussions kind of the least interesting and that's because here's what you're going to say you're going to say something like I use AWS API Gateway
here which is managed it has its own load balancer so this is scaling um each of these have their own load balancers
and dynamically Scale based on memory consumption or CPU consumption so these scale horizontally that's great um for
my databases here maybe you talk about sharding this would be an appropriate time actually to even do some math um
actually quick aside on math uh astute Watchers might have realized that I didn't do any back of the envelope
estimations after my non-functional requirements um this is on purpose
actually recommend this so most candidates will do some back of the envelope estimations there and it'll be things like um QPS and daily active
users and storage and at the end of it they'll go wow okay it's a lot so it's going to be a big system and then
they'll keep going I didn't learn anything about the candidate the candidate didn't learn anything that would inform their design they were just
checking a box so I considered this useless I consider this math without a purpose so math is good but my
recommendation is that you only do calculations if the result of the calculations will have a direct influence on your design and usually the
right time to do that is either in your high level design or in your deep Dives so for example maybe I do some math here
now and I won't because I don't want this video to go a little uh too long but I could do some math to see what the
storage is here in this postgress DB to make a determination as to whether we need to Shard or not or it could fit
into uh you know a single postgress instance and so if I came to the conclusion that we did need to Shard
then I would have a conversation about what I need to Shard on and maybe that's event ID because that's what the majority of my queries are in or if
we're sharding and then Distributing these shards geographically maybe I do it over venue ID if there's High
correlation between people searching for events that are in venues close to them
then maybe that makes sense too so you would weigh that um again no wrong no
right answer it's a discussion maybe to have with the interviewer weigh the pros and cons but that's something that you could talk about there too so that's the
general scaling conversation and then given that reads are so much higher than wres another thing that we could do is
to reduce the read load on our postgress DB here and especially because event venue and performer never change or very
infrequently change it makes them a great candidate to just cash them to hell so we could have reddis
here and we can cash those events venues and performers in reddis make sure that
if we make any updates to our database then we'll have to invalidate or update our cash as well there doesn't need to be an eviction policy like least
frequently used or least recently used or anything because we can probably fit them all in there um or maybe we just do
events that are you know upcoming or within the last four months and in the
next 2 years whatever it may be you introduce some bounds there but now this makes this view API call this one wicked
fast because we can just cash a key value pairer of an event ID to the event
venue and performer relevant to it and then we only need to make a query to get tickets cuz that's the one that's
Dynamic so we'll we'll not cash that one in this case awesome um okay so that's a little
taste of some of the deep Dives that you could do I think what we end up here is a pretty solid design if you did this
you certainly passed a mid-level interview uh with flying flying flying colors this is overkill for a mid-level
interview by far you definitely pass a senior interview that's great you probably pass a St interview um
depending on how well you executed how well you were able to answer some questions and if you showed some depth in other places um and you know
principles usually evaluated at the same level of staff so you pass that as well um okay last
thing here is that when you conclude you should be able to look at your design concretely and you should be able to say
does this satisfy all of my functional requirements and does it satisfy all of my non-functional requirements if you
can say yes to both of those things then you should feel confident just put your hands up you should say I know I passed
this interview I can't wait to get the call back obviously don't say that um and you're probably hired so that's the
the process that you should follow all right thanks everyone for
Conclusion
watching I really hope you found this valuable uh if you did let me know in the comments I want to do more of these and uh if people are finding value out
of them then that'll encourage me to keep pumping them out um also if there's anything that I did wrong uh if you
think was silly was a bad design decision or if you just have general questions please leave those in the comments I'd love to chat about it um
but thanks so much for watching and good luck with your upcoming interviews take care
