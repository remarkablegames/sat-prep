﻿# https://satsuite.collegeboard.org/media/pdf/sat-practice-test-4-digital.pdf
# https://satsuite.collegeboard.org/media/pdf/sat-practice-test-4-answers-digital.pdf
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
            """
            ❌
            {i}Choice A{/i} is incorrect because in this context “attached” means connected or
            affixed. The text indicates that OSIRIS-REx gathered pieces of 101955 Bennu to
            bring to Earth; it doesn’t suggest that the spacecraft attached anything to the
            asteroid.
            """

        "{font=PTSerif.ttf}B) collected":
            $ reading_and_writing += 1

            """
            ✅
            {b}Choice B{/b} is the best answer because it most logically completes the text’s
            discussion of the OSIRIS-REx spacecraft’s contact with the asteroid 101955
            Bennu. In this context, “collected” means acquired and took away. The text
            indicates that although the boulders on the asteroid’s surface caused some
            unforeseen problems, OSIRIS-REx was able to gather a sample to return to
            Earth. This context suggests that OSIRIS-REx successfully collected a sample of
            101955 Bennu.
            """

        "{font=PTSerif.ttf}C) followed":
            """
            ❌
            {i}Choice C{/i} is incorrect because in this context “followed” means tracked
            or traveled behind and the text discusses OSIRIS-REx’s brief encounter with
            101955 Bennu during which the spacecraft gathered a sample to bring to Earth.
            The text doesn’t suggest that the spacecraft tracked the sample, and it’s not clear
            what it would mean for the spacecraft to travel behind the sample it collected.
            """

        "{font=PTSerif.ttf}D) replaced":
            """
            ❌
            {i}Choice D{/i} is incorrect because in this context “replaced” means put back or
            returned. The text indicates that OSIRIS-REx gathered pieces of 101955 Bennu to
            bring to Earth but doesn’t suggest that anything was returned to the asteroid.
            """

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

            """
            ✅
            {b}Choice A{/b} is the best answer because it most logically completes the text’s
            discussion of the Moon’s surface. In this context, “reflect” means show or make
            apparent. The text states that because the surface of the Moon was softer when
            the Moon was still forming than it is now, early asteroid and meteoroid impacts
            “would have left less of an impression” and, as a result, evidence of them may no
            longer exist. This context supports the idea that the surface of the Moon may not
            accurately show signs of early impact events.
            """

        "{font=PTSerif.ttf}B) receive":
            """
            ❌
            {i}Choice B{/i} is incorrect because it wouldn’t make sense to say that the surface
            of the Moon may not accurately “receive,” or acquire or experience, early
            impacts from asteroids or meteoroids. The text indicates that the impacts have
            already occurred, and it isn’t clear how the Moon’s surface could be accurate
            or inaccurate in experiencing them.
            """

        "{font=PTSerif.ttf}C) evaluate":
            """
            ❌
            {i}Choice C{/i} is incorrect because it wouldn’t
            make sense to say that the surface of the Moon may not accurately “evaluate,”
            or determine the significance or condition of, early impacts from asteroids or
            meteoroids, since that would suggest that it’s possible for the Moon’s surface to
            make a decision of any kind.
            """

        "{font=PTSerif.ttf}D) mimic":
            """
            ❌
            {i}Choice D{/i} is incorrect. In this context, “mimic” would
            mean to deliberately simulate or closely imitate something. It wouldn’t make sense
            to say that the surface of the Moon may not accurately mimic early asteroid and
            meteoroid impacts, since that would suggest that it’s possible for the Moon to
            deliberately imitate something.
            """

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

            """
            ✅
            {b}Choice A{/b} is the best answer because it most logically completes the text’s
            discussion about handedness in animals. As used in this context, “recognizable”
            means apparent or identifiable. The text indicates that handedness is “easy to
            observe in humans,” but that animal-behavior researchers use special tasks to
            determine handedness in other animals. This context and the use of “less” before
            the blank indicate that compared with handedness in humans, handedness in
            other animals is less recognizable.
            """

        "{font=PTSerif.ttf}B) intriguing":
            """
            ❌
            {i}Choice B{/i} is incorrect because there’s nothing in the text to suggest that
            handedness is less “intriguing,” or fascinating, in nonhuman animals than it is in
            humans. The text focuses on how easy it is to observe handedness in humans
            as compared with other animals; the text doesn’t suggest that handedness is
            more fascinating in humans.
            """

        "{font=PTSerif.ttf}C) significant":
            """
            ❌
            {i}Choice C{/i} is incorrect because there’s nothing in the
            text to suggest that handedness is less “significant,” or important or meaningful,
            in nonhuman animals than it is in humans. The text focuses on how easy it is to
            observe handedness in humans as compared with other animals; the text doesn’t
            suggest that handedness is more significant in humans.
            """

        "{font=PTSerif.ttf}D) useful":
            """
            ❌
            {i}Choice D{/i} is incorrect
            because “useful,” or functional or helpful, wouldn’t make sense in context. The
            text focuses on the ease with which researchers can determine whether an animal
            or person is right- or left-handed, not on how useful handedness in nonhuman
            animals is compared with handedness in humans.
            """

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
            """
            ❌
            {i}Choice A{/i} is incorrect because it wouldn’t make sense to say that recognizing
            Bosch’s influence on Banisadr isn’t “substantial,” or meaningful. The text states
            that Banisadr himself cites Bosch as an influence.
            """

        "{font=PTSerif.ttf}B) satisfying":
            """
            ❌
            {i}Choice B{/i} is incorrect because
            it wouldn’t make sense to say that it isn’t “satisfying,” or pleasing, to recognize
            Bosch’s influence on Banisadr. The text states that Banisadr himself cites Bosch
            as an influence.
            """

        "{font=PTSerif.ttf}C) unimportant":
            $ reading_and_writing += 1

            """
            ✅
            {b}Choice C{/b} is the best answer because it most logically completes the text’s
            discussion of the influences on Banisadr’s work. As used in this context,
            “unimportant” means trivial or lacking value. “It is by no means” establishes
            that the word that goes in the blank is contradicted by other information; the
            material that follows “indeed” later in that sentence provides the contradicting
            information—namely, that Banisadr himself cites Bosch as an inspiration. In other
            words, the sentence indicates that Bosch’s influence on Banisadr is significant,
            and thus recognizing that influence is by no means unimportant.
            """

        "{font=PTSerif.ttf}D) appropriate":
            """
            ❌
            {i}Choice D{/i} is incorrect because it wouldn’t make sense to say that
            recognizing Bosch’s influence on Banisadr isn’t “appropriate,” or suitable. The text
            indicates that Banisadr himself notes that Bosch’s work has had an effect on him.
            """

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

            """
            ✅
            {b}Choice A{/b} is the best answer because it most accurately describes the main
            purpose of the text. The text begins by stating that the new picture “failed to fit
            in” with the other items that the shop owner has. The text goes on to illustrate
            that point by describing the other pictures the shop owner has, indicating that
            the shop owner is fuming because he doesn’t think the new picture belongs in the
            store. In the second paragraph, however, the text indicates that the shop owner is
            “secretly proud of his acquisition.” The main purpose of the text is thus to reveal
            the shop owner’s conflicted feelings about the new picture.
            """

        "{font=PTSerif.ttf}B) To convey the shop owner’s resentment of the\n
        \ \ \ \ person he got the new picture from":
            """
            ❌
            {i}Choice B{/i} is incorrect because the text doesn’t suggest that the shop owner
            resents the young man who sold him the new picture; in fact, the text gives
            no indication of the owner’s feelings about the young man at all.
            """

        "{font=PTSerif.ttf}C) To describe the items that the shop owner most\n
        \ \ \ \ \ highly prizes":
            """
            ❌
            {i}Choice C{/i} is
            incorrect. Although the text indicates that the new picture is different from the
            other items in the shop, there’s no suggestion that the shop owner prizes either
            the new picture or the pictures of the city, pets, and landscapes more than he
            prizes any other items.
            """

        "{font=PTSerif.ttf}D) To explain differences between the new picture\n
        \ \ \ \ \ and other pictures in the shop":
            """
            ❌
            {i}Choice D{/i} is incorrect because the text doesn’t describe
            what the new picture looks like; rather, the text identifies some of the other kinds
            of images that the shop owner has and states that they’re different from the new
            picture without explaining how they’re different.
            """

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
            """
            ❌
            {i}Choice A{/i} is incorrect because the speaker assesses a natural sight—a “black
            cypress” tree standing “against a gold, gold sky” like a pointed finger—but doesn’t
            question the accuracy of her own assessment. Although she wonders why the
            finger, which is really a tree, is black and why it’s pointing, the speaker doesn’t
            suggest that her belief that the tree resembles a finger is wrong.
            """

        "{font=PTSerif.ttf}B) The speaker describes a distinctive sight in\n
        \ \ \ \ nature, then ponders what meaning to attribute\n
        \ \ \ \ to that sight.":
            $ reading_and_writing += 1

            """
            ✅
            {b}Choice B{/b} is the best answer because it most accurately describes the overall
            structure of the text. First, the speaker describes observing a “most beautiful”
            sight: a tree (“black cypress”) standing out from the golden sky behind it, looking
            like a person’s finger “pointing upwards” and appearing “sensitive” and “exquisite.”
            Then the speaker wonders about the image’s meaning, asking why the finger
            is black and why it’s pointing upward. Thus, the text moves from the speaker’s
            description of a distinctive sight in nature to her pondering about what meaning
            to attribute to that sight.
            """

        "{font=PTSerif.ttf}C) The speaker presents an outdoor scene, then\n
        \ \ \ \ \ considers a human behavior occurring within\n
        \ \ \ \ \ that scene.":
            """
            ❌
            {i}Choice C{/i} is
            incorrect. Although the speaker describes seeing a “black cypress” tree standing
            “against a gold, gold sky” like a pointed finger, she wonders about that natural
            image (asking why the finger, which is really a tree, is black and why it’s pointing)
            and doesn’t give any indication that any people are present in the scene.
            """

        "{font=PTSerif.ttf}D)  The speaker examines her surroundings, then\n
        \ \ \ \ \ speculates about their influence on her\n
        \ \ \ \ \ emotional state.":
            """
            ❌
            {i}Choice D{/i}
            is incorrect. Although the speaker examines and wonders about one thing in her
            surroundings—a “black cypress” tree standing “against a gold, gold sky” like a
            pointed finger—she doesn’t address her own emotional state or consider how it’s
            affected by her surroundings.
            """

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
            """
            ❌
            {i}Choice A{/i} is incorrect. While the speaker does address an opinion of him that
            he believes to be untrue, he doesn’t indicate that this attitude has become
            increasingly prevalent. The speaker also concludes by explaining his goal for the
            future rather than his current worldview.
            """

        "{font=PTSerif.ttf}B) The speaker regrets his isolation from others,\n
        \ \ \ \ \ then predicts a profound change in society.":
            """
            ❌
            {i}Choice B{/i} is incorrect because the text
            doesn’t portray the speaker as isolated or regretful, and the speaker gestures
            toward a hope for societal change but doesn’t offer an explicit prediction that it
            will happen.
            """

        "{font=PTSerif.ttf}C) The speaker concedes his personal\n
        \ \ \ \ \ shortcomings, then boasts of his many\n
        \ \ \ \ \ achievements.":
            """
            ❌
            {i}Choice C{/i} is incorrect because the speaker addresses a criticism of
            him that he believes to be false; he doesn’t admit any personal shortcomings.
            Moreover, the speaker concludes by stating a goal he has rather than showcasing
            his achievements.
            """

        "{font=PTSerif.ttf}D) The speaker addresses a criticism leveled against\n
        \ \ \ \ \ him, then announces a grand ambition of his.":
            $ reading_and_writing += 1

            """
            ✅
            {b}Choice D{/b} is the best answer because it best describes the overall structure of the
            text. The speaker begins by stating that he has heard that others are accusing him of
            seeking to destroy institutions. The speaker then addresses this criticism by stating
            that he is “neither for nor against institutions.” Instead, the speaker states that his
            ultimate goal is to instill “the institution of the dear love of comrades” everywhere
            in the country. Therefore, the overall structure of the text is best described as an
            address of criticism followed by an announcement of a grand ambition.
            """

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
            """
            ❌
            {i}Choice A{/i} is incorrect because the third sentence doesn’t indicate that Chang and
            colleagues were investigating any particular hypothesis. According to the text,
            Chang and colleagues were simply monitoring mimosa trees when the beetles
            happened to be introduced to the area.
            """

        "{font=PTSerif.ttf}B) It presents a generalization that is exemplified\n
        \ \ \ \ by the discussion of the mimosa trees and\n
        \ \ \ \ {i}B. terrenus{/i}.":
            $ reading_and_writing += 1

            """
            ✅
            {b}Choice B{/b} is the best answer because it most accurately describes the function
            of the third sentence within the overall structure of the text. The third sentence
            makes a generalization, asserting that evolutionary links between predators and
            prey can persist across great expanses of time and distance. This generalization
            is exemplified by the text’s discussion of the relationship between mimosa trees
            and {i}B. terrenus{/i} beetles. When mimosa trees were introduced to North America
            in 1785, no {i}B. terrenus{/i} beetles were present, so the relationship between the
            trees and the beetles that exists in their native East Asia was disrupted. When the
            beetles were introduced to North America more than 200 years later, however,
            they quickly attacked mimosa trees, illustrating the generalization that links
            between predators and prey “can persist across centuries and continents.”
            """

        "{font=PTSerif.ttf}C) It offers an alternative explanation for the\n
        \ \ \ \ findings of Chang and colleagues.":
            """
            ❌
            {i}Choice C{/i} is incorrect because the third
            sentence offers a generalization about the relationship between predators and
            prey, not an explanation for the findings of Chang and colleagues that differs from
            an explanation presented elsewhere in the text.
            """

        "{font=PTSerif.ttf}D) It provides context that clarifies why the species\n
        \ \ \ \ mentioned spread to new locations.":
            """
            ❌
            {i}Choice D{/i} is incorrect because
            the third sentence doesn’t discuss any particular species (either the species
            mentioned elsewhere in the text or any other) and doesn’t help explain why
            species spread to new locations.
            """

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
            """
            ❌
            {i}Choice A{/i} is incorrect because nothing in Text 2 suggests that Graeber and
            Wengrow believe that decentralized collective societies are more significant
            than hierarchical systems. Text 2 is focused on Graeber and Wengrow’s view
            that humans have flexibly shifted among various social structures, not on the
            importance of particular structures relative to others.
            """

        "{font=PTSerif.ttf}B) By disputing the idea that developments in social\n
        \ \ \ \ structures have followed a linear progression\n
        \ \ \ \ through distinct stages":
            $ reading_and_writing += 1

            """
            ✅
            {b}Choice B{/b} is the best answer because it describes the most likely way that Graeber
            and Wengrow (Text 2) would respond to the “conventional wisdom” presented
            in Text 1. According to Text 1, the conventional wisdom about human social
            systems is that they developed through stages, beginning with hunter-gatherer
            bands, then moving to clan associations, then chiefdoms, and finally arriving at
            states with bureaucratic structures. Text 2 indicates that Graeber and Wengrow
            believe that human social systems have been flexible, shifting between different
            types of structures, including both hierarchical and collective systems, and that
            these shifts may have even occurred seasonally. This suggests that Graeber and
            Wengrow would dispute the idea that developments in social structures have
            followed a linear progression through distinct stages.
            """

        "{font=PTSerif.ttf}C) By acknowledging that hierarchical roles likely\n
        \ \ \ \ weren’t a part of social systems before the rise of\n
        \ \ \ \ agriculture":
            """
            ❌
            {i}Choice C{/i} is incorrect
            because Text 2 doesn’t include any information suggesting that Graeber and
            Wengrow believe that hierarchies didn’t emerge until after the rise of agriculture.
            In fact, Text 2 indicates that Graeber and Wengrow cite evidence suggesting that
            some hunter-gatherer groups formed social structures with hierarchical elements
            (“communities that included esteemed individuals”) 50,000 years ago, long before
            the rise of agriculture, which Text 1 says occurred around 12,000 years ago.
            """

        "{font=PTSerif.ttf}D) By challenging the assumption that groupings of\n
        \ \ \ \ hunter-gatherers were among the earliest forms\n
        \ \ \ \ of social structure":
            """
            ❌
            {i}Choice D{/i} is incorrect because there’s no information in Text 2 suggesting that
            Graeber and Wengrow would challenge the assumption that groupings of huntergatherers were among the earliest forms of social structure. Although Text 1 does
            indicate that hunter-gatherer groups are assumed to be the earliest human social
            system, Text 2 says only that Graeber and Wengrow believe that some huntergatherer groups made use of different social structures at different times. Text 2
            doesn’t imply that Graeber and Wengrow doubt that hunter-gatherer groups
            preceded most other social structures.
            """

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
            """
            ❌
            {i}Choice A{/i} is incorrect because the text never makes any mention of Mary’s
            chores.
            """

        "{font=PTSerif.ttf}B) Mary is getting bored with pulling up so many
        weeds in the garden.":
            """
            ❌
            {i}Choice B{/i} is incorrect because the text indicates that Mary finds pulling up
            weeds to be fascinating, not boring.
            """

        "{font=PTSerif.ttf}C) Mary is clearing out the garden to create a space
        to play.":
            """
            ❌
            {i}Choice C{/i} is incorrect because Mary thinks of
            garden activities in and of themselves as play, not as something necessary to do
            to create a space to play.
            """

        "{font=PTSerif.ttf}D) Mary feels very satisfied when she’s taking care
        of the garden.":
            $ reading_and_writing += 1

            """
            ✅
            {b}Choice D{/b} is the best answer because it most accurately states the main idea
            of the text. The text describes Mary’s activities in an overgrown hidden garden,
            saying that she was “very much absorbed” and was “only becoming more pleased
            with her work every hour” rather than getting tired of it. She also thinks of garden
            activities as a “fascinating sort of play.” Thus, the main idea of the text is that Mary
            feels very satisfied when taking care of the garden.
            """

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

    jump test4_module1_question17

