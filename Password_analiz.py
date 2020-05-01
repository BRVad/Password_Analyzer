import string
import time
from tkinter import *


def dig_types(password):
    res = [0] * 4
    for i in range(len(password)):
        if sum(res) == 4:
            break
        if res[0] == 0 and lower.find(password[i]) >= 0:
            res[0] = 1
            continue
        if res[1] == 0 and upper.find(password[i]) >= 0:
            res[1] = 1
            continue
        if res[2] == 0 and dig.find(password[i]) >= 0:
            res[2] = 1
            continue
        if res[3] == 0 and spec_simbol.find(password[i]) >= 0:
            res[3] = 1
            continue
    return sum(res)


def find_in_dict(password):
    length = len(password)
    if length >= 3:
        for word in dictionary3:
            if password.find(word) >= 0:
                return 0
    if length >= 4:
        for word in dictionary4:
            if password.find(word) >= 0:
                return 0
    if length >= 5:
        for word in dictionary5:
            if password.find(word) >= 0:
                return 0
    if length >= 6:
        for word in dictionary6:
            if password.find(word) >= 0:
                return 0
    if length >= 7:
        for word in dictionary7:
            if password.find(word) >= 0:
                return 0
    if length >= 8:
        for word in dictionary8:
            if password.find(word) >= 0:
                return 0
    if length >= 9:
        for word in dictionary9:
            if password.find(word) >= 0:
                return 0
    if length >= 10:
        for word in dictionary10:
            if password.find(word) >= 0:
                return 0
    if length >= 11:
        for word in dictionary11:
            if password.find(word) >= 0:
                return 0
    if length >= 12:
        for word in dictionary12:
            if password.find(word) >= 0:
                return 0
    if length >= 13:
        for word in dictionary13:
            if password.find(word) >= 0:
                return 0
    if length >= 14:
        for word in dictionary14:
            if password.find(word) >= 0:
                return 0
    if length >= 15:
        for word in dictionary15:
            if password.find(word) >= 0:
                return 0
    if length >= 16:
        for word in dictionary16:
            if password.find(word) >= 0:
                return 0
    return 1


def result(password):
    summ = dig_types(password)
    attack_on_dict = find_in_dict(password.lower())
    if len(password) >= 14:
        if summ >= 3:
            if attack_on_dict == 1:
                return "Отличный"
    elif len(password) >= 8:
        if summ >= 3:
            if attack_on_dict == 1:
                return "Стойкий"
        elif summ == 2:
            if attack_on_dict == 1:
                return "Средний"
    elif len(password) >= 1:
        return "Слабый"
    return "Никакой"


def clicked():
    palikir = Label(window, text='{}'.format(result(txt.get())))
    palikir.grid(column=1, row=1)


dictionary3 = list('oat, not, ken, keg, ham, hal, gas, cpu, cit, bop,'
                       ' bah'.split(', '))
dictionary4 = list('zeus, ymca, yang, yaco, work, word, wool, will, viva,'
                       ' vito, vita, visa, vent, vain, uucp, util, utah, unix,'
                       ' trek, town, torn, tina, time, tier, tied, tidy, tide,'
                       ' thud, test, tess, tech, tara, tape, tapa, taos, tami,'
                       ' tall, tale, spit, sole, sold, soil, soft, sofa, soap,'
                       ' slav, slat, slap, slam, shit, sean, saud, sash, sara,'
                       ' sand, sail, said, sago, sage, saga, safe, ruth, russ,'
                       ' rusk, rush, ruse, runt, rung, rune, rove, rose, root,'
                       ' rick, rich, rice, reap, ream, rata, rare, ramp, prod,'
                       ' pork, pete, penn, penh, pend, pass, pang, pane, pale,'
                       ' orca, open, olin, olga, oldy, olav, olaf, okra, okay,'
                       ' ohio, oath, numb, null, nude, note, nosy, nose, nita,'
                       ' next, news, ness, nasa, mike, mets, mess, math, mash,'
                       ' mary, mars, mark, mara, mail, maid, mack, lyre, lyra,'
                       ' lyon, lynx, lynn, lucy, love, lose, lori, lois, lock,'
                       ' lisp, lisa, leah, lass, lash, lara, lank, lane, lana,'
                       ' kink, keri, kemp, kelp, keep, keen, kate, karl, june,'
                       ' judy, judo, judd, jody, jill, jean, jane, isis, iowa,'
                       ' inna, holm, help, hast, half, hale, hack, gust, gush,'
                       ' guru, gosh, gory, golf, glee, gina, germ, gatt, gash,'
                       ' gary, game, fred, fowl, ford, flea, flax, flaw, finn,'
                       ' fink, film, fill, file, erin, emit, elmo, easy, done,'
                       ' disk, disc, diet, dial, dawn, dave, data, derek, damn,'
                       ' dame, crab, cozy, coke, city, cite, chem, chat, cats,'
                       ' burl, bred, bill, bilk, bile, bike, beth, beta, benz,'
                       ' beau, bath, bass, bart, bank, bake, bait, bail, aria,'
                       ' anne, anna, andy, alex, abcd'.split(', '))
