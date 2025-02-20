def count_words_in_md_files():
    # Open the GitHub Actions step summary file
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as summary:
        summary.write("## Word Counts in Markdown Files\n")

        # Walk through the repository directory to find all .md files
        for root, dirs, files in os.walk("."):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    
                    # Open the markdown file and count the words
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        word_count = len(content.split())
                        
                    # Append the result to the step summary
                    summary.write(f"File: {file_path} has {word_count} words\n")

if __name__ == "__main__":
    count_words_in_md_files()
