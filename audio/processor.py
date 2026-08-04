import os
import tempfile

from audio.effects import (
    apply_reverb,
    apply_tunnel,  
    apply_radio,
    apply_eq
)


# This function applies the selected audio effects to the input audio file and saves the final output to the same file.
def apply_effects(input_file, effects):

    # Create a temporary file in the same directory as the input file
    def create_temp_file():
        return tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False,
        ).name
        
       
    current_file = input_file

    for effect in effects:

        temp_file = create_temp_file()

        # Apply the selected effect to the current audio file and save it to a temporary file
        if effect == "reverb":
            apply_reverb(
                current_file,
                temp_file
            )

            current_file = temp_file

        elif effect == "tunnel":
            apply_tunnel(
                current_file,
                temp_file
            )

            current_file = temp_file

        elif effect == "radio":
            apply_radio(
                current_file,
                temp_file
            )

            current_file = temp_file

        elif effect == "eq":
            apply_eq(
                current_file,
                temp_file
            )

            current_file = temp_file

    # Replace the saved audio file with the final effected audio if it has changed
    if current_file != input_file:
        os.replace(
            current_file,
            input_file
        )

    return input_file