label test4_module1_question17:

    nvl clear

    "17"

    show test4_module1_question17 at truecenter onlayer overlay

    pause

    """
    {font=PTSerif.ttf}Mycorrhizal fungi in soil benefits many plants, substantially increasing
    the mass of some. A student conducted an experiment to illustrate this
    effect. The student chose three plant species for the experiment,
    including two that are mycorrhizal hosts (species known to benefit
    from mycorrhizal fungi) and one nonmycorrhizal species (a species
    that doesn’t benefit from and may even be harmed by mycorrhizal
    fungi). The student then grew several plants from each species both in
    soil containing mycorrhizal fungi and in soil that had been treated to
    kill mycorrhizal and other fungi. After several weeks, the student
    measured the plants’ average mass and was surprised to discover
    that _______

    {font=PTSerif.ttf}Which choice most effectively uses data from the table to complete the
    statement?
    """

    nvl clear

    menu:
        "{font=PTSerif.ttf}A) broccoli grown in soil containing mycorrhizal fungi had a slightly\n
        \ \ \ \ higher average mass than broccoli grown in soil that had been\n
        \ \ \ \ treated to kill fungi.":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}B) corn grown in soil containing mycorrhizal fungi had a higher\n
        \ \ \ \ average mass than broccoli grown in soil containing mycorrhizal fungi.":
            pass

        "{font=PTSerif.ttf}C) marigolds grown in soil containing mycorrhizal fungi had a much\n
        \ \ \ \ higher average mass than marigolds grown in soil that had been\n
        \ \ \ \ treated to kill fungi.":
            pass

        "{font=PTSerif.ttf}D) corn had the highest average mass of all three species grown in soil\n
        \ \ \ \ that had been treated to kill fungi, while marigolds had the lowest.":
            pass

    jump test4_module1_question18

