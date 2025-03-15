# https://satsuite.collegeboard.org/media/pdf/sat-practice-test-4-digital.pdf
# https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-4-digital.pdf
label test4:

    window hide
    nvl clear

    $ reading_and_writing = 0
    $ math = 0

    scene bg classroom with dissolve
    window show

    """
    Module 1

    {b}{size=*1.5}Reading and Writing

    33 QUESTIONS\n

    {b}DIRECTIONS

    The questions in this section address a number of important reading and writing skills. Each
    question includes one or more passages, which may include a table or graph. Read each passage
    and question carefully, and then choose the best answer to the question based on the passage(s).

    All questions in this section are multiple-choice with four answer choices. Each question has a
    single best answer.
    """

    jump test4_module1_question1

label test4_module1_question1:

    nvl clear

    """
    1

    {font=PTSerif.ttf}The spacecraft OSIRIS-REx briefly made contact
    with the asteroid 101955 Bennu in 2020. NASA
    scientist Daniella DellaGiustina reports that despite
    facing the unexpected obstacle of a surface mostly
    covered in boulders, OSIRIS-REx successfully
    _______ a sample of the surface, gathering pieces of
    it to bring back to Earth.

    {font=PTSerif.ttf}Which choice completes the text with the most
    logical and precise word or phrase?
    """

    menu:
        "{font=PTSerif.ttf}A) attached":
            pass

        "{font=PTSerif.ttf}B) collected":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}C) followed":
            pass

        "{font=PTSerif.ttf}D) replaced":
            pass

    jump test4_module1_question2

label test4_module1_question2:

    nvl clear

    """
    2

    {font=PTSerif.ttf}Research conducted by planetary scientist Katarina
    Miljkovic suggests that the Moon’s surface may not
    accurately _______ early impact events. When the
    Moon was still forming, its surface was softer, and
    asteroid or meteoroid impacts would have left less
    of an impression; thus, evidence of early impacts may no longer be present.

    {font=PTSerif.ttf}Which choice completes the text with the most
    logical and precise word or phrase?
    """

    menu:
        "{font=PTSerif.ttf}A) reflect":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}B) receive":
            pass

        "{font=PTSerif.ttf}C) evaluate":
            pass

        "{font=PTSerif.ttf}D) mimic":
            pass

    jump test4_module1_question3

label test4_module1_question3:

    nvl clear

    """
    3

    {font=PTSerif.ttf}Handedness, a preferential use of either the right or
    left hand, typically is easy to observe in humans.
    Because this trait is present but less _______ in
    many other animals, animal-behavior researchers
    often employ tasks specially designed to reveal
    individual animals’ preferences for a certain hand
    or paw.

    {font=PTSerif.ttf}Which choice completes the text with the most
    logical and precise word or phrase?
    """

    menu:
        "{font=PTSerif.ttf}A) recognizable":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}B) intriguing":
            pass

        "{font=PTSerif.ttf}C) significant":
            pass

        "{font=PTSerif.ttf}D) useful":
            pass

    jump test4_module1_question4

label test4_module1_question4:

    nvl clear

    """
    4

    {font=PTSerif.ttf}It is by no means _______ to recognize the influence
    of Dutch painter Hieronymus Bosch on Ali
    Banisadr’s paintings; indeed, Banisadr himself cites
    Bosch as an inspiration. However, some scholars
    have suggested that the ancient Mesopotamian poem
    {i}Epic of Gilgamesh{/i} may have had a far greater impact
    on Banisadr’s work.

    {font=PTSerif.ttf}Which choice completes the text with the most
    logical and precise word or phrase?
    """

    menu:
        "{font=PTSerif.ttf}A) substantial":
            pass

        "{font=PTSerif.ttf}B) satisfying":
            pass

        "{font=PTSerif.ttf}C) unimportant":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}D) appropriate":
            pass

    jump test4_module1_question5

