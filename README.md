# FLAVEL

FLAVEL is a Flask application with minimal ideas borrowed from Laravel, combining the simplicity and elegance of Flask with some convenient features inspired by Laravel.

## Features

- **Artisan Commands**: FLAVEL includes an `artisan` command-line tool with the following commands:
  - `install_requirements`: Install dependencies from requirements.txt
  - `serve`: Start the Flask development server
  - `shell`: Open a Python shell with Flask context
  - `test`: Run unit tests
  - `lint`: Lint the code
  - `clean`: Clean up compiled Python files and __pycache__ directories
  - `make:controller <name>`: Create a new controller
  - `make:model <name>`: Create a new model
  - `make:view <name>`: Create a new view in the templates folder
  - `generate_secret_key`: Generate Secret Key

## Getting Started

To get started with FLAVEL, follow these steps:

1. Clone this repository `git clone git@github.com:Ahmadrezagh/FLAVEL.git`.
2. Install dependencies by running `artisan install_requirements`.
3. Generate a secret key by running `artisan generate_secret_key`.
4. Start the development server using `artisan serve`.
5. You're ready to start building your Flask application with FLAVEL!

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests if you have any ideas for improvements or if you encounter any bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
