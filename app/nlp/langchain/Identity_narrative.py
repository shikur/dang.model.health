# Generate
import string


def generate_subject_introduction(age, racial_background, location, parental_role, professional_role, community_roles):
    """
    Generates an introduction to the subject based on the provided details.
    """
    prompt = f"Introduction to the Subject:\n\n" \
            f"Generate a detailed introduction for a subject based on the following criteria:\n\n" \
            f"1. Basic Information:\n" \
            f"   - Age: {age}\n" \
            f"   - Racial or Ethnic Background: {racial_background}\n" \
            f"   - Geographical Location: {location}\n\n" \
            f"2. Key Roles in Life:\n" \
            f"   - Parental Role: {parental_role}\n" \
            f"   - Professional Role: {professional_role}\n" \
            f"   - Community Roles: {community_roles}\n\n" \
            "This introduction should offer a comprehensive overview of the subject's demographic background and their roles in life, providing insights into their daily responsibilities and contributions."
            
    introduction = llm.generate(prompt)
    return introduction


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


def core_challenges(age: string, racial_background: string, location: string):
    core_challenge =    f"3. Describe the central challenges or conflicts the subject faces:\n" \
                        f"   - challenges: {challenges}\n" \
                        f"   - conflicts: {conflicts}\n" \
                        f"   - emotional: {emotional}\n" \
                        f"   - psychological struggles: {psychological_struggles}\n" \
                        f"   - circumstances: {circumstances}\n" \
                        f"   - psychological struggles: {psychological_struggles}\n\n" 

    return core_challenge

def value_beliefs(parental_role: string, professional_role: string, community_roles: string):
    value_belief =f"4. VALUES AND BELIEFS:\n" \
               f"   - keyvalues: {parental_role}\n" \
               f"   - Professional: {professional_role}\n" \
               f"   - philosophical: {community_roles}\n\n" \
               f"   - moralprinciples: {moral_principles}\n" \
               f"   - philosophical: {community_roles}\n\n" \
               
    return value_belief

def lifeevents(parental_role: string, professional_role: string, community_roles: string):
    life_events =f"4. LIFE EVENTS:\n" \
               f"   - life events: {parental_role}\n" \
               f"   - turning points: {professional_role}\n" \
               f"   that have had a profound impact on the subject's identity and life path."
              
               
    return life_events


def aspirations_dreams(age: string, racial_background: string, location: string):
    aspirations_dream = f"5. ASPIRATIONS AND DREAMS:\n" \
                        f"   - aspirations: {age}\n" \
                        f"   - dreams: {racial_background}\n" \
                        f"   - hope_achieve: what they hope to {achieve} or {experience} in the future\n\n" 

    return aspirations_dream

def personalgrowth(parental_role: string, professional_role: string, community_roles: string):
    personal_growth =f"6. PERSONAL GROWTH AND CHANGE:\n" \
               f"Reflect on the subject's journey of " \
               f"   - personalgrowth: {parental_role}\n" \
               f"   - personalchange: {personal_change}\n" \
               f"   - Community Roles: {community_roles}\n" \
               f" Mention how they have evolved over time and any lessons learned. " \

    return personal_growth

def contemplations(parental_role: string, professional_role: string, community_roles: string):
    contemplations =f"7. ASPIRATIONS AND DREAMS:\n" \
               f"Explore the subject's internal" \
               f"   - contemplations: {parental_role}\n" \
               f"   - conflicts: {personal_change}\n" \
               f"   - doubts: {community_roles}\n" \
               f"   - regrets: {community_roles}\n" \
               f"   - unresolved: {unresolved} tension.\n" \
               f"   - tension: {unresolved} .\n" \
         

    return contemplations




def lifestyle(parental_role: string, professional_role: string, community_roles: string):
    life_style =f"8. CURRENT LIFESTYLE AND INTERESTS:\n" \
               f"Explore the subject's internal" \
               f"   - lifestyle: {parental_role}\n" \
               f"   - habits: {personal_change}\n" \
               f"   - interests: {community_roles}\n" \
               f"   - hobbies: {community_roles}\n" \
               f"   - passions: {unresolved} tension.\n" \
               f"   - routine activities: {unresolved} .\n"      

    return life_style

def interacts_with_society(parental_role: string, professional_role: string, community_roles: string):
    interacts_society =f"9. RELATIONSHIP WITH THE OUTER WORLD:\n" \
               f"Explore the subject's internal" \
               f"   - critical thoughts societal norms: {critical_thoughts}\n" \
               f"   - culture: {personal_change}\n" \
               f"   - global issues: {community_roles}\n" \
                     

    return interacts_society

def personal_anecdote(parental_role: string, professional_role: string, community_roles: string):
    personal_anecdote =f"10. PERSONAL ANECDOTES OR QUOTES:\n" \
               f"Explore the subject's internal" \
               f" - personal anecdote: {critical_thoughts}\n" \
               f" - personal quotes: {personal_change}\n" \
               f"  - global issues: {community_roles}\n" \
               f" - experiences: {community_roles}\n" \
               f" - subject's perspective: {community_roles}\n" \
                     

    return personal_anecdote

def conclusion(parental_role: string, professional_role: string, community_roles: string):
    conclusion =f"11. CONCLUSION:\n" \
               f"Explore the subject's internal" \
               f" - ongoing questions: {ongoing_questions}\n" \
               f" - dilemmas they are facing: {dilemmas}\n" \
               f" - what they are seeking or moving towards in their life journey: {life_journey}\n" \
                                    

    return conclusion


    