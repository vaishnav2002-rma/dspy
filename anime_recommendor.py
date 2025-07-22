import dspy

class AnimeRecommendor(dspy.Predict):
    def __init__(self):
        super().__init__(signature="genre -> str")

    def forward(self, genre:str) -> str:
        anime_dict = {
            "action": "Solo Levelling",
            "comedy": "Spy Family",
            "adventure": "One Piece",
            "sci-fi": "Dr. Stone"
        }
        return anime_dict.get(genre.lower(), "No recommendation")
    
anime_recommendor = AnimeRecommendor()
print(anime_recommendor(genre="adventure"))