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
        try:
            if basic_info is None or basic_info == '':
                return ''
            else:
             return f"1. Basic Information:\n" \
               f"   - Age: {basic_info['age']}\n" \
               f"   - Racial or Ethnic Background: {basic_info['racial_background']}\n" \
               f"   - Geographical Location: {basic_info['location']}\n\n"
               
        except Exception as e:
          print(f"Error: {e}")
        return {"error": str(e)}       

    def key_roles(self, roles: KeyRoles) -> str:
        try:
            if roles is None or roles == '':
                return ''
            else:
             return f"2. Key Roles in Life:\n" \
               f"   - Parental Role: {roles['parental_role']}\n" \
               f"   - Professional Role: {roles['professional_role']}\n" \
               f"   - Community Roles: {roles['community_roles']}\n\n"
        except Exception as e:
          print(f"Error: {e}")
        return {"error": str(e)}       

    def core_challenges(self, challenges: CoreChallenges) -> str:
        try:
            if challenges is None or challenges == '':
                return ''
            else:
             return f"3. Core Challenges:\n" \
               f"   - Challenges: {challenges['challenges']}\n" \
               f"   - Conflicts: {challenges['conflicts']}\n" \
               f"   - Emotional: {challenges['emotional']}\n" \
               f"   - Psychological Struggles: {challenges['psychological_struggles']}\n" \
               f"   - Circumstances: {challenges['circumstances']}\n\n"
               
        except Exception as e:
          print(f"Error: {e}")
        return {"error": str(e)}       
   
    def life_events(self, lifeevent: LifeEvents) -> str:
        try:
            if lifeevent is None or lifeevent == '':
                return ''
            else:
             life_events = f"4. LIFE EVENTS:\n" \
               f"   - life events: {lifeevent['life_events']}\n" \
               f"   - turning points: {lifeevent['turning_points']}\n" \
               f"   that have had a profound impact on the subject's identity and life path."
             return life_events
        except Exception as e:
          print(f"Error: {e}")
        return {"error": str(e)}

   
    def value_beliefs(self, valuebliefs: ValueBeliefs)-> str:
        try:
            if valuebliefs is None or valuebliefs == '':
                return ''
            else:
             value_belief = f"4. VALUES AND BELIEFS:\n" \
               f"   - keyvalues: {valuebliefs['keyvalues']}\n" \
               f"   - Professional: {valuebliefs['professional_role']}\n" \
               f"   - philosophical: {valuebliefs['philosophical']}\n\n" \
               f"   - moralprinciples: {valuebliefs['moral_principles']}\n" \
               
               
             return value_belief
        except Exception as e:
          print(f"Error: {e}")
        return {"error": str(e)}


    def aspirations_dreams(self, aspirationsdream: AspirationsDreams) -> str:
        try:
            if aspirationsdream is None or aspirationsdream == '':
                return ''
            else:
             aspirations_dream = f"5. ASPIRATIONS AND DREAMS:\n" \
                            f"   - aspirations: {aspirationsdream['aspirations']}\n" \
                            f"   - dreams: {aspirationsdream['dreams']}\n" \
                            f"   - hope: {aspirationsdream['hope']} \n\n" \
                            f"   - achieve: {aspirationsdream['achieve']}  in the future\n\n" \
                            f"   - experience: {aspirationsdream['experience']} in the future\n\n" 

            return aspirations_dream
        except Exception as e:
          print(f"Error: {e}")
        return {"error": str(e)}

    def personal_growth(self, personalgrowth: PersonalGrowth) -> str:
        try:
            if personalgrowth is None or personalgrowth == '':
                return ''
            else:
             personal_growth = f"6. PERSONAL GROWTH AND CHANGE:\n" \
                    f"Reflect on the subject's journey of " \
                    f"   - personalgrowth: {personalgrowth['personal_growth']}\n" \
                    f"   - personalchange: {personalgrowth['personal_change']}\n" \
                    f"   - Community Roles: {personalgrowth['community_roles']}\n" \
                    f" Mention how they have evolved over time and any lessons learned. " \

            return personal_growth
        except Exception as e:
         print(f"Error: {e}")
        return {"error": str(e)}


    def contemplations(self, contemplations: Contemplations) -> str:
        try:
            if contemplations is None or contemplations == '':
                return ''
            else:
             contemplations = f"7. ASPIRATIONS AND DREAMS:\n" \
                f"Explore the subject's internal" \
                f"   - contemplations: {contemplations['contemplations']}\n" \
                f"   - conflicts: {contemplations['conflicts']}\n" \
                f"   - doubts: {contemplations['doubts']}\n" \
                f"   - regrets: {contemplations['regrets']}\n" \
                f"   - unresolved: {contemplations['unresolved']} tension.\n" \
                f"   - tension: {contemplations['tension']} .\n" \
            

            return contemplations
        except Exception as e:
         print(f"Error: {e}")
        return {"error": str(e)}


    def life_style(self, lifestyle: LifeStyle) -> str:
        try:
            if lifestyle is None or lifestyle == '':
                return ''
            else:
             life_style = f"8. CURRENT LIFESTYLE AND INTERESTS:\n" \
                f"Explore the subject's internal" \
                f"   - lifestyle: {lifestyle['lifestyle']}\n" \
                f"   - habits: {lifestyle['habits']}\n" \
                f"   - interests: {lifestyle['interests']}\n" \
                f"   - hobbies: {lifestyle['hobbies']}\n" \
                f"   - passions: {lifestyle['passions']} tension.\n" \
                f"   - routine activities: {lifestyle['routine_activities']} .\n"      

            return life_style
        except Exception as e:
         print(f"Error: {e}")
        return {"error": str(e)}

    def interacts_with_society(self, interactswithsociety: InteractsWithSociety) -> str:
        try:
            if interactswithsociety is None or interactswithsociety == '':
                return ''
            else:
             interacts_society = f"9. RELATIONSHIP WITH THE OUTER WORLD:\n" \
                f"Explore the subject's internal" \
                f"   - critical thoughts societal norms: {interactswithsociety['critical_thoughts']}\n" \
                f"   - culture: {interactswithsociety['culture']}\n" \
                f"   - global issues: {interactswithsociety['global_issues']}\n" \
                        

            return interacts_society
        except Exception as e:
         print(f"Error: {e}")
        return {"error": str(e)}

    def personal_anecdote(self, personalanecdote: PersonalAnecdote) -> str:
        try:
            if personalanecdote is None or personalanecdote == '':
                return ''
            else:
             personal_anecdote = f"10. PERSONAL ANECDOTES OR QUOTES:\n" \
                f"Explore the subject's internal" \
                f" - personal anecdote: {personalanecdote['personal_anecdote']}\n" \
                f" - personal quotes: {personalanecdote['personal_quotes']}\n" \
                f"  - global issues: {personalanecdote['global_issues']}\n" \
                f" - experiences: {personalanecdote['experiences']}\n" \
                f" - subject's perspective: {personalanecdote['subject_perspective']}\n" \
                        

            return personal_anecdote
        except Exception as e:
         print(f"Error: {e}")
        return {"error": str(e)}

    def conclusion(self, conclusion: Conclusion) -> str:
        try:
            if conclusion is None or conclusion == '':
                return ''
            else:
             conclusion = f"11. CONCLUSION:\n" \
                f"Explore the subject's internal" \
                f" - ongoing questions: {conclusion['ongoing_questions']}\n" \
                f" - dilemmas they are facing: {conclusion['dilemmas']}\n" \
                f" - what they are seeking or moving towards in their life journey: {conclusion['life_journey']}\n" \
                                       

            return conclusion
        except Exception as e:
          print(f"Error: {e}")
        return {"error": str(e)}