label test4_module1_question5:

    nvl clear

    """
    5

    {font=PTSerif.ttf}The following text is adapted from Susan Glaspell’s
    1912 short story “‘Out There.’” An elderly shop
    owner is looking at a picture that he recently
    acquired and hopes to sell.
    """

    quote """
    {font=PTSerif.ttf}It did seem that the picture failed to fit in with
    the rest of the shop. A persuasive young fellow
    who claimed he was closing out his stock let the
    old man have it for what he called a song. It was
    only a little out-of-the-way store which subsisted
    chiefly on the framing of pictures. The old man
    looked around at his views of the city, his
    pictures of cats and dogs, his flaming bits of
    landscape. “Don’t belong in here,” he fumed.

    {font=PTSerif.ttf}And yet the old man was secretly proud of his
    acquisition. There was a hidden dignity in his
    scowling as he shuffled about pondering the least
    ridiculous place for the picture.
    """

    """
    {font=PTSerif.ttf}Which choice best states the main purpose of the
    text?
    """

    nvl clear

    menu:
        "{font=PTSerif.ttf}A) To reveal the shop owner’s conflicted feelings\n
        \ \ \ \ \ about the new picture":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}B) To convey the shop owner’s resentment of the\n
        \ \ \ \ person he got the new picture from":
            pass

        "{font=PTSerif.ttf}C) To describe the items that the shop owner most\n
        \ \ \ \ \ highly prizes":
            pass

        "{font=PTSerif.ttf}D) To explain differences between the new picture\n
        \ \ \ \ \ and other pictures in the shop":
            pass

    jump test4_module1_question6

label test4_module1_question6:

    nvl clear

    """
    6

    {font=PTSerif.ttf}The following text is from the 1923 poem “Black
    Finger” by Angelina Weld Grimké, a Black American
    writer. A cypress is a type of evergreen tree.
    """

    quote """
    {font=PTSerif.ttf}I have just seen a most beautiful thing,\n
    Slim and still,\n
    Against a gold, gold sky,\n
    A straight black cypress,\n
    Sensitive,\n
    Exquisite,\n
    A black finger\n
    Pointing upwards.\n
    Why, beautiful still finger, are you black?\n
    And why are you pointing upwards?
    """

    """
    {font=PTSerif.ttf}Which choice best describes the overall structure of
    the text?
    """

    nvl clear

    menu:
        "{font=PTSerif.ttf}A) The speaker assesses a natural phenomenon,\n
        \ \ \ \ \ then questions the accuracy of her assessment.":
            pass

        "{font=PTSerif.ttf}B) The speaker describes a distinctive sight in\n
        \ \ \ \ nature, then ponders what meaning to attribute\n
        \ \ \ \ to that sight.":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}C) The speaker presents an outdoor scene, then\n
        \ \ \ \ \ considers a human behavior occurring within\n
        \ \ \ \ \ that scene.":
            pass

        "{font=PTSerif.ttf}D)  The speaker examines her surroundings, then\n
        \ \ \ \ \ speculates about their influence on her\n
        \ \ \ \ \ emotional state.":
            pass

    jump test4_module1_question7

label test4_module1_question7:

    nvl clear

    """
    7

    {font=PTSerif.ttf}The following text is from Walt Whitman’s 1860
    poem “Calamus 24.”
    """

    quote """
    {font=PTSerif.ttf}I HEAR it is charged against me that I seek to\n
    \ \ \ \ destroy institutions;\n
    But really I am neither for nor against\n
    \ \ \ \ institutions\n
    (What indeed have I in common with them?—\n
    \ \ \ \ Or what with the destruction of them?),\n
    Only I will establish in the Mannahatta\n
    \ \ \ \ \[Manhattan] and in every city of These States,\n
    \ \ \ \ inland and seaboard,\n
    And in the fields and woods, and above every\n
    \ \ \ \ keel \[ship] little or large, that dents the water,\n
    Without edifices, or rules, or trustees, or any\n
    \ \ \ \ argument,\n
    The institution of the dear love of comrades.
    """

    """
    {font=PTSerif.ttf}Which choice best describes the overall structure of
    the text?
    """

    nvl clear

    menu:
        "{font=PTSerif.ttf}A) The speaker questions an increasingly prevalent\n
        \ \ \ \ \ attitude, then summarizes his worldview.":
            pass

        "{font=PTSerif.ttf}B) The speaker regrets his isolation from others,\n
        \ \ \ \ \ then predicts a profound change in society.":
            pass

        "{font=PTSerif.ttf}C) The speaker concedes his personal\n
        \ \ \ \ \ shortcomings, then boasts of his many\n
        \ \ \ \ \ achievements.":
            pass

        "{font=PTSerif.ttf}D) The speaker addresses a criticism leveled against\n
        \ \ \ \ \ him, then announces a grand ambition of his.":
            $ reading_and_writing += 1

    jump test4_module1_question8

