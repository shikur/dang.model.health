from typing import TypedDict, List

# Define typed dictionaries for each function's parameters
class BasicInformation(TypedDict):
    age: str
    racial_background: str
    location: str

class KeyRoles(TypedDict):
    parental_role: str
    professional_role: str
    community_roles: str

class CoreChallenges(TypedDict):
    challenges: str
    conflicts: str
    emotional: str
    psychological_struggles: str
    circumstances: str
class LifeEvents(TypedDict):
    life_events: str
    turning_points: str

class ValueBeliefs(TypedDict):
    keyvalues: str
    professional_role: str
    philosophical: str
    moral_principles: str

class AspirationsDreams(TypedDict):
    aspirations: str
    dreams: str
    hope: str
    achieve: str
    exprience: str

class PersonalGrowth(TypedDict):
    personal_growth: str
    personal_change: str
    community_roles: str

class Contemplations (TypedDict):
      contemplations : str
      conflicts: str
      doubts: str
      regrets: str
      unresolved: str
      tension: str

class LifeStyle(TypedDict):
      lifestyle: str
      habits: str
      interests: str
      hobbies: str
      passions: str
      unresolved: str
      routine_activities: str

class InteractsWithSociety(TypedDict):
      critical_thoughts: str
      culture: str
      global_issues: str

class PersonalAnecdote(TypedDict):
      personal_anecdote: str
      personal_quotes: str
      global_issues: str
      experiences: str
      subject_perspective :str
                 
class Conclusion(TypedDict): 
      ongoing_questions: str
      dilemmas: str
      life_journey: str
      
      
# Define the class interface
class IdentityNarrativeInterface:
    def basic_information(self, basic_info: BasicInformation) -> str:
        return f"1. Basic Information:\n" \
               f"   - Age: {basic_info['age']}\n" \
               f"   - Racial or Ethnic Background: {basic_info['racial_background']}\n" \
               f"   - Geographical Location: {basic_info['location']}\n\n"

    def key_roles(self, roles: KeyRoles) -> str:
        return f"2. Key Roles in Life:\n" \
               f"   - Parental Role: {roles['parental_role']}\n" \
               f"   - Professional Role: {roles['professional_role']}\n" \
               f"   - Community Roles: {roles['community_roles']}\n\n"

    def core_challenges(self, challenges: CoreChallenges) -> str:
        return f"3. Core Challenges:\n" \
               f"   - Challenges: {challenges['challenges']}\n" \
               f"   - Conflicts: {challenges['conflicts']}\n" \
               f"   - Emotional: {challenges['emotional']}\n" \
               f"   - Psychological Struggles: {challenges['psychological_struggles']}\n" \
               f"   - Circumstances: {challenges['circumstances']}\n\n"
   
    def lifeevents(self, lifeevent:LifeEvents):
        life_events =f"4. LIFE EVENTS:\n" \
               f"   - life events: {lifeevent['parental_role']}\n" \
               f"   - turning points: {lifeevent['professional_role']}\n" \
               f"   that have had a profound impact on the subject's identity and life path."
        return life_events
   
    def value_beliefs(self, valuebliefs: ValueBeliefs):
        value_belief =f"4. VALUES AND BELIEFS:\n" \
               f"   - keyvalues: {valuebliefs['keyvalues']}\n" \
               f"   - Professional: {valuebliefs['professional_role']}\n" \
               f"   - philosophical: {valuebliefs['philosophical']}\n\n" \
               f"   - moralprinciples: {valuebliefs['moral_principles']}\n" \
               
               
        return value_belief


    def aspirations_dreams(self, aspirationsdream: AspirationsDreams):
        aspirations_dream = f"5. ASPIRATIONS AND DREAMS:\n" \
                        f"   - aspirations: {aspirationsdream['aspirations']}\n" \
                        f"   - dreams: {aspirationsdream['dreams']}\n" \
                        f"   - hope: what they hope to {achieve} or {experience} in the future\n\n" \
                        f"   - achieve: what they hope to {achieve} or {experience} in the future\n\n" \
                        f"   - experience: what they hope to {achieve} or {experience} in the future\n\n" 

        return aspirations_dream

    def personalgrowth(self, personalgrowth: PersonalGrowth):
        personal_growth =f"6. PERSONAL GROWTH AND CHANGE:\n" \
                f"Reflect on the subject's journey of " \
                f"   - personalgrowth: {personalgrowth['personal_growth']}\n" \
                f"   - personalchange: {personalgrowth['personal_change']}\n" \
                f"   - Community Roles: {personalgrowth['community_roles']}\n" \
                f" Mention how they have evolved over time and any lessons learned. " \

        return personal_growth


    def contemplations(self, contemplations: Contemplations):
        contemplations =f"7. ASPIRATIONS AND DREAMS:\n" \
                f"Explore the subject's internal" \
                f"   - contemplations: {contemplations['contemplations']}\n" \
                f"   - conflicts: {contemplations['conflicts']}\n" \
                f"   - doubts: {contemplations['doubts']}\n" \
                f"   - regrets: {contemplations['regrets']}\n" \
                f"   - unresolved: {contemplations['unresolved']} tension.\n" \
                f"   - tension: {contemplations['tension']} .\n" \
            

        return contemplations


    def lifestyle(self, lifestyle: LifeStyle):
        life_style =f"8. CURRENT LIFESTYLE AND INTERESTS:\n" \
                f"Explore the subject's internal" \
                f"   - lifestyle: {lifestyle['lifestyle']}\n" \
                f"   - habits: {lifestyle['habits']}\n" \
                f"   - interests: {lifestyle['interests']}\n" \
                f"   - hobbies: {lifestyle['hobbies']}\n" \
                f"   - passions: {lifestyle['passions']} tension.\n" \
                f"   - routine activities: {lifestyle['routine_activities']} .\n"      

        return life_style

    def interacts_with_society(self, interactswithsociety: InteractsWithSociety):
        interacts_society =f"9. RELATIONSHIP WITH THE OUTER WORLD:\n" \
                f"Explore the subject's internal" \
                f"   - critical thoughts societal norms: {interactswithsociety['critical_thoughts']}\n" \
                f"   - culture: {interactswithsociety['culture']}\n" \
                f"   - global issues: {interactswithsociety['global_issues']}\n" \
                        

        return interacts_society

    def personal_anecdote(self, personalanecdote: PersonalAnecdote):
        personal_anecdote =f"10. PERSONAL ANECDOTES OR QUOTES:\n" \
                f"Explore the subject's internal" \
                f" - personal anecdote: {personalanecdote['personal_anecdote']}\n" \
                f" - personal quotes: {personalanecdote['personal_quotes']}\n" \
                f"  - global issues: {personalanecdote['global_issues']}\n" \
                f" - experiences: {personalanecdote['experiences']}\n" \
                f" - subject's perspective: {personalanecdote['subject_perspective']}\n" \
                        

        return personal_anecdote

    def conclusion(self, conclusion: Conclusion):
        conclusion =f"11. CONCLUSION:\n" \
                f"Explore the subject's internal" \
                f" - ongoing questions: {conclusion['ongoing_questions']}\n" \
                f" - dilemmas they are facing: {conclusion['dilemmas']}\n" \
                f" - what they are seeking or moving towards in their life journey: {conclusion['life_journey']}\n" \
                                        

        return conclusion




