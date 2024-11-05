from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import logging
import random  # Import the random module to select random sentences

logger = logging.getLogger(__name__)

@api_view(['POST'])
def create_madlib(request):
    # Extracting data from the request
    noun = request.data.get('noun')
    verb = request.data.get('verb')
    adjective = request.data.get('adjective')
    adverb = request.data.get('adverb')

    # Basic validation example
    if not all([noun, verb, adjective, adverb]):
        logger.warning("Missing fields in request data.")
        return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

    # Define a list of possible Mad Lib sentences for each genre
    madlib_templates = {
        "Adventure": [
            f"The brave {noun} set out on a journey to {verb} across the {adjective} land.",
            f"In the heart of the jungle, a {adjective} {noun} discovered a hidden treasure.",
            f"The {noun} climbed the {adjective} mountain, eager to {verb} at the peak.",
            f"A mysterious map led the {noun} to {verb} the ancient ruins {adverb}.",
            f"The crew of the ship was {adjective}, ready to {verb} into uncharted waters.",
            f"While {verb}ing {adverb}, the {noun} stumbled upon a secret cave.",
            f"The {noun} faced fierce storms while trying to {verb} home.",
            f"During their adventure, the {noun} met a {adjective} guide who helped them {verb}.",
            f"With the help of a {adjective} artifact, the {noun} could finally {verb} their way to safety.",
            f"As the sun set, the {noun} realized they must {verb} before darkness fell.",
            f"The {noun} enjoyed a peaceful life, surrounded by {adjective} friends and family.",
            f"One day, a mysterious stranger arrived, {verb}ing {adverb} about a great adventure.",
            f"The village was suddenly attacked by a {adjective} monster, calling the {noun} to action.",
            f"At first, the {noun} hesitated to leave, feeling {adjective} and uncertain.",
            f"Despite the call to adventure, the {noun} preferred to stay home and {verb} {adverb}.",
            f"Then, an old {noun} appeared, offering {adjective} advice on how to {verb}.",
            f"The wise mentor taught the {noun} to be brave and {verb} {adverb} in the face of danger.",
            f"With newfound courage, the {noun} set out, ready to {verb} {adverb} into the unknown.",
            f"The {noun} crossed the threshold into the enchanted forest, feeling {adjective} excitement.",
            f"Along the way, the {noun} met a {adjective} ally who helped them {verb} {adverb}.",
            f"The journey was fraught with challenges, as the {noun} had to face a {adjective} enemy.",
            f"Finally, the {noun} approached the {adjective} cave, ready to confront their fears.",
            f"The {noun} prepared to {verb} {adverb} and enter the dark cave filled with secrets.",
            f"In the cave, the {noun} faced their greatest challenge and felt {adjective} fear.",
            f"The battle was fierce as the {noun} had to {verb} {adverb} to survive the ordeal.",
            f"After the fight, the {noun} discovered a {adjective} treasure that granted them power.",
            f"The {noun} returned victorious, carrying a {adjective} trophy of their bravery.",
            f"As the {noun} made their way home, they felt a sense of {adjective} accomplishment.",
            f"The journey back was filled with {adjective} memories of the adventures they had.",
            f"Back in the village, the {noun} was celebrated as a hero, feeling {adjective} and proud.",
            f"The once timid {noun} had transformed into a {adjective} hero, ready to inspire others.",
            f"The {noun} returned with tales of {adjective} adventures, sharing wisdom with all.",
            f"From that day on, the {noun} taught others how to {verb} {adverb} in their own lives."
        ],
        "Comedy": [
            f"The {noun} slipped on a {adjective} banana peel while trying to {verb} {adverb}.",
            f"In a world where everyone was {adjective}, the {noun} decided to {verb} {adverb}.",
            f"A {noun} walks into a bar and starts to {verb} {adverb} at the bartender.",
            f"The {adjective} {noun} tried to {verb} but ended up {adverb} embarrassing themselves.",
            f"When the {noun} tried to impress their crush, they accidentally {verb} a {adjective} dance.",
            f"Feeling {adjective}, the {noun} decided to {verb} {adverb} in front of a crowd.",
            f"The {noun} told a joke so {adjective} that everyone started to {verb} {adverb}.",
            f"After eating a {adjective} meal, the {noun} felt the need to {verb} immediately.",
            f"When the {noun} was asked to {verb}, they replied with a {adjective} pun.",
            f"Every time the {noun} tried to {verb}, something {adjective} went hilariously wrong."
        ],
        "Drama": [
            f"The {noun} faced a {adjective} choice that would change their life forever.",
            f"In a moment of desperation, the {noun} chose to {verb} {adverb}.",
            f"The {adjective} letter arrived just as the {noun} was about to {verb}.",
            f"Under the {adjective} sky, the {noun} decided to {verb} their feelings.",
            f"The {noun} watched as everything they loved was taken away, leaving only {adjective} memories.",
            f"In a quiet moment, the {noun} reflected on how to {verb} with {adjective} emotions.",
            f"The {adjective} truth was finally revealed, forcing the {noun} to {verb} for justice.",
            f"Feeling {adjective}, the {noun} knew they had to {verb} before it was too late.",
            f"As the {noun} stood on stage, they felt {adjective} vulnerability before {verb}ing their story.",
            f"The {noun} realized that sometimes, to {verb}, you must first confront the {adjective} past."
        ],
        "Fantasy": [
            f"In a land where {adjective} creatures roamed, the {noun} learned to {verb} {adverb}.",
            f"The {adjective} potion granted the {noun} the power to {verb} like never before.",
            f"With a {adjective} spell, the {noun} transformed into a magnificent beast and decided to {verb}.",
            f"The {noun} discovered a {adjective} portal that led to a world of {verb}ing adventures.",
            f"A {adjective} prophecy foretold that only the {noun} could {verb} the darkness.",
            f"The enchanted {noun} held the secret to {verb}ing the realm from the {adjective} sorceress.",
            f"While {verb}ing in the forest, the {noun} encountered a {adjective} fairy.",
            f"The {adjective} crown was said to give its wearer the ability to {verb} with ease.",
            f"As the {noun} stepped into the {adjective} castle, they felt an urge to {verb}.",
            f"The {adjective} dragon offered the {noun} a chance to {verb} their destiny."
        ],
        "Horror": [
            f"The {noun} heard a {adjective} noise in the dark, causing them to {verb} in fear.",
            f"On a stormy night, the {noun} realized they were not alone and began to {verb} {adverb}.",
            f"The {adjective} house was rumored to hold secrets that the {noun} dared to {verb}.",
            f"After finding an old {adjective} diary, the {noun} decided to {verb} to uncover the truth.",
            f"As the lights flickered, the {noun} felt a {adjective} presence behind them, urging them to {verb}.",
            f"The {adjective} scream echoed through the halls as the {noun} tried to {verb} to safety.",
            f"In a {adjective} twist, the {noun} discovered they were part of the horror story they tried to {verb}.",
            f"The {noun} stumbled upon a {adjective} artifact that changed their ability to {verb}.",
            f"When the clock struck midnight, the {noun} had to {verb} or face the {adjective} fate.",
            f"With every step, the {noun} felt the urge to {verb} but was held back by {adjective} terror."
        ],
        "Romance": [
            f"The {noun} found a {adjective} love letter that made them want to {verb} {adverb}.",
            f"Under the {adjective} stars, the {noun} knew it was time to {verb} their feelings.",
            f"The {adjective} moment was perfect for the {noun} to finally {verb} and confess their love.",
            f"After a {adjective} encounter, the {noun} could not stop thinking about how to {verb}.",
            f"The {noun} decided to {verb} a heartfelt message to their {adjective} crush.",
            f"In a {adjective} twist of fate, the {noun} met someone who would change their life and make them {verb}.",
            f"The {adjective} melody played as the {noun} prepared to {verb} in the dance of love.",
            f"The {noun} realized that sometimes, to {verb}, you must take a leap of {adjective} faith.",
            f"When the {noun} held the {adjective} gift, they felt a rush of emotions that made them want to {verb}.",
            f"The {noun} knew that true love often required them to {verb} through challenges together."
        ]
    }

    # Randomly select a genre
    selected_genre = random.choice(list(madlib_templates.keys()))
    selected_templates = madlib_templates[selected_genre]

    # Randomly select a template from the chosen genre
    madlib_sentence = random.choice(selected_templates)

    # Return the response with a single sentence
    logger.info("Madlib created successfully.")
    
    return Response(madlib_sentence, status=status.HTTP_200_OK)
