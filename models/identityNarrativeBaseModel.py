from pydantic import BaseModel
from typing import List

class BasicInformation(BaseModel):
    age: str
    racial_background: str
    location: str

class KeyRoles(BaseModel):
    parental_role: str
    professional_role: str
    community_roles: str

class CoreChallenges(BaseModel):
    challenges: str
    conflicts: str
    emotional: str
    psychological_struggles: str
    circumstances: str
class LifeEvents(BaseModel):
    life_events: str
    turning_points: str

class ValueBeliefs(BaseModel):
    keyvalues: str
    professional_role: str
    philosophical: str
    moral_principles: str

class AspirationsDreams(BaseModel):
    aspirations: str
    dreams: str
    hope: str
    achieve: str
    exprience: str

class PersonalGrowth(BaseModel):
    personal_growth: str
    personal_change: str
    community_roles: str

class Contemplations (BaseModel):
      contemplations : str
      conflicts: str
      doubts: str
      regrets: str
      unresolved: str
      tension: str

class LifeStyle(BaseModel):
      lifestyle: str
      habits: str
      interests: str
      hobbies: str
      passions: str
      unresolved: str
      routine_activities: str

class InteractsWithSociety(BaseModel):
      critical_thoughts: str
      culture: str
      global_issues: str

class PersonalAnecdote(BaseModel):
      personal_anecdote: str
      personal_quotes: str
      global_issues: str
      experiences: str
      subject_perspective :str
                 
class Conclusion(BaseModel): 
      ongoing_questions: str
      dilemmas: str
      life_journey: str

class IdentityNarrative(BaseModel):
     basic_information: BasicInformation
     key_roles: KeyRoles
     core_challenges:CoreChallenges
     lifeevents: LifeEvents
     value_beliefs: ValueBeliefs
     aspirations_dreams: AspirationsDreams
     personal_growth: PersonalGrowth
     contemplations: Contemplations 
     lifestyle: LifeStyle
     interactswithsociety: InteractsWithSociety
     personal_anecdote:  PersonalAnecdote
     conclusion: Conclusion
                 
 
     