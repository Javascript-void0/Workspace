from pytube import YouTube

link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley'
# link = input('Link: ')
yt = YouTube(link)
print(f'Title: {yt.title}')
print(f'Views: {yt.views} views')
print(f'Length: {round(yt.length / 60,2)}m')
print(f'Channel: {yt.author}')