label test4_module1_question18:

    nvl clear

    """
    18

    {font=PTSerif.ttf}Several artworks found among the ruins of the
    ancient Roman city of Pompeii depict a female figure
    fishing with a cupid nearby. Some scholars have
    asserted that the figure is the goddess Venus, since
    she is known to have been linked with cupids in
    Roman culture, but University of Leicester
    archaeologist Carla Brain suggests that cupids may
    have also been associated with fishing generally. The
    fact that a cupid is shown near the female figure,
    therefore, _______

    {font=PTSerif.ttf}Which choice most logically completes the text?
    """

    menu:
        "{font=PTSerif.ttf}A) is not conclusive evidence that the figure is
        Venus.":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}B) suggests that Venus was often depicted fishing.":
            pass

        "{font=PTSerif.ttf}C) eliminates the possibility that the figure is
        Venus.":
            pass

        "{font=PTSerif.ttf}D) would be difficult to account for if the figure is
        not Venus.":
            pass

    jump test4_module1_question19

label test4_module1_question19:

    nvl clear

    """
    19

    {font=PTSerif.ttf}Literary agents estimate that more than half of all
    nonfiction books credited to a celebrity or other
    public figure are in fact written by ghostwriters,
    professional authors who are paid to write other
    _______ but whose names never appear on book
    covers.

    {font=PTSerif.ttf}Which choice completes the text so that it conforms
    to the conventions of Standard English?
    """

    menu:
        "{font=PTSerif.ttf}A) people’s stories":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}B) peoples story’s":
            pass

        "{font=PTSerif.ttf}C) peoples stories":
            pass

        "{font=PTSerif.ttf}D) people’s story’s":
            pass

    jump test4_module1_question20

