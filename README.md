# Password Generator

### Features:
- Creates strong and random passwords using a mix of letters, digits, and special characters.
- Allows users to specify the desired length of the password.

### Installation and Run Instructions:
Clone the repo and run it in any IDE which supports Python.

### Interesting Parts during the Build Process:
Creating the logic to generate random and secure passwords was interesting. I used Python's `random` and `string` modules to include letters, digits, and special characters. The `random.shuffle()` method ensures that the generated passwords are well-randomized.

### Difficulties Faced and Solutions:
Ensuring that the generated passwords were truly random and secure. Using `random.shuffle()` both before selecting characters and after constructing the password helped enhance the randomness. This step was crucial to meet the security standards expected of a good password generator.

### Screenshots:
<img src="https://github.com/shubhhh19/Password-Generator/assets/126296317/80fe59e7-5fc6-4578-ad0c-08a04b336452" width="500" height="200">