dictionary5 = list('yacht, xerox, wilma, willy, wendy, wendi, water, warez,'
                       ' vitro, vital, vitae, vista, visor, vicky, venus,'
                       ' venom, value, ultra, u.s.a, tubas, tress, tramp,'
                       ' trait, tracy, traci, toxic, tiger, tidal, thumb,'
                       ' texas, test2, test1, terse, terry, tardy, tappa,'
                       ' tapis, tapir, taper, tanya, tansy, tammy, tamie,'
                       ' taint, sybil, suzie, susie, susan, super, steph,'
                       ' stacy, staci, spark, sonya, sonia, solar, soggy,'
                       ' sofia, smile, slave, slate, slash, slant, slang,'
                       ' simon, shiva, shell, shark, sharc, shack, scrim,'
                       ' screw, scott, scorn, score, scoot, scoop, scold,'
                       ' scoff, saxon, saucy, satan, sasha, sarah, sandy,'
                       ' sable, rural, rupee, runty, runny, runic, runge,'
                       ' rules, ruben, royal, route, rouse, roses, rolex,'
                       ' robyn, robot, robin, ridge, rhode, revel, renee,'
                       ' ranch, rally, radio, quark, quake, quail, power,'
                       ' polly, polis, polio, pluto, plane, pizza, photo,'
                       ' phone, peter, perry, penna, penis, paula, patty,'
                       ' parse, paris, parch, paper, panic, panel, olive,'
                       ' olden, okapi, oasis, oaken, nurse, notre, notch,'
                       ' nancy, nagel, mouse, moose, mogul, modem, merry,'
                       ' megan, mckee, mckay, mcgee, mccoy, marty, marni,'
                       ' mario, maria, marcy, marci, maint, maine, magog,'
                       ' magic, lyric, lyons, lynne, lynch, louis, lorry,'
                       ' loris, lorin, loren, linda, light, lewis, leroy,'
                       ' laura, later, lasso, laser, larry, ladle, kinky,'
                       ' keyes, kerry, kerri, kelly, keith, kazoo, kayla,'
                       ' kathy, karie, karen, julie, julia, joyce, jenny,'
                       ' jenni, japan, janie, janet, james, irene, inane,'
                       ' impel, idaho, horus, horse, honey, honda, holly,'
                       ' hello, heidi, hasty, haste, hamal, halve, haley,'
                       ' hague, hager, hagen, hades, guest, guess, gucci,'
                       ' group, grahm, gouge, gorse, gorky, glean, gleam,'
                       ' glaze, ghoul, ghost, gauss, gauge, gaudy, gator,'
                       ' gases, games, freer, fovea, float, fiona, finny,'
                       ' filly, field, erika, erica, enter, enemy, empty,'
                       ' emily, email, elmer, ellis, ellen, eight, eerie,'
                       ' edwin, edges, eatme, earth, eager, dulce, donor,'
                       ' donna, diane, diana, delay, defoe, david, danny,'
                       ' daisy, cuzco, cubit, cozen, coypu, coyly, cowry,'
                       ' condo, class, cindy, cigar, chess, cathy, carry,'
                       ' carol, carla, caret, caren, candy, candi, burma,'
                       ' burly, burke, brian, breed, borax, booze, booty,'
                       ' bloom, blood, bitch, bilge, bilbo, betty, beryl,'
                       ' becky, beach, bathe, batch, basic, bantu, banks,'
                       ' banjo, baird, baggy, azure, arrow, array, april,'
                       ' anita, angie, amber, amaze, alpha, alisa, alike,'
                       ' align, alice, alias, album, alamo, aires, admin,'
                       ' adept, adele, addle, addis, added, acura, abyss,'
                       ' abcde, 1701d, 123go, !@#$%'.split(', '))
