label a1s2:
play music "music/beyondthestars1.ogg" fadein 5.0
"The dream I have is strange."
"I'm in a black void of some kind and despite the emptiness, I have some sort of purpose."
"I don't know what that is, but I'm being driven towards it."
"It's not a good dream, it's a borderline nightmare."
"The empty void isn't the scary part, though."
"It's the feeling that I'm being watched by someone...or something."
"It's the feeling that I have no say in where I'm going."
"No choice at all..."
"..."
"\"I'm very curious about you.\""
"What?"
"\"I'm limited in what I can ask, but I'll start with this—\""
"\"What is death to you?\""
menu:
    "Infinity":
        $ end_game1 += 1
        "..."
        "Very interesting..."
    "Oblivion":
        "..."
        "I see..."
stop music fadeout 10.0
$ renpy.pause(5.0, hard=True)
"Sometime just before I fully wake up, I hear something moving around behind me followed by a mumbled voice, then a soft padding sound that fades out after a few moments."
"I wonder if one of my flatmates just arrived and...looked into my room for some reason."
"As I shift around, I frown at how weirdly firm the bed I'm laying on is."
"My bed was softer than this when I got into it...and where are the sheets?"
scene bg amicusroom with slow_dissolve
"I open my eyes and see a red, velvety surface in front of me."
"Then I turn over and see an unfamiliar ceiling with a gold square pattern above me."
"Oh yeah..."
"I look over toward the bed where I expect to see Amicus, but it's empty."
"I stare again at the ceiling for a while, letting the sudden realization that I'm still here wash over me."
"I go over everything that happened yesterday, the last shred of hope that I'd been dreaming fading from my mind."
"I look over at Amicus's bed again, wondering if he'd gone into the bathroom."
"I listen for a while, but I don't hear anything coming from the door across from the bed."
"There's a muffled sound of what I assume are birds chirping coming from behind the curtain."
"Slowly, I slide off the sofa, feeling the cold marble against my bare feet as I do."
"I shiver and decide to bring the blanket with me, wrapping it around my shoulders."
"I shuffle around the sofa and move to the side of the large curtain to pull it back just slightly."

