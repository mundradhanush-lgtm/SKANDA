from backend.ai.router import ai_request
from backend.history.history_manager import new_conversation_file, save_message
from backend.history.history_classifier import classification
from backend.history.history_retriever import search_history
from backend.history.semantic_search.semantic_history_manager import new_semantic_conversation_file, save_semantic_message
from backend.history.semantic_search.router_of_semantic_search import create_user_embedding, create_assistant_embedding
from backend.history.semantic_search.semantic_history_retriever import search_semantic_history
from backend.computer.control.computer_intent_classifier import input_classification
from backend.computer.control.computer_controller import computer_control

def main():
    file_path=None
    while True:
        user_input=str(input("You: "))
        if(user_input=="exit"):
            break

        if(file_path==None):
            file_path=new_conversation_file(user_input)
            semantic_file_path=new_semantic_conversation_file(file_path)

        if(user_input!="exit"):
            user_input_decision=input_classification(user_input)
            if(user_input_decision==None or "normal chat" in user_input_decision):
                classification_result=classification(user_input)
                save_message(file_path, {"role": "user", "content": user_input})
                user_embedding=create_user_embedding(user_input)
                save_semantic_message(semantic_file_path, {"role": "user", "content": user_embedding})

                if(classification_result==None or "semantic history needed" in classification_result):
                    retrieved_relevent_history=search_semantic_history(user_input)
                
                elif("keyword history needed" in classification_result):
                    retrieved_relevent_history=search_history(user_input)

                elif(classification_result=="history not needed"):
                    retrieved_relevent_history=None

                else:
                    retrieved_relevent_history=None

                try:
                    response=ai_request(user_input, retrieved_relevent_history)
                    print(f"SKANDA: {response}")
                    assistant_embedding=create_assistant_embedding(response)
                    save_message(file_path, {"role": "assistant", "content": response})
                    save_semantic_message(semantic_file_path, {"role": "assistant", "content": assistant_embedding})
                except RuntimeError:
                    print("All AI providers failed.")
            elif("computer control" in user_input_decision):
                decision=computer_control(user_input)
                print(decision)

if(__name__=="__main__"):
    main()