label test4_module1_question8:

    nvl clear

    """
    8

    {font=PTSerif.ttf}The mimosa tree evolved in East Asia, where the
    beetle {i}Bruchidius terrenus{/i} preys on its seeds. In 1785,
    mimosa trees were introduced to North America, far
    from any {i}B. terrenus{/i}. {u}But evolutionary links between
    predators and their prey can persist across centuries
    and continents.{/u} Around 2001, {i}B. terrenus{/i} was
    introduced in southeastern North America near
    where botanist Shu-Mei Chang and colleagues had
    been monitoring mimosa trees. Within a year,
    93 percent of the trees had been attacked by the
    beetles.

    {font=PTSerif.ttf}Which choice best describes the function of the third
    sentence in the overall structure of the text?
    """

    nvl clear

    menu:
        "{font=PTSerif.ttf}A) It states the hypothesis that Chang and\n
        \ \ \ \ colleagues had set out to investigate using\n
        \ \ \ \ mimosa trees and {i}B. terrenus{/i}.":
            pass

        "{font=PTSerif.ttf}B) It presents a generalization that is exemplified\n
        \ \ \ \ by the discussion of the mimosa trees and\n
        \ \ \ \ {i}B. terrenus{/i}.":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}C) It offers an alternative explanation for the\n
        \ \ \ \ findings of Chang and colleagues.":
            pass

        "{font=PTSerif.ttf}D) It provides context that clarifies why the species\n
        \ \ \ \ mentioned spread to new locations.":
            pass

    jump test4_module1_question9

label test4_module1_question9:

    nvl clear

    """
    9

    {font=PTSerif.ttf}{b}Text 1

    {font=PTSerif.ttf}Conventional wisdom long held that human
    social systems evolved in stages, beginning with
    hunter-gatherers forming small bands of members
    with roughly equal status. The shift to agriculture
    about 12,000 years ago sparked population growth
    that led to the emergence of groups with hierarchical
    structures: associations of clans first, then chiefdoms,
    and finally, bureaucratic states.

    {font=PTSerif.ttf}{b}Text 2

    {font=PTSerif.ttf}In a 2021 book, anthropologist David Graeber and
    archaeologist David Wengrow maintain that humans
    have always been socially flexible, alternately forming
    systems based on hierarchy and collective ones with
    decentralized leadership. The authors point to
    evidence that as far back as 50,000 years ago some
    hunter-gatherers adjusted their social structures
    seasonally, at times dispersing in small groups but
    also assembling into communities that included
    esteemed individuals.
    """

    """
    {font=PTSerif.ttf}Based on the texts, how would Graeber and
    Wengrow (Text 2) most likely respond to the
    “conventional wisdom” presented in Text 1?
    """

    nvl clear

    menu:
        "{font=PTSerif.ttf}A) By conceding the importance of hierarchical\n
        \ \ \ \ systems but asserting the greater significance of\n
        \ \ \ \ decentralized collective societies":
            pass

        "{font=PTSerif.ttf}B) By disputing the idea that developments in social\n
        \ \ \ \ structures have followed a linear progression\n
        \ \ \ \ through distinct stages":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}C) By acknowledging that hierarchical roles likely\n
        \ \ \ \ weren’t a part of social systems before the rise of\n
        \ \ \ \ agriculture":
            pass

        "{font=PTSerif.ttf}D) By challenging the assumption that groupings of\n
        \ \ \ \ hunter-gatherers were among the earliest forms\n
        \ \ \ \ of social structure":
            pass

    jump test4_module1_question10

label test4_module1_question10:

    nvl clear

    """
    10

    {font=PTSerif.ttf}The following text is adapted from Frances Hodgson
    Burnett’s 1911 novel {i}The Secret Garden{/i}. Mary, a
    young girl, recently found an overgrown hidden
    garden.
    """

    quote """
    {font=PTSerif.ttf}Mary was an odd, determined little person,
    and now she had something interesting to be
    determined about, she was very much absorbed,
    indeed. She worked and dug and pulled up
    weeds steadily, only becoming more pleased with
    her work every hour instead of tiring of it. It
    seemed to her like a fascinating sort of play.
    """

    "{font=PTSerif.ttf}Which choice best states the main idea of the text?"

    menu:
        "{font=PTSerif.ttf}A) Mary hides in the garden to avoid doing her
        chores.":
            pass

        "{font=PTSerif.ttf}B) Mary is getting bored with pulling up so many
        weeds in the garden.":
            pass

        "{font=PTSerif.ttf}C) Mary is clearing out the garden to create a space
        to play.":
            pass

        "{font=PTSerif.ttf}D) Mary feels very satisfied when she’s taking care
        of the garden.":
            $ reading_and_writing += 1

    jump test4_module1_question11

