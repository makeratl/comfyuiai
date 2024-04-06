from .chat_codegpt import CodeGPTNode

NODE_CLASS_MAPPINGS = { "comfyUIAI": CodeGPTNode }

NODE_DISPLAY_NAME_MAPPINGS = { "comfyUIAI": "CodeGPT Chat Node" }

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