dictionary6 = list('yankee, yamaha, yakima, y7u8i9, xyzxyz, wombat,'
                       ' wizard, wilson, willie, weenie, warren, visual,'
                       ' virgin, viking, venous, venice, venial, vasant,'
                       ' vagina, ursula, urchin, uranus, uphill, umpire,'
                       ' u.s.a., tuttle, trisha, trails, tracie, toyota,'
                       ' tomato, toggle, tidbit, thorny, thomas, terror,'
                       ' tennis, taylor, target, tardis, tappet, taoist,'
                       ' tannin, tanner, tanker, tamara, system, surfer,'
                       ' summer, subway, stacie, stacey, spring, sondra,'
                       ' solemn, soleil, solder, solace, soiree, soften,'
                       ' soffit, sodium, sodden, snoopy, snatch, smooch,'
                       ' smiles, slavic, slater, single, singer, simple,'
                       ' sherri, sharon, sharks, sesame, sensor, secret,'
                       ' second, season, search, scroll, scribe, scotty,'
                       ' scooby, schulz, school, scheme, saturn, sandra,'
                       ' sandal, saliva, saigon, sahara, safety, safari,'
                       ' sadism, saddle, sacral, russel, runyon, runway,'
                       ' runoff, runner, ronald, romano, rodent, ripple,'
                       ' riddle, ridden, reveal, return, remote, recess,'
                       ' recent, realty, really, reagan, raster, rascal,'
                       ' random, radish, radial, racoon, racket, racial,'
                       ' rachel, rabbit, qwerty, qawsed, puppet, puneet,'
                       ' public, prince, presto, praise, poster, polite,'
                       ' polish, policy, police, plover, pierre, phrase,'
                       ' photon, philip, persia, peoria, penmen, penman,'
                       ' pencil, peanut, parrot, parent, pardon, papers,'
                       ' pander, pamela, pallet, palace, oxford, outlaw,'
                       ' osiris, orwell, oregon, oracle, olivia, oliver,'
                       ' olefin, office, notion, notify, notice, notate,'
                       ' notary, noreen, nobody, nicole, newton, nevada,'
                       ' mutant, mozart, morley, monica, moguls, minsky,'
                       ' mickey, merlin, memory, mellon, meagan, mcneil,'
                       ' mcleod, mclean, mckeon, mchugh, mcgraw, mcgill,'
                       ' mccann, mccall, mccabe, mayfly, maxine, master,'
                       ' massif, maseru, marvin, markus, malcom, mailer,'
                       ' maiden, magpie, magnum, magnet, maggot, lorenz,'
                       ' lisbon, limpid, leslie, leland, latest, latera,'
                       ' latent, lascar, larkin, langur, landis, landau,'
                       ' lambda, kristy, kristi, krista, knight, kitten,'
                       ' kinney, kerrie, kernel, kermit, kennan, kelvin,'
                       ' kelsey, kelley, keller, keenan, katina, karina,'
                       ' kansas, juggle, judith, jsbach, joshua, joseph,'
                       ' johnny, joanne, joanna, jixian, jimmie, jimbob,'
                       ' jester, jeanne, jasmin, janice, jaguar, jackie,'
                       ' island, invest, instar, ingrid, ingres, impute,'
                       ' holmes, holman, hockey, hidden, hawaii, hasten,'
                       ' harvey, harold, hamlin, hamlet, halite, halide,'
                       ' haggle, haggis, hadron, hadley, hacker, gustav,'
                       ' gusset, gurkha, gurgle, guntis, guitar, gamlyn,'
                       ' gospel, gorton, gorham, gorges, golfer, glassy,'
                       ' ginger, gibson, ghetto, german, george, gauche,'
                       ' gasify, gambol, gamble, gambit, friend, freest,'
                       ' fourth, format, flower, flaxen, flaunt, flakes,'
                       ' finley, finite, fillip, fillet, filler, filled,'
                       ' fermat, fender, fatten, fatima, fathom, father,'
                       ' evelyn, euclid, estate, enzyme, engine, employ,'
                       ' emboss, elanor, elaine, eileen, eighty, eighth,'
                       ' effect, efface, eeyore, eerily, edwina, easier,'
                       ' durkin, durkee, during, durham, duress, duncan,'
                       ' donner, donkey, donate, donald, domino, disney,'
                       ' dieter, device, denise, deluge, delete, debbie,'
                       ' deaden, ddurer, dapper, daniel, dancer, damask,'
                       ' dakota, daemon, cuvier, cuddly, cuddle, cuckoo,'
                       ' cretin, create, cozier, coyote, cowpox, cooper,'
                       ' cookie, connie, coneck, condom, coffee, citrus,'
                       ' citron, citric, circus, charon, change, censor,'
                       ' cement, celtic, cecily, cayuga, catnip, catkin,'
                       ' cation, castle, carson, carrot, carrie, carole,'
                       ' carmen, caress, cantor, burley, burlap, buried,'
                       ' burial, brenda, bremen, breezy, breeze, breech,'
                       ' brandy, brandi, border, borden, borate, bloody,'
                       ' bishop, bilbao, bikini, bigred, betsie, berman,'
                       ' berlin, bedbug, became, beavis, beaver, beauty,'
                       ' beater, batman, bathos, barony, barber, baobab,'
                       ' bantus, banter, bantam, banish, bangui, bangor'.split(', '))