label test4_module1_question20:

    nvl clear

    """
    20

    {font=PTSerif.ttf}Like other amphibians, the wood frog ({i}Rana
    sylvatica{/i}) is unable to generate its own heat, so
    during periods of subfreezing temperatures, it
    _______ by producing large amounts of glucose, a
    sugar that helps prevent damaging ice from forming
    inside its cells.

    {font=PTSerif.ttf}Which choice completes the text so that it conforms
    to the conventions of Standard English?
    """

    menu:
        "{font=PTSerif.ttf}A) had survived":
            pass

        "{font=PTSerif.ttf}B) survived":
            pass

        "{font=PTSerif.ttf}C) would survive":
            pass

        "{font=PTSerif.ttf}D) survives":
            $ reading_and_writing += 1

    jump test4_module1_question21

label test4_module1_question21:

    nvl clear

    """
    21

    {font=PTSerif.ttf}After a spate of illnesses as a child, Wilma Rudolph
    was told she might never walk again. Defying all
    odds, Rudolph didn’t just walk, she _______ the
    1960 Summer Olympics in Rome, she won both the
    100- and 200-meter dashes and clinched first place
    for her team in the 4 ×100-meter relay, becoming
    the first US woman to win three gold medals in a
    single Olympics.

    {font=PTSerif.ttf}Which choice completes the text so that it conforms
    to the conventions of Standard English?
    """

    menu:
        "{font=PTSerif.ttf}A) ran—fast—during":
            pass

        "{font=PTSerif.ttf}B) ran—fast during":
            pass

        "{font=PTSerif.ttf}C) ran—fast, during":
            pass

        "{font=PTSerif.ttf}D) ran—fast. During":
            $ reading_and_writing += 1

    jump test4_module1_question22

