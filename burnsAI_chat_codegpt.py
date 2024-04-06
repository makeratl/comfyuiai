from judini import CodeGPTPlus

class CodeGPTNode:
    FUNCTION = "execute"
    CATEGORY = "comfyUIAI"

    def __init__(self, api_key="YOUR_API_KEY", org_id="YOUR_ORG_ID", agent_id="YOUR_AGENT_ID"):
        self.codegpt = CodeGPTPlus(api_key=api_key, org_id=org_id)
        self.agent_id = agent_id

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "user_message": ("STRING", {
                    "multiline": True,
                    "default": "Favorite color"
                }),
                "api_key": ("STRING", {  # Added input type for api_key
                    "default": "YOUR_API_KEY"
                }),
                "org_id": ("STRING", {  # Added input type for org_id
                    "default": "YOUR_ORG_ID"
                }),
                "agent_id": ("STRING", {  # Added input type for agent_id
                    "default": "YOUR_AGENT_ID"
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ai_response",)

    def execute(self, user_message, api_key, org_id, agent_id):
        # Initialize CodeGPTPlus with the provided api_key, org_id, and agent_id
        self.codegpt = CodeGPTPlus(api_key=api_key, org_id=org_id)
        self.agent_id = agent_id

        messages = [{"role": "user", "content": user_message}]

        # Call the CodeGPTPlus API for a chat completion
        chat = self.codegpt.chat_completion(agent_id=self.agent_id, messages=messages)

        # Extract the AI response from the chat completion
        if chat:
            ai_response = chat
            return (ai_response,)
        else:
            return ("Failed to generate a response. Please try again.",)

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "comfyUIAI": CodeGPTNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "comfyUIAI": "CodeGPT Chat Node"
}