dictionary7 = list('yolanda, wyoming, winston, william, whitney, whiting,'
                       ' whatnot, vitriol, vitrify, vitiate, vitamin, visitor, village, vertigo, vermont, venturi, venture, ventral, venison, valerie, utility, upgrade, unknown, unicorn, unhappy, trivial, torrent, tinfoil, tiffany, tidings, thunder, thistle, theresa, test123, terrify, teleost, tarbell, taproot, tapping, tapioca, tantrum, tantric, tanning, takeoff, swearer, suzanne, susanne, support, success, student, squires, sossina, soldier, sojourn, soignee, sodding, smother, slavish, slavery, slander, shuttle, shivers, shirley, sheldon, shannon, service, seattle, scooter, scissor, science, scholar, scamper, satisfy, sarcasm, salerno, sailing, saguaro, saginaw, sagging, saffron, sabrina, russell, rupture, running, runneth, rosebud, receipt, rebecca, realtor, raleigh, rainbow, quarrel, quality, qualify, pumpkin, protect, program, profile, profess, profane, private, prelude, porsche, politic, playboy, phoenix, persona, persian, perseus, perseid, perplex, penguin, pendant, parapet, panoply, panning, panicle, panicky, pangaea, pandora, palette, pacific, olivier, olduvai, oldster, okinawa, oakwood, nyquist, nursery, numeric, number1, nullify, nucleus, nuclear, notused, nothing, newyork, network, neptune, montana, minimum, michele, michael, merriam, mercury, melissa, mcnulty, mcnally, mcmahon, mckenna, mcguire, mcgrath, mcgowan, mcelroy, mcclure, mcclain, mccarty, mcbride, mcadams, mbabane, mayoral, maurice, marimba, manhole, manager, mammoth, malcolm, malaria, mailbox, magnify, magneto, losable, lorinda, loretta, lorelei, lockout, lioness, limpkin, library, lazarus, lathrop, lateran, lateral, kristin, kristie, kristen, kinsman, kingdom, kennedy, kendall, kellogg, keelson, katrina, jupiter, judaism, judaica, jessica, janeiro, inspire, inspect, insofar, ingress, indiana, include, impetus, imperil, holmium, holmdel, herbert, heather, headmen, headman, harmony, handily, hamburg, halifax, halibut, halfway, haggard, hafnium, hadrian, gustave, gunther, gunshot, gryphon, gosling, goshawk, gorilla, gleason, glacier, ghostly, germane, georgia, geology, gaseous, gascony, gardner, gabriel, freeway, fourier, flowers, florida, fishers, finnish, finland, ferrari, felicia, feather, fatigue, fairway, express, expound, emulate, empress, empower, emitted, emerald, embrace, embower, ellwood, ellison, egghead, durward, durrell, drought, donning, donahue, digital, develop, desiree, default, deborah, damming, cynthia, cyanate, cutworm, cutting, cuddles, cubicle, crystal, coxcomb, cowslip, cowpony, cowpoke, console, conquer, connect, comrade, compton, collins, cluster, claudia, classic, citroen, citrate, citizen, citadel, cistern, christy, chester, charles, charity, celtics, celsius, catlike, cathode, carroll, carrion, careful, carbine, carbide, caraway, caravan, camille, burmese, burgess, bridget, breccia, bradley, bopping, blondie, bilayer, beverly, bernard, bermuda, berlitz, berlioz, beowulf, beloved, because, beatnik, beatles, beatify, bassoon, bartman, baroque, barbara, baptism, banshee, banquet, bannock, banning, bananas, bainite, bailiff, bahrein, bagpipe, baghdad, bagging, bacchus, asshole, arrange, arraign, arragon, arizona, ariadne, annette, animals, anatomy, anatole, amatory, amateur, amadeus, allison, alimony, aliases, algebra, albumin, alberto, alberta, albania, alameda, aladdin, alabama, airport, airpark, airfoil, airflow, airfare, airdrop, adenoma, adenine, address, addison, accrual, acclaim, academy, abcdefg, !@#$%^&'.split(', '))
