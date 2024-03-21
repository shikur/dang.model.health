

from typing import List
from models.identityNarrativeBaseModel import IdentityNarrative
from models.identityNarrativeModel import AspirationsDreams, BasicInformation, Conclusion, Contemplations, IdentityNarrativeInterface, InteractsWithSociety , KeyRoles, CoreChallenges, LifeEvents, LifeStyle, PersonalAnecdote, ValueBeliefs




def concated_inputNarrative(details: List[IdentityNarrative]):
    print(details)
    identity_Narrative = IdentityNarrative()
    detail_list=[]
    life_events_str ="" 
    key_roles_str = ''
    core_challenges_str = ''
    value_beliefs_str =''
    personal_growth_str = ''
    contemplations_str= ''
    interacts_with_society_str = ''
    conclusion_str = ''
    personal_anecdote_str= ''
    aspirations_dreams_str = ''
    life_style_str = ''
    
    
    try:
       for detail in details:
                   
           if detail.basic_information:
               identity_Narrative.update_basic_information(detail.basic_information) 
               basic_information_str = BasicInformation(age=detail.basic_information.age, 
                                                        location=detail.basic_information.location, 
                                                        racial_background=detail.basic_information.racial_background) 
           if detail.key_roles:
               identity_Narrative.update_core_challenges(detail.core_challenges) 
               key_roles_str = KeyRoles(parental_role=detail.key_roles.parental_role, 
                                        professional_role=detail.key_roles.professional_role, 
                                        community_roles=detail.key_roles.community_roles ) 
           if detail.core_challenges:
               identity_Narrative.update_key_roles(detail.key_roles)
               core_challenges_str = CoreChallenges(challenges=detail.core_challenges.challenges, 
                                                    conflicts=detail.core_challenges.conflicts,
                                                    psychological_struggles=detail.core_challenges.psychological_struggles, 
                                                    emotional=detail.core_challenges.emotional, 
                                                    circumstances=detail.core_challenges.circumstances) 
            
           if detail.life_events is not None:
               identity_Narrative.update_life_events(detail.life_events)
               life_events_str = LifeEvents( life_events=detail.life_events.life_events, turning_points= detail.life_events.turning_points)
           
               
           if detail.value_beliefs:
               identity_Narrative.update_value_beliefs(detail.value_beliefs)
               value_beliefs_str = ValueBeliefs(keyvalues=detail.value_beliefs.keyvalues, 
                                            professional_role=detail.value_beliefs.professional_role, 
                                            philosophical=detail.value_beliefs.philosophical,
                                            moral_principles=detail.value_beliefs.moral_principles) 
               
           if detail.personal_growth:
               identity_Narrative.update_personal_growth(detail.personal_growth)
               personal_growth_str = CoreChallenges( personal_growth=detail.personal_growth.personal_growth, 
                                                    personal_change=detail.personal_growth.personal_change,
                                                    psychological_struggles=detail.personal_growth.psychological_struggles)

               
           if detail.aspirations_dreams:
               identity_Narrative.update_aspirations_dreams(detail.aspirations_dreams)
               aspirations_dreams_str = AspirationsDreams( aspirations=detail.aspirations_dreams.aspirations, 
                                                          dreams=detail.aspirations_dreams.dreams,
                                                          hope=detail.aspirations_dreams.hope,                            
                                                          achieve=detail.aspirations_dreams.achieve)
           
               
           if detail.contemplations:
               identity_Narrative.update_contemplations_dreams(detail.contemplations)
               contemplations_str = Contemplations(contemplations=detail.contemplations.aspirations, 
                                                          conflicts=detail.contemplations.conflicts,
                                                          doubts=detail.contemplations.doubts,                            
                                                          unresolved=detail.contemplations.unresolved,
                                                          tension=detail.contemplations.tension)
                
           if detail.life_style:
               identity_Narrative.update_life_style(detail.life_style)
               life_style_str = LifeStyle(lifestyle=detail.life_style.aspirlifestyleations, 
                                                          habits=detail.life_style.habits,
                                                          interests=detail.life_style.interests,                            
                                                          hobbies=detail.life_style.hobbies,
                                                          passions=detail.life_style.passions,
                                                          unresolved=detail.life_style.unresolved,
                                                          routine_activities=detail.life_style.routine_activities)  
               
           if detail.interacts_with_society:
               identity_Narrative.update_interacts_with_society(detail.interacts_with_society)
               interacts_with_society_str = InteractsWithSociety(critical_thoughts=detail.interacts_with_society.critical_thoughts, 
                                                          culture=detail.interacts_with_society.culture,
                                                          global_issues=detail.interacts_with_society.global_issues)   
               
           if detail.personal_anecdote:
               identity_Narrative.update_personal_anecdote(detail.personal_anecdote)
               personal_anecdote_str = PersonalAnecdote(personal_anecdote=detail.personal_anecdote.personal_anecdote, 
                                                          personal_quotes=detail.personal_anecdote.personal_quotes,
                                                          global_issues=detail.personal_anecdote.global_issues,
                                                          experiences=detail.personal_anecdote.experiences,
                                                          expersubject_perspective=detail.personal_anecdote.subject_perspective
                                                          )            
           if detail.conclusion:
               identity_Narrative.update_conclusion(detail.conclusion)
               conclusion_str = Conclusion(ongoing_questions=detail.conclusion.ongoing_questions, 
                                                          dilemmas=detail.conclusion.dilemmas,
                                                          life_journey=detail.conclusion.life_journey)   
               
           narrative_interface = IdentityNarrativeInterface()    
           final_input_narrative = f"{narrative_interface.basic_information(basic_information_str)if basic_information_str is not None else ''}\n" \
                       f"{narrative_interface.key_roles(key_roles_str) if key_roles_str is not None else ''} \n" \
                       f"{narrative_interface.core_challenges(core_challenges_str) if core_challenges_str is not None else ''} " \
                       f"{narrative_interface.life_events(life_events_str) if life_events_str is not None else ''} \n" \
                       f"{narrative_interface.value_beliefs(value_beliefs_str) if value_beliefs_str is not None else ''} \n" \
                       f"{narrative_interface.personal_growth(personal_growth_str) if personal_growth_str is not None else ''} \n" \
                       f"{narrative_interface.aspirations_dreams(aspirations_dreams_str) if aspirations_dreams_str is not None else ''} \n"\
                       f"{narrative_interface.contemplations(contemplations_str) if contemplations_str is not None else ''} \n"\
                       f"{narrative_interface.life_style(life_style_str) if life_style_str is not None else ''} \n"\
                       f"{narrative_interface.interacts_with_society(interacts_with_society_str) if interacts_with_society_str is not None else ''} \n"\
                       f"{narrative_interface.personal_anecdote(personal_anecdote_str) if personal_anecdote_str is not None else ''} \n"\
                       f"{narrative_interface.conclusion(conclusion_str)} \n" 
                           
           detail_list.append(final_input_narrative)           
           return detail_list
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}