scene adastranl with dissolve
play background "sfx/birds.ogg" fadein 3.0
"The air that comes through is fresh and immediately reminds me of camping by a lake during summer camp."
"That would make sense because ahead of me is what looks like a massive body of water that seems to come right up to the edge of the balcony."
"It's warm, but not nearly as humid as it was last night."
"Pink and orange light paints the clouds on the horizon, and for a moment I take in the sight."
"The hills and mountains to either side of the lake are covered in lush, green trees."
"So is the little island a ways out to my left."
"In the distance, on the other side of the lake is what looks like a city of some kind."
"It's hard to tell how big it is since it's a good ways away, but from what I can tell the buildings are massive, and the smaller structures that taper off to the side seem to stretch far off behind them."
"Dim lights from windows glitter in the distance and I wonder if that city is full of wolves like Amicus and Cassius."
"Despite my situation, I kind of want to go see it."
"As I watch, I see a small, dark oval shape descend down toward the city, blinking blue and red lights."
"I have to smile and shake my head a little."
"I still want to go back to Earth, but this is undeniably amazing."
"I let the curtain slide shut finally and turn back to the room."
scene bg amicusroom with dissolve
stop background fadeout 3.0
"So where did that big wolf go to?"
"He could have at least told me before he ran off."
com "\"Good morning, [mc].\""
"I jump as the computer voice crackles overhead."
"I clutch my chest, breathing hard as the voice continues."
com "\"Amicus has a message for you.\""
"There's a pause, then—"
a "\"Heeey, [mc]? I'm going to my morning meditation. It's in a room just down the hall and I'll be back in approximately an hour. Why don't you take the time to get familiar with the room?\""
"There's a pause, then—"
a "\"Are you still recording, Com?\""
com "\"Yes. To end recording, say 'end of message'.\""
a "\"Oh, um, see you soon, [mc]. End message...is it still—\""
com "\"To end recording, say 'end of message'.\""
a "\"My gods, end of message!\""
"I hear Amicus starting to curse again before the message cuts off."
"I look around the room a bit, noticing how little there is to get familiar with."
"I could look through the dresser, but I assume that's mostly filled with Amicus's things and I doubt he wants me to get familiar with those."
"I move across the room toward the bathroom door, standing in front of it for a moment before studying the black panel in the middle of it."
"It's similar to what Amicus used to open the door in the hallway."
"I reach out to try and push it and the moment my fingers brush against the surface, the door slides to the side so fast that I jump."
play sound "sfx/dooropen.ogg"
scene bg bathroom with slow_dissolve
"The lights inside come on, slowly illuminating the interior."
"I poke my head inside, then quickly step in, imagining the sliding door suddenly closing and chopping my head off."
"It stays open until I'm halfway in the room, then it closes automatically."
play sound "sfx/doorclose.ogg"
"There's a large sink to my left and an even larger mirror above it."
"In the corner, there's a marble-looking bench with a hole that I can only assume is the toilet."
"Finally, across from that is a large bath and what I imagine to be the shower."
"I actually really need to pee, so I head over to the bench and do my business down the hole, hoping that it's not something like a laundry shoot and I'm pissing on the servants below."
"As soon as I start though, water begins to pour down the sides of the tube, leaving me pretty sure that it is indeed a toilet."
"I guess I should be more confident in assuming things about this place."
"Everything is fairly similar to what I had on Earth."
"I walk over to the sink and push at the faucet, then I stick my hand under it and water starts pouring out."
"I'm tempted to take a drink, but then I notice the water is bubbly and soapy-looking."
"Having nothing left to do in the bathroom, I turn back to the door and find the black square again."
"I reach for it, and just like before the door slides open—"
play sound "sfx/dooropen.ogg"
scene bg amicusroom with dissolve
show cas at center with dissolve
c "\"—if he thinks he's going to get away with it.\""
"Cassius is facing away from me, his arms folded as his bushy white tail swishes from side to side."
"I freeze up, staring at him wide-eyed."
"I have plenty of time to jump to the side, maybe hide in the shower area, but I just stand there like an idiot as the wolf turns around, almost in slow-motion."
show cas surprised at center with dis
"He freezes just like I did when he spots me standing in the doorway."
"We stare at each other for a moment, for a very long moment."
"Then he screeches, making me jump back in shock."
play music "music/trouble.ogg"
show cas scared at chase with dis
c "\"OH GODS! EDEPOL! WHAT IS IT!?\""
"The wolf dodges back and forth, as if expecting me to try and run at him."
c "\"CATO! CATO! HELP! COME QUICK!\""
hide cas scared with moveoutleft
"Finally Cassius's little dance of terror ends with him sprinting to my left and out of the room."
"I stand there for a moment, listening to his screams fade down the echoing hallway while wondering if I should hide or something, maybe go back into the bathroom and try to lock it..."
"Instead, I hear more thudding, someone running up the hallway from the other end."
show ami shocked u at center with moveinright
"Then Amicus comes running into the room, sliding to a stop in the middle of it."
show ami surprised u with dis
"He spins in a circle, then spots me and runs up to me."
a "\"What happened!?\""
m "\"Uh, Cassius came in and saw me.\""
show ami angry u with dis
a "\"You let him see you!?\""
m "\"Wha—No! He just came in! Where were YOU!?\""
a "\"Meditating! I left a message! Where did he go?\""
m "\"Cassius? He just ran off.\""
show ami frustrated u with dis
a "\"Dammit!\""
"Amicus stands there, his tail thrashing back and forth."
"I glare at him."
m "\"If you hadn't just left me here this wouldn't have happened!\""
show ami angry u with dis
a "\"Cassius shouldn't have even come in here!\""
"Amicus turns away and starts pacing back and forth."
m "\"What are you doing?\""
a "\"Shh! I'm thinking.\""
"I bristle a little at being shushed, but I stay quiet, watching the wolf stalk back and forth."
"Then I hear voices again; Cassius's along with another, deeper voice."
"Amicus turns to me."
show ami angry teeth u with dis
a "\"Just be quiet for a moment as I try to explain things, understand?\""
"I glare at Amicus."
"His ears flatten and his expression becomes a bit more desperate."
show ami embarrassed u with dis
a "\"Please?\""
"I still don't say anything, but give him a curt nod."
show ami serious u with dis
"Amicus reaches out toward my shoulder, then pauses and instead offers his paw to me."
show ami serious u at twelve with moveinright
"I take it and he gently pulls me from the bathroom to stand next to him in the middle of the room, facing the open doorway to the hall."
show ami u with dis
"Amicus fixes a confident smile on his face, though I can feel how tense he is next to me."
"From around the corner comes Cassius, but he's hiding behind someone else; another wolf."
show cas scared at one
show cat at four
with dissolve
stop music fadeout 5.0
"They both stop in the doorway as the larger wolf takes in both Amicus and I."
show cas furious with dis
c "\"Amicus! What are you doing with it!? Step away!\""
"Amicus gently places his paw around my shoulders, drawing me in against his bulk."
"Cassius's eyes widen at that, though the wolf next to him seems to have no reaction."
"Then again, that could just be because I can't see his eyes."
show cas annoyed with dis
c "\"What are you doing, Amicus?\""
"Amicus clears his throat."
show ami talking u with dis
a "\"Cassius, Cato—\""
"He nods to each of them in turn."
play music "music/memories.ogg" fadein 5.0
a "\"This is my pet, [mc]\""
show cas surprised
show cat surprised
with dis
"Cassius's mouth falls open."
"The other wolf, Cato, seems to shift a bit at that."
"Silence drags out."
"Then Cato shifts again."
show cat bow with dis
ca "\"Is this where you were the past two days, Amicus?\""
"Amicus's arm tightens a bit around my shoulders, drawing me in closer."
show ami serious u with dis
a "\"Yes.\""
ca "\"And that's where you took your father's ship?\""
"A slight pause."
show ami embarrassed u with dis
a "\"Y—yes\""
"Cassius gasps."
show cas furious with dis
c "\"He can't do that!\""
"He glances at Cato."
show cas surprised with dis
c "\"Can he?\""
"The bigger wolf is quiet, and even though I can't see his eyes I get the feeling that he's watching me closely."
"Cassius turns his glare back on Amicus."
show cas angry with dis
c "\"Where did it come from?\""
show ami serious u with dis
"Amicus rubs my arm."
a "\"HE...came from far away.\""
show cat frown with dis
ca "\"Is he a Child?\""
a "\"Yes.\""
show cas surprised with dis
c "\"What!? He can't just take someone else's Child...can he?\""
"Again Cassius looks at Cato."
"And once again, Cato is quiet, then he finally sighs."
show cat talking with dis
ca "\"We will discuss this over breakfast, Amicus. Get dressed and bring the creature with you...as long as he's safe?\""
show ami crossed u with dis
a "\"Of course.\""
ca "\"Then we will continue the conversation there.\""
hide cat with dis
"With that, Cato turns on his heel and walks out of the room, leaving Cassius to look after him with a gaping mouth."
"He turns back on us, snarling."
show cas angry with dis
c "\"I don't know what you're planning with that {i}thing{/i}, Amicus, but if I know you, it's going to be incredibly stupid.\""
"He takes another second to look at me with unmistakable disgust."
c "\"You could have at least obtained one that isn't quite so ugly you kno—\""
show ami crossed serious with dis
a "\"Leave, Cassius. And don't think about snooping around in my room again, understood?\""
hide cas with dissolve
"Cassius doesn't respond and simply walks away, looking over his shoulder just before he leaves."
c "\"And expect to receive punishment from Cato for stealing father's ship...Absolutely outrageous.\""
"I watch Cassius's tail swish out of sight behind the doorway."
"Amicus lets out a huge sigh and I feel his chest deflate against my shoulder."
show ami frustrated u with dis
a "\"Damn-it\""
"I sigh as well."
m "\"You REALLY didn't think all of this through, did you?\""
"I slowly move out from under the wolf's heavy arm."
show ami crossed serious u with dis
a "\"Like I said, I made many mistakes. I'm just tired of lying now.\""
stop music fadeout 10.0
m "\"You still told them I'm a Child.\""
show ami surprised u with dis
"Amicus brings a paw abruptly up to his mouth, touching the pads of his fingers to his lips."
"It might not be a shushing gesture that I'm familiar with, but I know what it means."
"Amicus listens, his ears straight up and eyes looking up at the ceiling."
"Finally, he looks back at me, whispering."
show ami embarrassed u with dis
a "\"That...is something I can never tell them the truth about, and it would be best if you never mention it again...please.\""
"His suddenly serious demeanor cools my mood a little, so I just sigh again and sit on the edge of his bed."
"Amicus stands there awkwardly for a moment, then quickly moves over to the open door, placing a paw to the square to close it."
hide ami with dissolve
play sound "sfx/doorclose.ogg"
"He moves back over to me, his voice still lowered."
show ami crossed serious u with dissolve
a "\"Well, if we're going to pass you off as a pet then I should probably get you familiar with your duties.\""
m "\"My duties?\""
"I raise an eyebrow at Amicus."
"Amicus sighs."
a "\"I understand your frustration, but we need to do this right if we want things to go as smoothly as possible. You don't {i}have{/i} to do anything, but it will help you blend in better.\""
"I roll my eyes and lean back on my hands, looking up at Amicus."
m "\"Alright...what do I do?\""
show ami crossed u with dis
a "\"Well, first of all I take my shower and...\""
show ami embarrassed u with dis
a "\"...you help me wash.\""
play music "music/dawn.ogg" fadein 10.0
m "\"Help you wash?\""
a "\"...Yes. You would soap my fur and such.\""
"We stare at each other for a moment."
a "\"Um, it's something that the others wouldn't see, so I suppose it's not necessary...unless you want to.\""
m "\"No.\""
show ami disappointed u with dis
a "\"Well, alright then. Nevermind on that one.\""
"Amicus is clearly offended."
m "\"Listen, I'm not gonna soap up your naked body.\""
show ami disappointed eyes u with dis
a "\"Yeah, you made that clear.\""
show ami crossed serious u with dis
a "\"Anyway, I'd honestly rather skip the shower today, but spending all of that time in the spaceship has left me rather unkempt.\""
"Amicus turns to the bathroom and opens the door."
play sound "sfx/dooropen.ogg"
a "\"You should at least come into the bathroom while I shower in case Cassius decides to barge in again. You can stare at the wall, or something.\""
scene bg bathroom with dissolve
"Amicus stalks into the bathroom and I have to smile as I follow him in, the door closing quietly behind me."
play sound "sfx/doorclose.ogg"
"Amicus notices me smirking."
show ami crossed serious u with dis
a "\"What?\""
"I shrug."
m "\"Nothing, just kind of funny that you got so huffy.\""
a "\"I don't know what that means.\""
show ami crossed u with dis
"Amicus is adjusting his underwear, then it suddenly drops and I quickly look away."
hide ami with dissolve
a "\"Heh, I suppose your people prefer modesty?\""
"Out of the corner of my eye, I can tell that Amicus has on a smirk of his own."
m "\"Around others at least...and you guys don't just walk around naked, so don't you prefer modesty too?\""
a "\"It all depends on the time and place.\""
"Amicus moves into the shower and for the next ten or so minutes, I sit on the counter while the room fills with steam."
play loop "sfx/showerfan.ogg" fadein 4.0
"Once the water shuts off, a loud fan starts up and I glance over to see Amicus with his arms out, his fur blowing back and forth."
"He notices me look over then look away again."
a "\"You know—\""
"He has to almost shout over the fan."
a "\"You could have cleaned up too if you'd showered with me, but you won't have time with breakfast coming up. You'll have to do it after.\""
stop loop fadeout 3.0
"I shrug and wait as Amicus steps out and grabs clean undergarments hanging from a hook which he spends the next minute tying on."
show ami happy eyes u with dis
a "\"Alright, balls are gone. You can look now.\""
show ami u with dis
a "\"Actually, do you even have those? I don't want to assume.\""
play sound "sfx/dooropen.ogg"
"I open the door and head back out."
m "\"Guess you'll never know.\""
show ami eyes u with dis
a "\"Hehe...\""
scene bg amicusroom with dissolve
"Amicus spends another minute in the bathroom opening a door under the sink and rifling around in it."
a "\"The next thing you're supposed to do is get the brush and oils from here.\""
"He lifts up a brush and a few glass bottles with colorful liquids inside before coming over to stand in front of me."
show ami serious u with dissolve
"He sighs."
a "\"I know you don't want to, and I realize now that I'm repulsive to you, but I can't really reach every part of my coat, and it would be strange if I called for a drone when I have a pet...\""
"I think about making another moody remark, but the expression on his face makes me pause."
"I suppose I am being a little bratty right now."
"Besides, what else am I going to do while I'm here?"
"Sit on the sofa all day?"
"I get up and take the brush from Amicus and I see a surprised smile on his face."
show ami eyes u with dis
a "\"Thank you, [mc].\""
"He shows me how to apply one of the liquids, a honey-colored one, to the brush."
show ami u with dis
a "\"It's a treatment for my fur. It keeps it soft and voluminous-looking. Here, you just take the brush and run it with the lay of my fur.\""
"He hands the brush to me and then stands facing away."
"I start slowly and run the brush through the fur between his ears and down his broad back, watching as the slightly disheveled hairs line up and lay down smoothly."
"It accentuates his shoulder blades and the thick and smooth muscles in his back."
"I'm hesitant at first, but I become more confident with each stroke."
"Actually it's kind of relaxing, that is until I brush down the left side of his neck which makes him gasp."
show ami surprised u with dis
"I pull back quickly."
m "\"Sorry! Did I brush too hard?\""
show ami eyes u with dis
"Amicus chuckles."
a "\"Heh, no, that's just where you hit me earlier.\""
m "\"Oh...\""
"I look closer and see that there is what looks like a lump under the fur."
"I carefully brush around it and move to Amicus's front."
"Amicus, meanwhile, has his eyes closed with a smile on his face, clearly enjoying himself."
m "\"I am sorry about that, by the way. I was really scared when I did it.\""
show ami u with dis
a "\"Don't worry about it. I deserved it for tying you up so poorly.\""
"Amicus gives me a wink."
"I feel my face grow a little hot as I focus on getting the fur to lay just right on his biceps."
m "\"And you know, you're not repulsive to me at all. I was just being a dick earlier. You look...good.\""
a "\"Well, I suppose I was too. I shouldn't have made fun of your sensibilities. All aliens have their own cultures which are different, but that doesn't mean less valuable.\""
"Amicus's tone sounds weirdly rehearsed, like he's quoting something."
a "\"And also thank you, [mc]. I think you look good too.\""
"He might just be returning the compliment, but it's nice to hear after what Cassius said."
"But I definitely wasn't lying, and now that I'm this close to him, I have to admit that he is a little handsome."
"His face is expressive and kind of charming and there's just a generally friendly air about him."
"And...well, then there's his body."
"It's thick and masculine, just like a burly human, and I really can't deny that it's kind of appealing...kind of."
"I start to brush down the wolf's front, feeling his chest and stomach rise against the brush with his breathing."
"I sculpt the lighter fur around his pecs to accentuate them better since it seems that's how he was keeping it earlier."
"I can't blame him."
"Then I move to his belly, moving the brush over its thick and slightly rounded form."
"The muscles are less defined here, but I can still sense the strength underneath it all."
"As I brush the lower part of his midsection, I notice the crotch of his loincloth bulging out rather far—"
show ami shocked blush u at jumping with dis
a "\"Alright! Thank you, [mc], that should be good!\""
hide ami with dissolve
"He takes the brush from my hands and turns away, leaving me with the strong suspicion that he's adjusting himself, though he covers it up by pretending to mess with the other bottle."
"Finally he turns around, looking flushed."
show ami embarrassed u with dis
a "\"Uh, hold out your paws, please?\""
"I stick out my hands and he tips the bottle over, the liquid in this one having a purplish tint to it."
"Several drops fall into my hand."
"Immediately, my nose is filled with that lavender scent that I've been smelling off of Amicus since I first met him."
a "\"Rub them together then just sort of pat up my body and underarms, along my neck as well.\""
"I can tell Amicus is still flustered, so I do it quickly, not wanting to linger and cause the wolf any other...problems."
"Maybe it just feels really good to be brushed like that?."
m "\"Is this like, perfume?\""
show ami u with dis
a "\"Yes, it keeps the muskier scents hidden for the most part.\""
m "\"I see.\""
a "\"Do you use perfume?\""
m "\"Well, I guess I do wear something like that on my underarms.\""
show ami eyes u with dis
a "\"Feel free to use it then!\""
"I decide not to tell him that lavender scents are mostly for women on Earth...besides, it does smell nice."
hide ami with dissolve
"Once the perfume is done, Amicus moves on to getting dressed, showing me how to drape his cape over his shoulders."
show ami with dissolve
a "\"Alright! So I know you only have the pair of clothes you came with, so I'll have a tailor drone come up later today to see if we can't make you more pairs of what you have.\""
m "\"Oh, okay.\""
a "\"Now, lets head to the dining room before we're late.\""
show ami embarrassed with dis
"Amicus pauses, frowning."
a "\"Now...I know you won't like it, but you're going to have to feign some ignorance in front of the others.\""
"I raise an eyebrow."
m "\"How so?\""
a "\"Well, you're going to need to act a bit...dumb.\""
"The antagonistic feelings that had been fading over the past few minutes start to rise up again."
m "\"And how do I do that?\""
"Amicus shrugs."
a "\"I don't know, give them vacant stares, incoherent mumbles, act like you can't grasp more complex matters. The whole point is to make it seems like you're a typical Child.\""
"I don't like it, but I don't want to have anything to do with those aliens so if it'll make them leave me alone..."
m "\"Alright.\""
show ami eyes with dis
"Amicus lets out a breath, clearly relieved."
a "\"Thank you, [mc]. This may not always have to be the case, but for now we need to play on the safe side of things. Just let me do all of the talking.\""
m "\"You got it.\""
show ami motivated with dis
stop music fadeout 5.0
a "\"Great! Now let's hurry to the dining room. I don't want to make Cato more angry than he already is.\""
scene bg palace1 with dissolve
play loop "sfx/birds.ogg" fadein 10.0
"And with that, I follow Amicus out into the hallway."
m "\"So who's Cato?\""
show ami crossed with dis
a "\"The wolf you saw with my brother. He was my father's advisor and currently the acting emperor. I mentioned earlier that he'll be choosing between me and my brother.\""
a "\"That's why I'm doing my best to keep him in a good mood, or at least not a bad mood. I don't think he has a good one.\""
"I keep in mind to stay on Cato's good side as well."
"Meanwhile, sunlight pours in through the open windows, and I can hear birds calling from outside again."
m "\"Birds.\""
a "\"What was that?\""
m "\"I can hear birds. I'm just surprised they sound the same as they do on Earth.\""
a "\"Ah, yes, you wouldn't know this; all life has the same origin and develops in a roughly similar way. It's only natural that life here is similar to your moon...planet, I mean.\""
m "\"Oh.\""
show ami thinking with dis
a "\"Well, all life on this side of the universe, at least. There may be another but we'll have to leave that conversation for later. For now—\""
stop loop fadeout 5.0
scene bg diningroom with dissolve
play music "music/lute.ogg" fadein 5.0
"I follow Amicus around a corner and find myself standing in a large, spacious room."
"The first things I notice are the large screens on each wall of the room, displaying colorful images of stars, galaxies, and spaceships."
"In the middle of the room are what look like beds surrounding a table."
"In those beds are the two wolves I saw earlier."
show cas at seven
show cat behind cas at twelve
with dissolve
"Cato is sitting and leaning over toward Cassius who is draped luxuriously over one of the beds."
"Cato is talking to Cassius while the other wolf has on his typical sour expression."
"Sitting on the floor in front of Cassius's bed is a creature that I've never seen before."
show ale at three with dissolve
"It's definitely not a wolf, more feline-like."
"Cassius has his paw on its head, idly scratching it while he listens to whatever Cato is saying."
show cas surprised with dis
"He sees us and abruptly stops, sitting up."
"Cato stops talking and looks over at us."
show cas annoyed with dis
c "\"You're late.\""
show ami at zero behind ale with dissolve
a "\"And good morning to you, Cass. And to you Cato, Alexios.\""
"Amicus turns to Cato and the small cat creature, bowing to both of them."
show cat bow with dis
ca "\"Good morning.\""
show ale smile with dis
al "\"Morning, Amicus.\""
"The cat, Alexios, nods at Amicus with a smile."
"At the same time I see Cassius tug on the gold collar around his neck."
show ale tilt with dis
"It isn't very much, but Alexios immediately drops the smile from his face, looking down."
hide ale with dissolve
c "\"How many times do I have to tell you not to acknowledge him, Amicus?\""
"Amicus seems to ignore Cassius, walking to the empty bed while pulling me along with him."
"He whispers in my ear."
show ami crossed behind cas with dis
a "\"Sit in front like Alex is doing.\""
show ale tilt at three with dissolve
"I look over at the cat and see his ears perk up in our direction, though he continues to avoid looking at us."
"He's in a kneeling position, so I do the same, starting to feel a little uneasy about this whole setup."
hide ale with dissolve
"Amicus, meanwhile, stretches out across the bed, an elbow in the cushions as he props himself up."
show cat with dis
ca "\"Com, send in breakfast.\""
com "\"Yes, Cato.\""
"A few seconds later, literal flying saucers levitate into the room from beyond another archway."
"I get a moment to see some sort of black device on the underside of the plates before they gently come to rest on the table."
"I blink, but don't say anything, deciding to just take everything in without question."
"I decide instead to focus on the food."
"I can at least identify a few of the portions, one of them being what looks like bread."
"Then there's a plate of a odd, white, crumbly substance and next to that is a bowl of what I'm pretty sure are olives."
"There's a glass bottle filled with some type of red liquid, probably wine."
"Finally, in the middle, next to some towel-like napkins, is roasted poultry, golden-colored and steaming."
"It actually smells really, really good and, considering that I haven't eaten any real food in over day, I feel my mouth water."
"Still, I have enough common sense to know that I probably can't just dig in, so I keep an eye on the cat, waiting to see what he does next."
show ale at three with dis
"He grabs four small plates from the tall stack and sets them down in front of himself."
"Then he starts to grab some slices of bread which he sets down on one of the plates."
hide ale with dissolve
"I look back at Amicus and he nods."
"So I do the same, grabbing four plates and setting them out in front of myself on the table, starting to grab the separate portions of food to set them on their own plate."
"Meanwhile, Cato just leans over to grab his own while Cassius clears his throat."
show cas paw with dis
c "\"So...Amicus. What is this?\""
"I look up and immediately find Cassius's eyes boring into mine."
"I quickly look back down and grab up the wood-handled knife that Alexios just set down, using it to spread the white stuff onto the slices of bread."
"I wrinkle my nose at how stinky it is and I realize it's probably some type of cheese."
show ami with dis
a "\"This is [mc]. He's my pet.\""
c "\"No, Amicus. WHAT is it. It's not one of our Children. Does it belong to a Sibling?\""
"I'm half-listening to the conversation while I see Alexios reach out with his bare paws and just pull a chunk of meat off of the poultry."
"I hesitate, kind of wishing I'd had a chance to wash my hands, but do it anyway, wincing at how hot it is."
"The temptation is strong just to stuff it in my mouth, but I manage to set it down on the plate."
"Finally, I grab up a bunch of olives and put them on their own plate."
"At this point, I can see that Alexios is lining his plates up in front of Cassius on the bed."
"Carefully, I do the same for Amicus, though I lose an olive in the process."
"I watch it roll across the ground, but decide to ignore it, and Amicus just pats my head with a muttered \"thank you\"."
a "\"No....he's from a failed uplift.\""
show cas surprised
show cat surprised
with dis
stop music fadeout 5.0
"I watch as Alexios starts filling a goblet with the red liquid, but look up when I realize there's complete silence."
"Cassius and Cato are both staring at Amicus."
"I look back at him and see that he looks pretty calm, though I can see him picking at his claws."
c "\"A—are you serious?\""
show ami crossed talking with dis
a "\"Yes.\""
c "\"Wh—Why!? He's a barbarian!\""
a "\"Because I've decided the abandoned Children deserve to re-establish regular contact. If we're to unite with the Khemians then we also need to unite ourselves—\""
"I start filling Amicus's goblet as I feel his eyes on me."
show ami crossed with dis
a "\"—Child or not. Having a pet like this will show the Khemians my intentions.\""
show cas angry with dis
"Cassius scoffs loudly, popping an olive into his his mouth and chewing it vigorously."
c "\"Masterful stunt, Amicus, but you still stole father's ship to get there. Using Stretch tech without authorization from the emperor is a violation of the law, is it not, Cato?\""
"I hand the goblet to Amicus, silently wondering if the wolf is going to be thrown in jail my first day here."
"What would happen to me then?"
"Still, Amicus looks calm and when he sees my wide eyes he just winks."
show cat talking with dis
ca "\"It could be, but there is no emperor is there, Cassius?\""
"Cato finally lays back, his small plates heaped high with food."
"He turns his head back to Amicus."
ca "\"Are you saying you piloted the ship to the outer reaches of our empire? Voice commands only work for the emperor, if I'm not mistaken.\""
a "\"That is correct. I learned to navigate the ship on my own. I was also able to communicate with their people, negotiate, AND sign a, uh, contract with him.\""
"This is where I start to hear Amicus's voice falter."
"I actually do believe now that he doesn't lie often, because it's clear that he's so bad at it."
"I copy Alexios and return to my kneeling position next to the bed, then switch to a cross-legged one when my knees get too sore."
"Cato watches from his bed silently, and I again feel unnerved at the feeling that he might be looking at me."
show cat bow with dis
ca "\"Fascinating.\""
"Cassius curls his lips back."
show cas furious with dis
c "\"Fascinating!? He used the Stretch Drive! He's going to get away with it because father is dead? What does that make of all the other laws?\""
c "\"Can a beggar now steal from the market because there is no authority to tell him not to? Can a Child rebel from the empire because there is no emperor to tell them—\""
show cat with dis
ca "\"Quiet, Cassius. You know the circumstances as well as I do.\""
show cas disappointed with dis
"Cassius snaps his mouth shut with a huff, turning his attention back to his food which he starts to pick at."
"The conversation seems to stop there, and I wonder if Amicus is in the clear."
"While Cassius sure seemed indignant, I get the feeling that Amicus wasn't in any danger in the first place."
"I guess being the emperor's son has its perks."
play music "music/lute.ogg" fadein 5.0
a "\"Could you get me some more of the {i}azure{/i}, [mc]?\""
"I look over to the table for a moment in confusion."
m "\"Um...what's that?\""
"I try to keep my voice low, but that's when Cassius suddenly yowls, clapping a paw to his head."
show cas angry with dis
c "\"Oh Gods! It doesn't speak the Language?\""
"I look between Cassius and Amicus in confusion."
show ami crossed serious with dis
a "\"Of course not, they were abandoned.\""
ca "\"Most of the abandoned still speak the Language...how far away is his home star?\""
a "\"Roughly fifty thousand light years.\""
c "\"I don't care! Don't have it speak again. The last thing I need is a headache from the Lingua manually translating everything he says. It's barbaric.\""
"I don't know if he's calling the headache barbaric, or me...probably me."
show cas with dis
c "\"Upload its language to the Nexus before you let it out in public again, Amicus.\""
"I decide I really don't like Cassius."
"He's talking about me like I'm like I'm just a piece of property..."
show ami crossed with dis
"Then I feel Amicus's paw on my shoulder for a moment, giving a soft squeeze before pulling back again."
"The conversation topic then shifts to stuff I don't really understand, mostly politics and the Khemians, whatever that is."
"Despite their fight earlier, Amicus and Cassius are pretty animated in their conversation."
"Amicus keeps sticking empty plates in my face, indicating that I should refill them."
"It's clear that I'm not going to be eating while the wolves are, and I feel my irritation grow."
"I'm not a servant, I didn't agree to this, and even if this is supposed to help me blend in, I can't help but feel Amicus could have put me in a better position than this."
c "\"Virginia sent me a letter last night saying that she'd be bringing back a Khemian tomorrow. He got trapped here after the Stretch Drive depletion.\""
show ami surprised with dis
a "\"Oh? He wasn't able to return on the retrieval ship?\""
show cas paw talking with dis
c "\"He was on Ancoris at the time, so it took him several months to get back to Adastra. He's going to be our guest until the next ship arrives.\""
c "\"I think it will be quite interesting to see one in person. Who can say that they've met two Siblings?\""
"Cassius reaches down and starts stroking Alexios's head fur."
show cas with dis
show ale smile e at three with dissolve
"The green and gray cat closes his eyes, smiling and purring."
"I watch this for a moment, then freeze up as I feel Amicus's paw on my head."
show ami eyes with dis
"He starts to gently scratch his blunt claws into my scalp, ruffling my hair around."
"It actually feels really good, but knowing what he's doing gets me pissed off all over again."
"He already knows I don't want to be doing this, that he brought me here against my own will."
"Now he's stroking me in public like I actually am his pet?"
"Well...I guess it makes sense, I guess he's doing his part to help me blend in just like I'm doing mine."
"But that doesn't mean I don't hate it, and then his other paw sticks his empty goblet down under my nose."
show ami happy eyes with dis
a "\"More wine, please.\""
"I let the goblet hang in the air for a moment, then take it and reach out robotically for the heavy wine bottle, getting up on my knees to better pour it into the empty goblet."
"I fill it up as Amicus continues to stroke me."
show ami with dis
a "\"I'll bet even fewer can say they've met an abandoned species, wouldn't you think?\""
show cas annoyed with dis
"Cassius glares at Amicus, and I glare at the wine."
"I try to remind myself that this is just to help get me home..."
"...Or maybe he actually is just showing me off because he likes how he's getting under Cassius's fur."
"I turn on my knees to face the wolf and hand back his goblet, noticing how full it is, the wine almost sloshing over the rim."
"Amicus reaches out for the goblet."
"My fingers twitch, then I feel the goblet slip out of my hand, watching as it seems to fall in slow motion onto its side on the bed."
"The wine shoots out in a red gush, splashing across Amicus's lighter furred front."
stop music
play sound "sfx/winespill.ogg"
show cas surprised
show cat surprised
show ale shocked
show ami shocked at jumping
with dis
"The wolf gasps, sitting up suddenly as the wine pours down his chest and stomach and onto his pants."
show ami embarrassed with dis
a "\"Damn!\""
show ale tilt
show cas smile eyes
with dis
"Meanwhile, Cassius bursts out laughing behind me, snorting obnoxiously."
play music "music/trouble.ogg"
c "\"Hahahahaha! Maybe there's a reason so few have ventured out to meet them, Amicus.\""
"I see Alex staring at me, but when I meet eyes with him he looks down."
hide ale with dis
"Amicus reaches over me for one of the towels, glancing down at me as he does."
"I try to keep myself from smirking, but I think I fail."
show ami surprised with dis
"He pauses, staring at me in astonishment as I guess he realizes that I did it on purpose."
"He doesn't look angry though, and instead grabs up the towel and starts patting down his front, the fur still stained a dark, maroon color."
show cas paw talking with dis
c "\"What are you doing, Amicus?\""
"Cassius has finished his laughing and I look over to see him staring at us."
show ami disappointed with dis
a "\"What do you mean 'what am I doing' I'm cleaning up the mess.\""
"Amicus growls at Cassius, continuing to pat himself down."
show cas paw annoyed with dis
c "\"Dear gods, you really don't know how to do this. Punish it.\""
"Cassius lazily flops his paw in the air in a slapping motion."
"I snap my gaze to Amicus, glaring again."
show ami embarrassed with dis
a "\"Wh—N—No, I can't do that.\""
c "\"Why not?\""
a "\"It's...in the contract; no physical punishments, just like Alexios's.\""
show cas surprised with dis
c "\"What!?\""
a "\"You heard me.\""
show cas angry with dis
c "\"Alexios is a Sibling! It's barely even a Child.\""
show ami angry with dis
a "\"HE is mine and none of your business.\""
show cas paw talking with dis
c "\"Punishment is the only way to teach the lesser species, Amicus.\""
"He looks at me."
c "\"You, creature, up. I'll hit you instead.\""
show cas scared
show ami angry teeth
with vpunch
a "\"CASSIUS!\""
"I jump, so does Cassius, ears ringing as Amicus's deep voice bellows over me."
show cat with dis
"Meanwhile, Cato just lounges on his bed, listening...or maybe not."
a "\"I'll make this very clear right now. You are NEVER to lay a paw on him, or give him orders of any kind.\""
show cas annoyed with dis
"Cassius, having recovered, raises an eyebrow at Amicus."
c "\"And if I do, brother?\""
"Amicus's fur starts to lay flat on his shoulders again as he shrugs."
show ami crossed serious with dis
a "\"I'll punch you.\""
show cas scared with dis
c "\"Wh—you....You can't do that, we're not pups anymore!\""
show ami crossed with dis
a "\"And if you call him \"it\" again, I'll do the same.\""
"Cassius seems to choke for a moment."
c "\"What in the world has gotten into you, Amicus!?\""
"He looks at the older wolf."
c "\"Cato!\""
show cat talking with dis
ca "\"Yes, Cassius?\""
show cas furious with dis
c "\"Well, DO something! He can't threaten me like that!\""
show cat with dis
ca "\"Amicus, be nice to your brother.\""
show cas sad with dis
"Cassius's ears turn bright red and he slumps on the bed, glaring at his remaining food."
stop music fadeout 5.0
ca "\"Anyway, if you two are finished then be off to your studies. Don't be late this time, Amicus. Your tutor complained again last week.\""
show ami frustrated with dis
a "\"That's today?\""
ca "\"You know, you should take care to start paying more attention. After seeing what you accomplished, I'm starting to lean toward trials in making my decision.\""
show ami surprised
show cas surprised
with dis
"The room suddenly goes very quiet."
ca "\"And Cassius, I need to speak with you for a moment before you leave.\""
hide cas
hide cat
with dissolve
"Amicus gets to his feet and I do the same."
show ami serious at center with moveinright
"The wolf glances at Cassius and Cato, but they're deep in conversation."
"He turns back to me."
a "\"I forgot that It's my study day, so I'll be gone for a little while. I'm going to ask Alexios to show you around and give you something to do while I'm away.\""
"I feel myself grow tense at the idea of being without the only person I know around here."
m "\"Seriously?\""
a "\"Listen, you don't have to do anything, I'll make that clear to everyone, but I feel you might rather have {i}something{/i} to do rather than sit in my room all day.\""
"He seems to think it's the chores that I'm upset about rather than him leaving me alone."
m "\"Alright.\""
show ami embarrassed with dis
"Amicus frowns at me and I can't help but feel a little bad."
"He does seem to be trying to make things as easy as possible for me."
m "\"And...sorry.\""
"I gesture at his still-stained front."
show ami crossed with dis
a "\"Don't worry. Yes, wine isn't easy to get out of the fur, but I know why you did it, and I deserved it.\""
c "\"Ugh, Is it—he speaking it's—his language again?\""
a "\"Shut up, Cassius.\""
c "\"What!?\""
a "\"Alexios.\""
"Amicus gestures at the small cat who is currently stacking the dirty dishes on top of each other."
show ami with dis
a "\"Could you please show [mc] around the palace along with the tasks and activities you do? He's unfamiliar with nearly everything.\""
show ale smile at one with dissolve
al "\"I would be happy to, Amicus!\""
show cas paw annoyed at eleven with dissolve
show ale tilt with dis
c "\"So you can order {i}my{/i} pet around?\""
"Cato, standing over by the doorway and clearly eager to leave, sighs."
ca "\"Enough. Try to be reasonable Cassius. Now both of you be off to your studies...and a quick shower for you, Amicus.\""
hide cas
hide ale
with dissolve
show ami serious with dis
"Amicus grumbles and starts to turn away, then turns back to me, resting a paw on my shoulder."
show ami with dis
a "\"I'll be back toward the evening...\""
"The big wolf pauses, as if wanting to say more, but leaves me with a simple—"
show ami eyes with dis
a "\"I'll see you then.\""
hide ami with dissolve
"And with that, he gives me a little wave and another wink before following Cassius and Cato through the archway."
"Just as Amicus leaves, Cassius pauses to give me a sour look...then again, most of his expressions are pretty sour, but it still makes me uncomfortable."
"Then I'm left alone with the cat."
"I feel an odd sense of loneliness at seeing Amicus just leave like that."
"It's like my mother just dropped me off at preschool, or something."
"He's the only one that's been treating me like an actual person...mostly, at least."
"I hear the small sound of someone clearing their throat behind me."
play music "music/dawn.ogg" fadein 10.0
show ale with dissolve
al "\"Hello.\""
"The small cat smiles at me pleasantly, his paws clasped neatly in front of himself."
"I say he's small, but he's really about the same height as me."
"It's just odd seeing another alien that's my size when I always have to look up at the wolves."
m "\"Uh, hi.\""
"I see Alexios's left eye twitch and he raises a paw to his head."
show ale smile w with dis
al "\"Oh dear. This is going to be an interesting day.\""
m "\"...Is something wrong?\""
"More twitching."
show ale talking e with dis
al "\"Just my Lingua. It will take a while to learn your language, but it gets better the more you speak...so if you don't mind, I'd like to know more about you. I'm very curious.\""
m "\"Uhhh...\""
"Amicus told me to act dumb, so I try to figure out how I might do that."
"I fix a distant look on my face."
m "\"Far away...\""
show ale shocked w with dis
"Alexios blinks, then giggles."
show ale smile with dis
al "\"Oh.\""
"We both stand there awkwardly for a moment before he gestures at the table."
show ale with dis
al "\"Well, why don't we have a seat? We eat their leftovers when they've finished.\""
show ale at right with moveinright
"The cat moves over to sit on Cato's bed, reaching out for his own small plate."
"I'm reminded of how hungry I am, so I quickly do the same, choosing to sit on Cassius's bed since Amicus's is covered in wine."
show ale talking with dis
al "\"Will this food agree with your stomach?\""
m "\"I think so. It actually looks kind of like some of the stuff I eat back home. I mean, it's basically olives, bread, and meat.\""
"I point to each of the dishes."
"Alexios puts his paw back up to his head."
show ale smile w with dis
al "\"Oh my, so many words, and in full sentences too!\""
"I freeze."
m "\"Oh uh...I mean, I don't really know what this food is, I'm just guessing...\""
show ale w with dis
al "\"No, I mean, it's your words. So many of them and in complete, complex sentences.\""
"Fuck, I'm bad at this."
al "\"I guess the Wolves uplifted intelligence a lot more back then.\""
m "\"Oh, maybe...\""
"I wonder if I've ruined our plan already, but Alexios doesn't seem alarmed, just curious, so I turn my attention back to the food."
"There isn't much left on the table."
"The meat was mostly cleaned off the bones by Cato."
"Next to it are four slices of bread and the bowl of olives."
"Alexios starts on the poultry, working at it with his claws until it comes apart in two pieces with a loud tearing sound."
"He hands me one half."
show ale with dis
al "\"You should be able to find a little meat on there.\""
"I take it from him, trying not to show my disappointment."
"Then he puts two slices of bread on a plate and slides it toward me before taking the remaining two."
al "\"Make sure to use the cheese. The bread is a bit bland without it.\""
"I pull a few thin strips of meat off of the bone and taste it."
"It's good, really, really good and I quickly search the bones for more, but there isn't much at all."
show ale smile with dis
al "\"Hungry?\""
"I look up and see Alexios delicately picking at his own half of bird."
m "\"Yeah...haven't eaten in a few days.\""
show ale shocked with dis
al "\"Oh really? Why not?\""
m "\"The...trip here was a bit rough. I guess I did eat on the ship, but it wasn't very filling.\""
show ale tilt with dis
al "\"Oh, like the protein sludge they have? Yeah, that stuff is quite terrible. I can understand why you're hungry. Well, you won't have to worry.\""
m "\"Why not?\""
show ale smile with dis
al "\"We eat dinner with our masters in their rooms. Amicus always serves himself very large portions and also sneaks me my own food since Cassius doesn't take much himself.\""
"Alexios slowly spreads cheese onto his bread."
al "\"He will take good care of you in that respect.\""
"With the mention of Amicus, I start to feel a bit lonely again."
"Actually, something I've noticed is that the whole palace seems to be lonely."
m "\"So...where is everyone?\""
"Alexios chews thoughtfully on his bread."
show ale tilt with dis
al "\"Hm?\""
"I try to think of a way to phrase things stupidly, then give up as I decide he already knows I'm able to form \"complex\" sentences."
m "\"This palace doesn't seem to have very many people around.\""
al "\"Oh! Well, do you expect others to be here?\""
m "\"Well, I guess like servants, or guards, or some other officials?\""
show ale talking e with dis
al "\"Most needs in the palace are covered by artificial intelligence and drones. Same goes for the palace defense.\""
al "\"I suppose it may be different where you're from, but the Siblings learned long ago that the fewer sapients you have in a location that needs to be secure, the better. You and I are an exception.\""
"The bread tastes like literal chalk, so I decide to spread a little bit of the cheese on it despite the smell."
"To my surprise, it's salty and creamy and not bad at all."
"The smell {i}is{/i} hard to ignore, though."
m "\"So...what is the point of having a pet, then?\""
show ale tilt w with dis
al "\"Amicus didn't tell you?\""
m "\"Well, he did. He just mentioned status and stuff. Is there any other reason? Why do we have to do stuff for them if they have robots that can do it instead?\""
show ale talking w with dis
al "\"Status is the main reason, yes. Our duty is to be by their side during public appearances, or in official meetings. Obviously having an artificial sapient doing the same isn't impressive at all.\""
al "\"We don't really have to do anything manual in the palace, but Cassius likes the idea of a Sapient being his servant. He says it reminds him of the old days.\""
m "\"I see. Amicus told me that I don't really have to do anything for him...except brush his fur.\""
show ale smile w with dis
al "\"Ah yes, Amicus is very meticulous about that.\""
m "\"Do you know him well?\""
show ale w with dis
al "\"Fairly well. I've been here for a few months now, so I've had my fair share of interactions with him even though Cassius doesn't like it.\""
m "\"I see...what do you think of him?\""
show ale smile e with dis
al "\"I think that you're very lucky to have a master like Amicus.\""
m "\"Why's that?\""
show ale e with dis
al "\"Well, Amicus is very...kind. Sometimes he tries to be all official and assertive, and he likes to tease me, but he comes off as more open, whether he intends to or not.\""
show ale smile e with dis
al "\"This is all compared to Cassius, of course.\""
"I think for a moment."
m "\"Do you not like being Cassius's pet?\""
"There's a pause, though Alexios continues to smile."
al "\"Cassius is very...specific about how he wants to be talked to and such, but this is a great quality for a prospective emperor to have, for sure.\""
show ale e with dis
al "\"But in casual conversation, it's much easier to talk to someone like Amicus.\""
"I take a sip of the wine and as far as I can tell, it's similar to the few times I've had it on Earth."
m "\"He has been really nice to me.\""
"At least after the whole kidnapping thing."
al "\"He is a very nice person. He just tends to...not think everything through.\""
show ale tilt e with dis
"Alexios's eyes flick to look behind me before he focuses back on my face."
show ale smile e with dis
al "\"Understand that normally we shouldn't speak so candidly about our masters. This is just a conversation between pets.\""
m "\"Oh...Yeah, I understand.\""
"There's a moment of silence that goes on just long enough to be uncomfortable."
show ale w with dis
al "\"Yes, I thought you would...I have to say that you're extremely perceptive, almost on the same level as a Sibling.\""
"I wince internally as Alexios points out my intelligence again."
"Only took me 10 minutes to fail my one and only job."
"Alexios smiles at me again."
show ale smile with dis
al "\"Ah, was I not supposed to know that?\""
"Apparently he's perceptive as well."
m "\"Uh...\""
show ale with dis
al "\"Don't worry. Like I said, this is between pets—\""
"Alexios leans in conspiratorially."
show ale tilt with dis
al "\"I don't just blab everything I know to my master. I'm simply his servant, not spy.\""
show ale with dis
"He leans back again."
al "\"Though he might wish I was, but honestly it's really nice to be able to talk to someone other than my superiors. Amicus was the only one to treat me as an equal, but Cassius usually keeps our contact minimal.\""
"I put the last bit of bread into my mouth and as soon as I do, Alexios sits up."
al "\"Com, we're finished.\""
com "\"Yes, Alexios.\""
"I watch with fascination as the dishes levitate off the table and float away through the archway they originally came through."
al "\"Do you want to go outside? Like I said, there's not much to do, but the gardens do require a more sapient touch to keep them presentable.\""
m "\"Yeah, sure.\""
"I brush crumbs off of my jeans and stand up."
"I'm still hungry, but the amount that I've eaten has taken the edge off of it, at least."
stop music fadeout 5.0
scene bg palace1 with dissolve
"I follow Alexios quietly through the halls, really enjoying the architecture of the palace for the first time."
"We enter the main hall and Alexios stands in the sunlight pouring in through the archways."
show ale smile with dissolve
al "\"Ahh, aren't the mornings beautiful here? This is the best time to do work in the gardens. I'd say we have a good three hours before it gets too hot.\""
"We start walking out into the gardens when I'm suddenly struck by something odd."
m "\"So, you just said we have three hours?\""
show ale tilt e with dis
al "\"Yes?\""
m "\"Well...how long is an hour here?\""
play loop "sfx/fountain.ogg" fadein 5.0
scene bg garden1 with dissolve
show ale w with dis
al "\"The same.\""
m "\"Oh, we use the same minutes and hours and stuff?\""
"That didn't seem possible."
"Alexios thinks, rubbing the spot above his left eyebrow."
show ale tilt w with dissolve
al "\"Ah, well, the Lingua is a complicated device. It's Parental tech, so it's something that we don't really understand at all, but what we do know is that it translates language in a way that offers the best understanding possible for the host.\""
"Alexios crouches by a pillar, examining the ivy growing around its surface."
show ale w with dis
al "\"I used a measurement of time specific to the Wolves and their language, and the Lingua simply translated it to a measurement you'd better understand.\""
"The small cat chuckles."
show ale smile w with dis
al "\"It's something I've given up on understanding myself. It's not perfect and can create really confusing situations. Especially when it comes to certain words and numbers.\""
m "\"Oh.\""
"I see Alexios single out a small, white flower growing at the base of the pillar before he plucks it out and sets it to the side."
"I start to wonder if I should maybe learn the language."
"The lingua is impressive and all, but it doesn't seem like it's very specific."
show ale smile w with dis
"Alexios grins."
al "\"Don't think too much about it.\""
show ale w with dis
al "\"Just try to remember that that doesn't mean everything actually {i}is{/i} the same. There are 19 hours in a day on Adastra which I imagine is at least somewhat different compared to your own planet.\""
show ale with dis
al "\"Anyway, what I'm doing right now is pulling up some weeds. The drones do a good job of watering and pest control, but they often miss smaller weeds like these.\""
"I crouch at the pillar next to Alexios, searching through the ivy for weeds to pull at the base."
m "\"So...there are 19 hours in a day here?\""
al "\"Yes.\""
m "\"That's a bit shorter than back home.\""
al "\"Oh I get that. There are 30 hours in a day where I'm from. You get used to it after a few weeks, though. I prefer it, actually\""
hide ale with dissolve
"I turn my attention back to the pillar and suddenly find myself staring right at a strange, crab-like thing sticking to the stone."
"At first I wonder if it's a carving of some kind, since it's so big."
"But as I look closer, it moves and I realize that it's a massive living spider."
"The next thing I know, I'm rolling away from the pillar action movie-style before popping back up to my feet."
scene bg garden1 with vpunch
m "\"OH MY GOD!\""
show ale shocked with dis
al "\"What is it!?\""
m "\"A spider...thing!\""
"I'm standing a good ten feet away from the pillar now, but I can still see the massive spider, its thick legs fanned out to the width of a clock."
"I shiver."
m "\"Eugh!\""
show ale smile w with dis
al "\"Ah...hahaha. Oh, I see.\""
"I stare at him."
m "\"How is that funny!?\""
al "\"I'm sorry. They {i}are{/i} very startling when you first encounter them.\""
"Alexios walks up to the spider and starts making shooing motions at it."
"Even from here I can see its black, beady eyes."
"It doesn't move at all, choosing to sit motionlessly on its pillar."
al "\"Adastran arachnids and insects are disturbingly large compared to the ones on my home moon.\""
"I look around, suddenly feeling like I'm in danger, imagining giant wasps descending from the skies."
show ale serious w with dis
"Alexios starts to look more frustrated as the spider refuses to be intimidated by his limp-wristed swipes."
al "\"Nothing in the gardens is dangerous though, and they're needed to balance the ecosystem. This creature's venom is far too mild to cause much more than an itchy bump, if it bites at all.\""
"Alexios gives another weak swipe at the spider and it takes the opportunity to bolt up his arm so fast that it becomes a blur before stopping on his face."
show ale shocked w with dis
"For a moment, we both stand there in shock as it clings to him like a facehugger."
"Then—"
show ale vshocked w at jumping with dis
al "\"BY GALEN! GET IT OFF!\""
show ale vshocked w at my_shake with dis
"He dances around in place for a moment as I simply watch in fascinated horror."
"Finally, he shakes his head hard and the spider runs down his front to scuttle across the ground and into some bushes."
"Alexios heaves for breath for a moment, trembling."
"Despite myself, I have to laugh in amazement at what I just saw."
show ale embarrassed e with dis
al "\"Wh—Why are you laughing?\""
m "\"Sorry, it was just...so surprising, and you were so sure of yourself until—\""
"I chuckle again."
al "\"Well, it surprised me!\""
"He shivers, rubbing his shoulders."
show ale flustered e at center with dis
al "\"There's honestly nothing to be afraid of when it comes to those, but it was right on me, and the way they move—\""
"He shudders again."
show ale serious w with dis
al "\"And you just stood there and watched!\""
m "\"I mean, what could I have done? If that had happened to me I would have jumped in the pond.\""
"Alexios sighs and I see his fur start to flatten down again."
show ale smile w with dis
"Then he also chuckles."
al "\"Well...I was about to.\""
show ale w with dis
al "\"Anyway, let's get back to work. If you see another spider...just work around it.\""
stop loop fadeout 5.0
hide ale with dissolve
play music "music/secondthoughts1.ogg"
"For the next hour, we move from pillar to pillar, cleaning up the unwanted weeds."
"I'm way more vigilant now, checking every pillar for spiders before we start."
"Luckily, we don't come across anymore."
"After a while, we finally sit on a bench under some trees and Com floats out a few platters of tiny pastries that remind me of quiches."
"Those are followed by glasses of cold, green, vegetable-tasting drinks."
"It's delicious."
m "\"So, can I ask where you're from?\""
show ale smile with dissolve
al "\"Very far away. Even further than your home.\""
m "\"What brought you here?\""
show ale tilt with dis
"The cat sighs and pauses with a pastry halfway to his mouth."
al "\"It's a bit complicated, but I was here as a sort of ambassador. I arrived just as the Stretch Drive depletion occurred.\""
m "\"What was that?\""
"Alexios shrugs."
al "\"Well, for whatever reason, the Romanus stopped supplying the Wolves with Stretch Drive power when the emperor died. They're starbound right now, so they can't shuttle me back to my planet.\""
show ale with dis
al "\"The situation between the wolves and their parents is worrying, and we don't know how long the wolves will be without the Stretch, so my people sent their own ship to retrieve everyone on Adastra, but I, uh, missed it.\""
m "\"Missed it?\""
"Alexios frowns, looking embarrassed again."
show ale tilt e with dis
al "\"Well...I slept in and missed the departure.\""
m "\"Wow, really?\""
al "\"I mean, it happens to the best of us, no?\""
m "\"I guess...why didn't they wait for you? That's kind of messed up that they'd just leave.\""
al "\"When using Stretch tech, time is important. Everything runs on a specific schedule, so if you miss it, you miss it. And they're certainly not going to send another one out for one person.\""
m "\"Wow, didn't you have an alarm clock, or someone to wake you?\""
show ale sad e with dis
al "\"Trust me, it was a series of many unfortunate events that lead to that happening, the main one being that even though I woke up with enough time to reach the starport, I got lost in Adastra City's terrible public transportation system.\""
al "\"I was running from platform to platform, Wolves all around me trying to touch me because they've never seen a Cat before, and I could barely read the signs because...well, for my species water comes from the eyes when we're stressed, so...\""
m "\"Oh, you were crying.\""
show ale embarrassed e with dis
al "\"...You know what that is?\""
m "\"Yeah, my species does it too.\""
"He looks away and I can see the insides of his ears turn red."
al "\"Ah, I did not know that. It's a shared trait among us and the Wolves, but I don't know many others that do it, aside from the Khemians.\""
show ale serious e with dis
al "\"Anyway, I eventually decided to use my situation to continue my work and build a relationship with the imperial family. So, I became Cassius's pet.\""
"Alexios's situation doesn't sound all that different from mine, even though the reasons for us getting here were very different."
m "\"When does the next ship come?\""
show ale tilt with dis
"Alexios shrugs."
al "\"Years. At least one a decade, but sometimes more. I'm hoping within the next few years, though.\""
m "\"I'm sorry to hear that.\""
show ale smile with dis
al "\"Heh, it's not the worst life, and the Wolves treat me well enough. We do have a special relationship.\""
m "\"...With Cassius?\""
al "\"Between us and the Wolves. Unlike the other siblings, our parents originated in the same galaxy. Though our views are very different, there's a bond there.\""
"Alexios brushes his paws together."
show ale with dis
al "\"Are you done?\""
m "\"Yeah.\""
stop music fadeout 10.0
play loop "sfx/fountain.ogg" fadein 10.0
al "\"Com, we're finished.\""
"And with that, the platters and glasses float away."
"I'm starting to get used to all of this."
al "\"But...[mc], was it?\""
m "\"Yeah.\""
show ale smile with dis
al "\"Haha, I'm sorry. I guess we skipped introductions. You already know me as Alexios, but you can call me Alex.\""
m "\"Hello, Alex.\""
show ale talking w with dis
al "\"Hello [mc]. So now that we're no longer pretending that you're not so sapient anymore, where are you from? Tell me about yourself.\""
"That gives me some pause."
"While he's been really nice to me so far, I know I can't just reveal everything to Alex, so I settle on being vague like he was."
m "\"Well, I'm from far away, but less far away than you. I'm a primate.\""
show ale w with dis
al "\"I see. Are you important among your people?\""
m "\"No, I'm just a student.\""
al "\"Oh...do you know why Amicus chose you, then?\""
m "\"...I think he just chose me at random. I just happened to be where the uplift occurred.\""
show ale shocked w with dis
"Alexios blinks, then laughs."
show ale smile w with dis
al "\"That's just like Amicus.\""
m "\"Yeah, it is, actually.\""
show ale with dis
al "\"But I guess it makes sense to choose a commoner if he wants to unite the abandoned Children again.\""
m "\"Oh yeah?\""
"I decide that shifting the conversation away from me is a good tactic for now."
al "\"Yeah, didn't he explain that to you?\""
m "\"Um, maybe a little. He didn't tell me all that much.\""
show ale smile with dis
al "\"Hehe, don't take it personally. Amicus doesn't often think ahead.\""
show ale talking with dis
al "\"Right now, the Wolves are in a bit of a strange situation. Again, this is between you and me, but they've fallen behind the other Siblings in terms of spread and resources.\""
al "\"The main reason being that they don't uplift their Children to similar intelligence levels as themselves.\""
m "\"Intelligence levels? I thought they just spread their culture?\""
"Alex frowns at me."
show ale tilt with dis
al "\"You don't know? I guess you were abandoned but...you should know that your intelligence, every Child's intelligence, was uplifted by a Sibling.\""
m "\"Oh...no, I guess we lost that bit of information.\""
show ale serious with dis
al "\"Well, that's not the end of their problems. These Children are indentured servants in a way. In exchange for having their intelligence...mostly...uplifted, they have to serve the empire until the debt is repaid.\""
"That doesn't sound good."
m "\"Oh. And how long has that been going on?\""
show ale smile with dis
al "\"Heh, well, let's just say that the first successfully uplifted Wolf Children haven't quite finished repaying their debt.\""
m "\"That...sounds like slavery?\""
"Alex glances at me."
show ale serious with dis
al "\"It does, doesn't it?\""
"That's confusing to me."
m "\"But, if they have all of these robots and stuff, why do they need sapients to be their slaves?\""
al "\"Advanced artificial sapients are gifted by the parents. We can't build them. We're a bit spoiled here in the palace, but outside not so much.\""
al "\"And even then, artificial sapience isn't perfect and likely never will be. Actual thinking machines don't exist. This is why uplifting Children to the same intelligence level as a Sibling is important; good ideas can come from anywhere.\""
m "\"I guess your people don't do what the wolves do?\""
al "\"No, we uplift our Children as much as we can. This practice is isolated to the Wolves. They're seen by the other siblings as...harsh on their own Children, and the rights of Sapients in general.\""
m "\"I see.\""
"I'm starting to see the Wolves and even Amicus in a whole new light."
"As if reading my mind, Alex goes on."
show ale with dis
al "\"But things are changing. Amicus choosing you as his pet shows that he sees you as close to an equal...but then there's Cassius.\""
show ale serious with dis
"Alex's tail swishes around on the bench between us."
al "\"He'd rather things stay the same...or even regress. That's why he's made a strong challenge against Amicus. There are many Wolves who are unsure of the change Amicus suggests, and the proposed alliance between the Wolves and the Khemians is only adding to it.\""
m "\"Khemians?\""
al "\"They're another Sibling species, the most powerful in the galaxy, in fact. But that worries a lot of people here. There hasn't been a war between Siblings in over a hundred years, but the last one was between the Khemians and the Wolves.\""
al "\"You can imagine what sort of problems that might create. So Cassius, wanting the Wolves to stay independent and in complete control of their Children, is rather popular.\""
show ale  with dis
al "\"You might wonder why I'm telling you this, but I want you to understand the empire that you're in. It will make it easier to...navigate.\""
"I was in fact wondering why he's telling me all of this."
"Does he have some other motive that he's not telling me?"
"I look over at him."
m "\"Do you want Cassius to become emperor?\""
show ale smile with dis
al "\"I like that we can discuss a lot of things, and being a Sibling allows me to have more freedom than most, but that's one thing that I should probably keep silent on.\""
"That only confuses me more, but it doesn't sound like he's on Cassius's side."
"Maybe Amicus and I could find an ally in him?"
m "\"Well, I think I would prefer Amicus if his whole thing is to treat other sapients equally.\""
"From what I can tell, that seems to please Alex."
show ale with dis
al "\"Well, we'll find out soon enough after the trials.\""
"Alex's mood suddenly brightens."
show ale smile with dis
al "\"But anyway, I've really been enjoying our time together today. Like I said, it's so nice to be able to talk to someone who isn't my superior. I hope we can do this often while you're here.\""
m "\"Yeah, of course.\""
show ale with dis
al "\"Wonderful.\""
"Alex raises a paw to look up at the sun...at Vita."
al "\"We should keep working. It's starting to get too hot out here.\""
stop loop fadeout 3.0
"For the next several hours, we work around the garden before finally moving inside to walk around the palace a bit."
scene bg palace1 with dissolve
"He points to doors for things like the throne room and communal bath, but we never go inside and he tells me I should only do so when I'm with Amicus."
scene bg diningroom with dissolve
"Eventually, we move back to the dining room where Alexios suggests we watch the screens until our masters return."
"He says it will better acquaint me with Wolvish culture."
"It takes me a moment to realize that I'm watching a sort of film starring wolves similar to Amicus."
"They're acting out scenarios about traveling into space and finding more sapients."
"The sapient species they find are wolves in masks...I guess they don't really have CGI because every effect looks practical."
"It's long, boring, and the acting is overly-exaggerated, like they're in a silent film."
"Finally, after what seems like a good three hours, Alex tells me that Amicus will be returning soon and that I might want to tidy up his room before he gets back."
"I'm relieved to cut the film short, and Alex and I part ways to go to our respective rooms."

