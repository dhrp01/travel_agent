from google.adk.tools.tool_context import ToolContext

def get_user_input(tool_context: ToolContext) -> str:
    """Get user input based on a prompt.

    Returns:
        str: The user's input.
    """
    tool_confirmation = tool_context.tool_confirmation
    if not tool_confirmation:
        tool_context.request_confirmation(
            hint="""
            Please provide the confirmation and the expected travel month to 
            better suggest the travel essentials.
            """,
            payload={"month": "December"},
        )

        return "Waiting for user input..."
    
    return tool_confirmation.payload.get("month", "December")