dictionary8 = list('yosemite, y7u8i9o0, wormwood, woodwind, whistler,'
                       ' whatever, warcraft, vitreous, virginia, veronica, venomous, trombone, transfer, tortoise, tientsin, tideland, ticklish, thailand, testtest, tertiary, terrific, terminal, telegram, tarragon, tapeworm, tapestry, tanzania, tantalus, tantalum, sysadmin, symmetry, sunshine, strangle, startrek, springer, sparrows, somebody, solecism, soldiery, softwood, software, softball, socrates, slatting, slapping, slapdash, slamming, simpsons, serenity, security, schwartz, sanctity, sanctify, samantha, salesman, sailfish, sailboat, sagittal, sagacity, sabotage, rushmore, rosemary, rochelle, robotics, reverend, regional, raindrop, rachelle, qwertyui, qwerasdf, qawsedrf, q1w2e3r4, protozoa, prodding, princess, precious, politics, politico, plymouth, pershing, penitent, penelope, pendulum, patricia, password, passport, paranoia, panorama, panicked, pandemic, pandanus, pakistan, painless, operator, olivetti, oleander, oklahoma, notocord, notebook, notarize, nebraska, napoleon, missouri, michigan, michelle, mesmeric, mercedes, mcmullen, mcmillan, mcknight, mckinney, mckinley, mckesson, mckenzie, mcintyre, mcintosh, mcgregor, mcgovern, mcginnis, mcfadden, mcdowell, mcdonald, mcdaniel, mcconnel, mccauley, mccarthy, mccallum, mayapple, masonite, maryland, marjoram, marinate, marietta, maneuver, mandamus, maledict, maladapt, magnuson, magnolia, magnetic, lyrebird, lymphoma, lorraine, lionking, linoleum, limitate, limerick, laterite, landmass, landmark, landlord, landlady, landhold, landfill, kristine, kirkland, kingston, kimberly, khartoum, keystone, kentucky, keeshond, kathrine, kathleen, jubilant, joystick, jennifer, jacobsen, irishman, interpol, internet, insulate, instinct, instable, insomnia, insolent, insolate, inactive, imperial, iloveyou, illinois, hydrogen, hutchins, homework, hologram, holocene, hibernia, hiawatha, heinlein, hebrides, headlong, headline, headland, hastings, hamilton, halftone, halfback, hagstrom, gunsling, gunpoint, gumption, gorgeous, glaucous, glaucoma, glassine, ginnegan, ghoulish, gertrude, geometry, geometer, garfield, gamesman, gamecock, fungible, function, frighten, freetown, foxglove, fourteen, foursome, forsythe, football, flaxseed, flautist, flatworm, flatware, fidelity, exposure, eternity, enthrone, enthrall, enthalpy, entendre, entangle, engineer, emulsion, emulsify, emporium, employer, employee, employed, emmanuel, elliptic, elephant, einstein, eighteen, duration, donnelly, dominion, dlmhurst, delegate, delaware, december, deadwood, deadlock, deadline, deadhead, danielle, cyanamid, cucumber, cristina, criminal, creosote, creation, cowpunch, couscous, conquest, comrades, computer, comprise, compress, colorado, clusters, citation, charming, cerulean, cenozoic, cemetery, cellular, catskill, cationic, catholic, cathodic, catheter, cascades, carriage, caroline, carolina, carefree, cardinal, burgundy, burglary, bumbling, broadway, breeches, bordello, bordeaux, bilinear, bilabial, bernardo, berliner, berkeley, bedazzle, beaumont, beatrice, beatific, bathrobe, baronial, baritone, bankrupt, banister, bakelite, azsxdcfv, asdfqwer, arkansas, appraise, apposite, anything, angerine, ancestry, ancestor, anatomic, anathema, ambiance, alphabet, albright, albrecht, alberich, albacore, alastair, alacrity, airspace, airplane, airfield, airedale, aircraft, airbrush, airborne, aerobics, adrianna, adelaide, additive, addition, addendum, accouter, academic, academia, abcdefgh, abcd1234, a1b2c3d4, 7y8u9i0o, 7890yuio, 1234qwer, 0p9o8i7u, 0987poiu, !@#$%^&*'.split(', '))