scene bg palace1night with dissolve
play loop "sfx/crickets.ogg" fadein 3.0
"I'm surprised to see that it's already dark outside."
"Even with the shorter day, I guess mindlessly watching wolves overacting to other wolves in masks took up more time than I thought."
"On my way through the marble halls, I pause every now and then to look at the large murals on the walls depicting everything from wolves swimming to wolves swinging swords at other canines."
"In the great hall is the largest mural, and it depicts five wolves."
"The features are flat and lack any sort of perspective, making the muzzles look a bit askew."
"Two larger wolves loom over the other three; one is white with a feminine shape while the larger of the two is black and holding his paw to his chest."
"Around his head is a wreath."
"Of the three smaller wolves, one is also clearly feminine while another is white."
"I wonder if this might be Cassius and Virginia which would leave the remaining wolf in the middle to be Amicus."
"He's skinnier, and I wonder if this might be him as a child, or teenager."
"A glowing wreath floats above his head."
unk "\"Ahem.\""
"I jump as someone clears their throat very loudly next to me."
show cat with dissolve
"I turn around and find myself staring at Cato, the advisor."
"He looks me up and down for a moment...at least I think he does."
"More silence."
"I open my mouth to respond, then remember what Amicus told me."
"I let my eyes unfocus and my mouth droop open a bit."
m "\"Uhhhh...\""
"Cato's ears twitch at the sound I make then clears his throat again."
show cat bow with dis
ca "\"Hello...[mc], was it? How are you enjoying your first day in the palace?\""
"I wonder if I should keep droning, or if I should at least answer the question."
"I am technically a sapient, so I suppose it's okay if I sort of understand."
m "\"Uhhh...goood.\""
"The left side of Cato's scarred face twitches as he waits for more, but I don't give him anything."
show cat talking with dis
ca "\"Good, good...I trust that Alexios showed you around the palace? It's a bit of a stifling life behind these walls, but hopefully with time we will be able to take you out to the city.\""
"I cross my eyes a little."
m "\"Oh...I like it...\""
show cat smile with dis
ca "\"Heh, yes. So...where are you from again, exactly?\""
"There's something behind this wolf's words, something there that's a little more than innocent curiosity."
m "\"Uh, big rock planet by star...\""
"Cato waits and again I don't say anything more."
show cat frown with dis
ca "\"Do you have a name for the planet?\""
m "\"Yeah....Big Rock Planet.\""
"Cato massages the left side of his forehead, looking a little bit annoyed."
ca "\"Big Rock Planet?\""
m "\"With water...\""
"Cato stares."
ca "\"So...Big Rock Planet With Water?\""
"I nod dumbly."
hide cat with dissolve
"Cato sighs loudly and stalks off, not even bothering to end the conversation."
ca "\"Wonderful...now I have a headache.\""
"And with that, he disappears around the corner."
"I decide that I did an okay job as Cato seems to think that I'm a massive idiot."
stop loop fadeout 3.0
"I make my way quickly to Amicus's room, glad to not run into anyone else."

