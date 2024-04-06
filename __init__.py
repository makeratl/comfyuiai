from .burnsAI_chat_codegpt import CodeGPTNode

NODE_CLASS_MAPPINGS = { "burnsAI": CodeGPTNode }

NODE_DISPLAY_NAME_MAPPINGS = { "burnsAI": "CodeGPT Chat Node" }

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
