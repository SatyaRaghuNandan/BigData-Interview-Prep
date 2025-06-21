Intro
hi everyone welcome back today we are going to break down another really common system design interview question
this time it's going to be design Dropbox um this is also referred to as design Google Drive sometimes they're
largely the same question it's a super popular question it's asked that all of the top fangs really popular at Google
and Amazon shows up a ton at meta as well um so by way of introduction just quickly my name is Evan I'm a former
interviewer and staff engineer at meta and I'm the current co-founder of hello interview
and hello interview is a company that helps candidates prepare for their upcoming interviews at Fang companies
and this is largely via mock interviews with current Fang interviewers so between asking this
question at meta and asking it at hello interview I've probably asked it I don't
know maybe around 50 times um and I have a really good understanding of where candidates do well and where they trip
up and this is candidates of all levels um so we're going to walk through this as if it's a real interview but of
course I'm going to periodically teaching jumping in with tips sharing the perspective from an
interviewer this question is a little bit on the easier side so it's asked most frequently of mid-level candidates
this is E4 L4 candidates but it also shows up a ton for senior and even staff
candidates so useful for all levels and I'll call out the Deltas as I mentioned um as it pertains to leveling as we go
lastly if videos aren't your thing you don't want to sit here and listen to me for an hour you can head over to hello interview.com where I have a detailed
write up sorry I was on the wrong page there I have a detailed write up of this very question um so you can come over
read through this instead this will be linked in the comments below and then that page that you just saw there is
that you can come here if you want to suggest whatever you want us to break down next and I'll continue to try to
make videos for each of these that we break down so come over here propose a new system design interview question and vote for the one that you want to see
next uh we'll break it down you know every two weeks or so we'll do a new one
awesome okay well without further Ado let's get into
The Approach
it all right before we dive in let's take a moment to talk about the approach to the problem this is the road map that
we're going to follow here today and it's the road map that I suggest that you follow for any of your system design interviews for which you're designing a
user facing product like Dropbox is so we're going to start by defining the requirements the requirements will
consist of functional requirements which are the core features of our system as well as non-functional requirements
which which are the qualities of our system and then we're going to move on to defining the core entities that are
persisted and exchanged via the apis which leads naturally to us defining
those user-facing apis before we move on to our highlevel designs this is where we'll draw our
boxes and arrows in order to sketch out a highle design whose primary goal is to satisfy those core functional
requirements those core features of the system so at this point it should be relatively simple and then we're going
we're going to move on to our last step which we call Deep Dives and this is where we go deeper in order to expand on
our highle design and make sure that the system is able to scale Vault tolerant
all of those things which we'll see when we Define our non-functional
Requirements
requirements so first up is those functional requirements again these are the core
features of the system so what is the product supposed to do you want to take this moment to identify those top three
features um now if it's a system that you know well this should be pretty easy if it's a system you don't know well
then this is the time where you would ask the interviewer some questions in order to better understand what the requirements of the system may be now in
our case for something like Dropbox they're pretty straightforward we know that we need to be able to upload a file from remote storage for example or to
remote storage also download a file this case from remote storage and then we want to be able to automatically sync
files sync files across devices so this is the
case where if anyone's used this feature in Dropbox you set up a local folder on
your local machine and your local desktop um and then anytime it file is uploaded to the remote storage it's
automatically synced with your uh local file system likewise if you were to drag and drop a new file into your local
folder then it should be automatically uploaded to your remote storage and then synced with all of the other connected
local devices um so hopefully that makes some sense we'll talk about of course how to implement this and then one thing
worth calling out here is that this system is not going to require us to design or roll our own blob storage um
so that's actually a different system design question that sometimes ask design S3 or something similar so we're
going to just say that that's out of scope so out of scope is you know roll own
blob storage cool and then next up we have those non-functional requirements
so the nonfunction requirements are the qualities of the system so these are the things that you're you're used to
reading in your books of low latency fault tolerant durability we talk about cap theorem here all of those things um
but most candidates overlook this they Breeze through it they write some generic words and it's entirely
uninformative and so for senior and staff and up candidates in particular the non-functional requirements are so
important because these are what's going to inform or lead your deep Dives later on and your depth is necess NE for you
being able to be leveled at those higher levels senior plus so for example here
um the first thing that we can talk about as we usually will is Cap theorem do we prioritize consistency or
availability in the context of cap theorem of course partition tolerance for the scale system we're dealing with is a must so in this case we're going to
prioritize availability over consistency so availability is more important than
consistency in this case but importantly we're going to put that in the context of this system
so what does that mean here it means that it's okay if we upload a file or we
change a file somewhere else in the world say Germany and somebody in America goes to read that file shortly
afterwards and they still see the old version of the file that's okay that's totally fine within our system and we're
willing to take that compromise such that everybody can still download a file
when they request download view whatever it may be when they request uh to download or view that file respectively
so in our case availability is much more important than consistency uh some other things that we
want to consider in our non-functional requirements is we want to have low latency uh uploads and downloads
respectively right so in this case it's not just low latency that's the buzzword it's what in the context of the system
uploads and downloads and then we'd want to quantify it so how much time now in
this case we don't know cuz files vary so I'm kind of going to take a cop out and just say as low as possible
possible um and then the next thing that we want to consider here is that we want to be able to support large files and
this is something I can quantify I want to say as large as 50 gigabytes this is actually exactly what Dropbox supports
um and then as part of that we should have resumable uploads so this is the case that if a user tries to upload a 50
gab file that can take some time if they system or they lose their internet whatever it may be halfway through that
download we don't want to make them start over that would suck we want to allow them to pick right back up where they left off uh and then another one
that we're going to add in here is that high data Integrity is really important um so this basically means our
sync accuracy is high so yes eventual
consistency is fine it can take a couple seconds but by the time things have stabilized into a consistent manner the
Integrity of our data should be high meaning what's in one folder should also be in remote storage should also be in
another folder hopefully that makes sense so these are the ones that I identify as particularly important these
are what are going to lead our deep Dives we may come back and add to these as we're going and this is normal to do
in an interview as you're going you might think of new ones come back keep it updated that would be
Core Entities & APIs
great now just quickly before we move on to the core entities in the API I want to call out that you'll notice I didn't
do back of the envelope estimations yet and I actually don't plan to up front here here and this is generally my
suggestion it's good to get an understanding of the scale of the system up front in this case we're talking about Dropbox scale talking about
hundreds of millions of daily active users and as it pertains to storage we're going to use some nearly infinitely
scalable um Technologies like S3 or or other Cloud hosted blob storage Technologies so it doesn't matter too
much there now estimations are important I don't want to um kind of belittle them
and you should use them when you're actually within your high Lev design so you should do a high level estimation
when the result of your calculations is going to have a direct impact on your design that's the general guidance that I give and typically it's hard to know
that up front and candidates here will just do some daily active users and some total storage and some bandwidth
estimations and then go wow that's a ton and then keep moving on with their day um and that's a waste of time it didn't
inform the design uh and I didn't learn anything about the candidate other than they can maybe do multiplication or
division so that's my suggestion as always overc communicate with your interviewer if you're going to take that
approach tell them that's the approach that you're going to take I uh kind of Highly expect that they they won't
disagree with you um but it's worth communicating that anyway let's move on
now to our core entities and API so core entities here I know other people will
refer to this as data model or data schema the reason that I say core entities and I choose this word
intentionally is because often times at this point in the design you know we're only 5 minutes in I don't know all the
columns I don't know my full scheme I'm still trying to figure all of that out but what I can take a moment to do is
just sit down and really think about what core entities or objects are persisted and exchanged um within my
system and so in our case the main one is that we know there's a file and this is like the the raw bytes of the file
we're going to store those in S3 or some other blob storage and then importantly we also know that there's file metadata
so this file metadata is going to have things like the file name the ID mime type size whatever else right uh and
then lastly and maybe most least importantly in some cases maybe I recommend you don't even put this because it's more of a distraction than
anything else but of course there are user objects within our system so if you're feeling comfortable at this point
to outline all the columns and in the case of Dropbox it's pretty simple the only ones that we would have would be
file metadata having those that I just talked about you can go ahead and just do it in line now I opt not to um and I
end up documenting the full Fields or columns directly next to my database while we're doing the high L design um
so that it's easy for me to keep it up to date and you guys will see that a little bit later on but those are the
main core entities really straightforward now as we move on to the API you'll see everything is growing on
each other so we're going to use those core entities as the kind of inputs and
outputs of our API and we're going to make sure that we have an API endpoint or a handful of API endpoints that satis
y each of our functional requirements that's the goal here do we have a user facing API that can satisfy each of
those functional requirements so let me make sure that they're in view so the first one that we're going to have is we
need to be able to upload a file so this is going to be a post files um and maybe
the body here is going to be the file and the file metadata so you can kind of see this nice abstraction where I might
not know all of what's in the file metadata yet but I know that it's going to need to be passed in here and what
does this return I don't know the 200 um and then what else we need to be able to
download so we're going to have git files and this is going to take in a file ID as a path parameter and what's
it going to return it's going to return the file and the file metadata associated with that file cool so super
easy right let's keep let's keep moving here the next one that we have is that we need to be able to automatically sync
files across devices now that's going to require calling our upload and download
endpoints respectively but we probably also need to know if something changed like you can imagine that in these local
folders or at least our local clients they're going to be calling and asking hey what's changed and once they get a
list of what's changed then they'll be able to upload or download respectively um so I'm going to call
this git changes um it's going to take in some Tim stamp this is going to be uh
you know the time that we want changes from and what's it going to return well this is probably going to return and
this might change as we design but I'm going to say like it's a list of file IDs like these are the ones that have
changed this is what need to be synced and so we can take those file IDs and then call our download for each of those
file IDs uh in order to to update them locally so a couple things here to call
out one there's shorthand going on this is great uh a lot of candidates spend too much time in the API by being able
to reference your core entities you can move quicker I think that's important um these make sure that they satisfy our
three functional requirements in this case it was one to one mapping it's not always the case but it was convenient here um but some astute viewers are
going to be pointing out these API endpoints are kind of wrong um and that's actually true the the API
endpoints in order to upload a file for example is not going to be a single post files upload like this but at this point
in the inter interiew most candidates from my experience and how many times I've asked this don't know that and
that's okay so we're going to show how we'll need to come back here and update these later on as we go through our high level design and we go through our deep
Dives we'll find out that these API endpoints actually need to be a bit more complex they needs to be a bit more
going on but this is our first guess and so we're going to run with this first guess and take this into our highle
design and then we'll come back and we'll amend them as needed um the last
thing that I'll say which I I've said in the first two videos is as well is I'm careful to not put user explicitly here
in the body of course we'll want a user ID on upload but I usually just mention verbally to an interviewer that the user
ID is going to be present in the request via the header either via a session token or a JWT so that's where we're
going to get the user information um it's minor most interviewers probably won't care some will but of course this
is a security concern it means that anybody could falsify a request here and upload or download a file on behalf of
another user so something minor there all right let's move on to the high level
High Level Design
design all right now it's time for the fun stuff so let's start sketching out our highle design and as a reminder the
goal of our highle design is to satisfy these three core functional requirements now conveniently so too did our apis our
apis satisfied those core functional requirements so actually the natural thing to do here is just go one by one
through our apis so being clear about what the user input is and then making sure that our system can satisfy the
requirement and return the expected user output so let's go ahead and do that I'm going to draw the design over here to
the right I'm going to start with a simple oh what is going on here I don't want
any fill okay uh I'm going to start with a
simple client box I'm going to introduce a this is going to be the load
balancer and the API Gateway uh this could be AWS managed API Gateway but
this is going to be responsible for handling some of that middleware like authentication rate limiting SSL
termination uh and then importantly routing so in a microservices architecture this guy is going to be
able to take those API endpoints and Route them to the correct service so we'll collect our client to our API
Gateway and now we're Focus strictly on this upload files API here so we're
going to introduce some file service I'm going to call
it and when a user goes to upload a file let's say this is our post I'm actually
going to do this in shorthand to make it clearer maybe I'm going to call this
upload so when a user goes upload a file it's going to hit our file service and then at this point we're going to have
two things we're going to have our file and we're going to have our file metadata metadata all right and so we
need to store both of those now we wouldn't store both of those in the same storage technology in the same database
and the reason for that is they're very different in nature so often times when it comes to raw files or the raw bytes
of the file not often times this is almost every single time we want to store those in Blob storage blob storage
is optimized for being able to store cheaply these large Blobs of byes these
large Blobs of data so in this case we're going to use S3 um so we're going to call it blob
storage and this could be any that you want if you want to use gcp that's fine too I'm going to use S3 in this case so
the first thing that we're going to do is we're going to uh upload file and then once the upload is
complete this is going to return with the link to where we can access that file in S3 so then import importantly
we're going to have this file metadata DB and after the upload is complete
we're going to write to our file metadata so write metadata and that metadata is going to
look something like this so we have file metadata we're going to have a file ID
we're going to have a file name uh we're going to have that mime type this is
like uh the type of the file is it a PDF is it an image Etc we'll probably have the size in bytes uh um you know of
course we'll we'll have the the owner ID this will be a foreign key to our user table um potentially shared though we
specified that it wasn't in the scope of our requirements um and then importantly
this is where we'll have that S3 link this is a link back to where the file is actually stored in Blob storage and then
I'm going to do this as Shand of course we'll probably have some other less important metadata but this is the main
content uh that we'll want to store now as I mentioned earlier I'm putting this directly beside my database because as
we complete the rest of our API endpoints we may find that there's other stuff needed here this makes it nice and handy we can just kind of update it uh
in line which will be great and so I'm also going to write here storing the raw bites of the files so storing the actual
files themselves great um so client uploads go
to the file service upload the file itself to blog storage save the metadata and then return with a 200 that the
upload was successful of course any other error code um if there was a failure so that's the first one pretty
straightforward now the next one is is equally a straight forward this is git file given a file ID and this is going
to go in the same path so I'm now going to have that git file and it takes in a file ID and it's going to hit our file
service it's going to use that file ID to look up the relevant metadata and
then that's going to give it an S S3 link so we'll go get the actual file from S3 and then we can return it to the user
and so what would actually happen here in practice is that we're going to get this file metadata we'll return that metadata directly and then we can
download from S3 so maybe we'll go like this we're not going to download to our
file service once and then download again to our client um so in this case it's download directly from S3 using
that S3 link that was returned via the metadata so there's other optimizations
that we can make here and we'll actually need to make to this upload download path and we'll talk about that in our
Deep dive but this is the the simple version here so at this point we can upload files granted small files but we
can upload files and we can download files in in the case of download we'll download them directly from S3 so great
super straightforward there now let's focus on our last and most interesting functional requirement the one to
automatically sync files across devices so the first thing that I want to note
here is that we often times just just put this client box nice and small and Abstract out the client for these system design interviews and that's appropriate
most of the time but for some systems this one being one another being those
that require streaming and adaptive bit rates like uh Spotify Netflix YouTube Etc there's actually Logic on the client
which is really important and we want to reflect that so let me let me demonstrate that um by making this
client box a lot bigger so that we can put some things in it right make it meaningful so this is our client and the
first thing that I want to make sure that I uh the first thing that I want to make sure that I put in it is we're
going to have our local file or our local folder I'll call it so this is the folder that we're syncing all right so
that's the first thing that's here and then the other thing that's going to be on here importantly is that we're going to require that users download some
client application either on their Mac or on their iPhone or Windows machine or or whatever it may be right so we have
some Client app and this client app is going to to be responsible for syncing
remote and the local F the local folder here right that makes a good amount of sense so let's break this down what does
it take to do this um file syncing uh in
the most simple way so there's two types of syncing directions maybe we can call
them the first is that remote changed and in the case we're remote changed um
we want to make sure that we can pull in those changes so we can pull uh for changes periodically maybe and
then we want to download the new file download new file and replace the old potentially excuse the kind of
misspellings I'm just going to run with it anyway and then the second thing that we want to do is what happens if something
happens in the other direction so if local changed so if local changed then
we need to upload the changed files to remote right so pretty straightforward
those are the two things that we need to be able to handle here and so let's talk about how we would do it um simply so
let's start with maybe uh remote changed so in the case that remote changed let's
do this I'm going to add a new server this is going to be our sync service and
so some strong arguments as to whether or not we're over modularizing here by separating these two I'm I'm going to just kind of look past that for now
especially since this service will grow in complexity during our deep Dives but we're going to have that git changes API
here and so that AP is going to look for anything that has changed maybe it's going to directly ask the file service
um to query its file metadata and tell us the IDS of anything that changed importantly that means that we
need some additional data here right we probably want the creation Tim
stamp U but then we also want the update timestamp right and so this way we can
just query our file metadata see which files have been updated we'll get those to our sync service our sync service is
going to respond with the IDS that have been updated and then our client app is going to download so it's going to ask
for the file metadata from each of those IDs get that metadata and then download directly from S3 all right so you might
have just noticed we had an additional round trip we had the G changes then we did the download so potentially you want
your sync changes to not just return the ID here but to return the full metadata so you can go and download directly
without that additional call um that seems reasonable to me this will all still evolve in our in our Deep dive
but if I just noticed that in an interview I would say that seems reasonable and I would come here and say that we return the full metadata so our
sync service gets the metadata of any file that changes and then our client app will download them put them into our local folder uh replacing any ones that
already existed there okay easy um the next one local changed so in the case
that local changed we want to upload those Chang files to remote right so if local changed we're going to notice that
and the big question is how do we notice that and the answer is that natively each of these operating systems provide
an API in order to watch uh changes to a folder or
directory so actually let me write those down in the case of uh Windows they
offer something that's called file system Watcher so you can look this up on your own time this is just an API
that's exposed by the operating system which is constantly L watching any changes to a local directory and then
based on changes to those directory you can of course do something um and then in the case of Mac what is it in the
case of Mac OS API it is called FS events so there's an object exposed
called FS events which has itself a handful of endpoints um such as watching from a local folder so in our client app
we'll have some code depending on which client and operating system the client's downloaded on in order to see changes
when a change occurs we will then upload them via our normal upload path and we'll just need to make sure that we
make any updates here so maybe we reupload to S3 change the S3 link and
then update the uh the update time right that's a real simple simple way to handle
this now one question you may be asking is how do we know for example that when
remote changed and we pull for changes how do we know that we don't already have that file in our local in our local folder in our local file system that's a
great question and the truth is that our client app is actually going to have to have something else here and so maybe
I'm actually going to represent this visually um we are going to need to have
some I'm going to call this a local DB so we're going to have some local database which has the metadata
including the IDS and some of the additional information um about each of the files that are in the local file
system so when a new file is updated we can look in that local DB in order to determine whether or not we've already
downloaded uh that file ID and if we have downloaded that file ID then we'll have kind of a reference from that file
ID to wherever it is in our local folder so there's going to be some important stuff that we'll talk here about what's
called fingerprinting in order to hash and identify a file as well I'm going to save that a bit for the Deep Dives but
this is kind of the simple way that we would do that we had some additional local database we're able to look here
and cross reference the metadata that's stored here with any of the metadata that's stored in remote and we'll want to make sure that those two things
remain as consistent as
Deep Dives
possible all right so our highle design is in place and as a reminder if we look back at our road map the highle design
was simple but did a good job to make sure that it met all of our functional requirements now our last step in the
process is to lead some deep Dives and this deep Dives goal is to make sure that we satisfy our non-functional
requirements and so how deep you go here and how proactive you are in leading is largely a function of your seniority
for example if you were a mid-level candidate then what you have here is is pretty good this is close to getting
hired to be honest um but the interviewer May jump in now and ask you some questions lead you in the right
direction some follow-up questions and and hope that you have competent answers too now if you're a senior engineer or
of course a staff engineer then you'd want to continue driving the conversation at this point you'd want to
come over here to your non-functional requirements as we'll do here in a second go one by one through them and make sure that you can enhance your
design in order to to uh ensure that they're satisfied and kind of go deep in each of the respective areas so for
senior candidates you want to go deep in maybe one to two places uh for staff candidates you want to go deep in two to
three places um and of course the level of depth should be increased you should have more hands-on experience the more
senior you are and as a result you should be able to to go deeper on each of these components so let's do this now
I'm going to go deepen maybe more areas than is necessary in an actual interview but this is illustrative um it's more so
to teach as opposed to adhering to exactly what you would do in a session so let's come
over here I'm actually going to go out of order I'm going to start with supporting large files as large as 50 gigabytes and resumable uploads and
you'll see why I do this in a second it actually will have consequences on some of our other non-functional
requirements so let's come over back to our design and talk about why this wouldn't work and actually I would point
this out to a mid-level candidate as an interviewer I would say this Design's great um but it actually won't work for large files this design would only work
for files as large as 5 to 10 megabytes and there's a reason for that so there's
two issues that we currently have when we want to upload large files Let Me Maybe start tracking here so upload
large files and I'm going to say 50
gigabytes so the very first issue that we have is that this upload path is
actually redundant so we upload the file once to the file service and then we upload it a second time to blob storage
it's a waste of bandwidth it's a waste of CPU resources here on the server so it's entirely redundant and unnecessary
it's kind of issue one and then issue two is that we couldn't even upload this through this path if we wanted to and
the reason for that is that request bodies have a limit this limit is often
times set by browsers it's set by servers it's set by the API gateways respectively such that what can be in
that post body in our case we're sending over the bytes of the file in that post body can only be so large so if we were
using for example AWS managed API Gateway here it has a limit of 10
megabytes in that post body so a 50 GB file is obviously far larger than that
we couldn't get through here anyway we would get an error so those are the two
issues let me start with the first one because it's the more simple to address and then we'll talk about how we can handle uh the bottleneck introduced here
so the first thing when it comes to making sure that we don't have this redundant upload path in this waste of
bandwidth we can actually upload directly to S3 just like we download it directly from S3 but the issue that we
run into is how do we know how to how to upload directly to S3 we don't want to
make it so that everyone can upload D3 that would be dangerous and so what we do is when we want to upload a file we
send just the metadata not the bytes of the file this time just the metadata to our file service which writes that
metadata to our file metadata DB it probably updates it's a field like status to say started or something like
this this is nice to have my schema right next to my database for this reason you see how we kind of continue to evolve it as we as we follow walk
through the flows but we're going to update the metadata and then instead of uploading the file to blob storage we're
going to actually request a pre-signed URL and so what pre-signed URLs are are
they're basically us asking blob storage with our authentication that we had from the file service we're an authenticated
user we say a blob storage I want to upload a file of this mime type like PDF or whatever else it's of this size and
then blob storage gives us a secure link and that secure link basically has some additional metadata at the end of the
URL which is signed by S3 which ensures that the file that can be uploaded is
only of that MIM type only of that size and it's only uh available for a limited period of time you can basically only
upload to this link for a short window actually don't remember what S3's default is there but let's say 10 15 30
minutes or so so we get that pre-signed URL and we return it back to our client and then our client can actually then
just directly upload directly to S3 with that pre-signed
URL so basically in that um rest call to upload the file we're not going to do it
um excuse me in that rest call to upload the file we're not going to do it to our own API endpoint to hit our own servers
we're going to post it directly to that pre-signed URL so we can upload directly
S3 so fantastic that solved the first issue no problem um but we still have
the issue of if this is a really large file than one this is going to take a
huge amount of time right so we could do a little bit of math there and we would find that you know to upload a 50
gigabyte file at an average internet speed of 100 megabits per second this is
going to take us 1 hour and 12 minutes I I did that math you know just before filming this so that you guys wouldn't
have to see us do it in line but that's good math to do at this time right so this would take an hour and 12 minutes
that's a long time and so from a user experience perspective it would suck if I got halfway through this upload and
then I lost my internet connection or something failed or anything else and I had to all of a sudden completely
restart that would be a bummer so the way that we handle this is we use something called chunking chunking is
what's really important here so what we do is we can chunk files on the client
so chunk files on the client to something like f 5 megabyte chunks these are smaller chunks and so if we
have a 50 gigabyte file here we'll create all of these 5 megabyte chunks and we'll update those chunks or upload
those chunks directly to S3 one after another either serially or in parallel depending on what our bandwidth is so we
can upload each of these chunks and importantly as we're uploading those chunks we also need to keep track of the
status of what chunks have been uploaded and this is so that of course if we fail we can compare the chunks that have been
uploaded to the chunks that we have in the file and only upload the ones that are missing and so in order to do that
we would need to update our file metadata over here to store those chunks now we didn't talk about what database
this was yet and to be honest it it could be either or any of the common SQL or nosql databases actually slight aside
the debate in an interview between whether you use SQL or no SQL is is kind of outdated at this point these
technologies have come a long way they've converged and such that when well configured they can largely do the
same things so I'm going to forgo that argument because I think it's uninteresting it could be no SQL it could be SQL if it was a SQL database
like postgress or something then we would use normalization and we would have another chunks table over here that
has our chunk information with some foreign key back to the metadata I'm actually going to opt for going with
Dynamo DB no SQL database um and I'm just going to add it directly on this
object then so I'm going to have a chunks and it's going to be a list of chunks and so what chunks are going to
have then each specific chunk item in this list is going to have an ID it's
going to have maybe the status and it's going to have you know its own S3 link right so we have a list
of all of our chunks so step one we took our 50 gigaby file we chunked it we sent
that with our metadata and we said here are all of my chunks and maybe all of their status at this point is not
started then we start uploading each of those chunks either in serial or in parallel to S3 as they get uploaded we
can upate update this status to success uploaded and update the S3 link now when we want to resume an
upload because it stopped halfway through or any other reason we simply need to request our file metadata get
our file metadata and compare the chunks from the file on the client to the chunks in our file metadata and only
upload the ones that are missing now importantly you might be
pointing out that well how do we know how do we compare the chunks here to the chunks here we need some unique way of
saying that this chunk that I have here is the same as a chunk that you've already uploaded and so we could do
silly things like maintaining indexes um this is not great it's Error
prone and instead we need a unique way to be able to identify a chunk and to track that chunk identification
and what we end up using here is something called fingerprint something called fingerprinting so we can
fingerprint each chunk and what fingerprinting is is it's just a hash of
the bytes of the file or the bytes of the Chunk in this case so step one chunk the files step two calculate their
fingerprint by running a hash over their bytes this will give you a unique ID and then this fingerprint is actually what
we're going to store here our ID is the fingerprint and so now when we we want
to uh check to see if any files have been uploaded we're just going to compare the fingerprint of the chunk that we have here stored in our server
in our database to the fingerprint that we've calculated on the client and if there are any fingerprints any chunks on
the client that have not successfully been uploaded as determined by our file metadata then we'll reupload them right
um okay hopefully hopefully that makes sense just to recap what we're going to do here when we want to upload a file is
we're first going to store our our file metadata and all of the chunk data with their fingerprints as um you know
started or not uploaded we're going to request a prend URL from blob storage we're then going to upload directly to
that presign URL now there's one last thing before we move on to another Deep dive actually um that I handwaved and
and that Watchers might have noticed and that's when I'm uploading chunks to S3 how do I know to how to update the
status how do I get that information back to my database here in order to update the status of that chunk and the
reason that this is an issue is because there's a couple ways to do it but the obvious way is insecure so the first
thing that we would do is we would upload a chunk we'd get a response from s saying that chunk uploaded then we would rely on our client to make an
additional request to our server a patch put whatever it would be in order to update our file metadata to say complete
now the issue with this approach is that we are directly relying or trusting our client client and our client could lie
to us right so this could be some malicious user for some reason and they could tell us incorrect information that
a chunk either was or was not uploaded successfully and then our status would be inconsistent with what actually
happened in S3 now there's a strong argument here that would say who cares hackers could
only mess up their own file upload so let them do it but of course having inconsistency between our metadata in S3
isn't ideal it's going to cause headaches for the engineering team to debug and Etc so instead of directly
trusting the client we can use a pattern called trust but verify and so when a chunk is uploaded to S3 we respond
saying success or S3 respond saying success the client then says this chunk was just successfully uploaded to the
file metadata service the file metadata service would then check with blob storage hey I just want to confirm the
client told me this chunk was uploaded was it s will respond and then we can update the status in our file metadata
so that pattern is called trust but verify and that's really useful here the other option which could be considered
is that most blob storage um you know Cloud providers
enable some version of change data capture so basically you can have some notification that's triggered off of
blob storage when something happens S3 uses something called S3 notifications so you could have
something here that would be S3 notifications that anytime a new chunk
is uploaded here then it would notify our file service hey a new chunk was uploaded and then our file service can
update our metadata this way we're not trusting or relying on the client at all
and so this is fine this is good this would work maybe it's added complexity there are pros and cons trade-offs to
way this is the interesting stuff to get into in an interview it is worth noting that this chunking and uploading is
actually really popular so like S3 for example just exposes an API called multi-part upload which does this stuff
that we're talking about it handles the chunking on the client the uploading the fingerprinting the comparing of fingerprinting to validate Etc and if
you were to use S3 multi-part upload then you would run into a situation where actually on each specific chunk of
the multipart upload blob storage doesn't support an S3 notification so Nuance there I don't want to go into
more detail but I know some Watchers might call that out this is an option if you didn't use multiart upload you'd probably want to use multiart upload so
you wouldn't use this all in all the trust but verify approach is the approach that I would probably go for in
an interview but both options are great okay for our next Deep dive let's go
ahead and talk about low latency upload and download as low as possible we've actually done a lot of the hard work here already this one should be pretty
quick so chunking actually helped a lot here um Beyond you being useful for the
resumable upload stuff that we just did uh it also helps us speed up this uh
upload process in particular so while bandwidth is fixed meaning that the the
pipe is only so big um chunking helps us make the most of that available bandwidth
so by sending multiple chunks in parallel in particular we're able to use like adaptive chunk sizes uh based on
the network condition and we can maximize the uh amount of bandwidth that we use basically use all of the
bandwidth that's available to us so that helped us speed up upload already a bit there's a couple other things we could
talk about a CDN and that's a common thing that candidates like to do is they like to talk about adding a CDN here why
does that keep happening um they like to talk about adding a CDN here and cdns are great they definitely bring the the
content closer to the um to the users speed up the download process in that way but maybe top candidates bring up a
really nice point when they talk about the CDN here where they weigh whether or not it's necessary so in our case
there's a strong argument that it's not and the justification here would be that users are mostly only downloading their
own files and so by downloading their own files they're likely located close
to the data warehouse or the servers you can imagine that we have this exact thing that you're seeing here replicated
all over the world right we have maybe five data centers or something and so the benefit of the CDN is that even if
your data is in one data center one of the benefits of a CDN um but you are out in Germany you'll be able to download
that content from the CDN in Germany and it'll be super quick and we probably don't have that usage pattern here um so
it's it's much less relevant it would only apply if a user is really traveling
or if a given file is super were super popular so if we had a ton of sharing and maybe for some reason the Declaration of Independence was in our
Dropbox and people over the world were viewing it or whatever then the CDN would be great um it certainly would
speed things up you could get closer to the user a bit um even considering what I just said but it's expensive CDN are
pretty expensive to manage so pros and cons here there's no right or wrong answer I'm going to opt for maybe not
including a CDN just because of that reason but it's a good conversation to have now another thing that we can do in
order to speed up the upload and download process respectively is we can transfer fewer bytes how can we transfer
fewer byes over the network we can use something called compression all right so compression takes a file compresses
it runs an algorithm on it this is like gzip you've ever used on your computer I'm sure you have it compresses it into
smaller into something smaller into fewer bytes and by sending fewer bytes over the network of course uploads and
downloads are going to be quicker now we don't want to just arbitrarily compress things though there's a downside to that
we have to decompress them which makes things slower on the other side so there are some file types that compress a lot
like text files I know to compress really well docx files maybe things like this but there are other file types like
media types um like jpegs pngs movs MP4s
Etc these are already naturally pretty well compressed so running a compression algorithm on them is only going to gain
you a couple percent uh decrease in the size of the file which isn't worth it considering that you know we have the
added time that's going to come from the compression and the decompression so you can end up doing some kind of intelligent compression logic here on
the client again based on the file type based on the network conditions should I compress or should I not compress um and
then you know maybe we add to our file metadata then compression algo if we did compress we would need to specify what
that compression algorithm was so that we could decompress respectively okay um I think that's just
about all there is to speeding up uploads and downloads relatively straightforward there the chunking helped a lot of course the CDN is a good
conversation to have and then potentially using compression algorithms but they don't make sense in every case
certainly not for every file type okay let's go into our last Deep
dive now and that's going to be this High data Integrity for sync accuracy maybe more generally let's just talk
about all the ways that we can improve um this sync between our local folder our local file system and our remote uh
repository or remote file system so when it comes to uh syncing there's two
things that are that are important to us we talked about the remote change we talked about the local change now let's talk about two potential optimizations
so deep dive on sync the two things that we care about is the first one is how can we make sync fast so we want this
thing to be as fast as possible uh this is within reason of course but what this means is that when something changes on
remote we want it to be reflected on our local folder kind of as soon as possible again within reason so that's the first
one and then the second one is that we want sync to be consistent and so what this means is
that whatever is in our local folder should be what's in remote whatever's in remote should be what's in our local folder so we're going to talk about
these two things and some optimizations that we can do for both respectively let's start with talking about how we make sync fast and so the
first thing is how can we know when there's changes we had talked about periodically pulling for changes and to
be honest I think this is still the best approach this means that the client here can just pull the database to know when
something is changed and we can play with the frequency in the intervals so if they have their client app open if
there's been a lot of changes recently if they're playing around in that folder maybe we increase or excuse me decrease
um the Delta between our polls so increase the frequency of our polls how often we're checking to see if there
were changes um that can be kind of like adap adaptive polling the other option
that candidates often times bring up is either websockets or sometimes even long pulling these are options but they're
they're totally Overkill right you're not going to want to set up a persistent always on connection between your client
in your remote server here when it's kind of always open right literally always open because it would be open
anytime um you're using your computer and it introduces a bunch of additional overhead you need a websocket manager
you need to be able to maintain that it's over coal kill for this system and from a product requirement perspective
like do you care if you see the updates within seconds or within milliseconds um or is it okay if you see them within
tens 20s seconds a minute whatever and of course on The Client app we can always put a refresh button so if you
really need that file there you can click that refresh button and it'll kick off a poll if that poll hadn't happened yet so in my opinion that's Overkill
long pulling doesn't make as much sense either long pulling is when you're going to make a request and then you're going to keep that request open for about a
minute or so for the server to be able to respond this is when you're expecting a response or several responses but
still within a relatively quick window there that that minute or so window and that's not the pattern that we have here
we don't know when changes are going to be made and are going to need to notify us so pulling with some adaptive
frequencies here I think is fully appropriate but then the next thing is if a change gets made to a file let's
say some change got got got made to a file um in our remote server here then
we don't want to have to download that entire file and update it in our local folder especially if that was a big file
that 50 gab file so this is where chunking comes in again right so now
what're we're going to do is something that I think Dropbox refers to is Delta sync and so what this means is that
we're only going to get the chunks that have changed so we probably want to up add you know like an updated at here too
and what we do is when we pull for changes we'll just specifically look for the the chunks that have changed in any given file so maybe there's a new file
that was added in which case we have no choice we'll download the entire file of course we'll update our local DB and
we'll stick that file in our local folder but in the case where we just made some changes to a single file which is is fairly common then all we need to
do is download the chunks that have been updated since kind of our last sync our last poll and so we can just download
those chunks our client app will do the stitching for us to make sure that our our our local file in our local folder
here now um has that updated chunk and this will help with speed a bunch because it'll make sure that we're only
downloading that latest chunk so I'm going to say here that we're going to do some adaptive polling and then we're
also going to do Delta sync to only only fetch change
chunks so those are kind of the two things that that we can do there um okay when we talk about
consistency this is where it introduces maybe some more interesting questions so I keep referring to polling but I'm
intentionally been a little vague up until this point as to what that actually means and so let's talk about what our options are there the first and
the most obvious is that we can pull the database directly we can just say that for any you know we'll probably
need some reference to a folder or user so actually that's probably good to have here this is folder ID this is the folder that's synced right so I can say
um for folder ID 123 get me any files for which a chunk has changed or been
added since our last sync this would be pulling the the database directly right pretty easy pretty straightforward great
option option two this is closer to what um Dropbox actually does for what it's
worth is that we can have an event bus with a cursor and so this is a fairly
common pattern and I'll sketch it out without um without maybe putting you
know all the gritty details in here um but this is going to be an event stream
or an event bus so this could be something like Kafka right kofka is always a fine Choice here
um and so what's going to happen is that any change that URS to any of these given files we're going to put that
change event on this bus and then we'll need to have some kind of additional data structure which we probably should
have had or some additional State here which we maybe should have had anyway um but we're going to have some folder and
that folder is going to have a cursor and this is the sync cursor let me call it the sync
cursor and so as events or changes are coming in we're going to put those changes on our event bus and so now the
very first time you set up a local folder then you're not going to have any cursor here so we're going to replay all
of these events in order to construct the correct local state basically here are all the things that have changed in
the lifetime of this folder go construct that in your local folder in your local DB create these files all good right
we'll request that from the sync service and then we'll update the cursor to say this is where you were in that update
process the last event that you read was this particular cursor and so the next
time that we want to sync when we do our next periodic polling instead of going to the database and asking for changes
we're going to come down here to our event bus which is a linear list of the events kind of think of it like a a
linked list and we're going to navigate to the cursor basically the last event that we read and we're going to take all
of the new events that have come in we're going to apply those changes to our local DB so this is definitely more
complicated you would talk about some additional things here like partitioning uh on either user ID or
folder ID this thing is going to grow um at some point you want to consolidate
changes here so like you don't want to have to read every single event maybe you have a snapshot point where you can
just restore from something directly in file metadata and then read events from there um the reason that I'm I'm being a
little bit intentionally vague here and not going into too much detail is because while this is what um Dropbox
does for this design and given our functional requirements and our non-functional requirements I think this
is over and the reason being that an event bus with cursor is great for when you need an audit Trail and you need some Version
Control it allows you to do data recovery you can roll back past events to go to a previous point right roll
forward um and so it's it's great for all of those reasons we didn't have that
in our functional requirements so we didn't explicitly say that we want to have an audit trail that we want to have Version Control um and and for that
reason I call this Overkill now in your design of Dropbox in an interview maybe that is something that's important so I
wanted to bring this up because it might be necessary but it adds a ton of complexity um that's kind of not
necessary relative to just pulling the database and looking for changes now of course if we made a change to this
database we would have overwritten a chunk then we don't know the old chunk so we can't handle versioning we can't
roll back whereas with the event bus we could do something like that um so that's the change there I'm going to
delete it because it's it's not making it into my design I'm going to opt for Simplicity here but that's the way that
we could handle that so for sync to be consistent it's either pulling the DB or um or it's
an event bus with cursor there's probably other options there of course too but those are the the two main ones
that I see Pop Up in interviews most often and then the very last thing that's worth discussing is that despite
all of our best efforts it's possible that our local folder and our remote uh
fall into an inconsistent state it can happen there's a lot of moving pieces here um you know anything could break at
any point whether it's a developer bug um or you know issues that we had in in
with connections Etc so what's often times applied in these situations is something that's called Recon I'm not
going to be able to spell this reconciliation anyway um kind of adding
reconciliation here and so what this is is that periodically maybe it's daily maybe it's weekly whatever it needs to
be your client app is going to go fetch all of the information in remote for this folder and it's going to compare it
to its local DB and compare the fingerprints to the files that it has in that local folder and make sure that everything is totally consistent and if
there are any issues then it's going to handle reconciliation it's going to fix those issues and so while our more real
time quote unquote real time syncing of these two should get the job done in
case there are any issues no problem we'll periodically uh do reconciliation whether it's every day um or every
week quickly before we recap I just want to call one thing out that I that I
Conclusion
mentioned and failed to come back to when we did these apis I told you these apis were wrong you'll see now why that
API was wrong right we don't post the file with the file body um or with the file itself in the file metadata because
we ended up writing directly to S3 so let me grab oops kind of what's a more
correct one here and I'll update it um this is a good thing to do in the interview but not necessary necessarily
you want to talk through it so this is now where we have those first we post with the file and we get back a presign URL then we upload the file chunks to
the presign URL and then we update our file metadata with the chunk status as we're going so I just updated those so
that uh when you guys have this resource you have something that's accurate okay fantastic so we went through all five of
these steps we did our requirements core entities API High Lev design and deep Dives I think we ended up landing on on
a pretty good system here that balances Simplicity with meeting all of our requirements um so I'm going to continue
to try try to do I've been doing one of these every 3 weeks that's the pace that I'm going to try to keep up um I'm going
to put a link in the description with a couple of things of course there's going to be the link to the written version of
this there's also going to be a link to um a place on the website where you can vote for the question that you want me
to do next so head over there vote if you're enjoying these and you want to see a different question you can suggest
a question or vote on a question directly um and then I've really been enjoying your guys' comment so there have been some really encouraging
comments that are motivating me to continue to keep doing these I really appreciate reading those there have also been some people who have pointed out um
you know whether it's great questions or things that were inaccurate same too please do that do that here um I'm
largely doing these in like oneish take it takes a couple takes but you know I I just run through it and talk about the
things that um you know I believe to be true and and have experience from doing these interviews but these aren't
particularly well rehearsed so I'm sure there's times where I misspoke there's inaccuracies call those out in the comments let's talk about them
um I want to hear from you guys and answer as many questions as I can so as always thanks again for watching we'll
have another one in in three weeks or so and best of luck with the upcoming interviews