label test4_module1_question22:

    nvl clear

    """
    22

    {font=PTSerif.ttf}In many of her landscape paintings from the 1970s
    and 1980s, Lebanese American artist Etel Adnan
    worked to capture the essence of California’s
    fog-shrouded Mount Tamalpais region through
    abstraction, using splotches of color to represent
    the area’s features. Interestingly, the triangle
    representing the mountain itself _______ among the
    few defined figures in her paintings.

    {font=PTSerif.ttf}Which choice completes the text so that it conforms
    to the conventions of Standard English?
    """

    menu:
        "{font=PTSerif.ttf}A) are":
            pass

        "{font=PTSerif.ttf}B) have been":
            pass

        "{font=PTSerif.ttf}C) were":
            pass

        "{font=PTSerif.ttf}D) is":
            $ reading_and_writing += 1

    jump test4_module1_question23

label test4_module1_question23:

    nvl clear

    """
    23

    {font=PTSerif.ttf}Seneca sculptor Marie Watt’s blanket art comes in a
    range of shapes and sizes. In 2004, Watt sewed strips
    of blankets together to craft a 10-by-13-inch
    _______ in 2014, she arranged folded blankets into
    two large stacks and then cast them in bronze,
    creating two curving 18-foot-tall blue-bronze pillars.

    {font=PTSerif.ttf}Which choice completes the text so that it conforms
    to the conventions of Standard English?
    """

    menu:
        "{font=PTSerif.ttf}A) sampler later,":
            pass

        "{font=PTSerif.ttf}B) sampler;":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}C) sampler,":
            pass

        "{font=PTSerif.ttf}D) sampler, later,":
            pass

    jump test4_module1_question24