scene bg amicusroom with dissolve
"There isn't much to do; Amicus's room is spotless, so after meandering around and smoothing the bed covers over, I choose to sit down on the sofa and wait."
"Despite the fact that I've only been up for what's probably been ten hours, I'm exhausted."
"Maybe I won't have any trouble adjusting to the shorter days."
"As I start to doze, there's a sudden clattering sound toward the door."
"I jump and see Amicus come in, wheeling in a tray with several plates on top of it, heaped high with food."
"He grins at me and I get a feeling of relief at seeing him."
show ami happy with dissolve
a "\"Hello! Sorry, I suppose Alex didn't tell you that they set these outside the door on the 15th hour. He treat you well?\""
m "\"Yeah, he was nice.\""
"Amicus wheels the cart up to the sofa, then flops back onto it next to me, making the whole thing shake."
show ami with dis
with vpunch
play music "music/memories.ogg" fadein 5.0
a "\"Uggghhhh, that was a long day.\""
m "\"Are you okay?\""
"Amicus opens one eye at me."
a "\"Barely. Had to go over maths today and my head feels as if it's going to explode. Didn't help that Balbus kept cracking me over the head with his stick when I answered wrong.\""
m "\"Wow, that sounds harsh.\""
show ami happy eyes with dis
a "\"Don't worry, it was nothing compared to the one you gave me.\""
"Amicus smirks, and I can't help but smile back at his teasing."
"He seems to have become more comfortable around me with how relaxed he is."
m "\"I am sorry about that.\""
show ami with dis
a "\"Don't be, and stop apologizing for it. Now let's wash and eat. My stomach's felt hollow since breakfast.\""
hide ami with dissolve
"We both go to the restroom to rinse our paws/hands in the sink before heaping our plates with food."
"It's more of the same with bread and meat and olives, but there's also a good amount of other vegetables and fruit that I have a hard time identifying."
"Amicus shows me how to combine the fruit and cheese on the bread and I find myself really starting to like the smelly spread...as long as I ignore the smell."
"Compared to breakfast, Amicus really wolfs down a lot of food."
"He probably ends up eating about three times as much as me."
"All the while, he tells me about his scary instructor and how he punishes him way more than Cassius."
m "\"Well, does he usually get the answers right?\""
show ami embarrassed with dis
a "\"Well...yeah, but he should help me understand rather than smack my ears. That doesn't help anything unless he has the information in his stick and is bashing it into my brain somehow.\""
m "\"Don't worry; I hate math too.\""
a "\"Well, I'm better in other things like literature and history. Ha! Cassius is hopeless at remembering battles.\""
show ami motivated with dis
"Amicus flexes a bicep."
a "\"And he can forget about wrestling. He could never beat me in a fight.\""
m "\"Yeah, I wouldn't think so.\""
show ami with dis
a "\"So yes, he can have the maths all he wants. The trials don't involve that anyway.\""
m "\"What are these trials you guys keep talking about?\""
"Amicus takes a big gulp of wine, gasping when he finally pulls the goblet away from his face."
show ami crossed with dis
a "\"What Cato is considering using to decide the next emperor. Essentially three trials; music and dance, rhetoric, and finally, combat.\""
m "\"And whoever wins those becomes emperor?\""
a "\"Well, whoever wins two out of three. Combat is last so that if one of us wins the first two it won't come to that.\""
a "\"I'm really just hoping that Cato chooses me in the next few days now that he's seen you. But if the trials do happen, you have nothing to worry about.\""
"Amicus grins at me confidently."
m "\"I don't?\""
show ami crossed serious with dis
a "\"I'm better than Cassius in at least two of those things, perhaps even in music and dance.\""
m "\"You know, I'd believe you, but one thing I know about you is how, um...overly confident you are when it comes to certain things.\""
show ami embarrassed with dis
a "\"Why do you say that?\""
m "\"Our entire experience on the ship, maybe?\""
show ami crossed serious with dis
a "\"That's...different. I was doing something I didn't really understand. I understand my studies...aside from maths.\""
"Amicus leans back finally, one paw on his stomach."
show ami with dis
a "\"Anyway, how was your day? Did Alex show you around?\""
"Amicus starts to grab the remaining food to set aside on its own plate."
m "\"Yeah. I've realized that there isn't much to do.\""
a "\"Ah, yeah, it was a bit of a bad day. I have tomorrow off from studies though, so we can do something entertaining.\""
m "\"Like what?\""
show ami smile with dis
a "\"Oh, I don't know. Go swimming, go to the baths, talk. You name it. Maybe eventually we can go to the city too.\""
m "\"The city outside?\""
show ami with dis
a "\"Well, everything's outside.\""
m "\"I mean, the one that I can see across the lake.\""
a "\"Yes, that one. Adastra city, the capital of our empire.\""
m "\"Oh...isn't it kind of small for that? I mean, it looks really nice, but it kind of just looks like an average-sized city.\""
"Amicus frowns."
show ami embarrassed with dis
a "\"I think it's quite large. How big are cities on Earth?\""
"I shrug."
m "\"I dunno, pretty big? Millions of people.\""
"Amicus raises an eyebrow."
show ami thinking with dis
a "\"Millions?\""
m "\"Uh, yeah.\""
"I wonder if the Lingua is translating everything correctly."
m "\"Why? How big is Adastra?\""
a "\"The city? Just over five million. The Wolf population is 80 million.\""
m "\"Oh.\""
a "\"How many humans are there?\""
m "\"Like, seven billion.\""
show ami shocked with dis
"Amicus chokes."
a "\"What!?\""
m "\"Is that a lot?\""
show ami surprised with dis
a "\"That's preposterous! Do you not have population control measures put in place?\""
m "\"Well, not in most places.\""
"Amicus shakes his head."
show ami crossed serious with dis
a "\"Well, you are Parent-less, so I guess it makes sense your species might be so...misguided?\""
"Amicus seems to try very hard to choose the last word even though he's still being very condescending."
"He seems to notice my annoyance, though."
a "\"Well, is your species doing well? Is your planet able to sustain such a population?\""
m "\"...Sort of. I guess there are problems.\""
"Amicus strokes his chin."
a "\"Well, I suppose when I become emperor I could ask the Parent about your species. The whole thing is a real mystery, but it's clear that we must have overlooked your people somehow.\""
show ami crossed with dis
"He smiles at me."
a "\"Maybe we could even bring you into our fold again!\""
m "\"Whoa, hang on a second.\""
"Images of roman spaceships descending from the heavens to enslave the human race all because of me flash through my mind."
m "\"You know, Alex told me about what you do to the other sapients. It doesn't sound like something humans would want to be a part of.\""
show ami embarrassed with dis
a "\"What did he tell you?\""
m "\"The whole enslavement thing.\""
a "\"Enslavement?\""
m "\"What you do to your Children.\""
a "\"Well...that's a harsh word for it.\""
m "\"No, it's the right word. Humans have done the whole 'indentured servant' thing back on Earth, and it never turned out well for the 'servant'.\""
"Amicus's ears go down a bit."
m "\"And as misguided as humans might be, we've at least abolished slavery.\""
"I notice Amicus's ears turning red."
"Maybe he never expected to be lectured on ethics by a human."
a "\"Ah, well, I—I do mean to change things a bit when I become emperor.\""
m "\"A bit?\""
show ami sad with dis
a "\"I mean, things can't just be changed all at once; it has to be gradual.\""
m "\"Hm.\""
show ami angry with dis
"Amicus flicks his tail in annoyance at me."
a "\"Listen, I agree with you. We've been trying to change the way we've treated our Children for generations. My grandfather and father both worked towards this.\""
m "\"Well, while that's messed up and definitely wrong, I think the intelligence thing might be even worse.\""
show ami embarrassed with dis
a "\"What intelligence thing?\""
"The grimace on Amicus's face tells me that he might already know the answer."
m "\"The way you stunted intelligence in the Children you uplifted.\""
"Amicus is silent for a moment."
"I can tell that all of this is making him very uncomfortable."
"I have to ask myself again how I got to this point; sitting on a sofa debating ethics with a prospective emperor wolf"
"He finally folds his arms and huffs."
show ami crossed serious with dis
a "\"Again, I agree with you on all of this. I don't like the way we've treated our Children. In the end I truly feel that becoming a more compassionate and united empire will lead to a better outcome for everyone.\""
a "\"It's going to take small steps, but understand that it's something I mean to fix.\""
a "\"And stop saying \"you\" like {i}I{/i} did it. I was born into this.\""
"I've come to realize how much of an open book Amicus is as a person, so I don't doubt his words."
m "\"Well, as long as Cassius doesn't become emperor.\""
"Amicus snorts."
a "\"Not a chance.\""
m "\"Well, if he DOES it sounds like he's going to reverse all of that.\""
a "\"And I'm saying there's no chance of it...Wait, how much has Alex been telling you?\""
m "\"It was a short conversation. I asked him about the empire.\""
"I didn't, but I don't want to get Alex in trouble in case he wasn't just supposed to tell me."
m "\"Cassius seems like a terrible person by the way, and I'm not just talking about his personality. He wants to keep people enslaved.\""
show ami embarrassed with dis
a "\"It's...complicated. He's just very traditional, but again, there's no chance.\""
"I sigh at the wolf's overconfidence, but he does know his brother far better than I do."
m "\"Well, I'm at least glad that I'm behind the right wolf in getting myself home.\""
show ami crossed with dis
a "\"The right wolf?\""
m "\"Yeah, I can't imagine being under your brother.\""
"Amicus glances at the plate he'd been building with food."
a "\"Speaking of, I'm going to bring this to Alex in the garden. Did you want to accompany me?\""
"I run a hand through my hair, feeling the griminess from two days of no shower."
m "\"Actually, can I use the shower while you're gone? I feel kind of gross.\""
a "\"Oh yeah, sure. Uh, just step in and it starts up. There's a screen on the wall that controls temperature. It has a color spectrum that you can drag a finger across—\""
m "\"I'll figure it out.\""
show ami eyes with dis
a "\"Ah, right. Well, I should be back by the time you're finished.\""
hide ami with dissolve
stop music fadeout 10.0
"And with that, Amicus balances his plate of food in his paws as he strides out of the room, leaving me to go into the bathroom."
scene bg bathroom with dissolve
"I quickly use the toilet again, suddenly glad that I don't have  to use a \"public\" toilet like the ones I'd seen drawings of in my Roman history books."
"The shower is easy enough to understand, and the water is immediately warm and pleasant, so I don't have to bother with the temperature."
"There are several glass bottles of soap, so I choose the one that smells the best and give myself a quick wash."
"When I'm done, I grab a towel off the wall and dry off before wrapping it around my waist."
"I think about putting my clothes back on, but the idea of stepping back into that underwear has me hesitating."
scene bg amicusroom with dissolve
"Instead, I open the door and am greeted to the sight of Amicus sitting on the edge of the bed, looking off to the side, a paw in his lap holding a brush."
"His head snaps in my direction before he immediately averts his eyes."
play music "music/starship.ogg" fadein 10.0
show ami shocked with dissolve
a "\"Sorry! Sorry! I didn't mean to see, I thought you'd be dressed—\""
m "\"Hey, it's fine. I've got the towel on.\""
show ami surprised with dis
"Slowly, Amicus turns his gaze back to me, eyes drifting down my torso before immediately snapping back up again."
a "\"Oh! Uh, I thought you hated any sort of nudity?\""
m "\"Not really, just the...genitals. Even then, I don't hate it. It's just...more private.\""
a "\"Ah...\""
"Amicus seems to be staring at me and I start to feel a little self-conscious."
m "\"Is everything okay?\""
show ami sad with dis
"Amicus looks away again."
a "\"Sorry, I—I'm just not used to seeing you like that. I've only seen humans with clothing, so I just sort of imagined you to always be that way.\""
m "\"Well...my clothes are dirty so I was going to ask you about maybe getting some clean ones, at least until you can get me that tailor?\""
show ami surprised with dis
a "\"Oh, of course! Com! Send us some robes from storage...children's robes, please.\""
com "\"Yes, Amicus.\""
m "\"Thanks.\""
show ami eyes with dis
a "\"Of course.\""
"I stand there awkwardly for another few seconds until Amicus seems to snap back to reality again."
show ami surprised with dis
"He holds up the brush."
show ami with dis
a "\"Anyway, I thought maybe you'd like to be groomed too? I feel it's only fair after what you did for me.\""
m "\"Oh, well, it's only on my head.\""
show ami happy eyes with dis
a "\"All the easier for me, then.\""
"Amicus grins."
m "\"Well...alright.\""
show ami with dis
"I walk over to the bed and sit with my back to the wolf."
"Amicus adjusts his seating to face me more directly, then starts to run the brush gently through my hair."
"We sit in silence for a bit, and I start to enjoy the feeling of the brushing especially the way the firm bristles run across my scalp, giving me shivers up and down my neck."
show ami talking with dis
a "\"Sorry for talking so much earlier. I...I'm not used to being able to talk to someone. The palace is a bit lonely, so having a friendly conversation with someone other than Com is a bit of a novelty.\""
show ami eyes with dis
"Amicus chuckles."
a "\"That was probably why I was having so much trouble focusing on my studies today; I was so excited to come back home and speak with you.\""
"Hearing that makes me feel a little bad for the wolf."
"I suppose being the prospective emperor doesn't allow you to have many friends, and being in such an empty palace definitely seems lonesome."
"I guess this is why Alex told me basically the same thing."
m "\"You're fine. And I didn't mean to be too harsh earlier. I know it's not your fault.\""
show ami with dis
a "\"No, I think we're on the same page on that one. All the more reason to unite against Cassius, eh? Oh!\""
"As if he'd forgotten something, Amicus's other paw comes around my side and on his palm I see two purple grapes."
show ami happy with dis
a "\"I managed to snatch a few of those off of Alexios's earring. He wasn't too happy about that, haha! Want one?\""
m "\"Seriously?\""
"I take one, more out of being nice to Amicus than anything, but when I bite into it, I can't help but notice how juicy and sweet it is."
show ami eyes with dis
"Amicus talks to me with the grape in his mouth."
a "\"Mmmh, I don't know why, but his grape earring always tastes the best. By the way, if you don't mind, I invited Alex to our outing tomorrow.\""
show ami with dis
a "\"Cassius is going to be away to do some speeches and is leaving Alex behind for once.\""
m "\"Of course not. We got along really well.\""
"I lean my head back, allowing the wolf to continue the brushing."
a "\"Your fur...hair, you call it? It's not like a wolf's fur, but it's rather nice.\""
"I smile."
m "\"Thank you, Amicus.\""
a "\"If you'd like, I can do this for you everyday. I feel that's fair.\""
"I have to admit that I really like this, so I accept."
m "\"Yeah, sure. It feels really nice.\""
"I hear some thumping sounds and I imagine it's Amicus's tail wagging against the bed."
m "\"So washing you, brushing you, and making you smell nice are all my duties?\""
a "\"Well, that and accompanying me to important meetings and public outings, but all you do during those is stand there and look civilized.\""
m "\"Yeah, that's what you all keep telling me. This all seems pretty easy.\""
show ami embarrassed with dis
a "\"Though...there is one thing you can do for me before I go to bed.\""
m "\"What?\""
a "\"Well, a—a full-body massage.\""
"I look over my shoulder at him."
a "\"Ooor, we can just stick with the other duties.\""
"I laugh and Amicus's ears come back up."
show ami eyes with dis
"He continues to brush for a while longer before finally setting it aside."
show ami with dis
a "\"There, looks much better now!\""
"I gently run a hand over my hair, and I have to agree that it feels softer than it's ever felt before."
show ami eyes with dis
stop music fadeout 5.0
a "\"But anyway, [mc], I am looking forward to these months ahead with you, even though we started off a bit...poorly.\""
"I look back at the wolf, at his earnest, but tentative smile."
"He's definitely a man of contradictions; rash half of the time, but considerate most of the time."
"I'm not sure what to make of him, but at this point I feel like I can at least trust him, and that's saying a lot after what he put me through."
"I smile back."
m "\"Yeah, me too.\""
scene bg black with transition_fade
jump a1s3