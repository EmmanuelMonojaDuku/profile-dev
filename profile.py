#profile.py

class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        print(f"👋 Hi, I’m {self.name}.")
        print(f"💻 My favorite programming language is {self.favorite_language}.")
        print(f"🎨 My hobby is {self.hobby}.")
        print(f"✨ Fun fact: {self.fun_fact}\n")

    def show_stack(self):
        print("🛠️ My Tech Stack includes:")
        for tool in self.tech_stack:
            print(f"   • {tool}")
        print()

    def github_link(self):
        return f"https://github.com/{self.github_username}"


# --- Example usage ---
if __name__ == "__main__":
    my_profile = Profile(
        name="Emmanuel Monoja Duku",
        favorite_language="Python",
        hobby="Exploring networking and coding projects",
        tech_stack=["Python","React", "Node.js", "MySQL"],
        github_username="your-github-username",  # Replace with your real GitHub username
        fun_fact="I can debug code faster with music on! 🎵"
    )

    my_profile.introduce()
    my_profile.show_stack()
    print("🔗 GitHub:", my_profile.github_link())