label test4_module1_question24:

    nvl clear

    """
    24

    {font=PTSerif.ttf}African American Percy Julian was a scientist and
    entrepreneur whose work helped people around the
    world to see. Named in 1999 as one of the greatest
    achievements by a US chemist in the past hundred
    years, _______ led to the first mass-produced
    treatment for glaucoma.

    {font=PTSerif.ttf}Which choice completes the text so that it conforms
    to the conventions of Standard English?
    """

    menu:
        "{font=PTSerif.ttf}A) Julian synthesized the alkaloid physostigmine in
        1935; it":
            pass

        "{font=PTSerif.ttf}B) in 1935 Julian synthesized the alkaloid
        physostigmine, which":
            pass

        "{font=PTSerif.ttf}C) Julian’s 1935 synthesis of the alkaloid
        physostigmine":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}D) the alkaloid physostigmine was synthesized by
        Julian in 1935 and":
            pass

    jump test4_module1_question25

label test4_module1_question25:

    nvl clear

    """
    25

    {font=PTSerif.ttf}The Arctic-Alpine Botanic Garden in Norway and
    the Jardim Botânico of Rio de Janeiro in Brazil are
    two of many botanical gardens around the world
    dedicated to growing diverse plant _______
    fostering scientific research; and educating the public
    about plant conservation.

    {font=PTSerif.ttf}Which choice completes the text so that it conforms
    to the conventions of Standard English?
    """

    menu:
        "{font=PTSerif.ttf}A) species, both native and nonnative,":
            pass

        "{font=PTSerif.ttf}B) species, both native and nonnative;":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}C) species; both native and nonnative,":
            pass

        "{font=PTSerif.ttf}D) species both native and nonnative,":
            pass

    jump test4_module1_question26

label test4_module1_question26:

    nvl clear

    """
    26

    {font=PTSerif.ttf}Sociologist Alton Okinaka sits on the review board
    tasked with adding new sites to the Hawai‘i Register
    of Historic Places, which includes Pi‘ilanihale
    Heiau and the ‘Ōpaeka‘a Road Bridge. Okinaka
    doesn’t make such decisions _______ all historical
    designations must be approved by a group of nine
    other experts from the fields of architecture,
    archaeology, history, and Hawaiian culture.

    {font=PTSerif.ttf}Which choice completes the text so that it conforms
    to the conventions of Standard English?
    """

    menu:
        "{font=PTSerif.ttf}A) single-handedly, however;":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}B) single-handedly; however,":
            pass

        "{font=PTSerif.ttf}C) single-handedly, however,":
            pass

        "{font=PTSerif.ttf}D) single-handedly however":
            pass

    jump test4_module1_question27