label test4_module1_question11:

    nvl clear

    """
    11

    {font=PTSerif.ttf}The following text is from Ezra Pound’s 1909 poem
    “Hymn III,” based on the work of Marcantonio
    Flaminio.
    """

    quote """
    {font=PTSerif.ttf}As a fragile and lovely flower unfolds its gleaming\n
    \ \ \ \ foliage on the breast of the fostering earth, if\n
    \ \ \ \ the dew and the rain draw it forth;\n
    So doth my tender mind flourish, if it be fed with the\n
    \ \ \ \ sweet dew of the fostering spirit,\n
    Lacking this, it beginneth straightway to languish,\n
    \ \ \ \ even as a floweret born upon dry earth, if the\n
    \ \ \ \ dew and the rain tend it not.
    """

    """
    {font=PTSerif.ttf}Based on the text, in what way is the human mind
    like a flower?
    """

    menu:
        "{font=PTSerif.ttf}A) It becomes increasingly vigorous with the
        passage of time.":
            pass

        "{font=PTSerif.ttf}B) It draws strength from changes in the weather.":
            pass

        "{font=PTSerif.ttf}C) It requires proper nourishment in order to
        thrive.":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}D) It perseveres despite challenging circumstances.":
            pass

    jump test4_module1_question12

label test4_module1_question12:

    nvl clear

    """
    12

    {font=PTSerif.ttf}The following text is adapted from Jack London’s
    1903 novel {i}The Call of the Wild{/i}. Buck is a sled dog
    living with John Thornton in Yukon, Canada.
    """

    quote """
    {font=PTSerif.ttf}Thornton alone held \[Buck]. The rest of
    mankind was as nothing. Chance travellers
    might praise or pet him; but he was cold under it
    all, and from a too demonstrative man he would
    get up and walk away. When Thornton’s
    partners, Hans and Pete, arrived on the
    long-expected raft, Buck refused to notice them
    till he learned they were close to Thornton; after
    that he tolerated them in a passive sort of way,
    accepting favors from them as though he favored
    them by accepting.
    """

    "{font=PTSerif.ttf}Which choice best states the main idea of the text?"

    menu:
        "{font=PTSerif.ttf}A) Buck has become less social since he began living
        with Thornton.":
            pass

        "{font=PTSerif.ttf}B) Buck mistrusts humans and does his best to
        avoid them.":
            pass

        "{font=PTSerif.ttf}C) Buck has been especially well liked by most of
        Thornton’s friends.":
            pass

        "{font=PTSerif.ttf}D) Buck holds Thornton in higher regard than any
        other person.":
            $ reading_and_writing += 1

    jump test4_module1_question13

label test4_module1_question13:

    nvl clear

    "13"

    show test4_module1_question13 at truecenter onlayer overlay

    pause

    """
    {font=PTSerif.ttf}Organic farming is a method of growing food that
    tries to reduce environmental harm by using natural
    forms of pest control and avoiding fertilizers made
    with synthetic materials. Organic farms are still a
    small fraction of the total farms in the United States,
    but they have been becoming more popular.
    According to the US Department of Agriculture, in
    2016 California had between 2,600 and 2,800 organic
    farms and _______

    {font=PTSerif.ttf}Which choice most effectively uses data from the
    graph to complete the text?
    """

    menu:
        "{font=PTSerif.ttf}A) Washington had between 600 and 800 organic
        farms.":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}B) New York had fewer than 800 organic farms.":
            pass

        "{font=PTSerif.ttf}C) Wisconsin and Iowa each had between 1,200 and
        1,400 organic farms.":
            pass

        "{font=PTSerif.ttf}D) Pennsylvania had more than 1,200 organic
        farms.":
            pass

    jump test4_module1_question14

label test4_module1_question14:

    nvl clear

    """
    14

    {font=PTSerif.ttf}Biologist Valentina Gómez-Bahamón and her team
    have investigated two subspecies of the fork-tailed
    flycatcher bird that live in the same region in
    Colombia, but one subspecies migrates south for part
    of the year, and the other doesn’t. The researchers
    found that, due to slight differences in feather shape,
    the feathers of migratory forked-tailed flycatcher
    males make a sound during flight that is higher
    pitched than that made by the feathers of
    nonmigratory males. The researchers hypothesize
    that fork-tailed flycatcher females are attracted to the
    specific sound made by the males of their own
    subspecies, and that over time the females’
    preference will drive further genetic and anatomical
    divergence between the subspecies.

    {font=PTSerif.ttf}Which finding, if true, would most directly support
    Gómez-Bahamón and her team’s hypothesis?
    """

    nvl clear

    menu:
        "{font=PTSerif.ttf}A) The feathers located on the wings of the\n
        \ \ \ \ \ migratory fork-tailed flycatchers have a narrower\n
        \ \ \ \ \ shape than those of the nonmigratory birds,\n
        \ \ \ \ \ which allows them to fly long distances.":
            pass

        "{font=PTSerif.ttf}B) Over several generations, the sound made by the\n
        \ \ \ \ feathers of migratory male fork-tailed flycatchers\n
        \ \ \ \ grows progressively higher pitched relative to\n
        \ \ \ \ that made by the feathers of nonmigratory\n
        \ \ \ \ males.":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}C) Fork-tailed flycatchers communicate different\n
        \ \ \ \ messages to each other depending on whether\n
        \ \ \ \ their feathers create high-pitched or low-pitched\n
        \ \ \ \ sounds.":
            pass

        "{font=PTSerif.ttf}D) The breeding habits of the migratory and\n
        \ \ \ \ \ nonmigratory fork-tailed flycatchers remained\n
        \ \ \ \ \ generally the same over several generations.":
            pass

    jump test4_module1_question15

