from pydantic import BaseModel
from typing import List, Optional

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
     basic_information: Optional[BasicInformation] = None
     key_roles: Optional[KeyRoles] = None 
     core_challenges: Optional[CoreChallenges] = None
     life_events: Optional[LifeEvents] = None
     value_beliefs: Optional[ValueBeliefs] = None
     aspirations_dreams: Optional[AspirationsDreams] = None
     personal_growth: Optional[PersonalGrowth] = None
     contemplations: Optional[Contemplations] = None
     life_style: Optional[LifeStyle] = None
     interacts_with_society: Optional[InteractsWithSociety] = None
     personal_anecdote:  Optional[PersonalAnecdote] = None
     conclusion: Optional[Conclusion] = None
    
     def update_basic_information(self, basic_info: BasicInformation):
        self.basic_information = basic_info              
 
     def update_key_roles(self, key_roles: KeyRoles):
        self.key_roles = key_roles

     def update_core_challenges(self, core_challenges: CoreChallenges):
        self.core_challenges = core_challenges

     def update_lifeevents(self, lifeevents: LifeEvents):
        self.lifeevents = lifeevents

     def update_value_beliefs(self, value_beliefs: ValueBeliefs):
        self.value_beliefs = value_beliefs

     def update_aspirations_dreams(self, aspirations_dreams: AspirationsDreams):
        self.aspirations_dreams = aspirations_dreams

     def update_personal_growth(self, personal_growth: PersonalGrowth):
        self.personal_growth = personal_growth

     def update_contemplations(self, contemplations: Contemplations):
        self.contemplations = contemplations

     def update_lifestyle(self, lifestyle: LifeStyle):
        self.lifest = lifestyle

     def update_interactswithsociety(self, interactswithsociety: InteractsWithSociety):
        self.interactswithsociety = interactswithsociety

     def update_personal_anecdote(self, personal_anecdote: PersonalAnecdote ):
        self.personal_anecdote = personal_anecdote

     def update_conclusion(self, conclusion: Conclusion):
        self.conclusion = conclusion

     def get_basic_information(self) -> BasicInformation:
        return self.basic_information

     def get_key_roles(self) -> KeyRoles:
        return self.key_roles

     def get_core_challenges(self) -> CoreChallenges:
        return self.core_challenges

     def get_lifeevents(self) -> LifeEvents:
        return self.lifeevents

     def get_value_beliefs(self) -> ValueBeliefs:
        return self.value_beliefs

     def get_aspirations_dreams(self) -> AspirationsDreams:
        return self.aspirations_dreams

     def get_personal_growth(self) -> PersonalGrowth:
        return self.personal_growth

     def get_contemplations(self) -> Contemplations:
        return self.contemplations

     def get_lifestyle(self) -> LifeStyle:
        return self.lifestyle

     def get_interactswithsociety(self) -> InteractsWithSociety:
        return self.interactswithsociety

     def get_personal_anecdote(self) -> PersonalAnecdote:
        return self.personal_anecdote

     def get_conclusion(self) -> Conclusion:
        return self.conclusion