label test4_module1_question27:

    nvl clear

    """
    27

    {font=PTSerif.ttf}In 1968, US Congressman John Conyers introduced
    a bill to establish a national holiday in honor of
    Dr. Martin Luther King Jr. The bill didn’t make it to
    a vote, but Conyers was determined. He teamed up
    with Shirley Chisholm, the first Black woman to be
    elected to Congress, and they resubmitted the bill
    every session for the next fifteen years. _______ in
    1983, the bill passed.

    {font=PTSerif.ttf}Which choice completes the text with the most
    logical transition?
    """

    menu:
        "{font=PTSerif.ttf}A) Instead,":
            pass

        "{font=PTSerif.ttf}B) Likewise,":
            pass

        "{font=PTSerif.ttf}C) Finally,":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}D) Additionally,":
            pass

    jump test4_module1_question28

label test4_module1_question28:

    nvl clear

    """
    28

    {font=PTSerif.ttf}Geoscientists have long considered Hawaii’s Mauna
    Loa volcano to be Earth’s largest shield volcano by
    volume, measuring approximately 74,000 cubic
    kilometers. _______ according to a 2020 study by
    local geoscientist Michael Garcia, Hawaii’s
    Pūhāhonu shield volcano is significantly larger,
    boasting a volume of about 148,000 cubic kilometers.

    {font=PTSerif.ttf}Which choice completes the text with the most
    logical transition?
    """

    menu:
        "{font=PTSerif.ttf}A) Secondly,":
            pass

        "{font=PTSerif.ttf}B) Consequently,":
            pass

        "{font=PTSerif.ttf}C) Moreover,":
            pass

        "{font=PTSerif.ttf}D) However,":
            $ reading_and_writing += 1

    jump test4_module1_question29

label test4_module1_question29:

    nvl clear

    """
    29

    {font=PTSerif.ttf}Samuel Coleridge-Taylor was a prominent classical
    music composer from England who toured the US
    three times in the early 1900s. The child of a West
    African father and an English mother, Coleridge-Taylor
    emphasized his mixed-race ancestry. For
    example, he referred to himself as Anglo-African.
    _______ he incorporated the sounds of traditional
    African music into his classical music compositions.

    {font=PTSerif.ttf}Which choice completes the text with the most
    logical transition?
    """

    menu:
        "{font=PTSerif.ttf}A) In addition,":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}B) Actually,":
            pass

        "{font=PTSerif.ttf}C) However,":
            pass

        "{font=PTSerif.ttf}D) Regardless,":
            pass

    jump test4_module1_question30

label test4_module1_question30:

    nvl clear

    """
    30

    {font=PTSerif.ttf}In 2019, researcher Patricia Jurado Gonzalez and
    food historian Nawal Nasrallah prepared a stew from
    a 4,000-year-old recipe found on a Mesopotamian
    clay tablet. When they tasted the dish, known as
    {i}pašrūtum{/i} (“unwinding”), they found that it had a
    mild taste and inspired a sense of calm. _______ the
    researchers, knowing that dishes were sometimes
    named after their intended effects, theorized that the
    dish’s name, “unwinding,” referred to its function: to
    help ancient diners relax.

    {font=PTSerif.ttf}Which choice completes the text with the most
    logical transition?
    """

    menu:
        "{font=PTSerif.ttf}A) Therefore,":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}B) Alternately,":
            pass

        "{font=PTSerif.ttf}C) Nevertheless,":
            pass

        "{font=PTSerif.ttf}D) Likewise,":
            pass

    jump test4_module1_question31

label test4_module1_question31:

    nvl clear

    """
    31

    {font=PTSerif.ttf}While researching a topic, a student has taken the
    following notes:

    {font=PTSerif.ttf}• Chemical leavening agents cause carbon dioxide
    to be released within a liquid batter, making the
    batter rise as it bakes.\n
    • Baking soda and baking powder are chemical
    leavening agents.\n
    • Baking soda is pure sodium bicarbonate.\n
    • To produce carbon dioxide, baking soda needs to
    be mixed with liquid and an acidic ingredient such
    as honey.\n
    • Baking powder is a mixture of sodium bicarbonate
    and an acid.\n
    • To produce carbon dioxide, baking powder needs
    to be mixed with liquid but not with an acidic
    ingredient.

    {font=PTSerif.ttf}The student wants to emphasize a difference between
    baking soda and baking powder. Which choice most
    effectively uses relevant information from the notes
    to accomplish this goal?
    """

    nvl clear

    menu:
        "{font=PTSerif.ttf}A) To make batters rise, bakers use chemical leavening agents\n
        \ \ \ \ such as baking soda and baking powder.":
            pass

        "{font=PTSerif.ttf}B) Baking soda and baking powder are chemical leavening agents\n
        \ \ \ \ that, when mixed with other ingredients cause carbon dioxide\n
        \ \ \ \ to be released within a batter.":
            pass

        "{font=PTSerif.ttf}C) Baking soda is pure sodium bicarbonate, and honey is a\n
        \ \ \ \ type of acidic ingredient.":
            pass

        "{font=PTSerif.ttf}D) To produce carbon dioxide within a liquid batter, baking soda\n
        \ \ \ \ needs to be mixed with an acidic ingredient, whereas baking\n
        \ \ \ \ powder does not.":
            $ reading_and_writing += 1

    jump test4_module1_question32

