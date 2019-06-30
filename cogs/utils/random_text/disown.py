from random import choice

from cogs.utils.random_text.text_template import TextTemplate


class DisownRandomText(TextTemplate):


    @classmethod
    def valid_target(cls, instigator=None, target=None):
        '''
        '''

        return choice(cls.get_valid_strings([
            "Oof, {target.mention}, {instigator.mention} doesn't seem to want you any more...",
            "Well, {instigator.mention}, say goodbye to {target.mention}.",
            "Might be good news for you, {target.mention}, but you're finally free of {instigator.mention}.",
            "One child down, the rest to go.",
            "A sad day when a parent disowns their child...",
            "I'm sure this is very emotional for you. I'm sorry for your loss.",
            "One less problem for you to deal with.",
            "They're just out to get some cigarettes and milk, I'm sure they'll be back soon.",
            "I guess they got the winning lottery numbers, huh?",
        ], *['instigator' if instigator else None, 'target' if target else None])).format(instigator=instigator, target=target)


    @classmethod 
    def instigator_is_unqualified(cls, instigator=None, target=None):
        '''
        '''

        return choice(cls.get_valid_strings([
            "They aren't your child...",
            "Have you considered disowning someone who's *actually* your child?",
            "Strangely enough you can only disown *your* children.",
            "Are you confusing that person for your child?",
        ], *['instigator' if instigator else None, 'target' if target else None])).format(instigator=instigator, target=target)
