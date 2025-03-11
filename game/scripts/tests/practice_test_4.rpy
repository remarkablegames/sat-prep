﻿label practice_test_4:

    $ reading_and_writing = 0
    $ math = 0

    scene bg classroom

    nvl clear

    # https://satsuite.collegeboard.org/media/pdf/sat-practice-test-4-digital.pdf
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

    nvl clear

    # https://satsuite.collegeboard.org/media/pdf/scoring-sat-practice-test-4-digital.pdf
    """
    Reading and Writing Score: [reading_and_writing]/66

    Math Score: [math]/54
    """

    nvl clear

    jump end
