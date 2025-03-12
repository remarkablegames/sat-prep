# https://satsuite.collegeboard.org/media/pdf/sat-practice-test-4-digital.pdf
# https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-4-digital.pdf
label test4:

    nvl clear

    $ reading_and_writing = 0
    $ math = 0

    scene bg classroom

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

    nvl clear

    """
    {font=PTSerif.ttf}Which choice best states the main purpose of the
    text?
    """

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

    nvl clear

    """
    {font=PTSerif.ttf}Which choice best describes the overall structure of
    the text?
    """

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
    \ \ \ \ \[Manhattan\] and in every city of These States,\n
    \ \ \ \ inland and seaboard,\n
    And in the fields and woods, and above every\n
    \ \ \ \ keel \[ship\] little or large, that dents the water,\n
    Without edifices, or rules, or trustees, or any\n
    \ \ \ \ argument,\n
    The institution of the dear love of comrades.
    """

    nvl clear

    """
    {font=PTSerif.ttf}Which choice best describes the overall structure of
    the text?
    """

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
    """

    nvl clear

    """
    {font=PTSerif.ttf}Which choice best describes the function of the third
    sentence in the overall structure of the text?
    """

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

    jump test4_score

label test4_score:

    nvl clear

    scene bg hallway

    """
    Reading and Writing Score: [reading_and_writing]/66

    Math Score: [math]/54
    """

    jump end
