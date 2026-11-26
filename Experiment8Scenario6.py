with open("news_feed.txt", "r") as file:
    headlines = file.readlines()

total = len(headlines)

print("Total Headlines:", total)

top_stories = headlines[:2]

with open("top_stories.txt", "w") as file:
    file.writelines(top_stories)

print("First Two Headlines:")
for headline in top_stories:
    print(headline.strip())

print("Top stories saved successfully!")
