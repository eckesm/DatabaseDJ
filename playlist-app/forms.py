"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField
from wtforms.validators import InputRequired, Optional



class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField("Name", validators=[InputRequired(
        message="Please enter a name for the playlist.")])
    description = TextAreaField("Description", validators=[Optional()])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title=StringField("Title",validators=[InputRequired(message="Please enter the song name.")])
    artist=StringField("Artist",validators=[InputRequired(message="Please enter the name of the artist.")])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