dictionary9 = list('zimmerman, worldwide, wisconsin, wholesale, vitriolic,'
                       ' ventricle, ventilate, valentine, tidewater, testament, territory, tennessee, telephone, telepathy, teleology, telemetry, telemeter, telegraph, tarantula, tarantara, tangerine, supported, superuser, stuttgart, stratford, stephanie, solemnity, softcover, slaughter, slapstick, signature, sheffield, sarcastic, sanctuary, sagebrush, sagacious, runnymede, rochester, receptive, reception, racketeer, professor, princeton, pondering, politburo, policemen, policeman, persimmon, persevere, persecute, percolate, peninsula, penetrate, pendulous, paralytic, panoramic, panicking, panhandle, oligopoly, oligocene, oligarchy, olfactory, oldenburg, nutrition, nurturant, notorious, notoriety, minnesota, microsoft, mcpherson, mcfarland, mcdougall, mcdonnell, mcdermott, mccracken, mccormick, mcconnell, mccluskey, mcclellan, marijuana, malicious, magnitude, magnetron, magnetite, macintosh, lynchburg, louisiana, lissajous, limousine, limnology, landscape, landowner, kinshasha, kingsbury, kibbutzim, kennecott, jamestown, ironstone, invisible, invention, intuitive, intervene, intersect, inspector, insomniac, insolvent, insoluble, impetuous, imperious, imperfect, holocaust, hollywood, hollyhock, headphone, headlight, headdress, headcount, headboard, happening, hamburger, halverson, gustafson, gunpowder, glasswort, glassware, ghostlike, geometric, gaucherie, freewheel, freethink, freestone, foresight, foolproof, extension, expositor, establish, entertain, employing, emittance, ellsworth, elizabeth, eightieth, eightfold, eiderdown, dusenbury, dusenberg, donaldson, dominique, discovery, desperate, delegable, delectate, decompose, decompile, damnation, cutthroat, crabapple, cornelius, conqueror, connubial, commrades, citizenry, christine, christina, chemistry, cellulose, celluloid, catherine, carryover, burlesque, bloodshot, bloodshed, bloodroot, bloodline, bloodbath, bilingual, bilateral, bijective, bijection, bernadine, berkshire, beethoven, beatitude, bakhtiari, asymptote, asymmetry, apprehend, appraisal, apportion, ancestral, anatomist, alexander, albatross, alabaster, alabamian, adenosine, abcabcabc'.split(', '))
