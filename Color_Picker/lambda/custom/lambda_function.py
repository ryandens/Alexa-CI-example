"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------
from Color_Picker.src.helpers import build_speechlet_response, build_response


# --------------- Functions that control the skill's behavior ------------------
from Color_Picker.src.skill_behavior import get_welcome_response, handle_session_end_request, \
    create_favorite_color_attributes, set_color_in_session, get_color_from_session

# --------------- Events ------------------
from Color_Picker.src.events import on_session_started, on_launch, on_intent, on_session_ended

# --------------- Main handler ------------------

from Color_Picker.src.main import lambda_handler
