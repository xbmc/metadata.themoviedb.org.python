import sys
import regex as re

def sanitize_title(title, year, trimPrefix=False, trimSuffix=False, trimSpecial=False):
    """
    Attempts to extract film title and year from messy file/directory names.
    trimPrefix and trimSuffix each trim a single whitespace-delimeted word. Don't use both at the same time.
    trimSpecial removes certain 'special' words and phrases like "Director's Cut" or "Special Edition"
    """

    year = _year_from_title(title, year)

    #words that essentially never appear to the left of the actual title
    splitwords = ["720p", "1080p", "2160p"]
    if _valid_year(year):
         splitwords.insert(0, str(year))

    remainder = ""
    for i in splitwords:
        s = title.split(i)
        title = s[0]
        if len(s) > 1:
            remainder += s[1]

    remainder = _strip_separators(remainder).lower()
    preserve, remainder = _extract_special_words(remainder)
    title = _strip_separators(title)

    if trimPrefix:
        trimmedTitle = title.partition(" ")[2]
        special, remainder = _extract_special_words(trimmedTitle)
        x = re.search("[a-zA-Z]+", remainder) #Make sure we're not trimming it so far that special words are all that's left!
        if (x is not None):
            if len(remainder) > 3:
                title = trimmedTitle

    if trimSuffix:
        #don't let it get trimmed all the way down to one word unless you have a valid date to go along with it
        if (len(title.split(" ")) > 2) or ((len(title.split(" ")) > 1) and _valid_year(year)):
            title = title.rsplit(" ", 1)[0]

    if trimSpecial:
        special, title = _extract_special_words(title)
        return title.title(), year
    else:
        return title.title() + preserve, year

def _year_from_title(title, year):
    """
    Attempts to extract year from title. If a valid year was provided by a higher layer, it doesn't overrule it
    """

    #if a higher layer passed in a year that looks legit, just use that
    if (year is not None):
        if _valid_year(year):
            return int(year)

    #if there's a date in the canonical parenthesized format, use that
    x = re.search("\([0-9][0-9][0-9][0-9]\)", title)
    if (x is not None):
        x = x.group().replace("(","").replace(")","")
        if _valid_year(x):
            return int(x)

    #otherwise find the first 4-digit number that looks legit
    x = re.findall("[^0-9]([0-9][0-9][0-9][0-9])[^0-9]", title, overlapped=True)
    for n in x:
        if _valid_year(n):
            return int(n)

    return 0

def _valid_year(year):
     return ((int(year) > 1920) and (int(year) < 2150)) #Make sure to update this if you're still using it in 2150

def _strip_separators(s):
    s = re.sub("[\(\)\[\]\{\}\.]", " ", s)
    s = re.sub("\s+", " ", s)
    return s

def _extract_special_words(s):
    """
    Extract special words and phrases like "Director's Cut" or "Disc 2" that aren't technically part of the title, but should be preserved
    """

    special = ""
    s = s.lower()

    for i in ["cut", "edition", "edit", "version", "collection"]:
        x = re.search("((:|-)\s?[a-z0-9\'-]+\s)*([a-z\'-]+\s)" + i , s)
        if (x is not None):
            special += (x.group() + " ")
            s = re.sub(x.group(), "", s)

    for i in ["remastered", "unrated", "uncensored", "criterion"]:
        x = re.search(i, s)
        if (x is not None):
            special += (x.group() + " ")
            s = re.sub(x.group(), "", s)

    x = re.search("(disc|disk|part|volume)\s*([0-9]+|one|two|three|four|five|six|seven|eight|nine|ten)", s)
    if (x is not None):
        special += (x.group() + " ")
        s = re.sub(x.group(), "", s)

    return special, s

def main(argv):

    title = argv[0]
    year = 0

    if len(argv) > 1:
        year = int(argv[1])

    title, year = sanitize_title(title, year)

    print(str(year) + ": " + title)

if __name__ == "__main__":
   main(sys.argv[1:])
