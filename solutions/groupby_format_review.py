def format_review(review):
    return dict([line.strip('\n').split(": ", 1) for line in review])