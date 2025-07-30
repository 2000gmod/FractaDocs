from pygments.style import Style
from pygments.token import Keyword, Comment, Name, String, Number, Operator, Punctuation, Generic, Text

class FractaStyle(Style):
    default_style = ""
    background_color = "#ffffff"
    
    styles = {
        Comment:              "italic #888888",
        Keyword:              "bold #0077aa",
        Name:                 "#0000aa",
        Operator:             "#aa00aa",
        String:               "#dd1144",
        Number:               "#009999",
        Punctuation:          "#333333",
        Text:                 "#000000",
    }
