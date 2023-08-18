from survey import AnonymousSurvey

question = "What languages did you learn?"
lang_survey = AnonymousSurvey(question)

lang_survey.show_question()
print("Enter 'q' to quit\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    lang_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
lang_survey.show_results()