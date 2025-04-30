# How to Start Continuous integration (CI) and Integrate with Github Action

Create file: `.github/workflows/ci-cd.yml`

Keyboard shortcut to display hidden files `Command + Shift + .` 

![Screenshot 2568-04-30 at 21 32 03](https://github.com/user-attachments/assets/4a4af974-a8de-4396-a8ac-0a4169b59099)

![Screenshot 2568-04-30 at 21 23 51](https://github.com/user-attachments/assets/06484317-9a1e-4600-a244-fd8e995ff3af)

- `name`: Use to display step name on Github action
- `on->pull_request->branches "develop"` : Setup pipeline will run when action with develop branch.
- `[opened, synchronize, reopened]`: Pipeline will trigger when an issue is opened.
- `actions/checkout@v4`: Setup Github action version.
- `Set up Python 3.11`: Steup Python version.
- `Install Dependencies`: Install dependencies that our project required.
- `OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}` Read secreat variable from our Github before run Unit test

`Steps: Go to your Github project > Settings > Secrets and variables > Actions > New repository secret > Add secret`

![Screenshot 2568-04-30 at 21 55 00](https://github.com/user-attachments/assets/d8f181fe-57c2-48e1-9b56-9812207c3dcd)


- `run: | pytest tests/ --cov=./ --cov-report=xml`: Run Unit test
- `Run Hadolint (Dockerfile Linter)`: Add Dockerfile linting with hadolint to improve Dockerfile quality.
- `Build Docker Image`: Run docker command for build Docker image file.
- `Run Security Scan with Trivy`: Use tools such as Trivy to scan your Docker image for vulnerabilities.

# Check CI when created Pull request

- When we create Pull request, Our pull request will start run Unit test on this step.

![Screenshot 2568-04-30 at 22 07 04](https://github.com/user-attachments/assets/fe5fc55e-5ab5-4164-aa01-8dfdb72cb6ef)

## Result inside of our Unit test

![Screenshot 2568-04-30 at 22 09 33](https://github.com/user-attachments/assets/433cf12b-af63-454c-984d-d5a1adc943ec)