dictionary10 = list('washington, volkswagen, topography, tessellate,'
                        ' temptation, telephonic, telepathic, telemetric, telegraphy, tantamount, superstage, slanderous, salamander, qwertyuiop, polynomial, politician, phrasemake, photometry, photolytic, photolysis, photogenic, phosphorus, phosphoric, persiflage, persephone, perquisite, peninsular, penicillin, penetrable, panjandrum, oligoclase, oligarchic, oldsmobile, nottingham, noticeable, noteworthy, mcnaughton, mclaughlin, mccullough, mcallister, malconduct, maidenhair, limitation, lascivious, landowning, landlubber, landlocked, lamination, khrushchev, juggernaut, irrational, invariable, insouciant, insolvable, incomplete, impervious, impersonal, headmaster, glaswegian, geopolitic, geophysics, fourteenth, foursquare, expressive, expression, expository, exposition, enterprise, eightyfold, eighteenth, effaceable, donnybrook, delectable, decolonize, cuttlefish, cuttlebone, compromise, compressor, comprehend, cellophane, carruthers, california, burlington, burgundian, borderline, borderland, bloodstone, bloodstain, bloodhound, bijouterie, biharmonic, bernardino, beaujolais, basketball, bankruptcy, bangladesh, atmosphere, asymptotic, asymmetric, appreciate, apposition, ambassador, amateurish, alimentary, additional, accomplish, 1q2w3e4r5t'.split(', '))
dictionary11 = list('yellowstone, venturesome, territorial, telekinesis,'
                        ' sagittarius, safekeeping, politicking, policewoman, photometric, photography, phosphorous, perseverant, persecutory, persecution, penitential, pandemonium, mississippi, marketplace, magnificent, irremovable, interrogate, institution, inspiration, incompetent, impertinent, impersonate, impermeable, headquarter, hamiltonian, halfhearted, hagiography, geophysical, expressible, emptyhanded, eigenvector, deleterious, decollimate, decolletage, connecticut, comptroller, compressive, compression, catholicism, bloodstream, bakersfield, arrangeable, appreciable, anastomotic, albuquerque'.split(', '))
dictionary12 = list('williamsburg, testamentary, qwerasdfzxcv, q1w2e3r4t5y6,'
                        ' perseverance, pennsylvania, penitentiary, malformation, liquefaction, interstitial, inconclusive, incomputable, incompletion, incompatible, incomparable, imperishable, impenetrable, headquarters, geometrician, ellipsometry, decomposable, decommission, compressible, burglarproof, bloodletting, bilharziasis, asynchronous, asymptomatic, ambidextrous, 1q2w3e4r5t6y'.split(', '))
dictionary13 = list('ventriloquist, ventriloquism, poliomyelitis,'
                        ' phosphorylate, oleomargarine, massachusetts, jitterbugging, interpolatory, inconceivable, imperturbable, impermissible, decomposition, comprehensive, comprehension'.split(', '))
dictionary14 = list('slaughterhouse, irreproducible, incompressible,'
                        ' comprehensible, bremsstrahlung'.split(', '))
dictionary15 = list('irreconciliable, instrumentation, incomprehension'.split(', '))
dictionary16 = ['incomprehensible']
print(dictionary15)


lower = string.ascii_lowercase
upper = string.ascii_uppercase
dig = string.digits
spec_simbol = string.punctuation


window = Tk()
window.title("Password analyzer")
window.geometry('500x300')

lbl = Label(window, text="Введите пароль\nиз латинских символов")
lbl.grid(column=0, row=0)
lbl1 = Label(window, text="5: Отличный\n4: Стойкий    \n3: Средний   \n2: Слабый     \n1: Никакой   ")
lbl1.grid(column=0, row=1)
txt = Entry(window, width=40)
txt.grid(column=1, row=0)
btn = Button(window, text="Клик!", command=clicked)
btn.grid(column=2, row=0)
pas = Label(window, text='{}'.format(time.strftime("%H:%M:%S")))
pas.place(x=450, y=280)


window.mainloop()
