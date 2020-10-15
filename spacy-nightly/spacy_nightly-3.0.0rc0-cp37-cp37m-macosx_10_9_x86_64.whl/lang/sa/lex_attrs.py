from ...attrs import LIKE_NUM

# reference 1: https://en.wikibooks.org/wiki/Sanskrit/Numbers

_num_words = [
    "एकः",
    "द्वौ",
    "त्रयः",
    "चत्वारः",
    "पञ्च",
    "षट्",
    "सप्त",
    "अष्ट",
    "नव",
    "दश",
    "एकादश",
    "द्वादश",
    "त्रयोदश",
    "चतुर्दश",
    "पञ्चदश",
    "षोडश",
    "सप्तदश",
    "अष्टादश",
    "एकान्नविंशति",
    "विंशति",
    "एकाविंशति",
    "द्वाविंशति",
    "त्रयोविंशति",
    "चतुर्विंशति",
    "पञ्चविंशति",
    "षड्विंशति",
    "सप्तविंशति",
    "अष्टाविंशति",
    "एकान्नत्रिंशत्",
    "त्रिंशत्",
    "एकत्रिंशत्",
    "द्वात्रिंशत्",
    "त्रयत्रिंशत्",
    "चतुस्त्रिंशत्",
    "पञ्चत्रिंशत्",
    "षट्त्रिंशत्",
    "सप्तत्रिंशत्",
    "अष्टात्रिंशत्",
    "एकोनचत्वारिंशत्",
    "चत्वारिंशत्",
    "एकचत्वारिंशत्",
    "द्वाचत्वारिंशत्",
    "त्रयश्चत्वारिंशत्",
    "चतुश्चत्वारिंशत्",
    "पञ्चचत्वारिंशत्",
    "षट्चत्वारिंशत्",
    "सप्तचत्वारिंशत्",
    "अष्टाचत्वारिंशत्",
    "एकोनपञ्चाशत्",
    "पञ्चाशत्",
    "एकपञ्चाशत्",
    "द्विपञ्चाशत्",
    "त्रिपञ्चाशत्",
    "चतुःपञ्चाशत्",
    "पञ्चपञ्चाशत्",
    "षट्पञ्चाशत्",
    "सप्तपञ्चाशत्",
    "अष्टपञ्चाशत्",
    "एकोनषष्ठिः",
    "षष्ठिः",
    "एकषष्ठिः",
    "द्विषष्ठिः",
    "त्रिषष्ठिः",
    "चतुःषष्ठिः",
    "पञ्चषष्ठिः",
    "षट्षष्ठिः",
    "सप्तषष्ठिः",
    "अष्टषष्ठिः",
    "एकोनसप्ततिः",
    "सप्ततिः",
    "एकसप्ततिः",
    "द्विसप्ततिः",
    "त्रिसप्ततिः",
    "चतुःसप्ततिः",
    "पञ्चसप्ततिः",
    "षट्सप्ततिः",
    "सप्तसप्ततिः",
    "अष्टसप्ततिः",
    "एकोनाशीतिः",
    "अशीतिः",
    "एकाशीतिः",
    "द्वशीतिः",
    "त्र्यशीतिः",
    "चतुरशीतिः",
    "पञ्चाशीतिः",
    "षडशीतिः",
    "सप्ताशीतिः",
    "अष्टाशीतिः",
    "एकोननवतिः",
    "नवतिः",
    "एकनवतिः",
    "द्विनवतिः",
    "त्रिनवतिः",
    "चतुर्नवतिः",
    "पञ्चनवतिः",
    "षण्णवतिः",
    "सप्तनवतिः",
    "अष्टनवतिः",
    "एकोनशतम्",
    "शतम्",
]


def like_num(text):
    """
    Check if text resembles a number
    """
    if text.startswith(("+", "-", "±", "~")):
        text = text[1:]
    text = text.replace(",", "").replace(".", "")
    if text.isdigit():
        return True
    if text.count("/") == 1:
        num, denom = text.split("/")
        if num.isdigit() and denom.isdigit():
            return True
    if text in _num_words:
        return True
    return False


LEX_ATTRS = {LIKE_NUM: like_num}
