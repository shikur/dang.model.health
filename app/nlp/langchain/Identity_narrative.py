# Generate
import string

def basicInformation(age: string, racial_background: string, location: string):
    basic_information = f"1. Basic Information:\n" \
                 f"   - Age: {age}\n" \
                 f"   - Racial or Ethnic Background: {racial_background}\n" \
                 f"   - Geographical Location: {location}\n\n" 

    return basic_information

def keyRoles(parental_role: string, professional_role: string, community_roles: string):
    key_roles =f"2. Key Roles in Life:\n" \
               f"   - Parental Role: {parental_role}\n" \
               f"   - Professional Role: {professional_role}\n" \
               f"   - Community Roles: {community_roles}\n\n" \

    return key_roles


def core_challenges(challenges: string, conflicts: string, emotional: string, psychological_struggles: string, circumstances: string):
    core_challenge =    f"3. Describe the central challenges or conflicts the subject faces:\n" \
                        f"   - challenges: {challenges}\n" \
                        f"   - conflicts: {conflicts}\n" \
                        f"   - emotional: {emotional}\n" \
                        f"   - psychological struggles: {psychological_struggles}\n" \
                        f"   - circumstances: {circumstances}\n" \
                        f"   - psychological struggles: {psychological_struggles}\n\n" 

    return core_challenge

def value_beliefs(keyvalues:string, professional_role: string, philosophical: string, moral_principles: string ):
    value_belief =f"4. VALUES AND BELIEFS:\n" \
               f"   - keyvalues: {keyvalues}\n" \
               f"   - Professional: {professional_role}\n" \
               f"   - philosophical: {philosophical}\n\n" \
               f"   - moralprinciples: {moral_principles}\n" \
              
               
    return value_belief

def life_events(parental_role: string, professional_role: string, community_roles: string):
    life_events =f"4. LIFE EVENTS:\n" \
               f"   - life events: {parental_role}\n" \
               f"   - turning points: {professional_role}\n" \
               f"   that have had a profound impact on the subject's identity and life path."
              
               
    return life_events


def aspirations_dreams(aspirations: string, dreams: string, achieve: string, experience: string):
    aspirations_dream = f"5. ASPIRATIONS AND DREAMS:\n" \
                        f"   - aspirations: {aspirations}\n" \
                        f"   - dreams: {dreams}\n" \
                        f"   - hope_achieve: what they hope to {achieve} or {experience} in the future\n\n" 

    return aspirations_dream

def personal_growth(parental_role: string, personal_change: string, community_roles: string):
    personal_growth =f"6. PERSONAL GROWTH AND CHANGE:\n" \
               f"Reflect on the subject's journey of " \
               f"   - personalgrowth: {parental_role}\n" \
               f"   - personalchange: {personal_change}\n" \
               f"   - Community Roles: {community_roles}\n" \
               f" Mention how they have evolved over time and any lessons learned. " \

    return personal_growth

def contemplations(contemplations: string, conflicts: string, doubts: string, regrets: string, unresolved: string, tension: string ):
    contemplations =f"7. ASPIRATIONS AND DREAMS:\n" \
               f"Explore the subject's internal" \
               f"   - contemplations: {contemplations }\n" \
               f"   - conflicts: {conflicts}\n" \
               f"   - doubts: {doubts}\n" \
               f"   - regrets: {regrets}\n" \
               f"   - unresolved: {unresolved} tension.\n" \
               f"   - tension: {tension} .\n" \
         

    return contemplations




def life_style(lifestyle: string, habits: string, interests: string, hobbies: string, passions: string, routine_activities: string):
    life_style =f"8. CURRENT LIFESTYLE AND INTERESTS:\n" \
               f"Explore the subject's internal" \
               f"   - lifestyle: {lifestyle}\n" \
               f"   - habits: {habits}\n" \
               f"   - interests: {interests}\n" \
               f"   - hobbies: {hobbies}\n" \
               f"   - passions: {passions} tension.\n" \
               f"   - routine activities: {routine_activities} .\n"      

    return life_style

def interacts_with_society(critical_thought: string, culture: string, global_issues: string):
    interacts_society =f"9. RELATIONSHIP WITH THE OUTER WORLD:\n" \
               f"Explore the subject's internal" \
               f"   - critical thoughts societal norms: {critical_thought}\n" \
               f"   - culture: {culture}\n" \
               f"   - global issues: {global_issues}\n" \
                     

    return interacts_society

def personal_anecdote(personal_anecdote: string, personal_quotes: string, global_issues: string, experience: string, subject_perspective: string):
    personal_anecdote =f"10. PERSONAL ANECDOTES OR QUOTES:\n" \
               f"Explore the subject's internal" \
               f" - personal anecdote: {personal_anecdote}\n" \
               f" - personal quotes: {personal_quotes}\n" \
               f"  - global issues: { global_issues}\n" \
               f" - experiences: {experience}\n" \
               f" - subject's perspective: {subject_perspective}\n" \
                     

    return personal_anecdote

def conclusion(ongoing_question: string, dilemmas: string, life_journey: string):
    conclusion =f"11. CONCLUSION:\n" \
               f"Explore the subject's internal" \
               f" - ongoing questions: {ongoing_question}\n" \
               f" - dilemmas they are facing: {dilemmas}\n" \
               f" - what they are seeking or moving towards in their life journey: {life_journey}\n" \
                                    

    return conclusion