label test4_module1_question32:

    nvl clear

    """
    32

    {font=PTSerif.ttf}While researching a topic, a student has taken the
    following notes:

    {font=PTSerif.ttf}• Soo Sunny Park is a Korean American artist who
    uses light as her primary medium of expression.\n
    • She created her work {i}Unwoven Light{/i} in 2013.\n
    • {i}Unwoven Light{/i} featured a chain-link fence fitted
    with iridescent plexiglass tiles.\n
    • When light passed through the fence, colorful
    prisms formed.

    {font=PTSerif.ttf}The student wants to describe {i}Unwoven Light{/i} to an
    audience unfamiliar with Soo Sunny Park. Which
    choice most effectively uses relevant information
    from the notes to accomplish this goal?
    """

    nvl clear

    menu:
        "{font=PTSerif.ttf}A) Park’s 2013 installation {i}Unwoven Light{/i}, which\n
        \ \ \ \ included a chain-link fence and iridescent tiles\n
        \ \ \ \ made from plexiglass, featured light as its\n
        \ \ \ \ primary medium of expression.":
            pass

        "{font=PTSerif.ttf}B) Korean American light artist Soo Sunny Park\n
        \ \ \ \ created {i}Unwoven Light{/i} in 2013.":
            pass

        "{font=PTSerif.ttf}C) The chain-link fence in Soo Sunny Park’s\n
        \ \ \ \ {i}Unwoven Light{/i} was fitted with tiles made from\n
        \ \ \ \ iridescent plexiglass.":
            pass

        "{font=PTSerif.ttf}D) In {i}Unwoven Light{/i}, a 2013 work by Korean\n
        \ \ \ \ American artist Soo Sunny Park, light formed\n
        \ \ \ \ colorful prisms as it passed through a fence Park\n
        \ \ \ \ had fitted with iridescent tiles.":
            $ reading_and_writing += 1

    jump test4_module1_question33

label test4_module1_question33:

    nvl clear

    """
    33

    {font=PTSerif.ttf}While researching a topic, a student has taken the
    following notes:

    {font=PTSerif.ttf}• Cambodia’s Angkor Wat was built in the 1100s to
    honor the Hindu god Vishnu.\n
    • It has been a Buddhist temple since the sixteenth
    century.\n
    • Decorrelation stretch analysis is a novel digital
    imaging technique that enhances the contrast
    between colors in a photograph.\n
    • Archaeologist Noel Hidalgo Tan applied
    decorrelation stretch analysis to photographs he
    had taken of Angkor Wat’s plaster walls.\n
    • Tan’s analysis revealed hundreds of images
    unknown to researchers.

    {font=PTSerif.ttf}The student wants to present Tan’s research to an
    audience unfamiliar with Angkor Wat. Which choice
    most effectively uses relevant information from the
    notes to accomplish this goal?
    """

    nvl clear

    menu:
        "{font=PTSerif.ttf}A) Tan photographed Angkor Wat’s plaster walls\n
        \ \ \ \ and then applied decorrelation stretch analysis to\n
        \ \ \ \ the photographs.":
            pass

        "{font=PTSerif.ttf}B) Decorrelation stretch analysis is a novel digital\n
        \ \ \ \ imaging technique that Tan used to enhance the\n
        \ \ \ \ contrast between colors in a photograph.":
            pass

        "{font=PTSerif.ttf}C)  Using a novel digital imaging technique, Tan\n
        \ \ \ \ revealed hundreds of images hidden on the walls\n
        \ \ \ \ of Angkor Wat, a Cambodian temple.":
            $ reading_and_writing += 1

        "{font=PTSerif.ttf}D) Built to honor a Hindu god before becoming a\n
        \ \ \ \ Buddhist temple, Cambodia’s Angkor Wat\n
        \ \ \ \ concealed hundreds of images on its plaster walls.":
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
