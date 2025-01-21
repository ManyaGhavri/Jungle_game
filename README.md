# 🎮 Jungle Game

Welcome to **Jungle Game**, a simple text-based adventure game where you make choices to navigate through a jungle. Each decision you make affects your outcome. Your goal is to find the right path and survive the challenges of the jungle.

## 🚀  How to Play

1. Run the Python script.
2. Follow the prompts and make your choices by entering `1` or `2` when prompted.
3. Depending on your choices, you'll either win, lose, or encounter various game-ending scenarios.

### 🔮 Example Gameplay:
```
Welcome to Jungle Game
Enter choice 1 for left and 2 for right: 1
Now you have further two options where to go:
Press 1 to go further left
Press 2 to go right: 2
Oh no! You are eaten by an animal. Game Over!
```

## 🔮 Code Explanation

The game consists of a series of conditional statements (`if-elif-else`) that guide the player through different scenarios based on their input.

### ✨ Main Features:
- **Choice-driven gameplay**: Players decide which path to take by entering `1` or `2`.
- **Multiple endings**: The game has different outcomes based on the player's choices.

### Code Snippet:
```python
print('Welcome to Jungle Game')
choice1 = input('Enter choice 1 for left and 2 for right: ')
if choice1 == '1':
    print('Now you have further two options where to go:')
    print('Press 1 to go further left')
    print('Press 2 to go right')
    choice2 = input('Enter choice from 1 or 2: ')
    if choice2 == '1':
        print('Oops! You fell in a pit. Game Over!')
    elif choice2 == '2':
        print('Oh no! You are eaten by an animal. Game Over!')
    else:
        print('Invalid choice. Game Over!')
elif choice1 == '2':
    print('Now you have further two options to go:')
    print('Press 1 for left')
    print('Press 2 for right')
    choice4 = input('Enter choice 1 for left and 2 for right: ')
    if choice4 == '1':
        print('Game Over!')
    elif choice4 == '2':
        print('Help! You win!')
    else:
        print('Invalid choice. Game Over!')
else:
    print('Invalid choice. Game Over!')
```

## 🎮 Requirements

- Python 3.x
- Ensure Python is correctly installed on your system.

## 🚀 How to Run the Game

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/jungle-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd jungle-game
   ```
3. Run the Python script:
   ```bash
   python jungle_game.py
   ```

## 🤝 Contributing

Contributions are welcome! If you find a bug or have a suggestion for improvement, feel free to fork the repository and submit a pull request.

### 👥Steps to Contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with a descriptive message.
4. Push the changes to your forked repository.
5. Open a pull request to the main branch of this repository.
   
## 💬Acknowledgments

Thank you for playing Jungle Game! We hope you enjoyed this simple adventure.

## 👩‍💻Developer
- **Manya Ghavri**
- 🌐 [GitHub Profile](https://github.com/ManyaGhavri)  
- 📧 Email: manyaghavri3211@gmail.com
- 🔗 LinkedIn: [Linkedin_link](https://www.linkedin.com/in/manya-ghavri-b00773310/)