label test4_module1_question15:

    nvl clear

    "15"

    show test4_module1_question15 at truecenter onlayer overlay

    pause

    """
    {font=PTSerif.ttf}Earth’s atmosphere is bombarded by cosmic dust
    originating from several sources: short-period
    comets (SPCs), particles from the asteroid belt
    (ASTs), Halley-type comets (HTCs), and Oort cloud
    comets (OCCs). Some of the dust’s material
    vaporizes in the atmosphere in a process called
    ablation, and the faster the particles move, the higher
    the rate of ablation. Astrophysicist Juan Diego
    Carrillo-Sánchez led a team that calculated average
    ablation rates for elements in the dust (such as iron
    and potassium) and showed that material in slower-
    moving SPC or AST dust has a lower rate than the
    same material in faster-moving HTC or OCC dust.
    For example, whereas the average ablation rate
    for iron from AST dust is 28\%, the average rate
    for _______

    {font=PTSerif.ttf}Which choice most effectively uses data from the
    table to complete the example?
    """

    menu:
        "{font=PTSerif.ttf}A) iron from SPC dust is 20\%.":
            pass

        "{font=PTSerif.ttf}B) sodium from OCC dust is 100\%.":
            pass

        "{font=PTSerif.ttf}C) iron from HTC dust is 90\%.":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}D) sodium from AST dust is 75\%.":
            pass

    jump test4_module1_question16

label test4_module1_question16:

    nvl clear

    """
    16

    {font=PTSerif.ttf}Art collectives, like the United States- and Vietnam-based 
    collective The Propeller Group or Cuba’s Los
    Carpinteros, are groups of artists who agree to work
    together: perhaps for stylistic reasons, or to advance
    certain shared political ideals, or to help mitigate the
    costs of supplies and studio space. Regardless of
    the reasons, art collectives usually involve some
    collaboration among the artists. Based on a recent
    series of interviews with various art collectives, an
    arts journalist claims that this can be difficult for
    artists who are often used to having sole control over
    their work.

    {font=PTSerif.ttf}Which quotation from the interviews best illustrates
    the journalist’s claim?
    """

    nvl clear

    menu:
        "{font=PTSerif.ttf}A) “The first collective I joined included many\n
        \ \ \ \ amazingly talented artists, and we enjoyed each\n
        \ \ \ \ other’s company, but because we had a hard time\n
        \ \ \ \ sharing credit and responsibility for our work,\n
        \ \ \ \ the collective didn’t last.”":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}B)  “We work together, but that doesn’t mean that\n
        \ \ \ \ individual projects are equally the work of all of\n
        \ \ \ \ us. Many of our projects are primarily the\n
        \ \ \ \ responsibility of whoever originally proposed the\n
        \ \ \ \ work to the group.”":
            pass

        "{font=PTSerif.ttf}C) “Having worked as a member of a collective for\n
        \ \ \ \ several years, it’s sometimes hard to recall what it\n
        \ \ \ \ was like to work alone without the collective’s\n
        \ \ \ \ support. But that support encourages my\n
        \ \ \ \ individual expression rather than limits it.”":
            pass

        "{font=PTSerif.ttf}D) “Sometimes an artist from outside the collective\n
        \ \ \ \ will choose to collaborate with us on a project,\n
        \ \ \ \ but all of those projects fit within the larger\n
        \ \ \ \ themes of the work the collective does on its own.”":
            pass

    jump test4_score

label test4_score:

    window hide
    nvl clear

    scene bg hallway with dissolve
    window show

    """
    Reading and Writing Score: [reading_and_writing]/66

    Math Score: [math]/54
    """

    jump end
