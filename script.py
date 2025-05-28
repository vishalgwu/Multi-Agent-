import mistune
import os
import json
import shutil
import re



from mistune.renderers.html import HTMLRenderer

class MyRenderer(HTMLRenderer):
    def list_item(self, text, level=None):  # ✅ correct
        return f"<li>{text}</li>\n"


def convert_md_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8', errors='replace') as md_file:
        md_content = md_file.read()

        # Convert Markdown to HTML with mistune for better control
        renderer = MyRenderer()
        md_parser = mistune.create_markdown(renderer=renderer)
        html_content = md_parser(md_content)

        # Keep spaces after numbers and dots in enumeration
        html_content = re.sub(r'(\d+)\. ', r'\1. ', html_content)

        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)


def generate_readme(data, output_file_path):
    readme_template = f"""
# Capstone Proposal
## {data['project_name']}
### Proposed by: {data['Proposed by']}
#### Email: {data['Proposed by email']}
#### Advisor: {data['instructor']}
#### The George Washington University, Washington DC  
#### Data Science Program


## 1 Objective:  
{data['Objective']}

![Figure 1: Example figure]({data['Year']}_{data['Semester']}_{data['Version']}.png)
*Figure 1: Caption*

## 2 Dataset:  
{data['Dataset']}

## 3 Rationale:  
{data['Rationale']}

## 4 Approach:  
{data['Approach']}

## 5 Timeline:  
{data['Timeline']}


## 6 Expected Number Students:  
{data['Expected Number Students']}

## 7 Possible Issues:  
{data['Possible Issues']}


## Contact
- Author: {data['instructor']}
- Email: [{data['instructor_email']}](mailto:{data['instructor_email']})
- GitHub: [{data['github_repo']}](https://github.com/{data['github_repo']})
"""
    with open(output_file_path + f"proposal_{data['Version']}.md", "w") as readme_file:
        readme_file.write(readme_template)


if __name__ == "__main__":
    input_file_path = 'input.json'
    Year = "2025"
    Semester = "summer"
    Version = "7"

    #output_file_path = os.getcwd() + os.sep + f'Arxiv{os.sep}Proposals{os.sep}{Year}{os.sep}{Semester}{os.sep}{Version}{os.sep}'
    #os.makedirs(output_file_path, exist_ok=True)

    output_file_path = os.getcwd() + os.sep

    #with open(output_file_path + input_file_path, 'r') as input_file:
    with open(os.path.join(output_file_path, input_file_path), 'r') as input_file:

        json_data = json.load(input_file)
    generate_readme(json_data, output_file_path)
    #md_file = f"proposal_{json_data['Version']}.md"
    #html_file = f"proposal_{json_data['Version']}.html"
    #convert_md_to_html(output_file_path + md_file, output_file_path + html_file)
    md_file = os.path.join(output_file_path, f"proposal_{json_data['Version']}.md")
    html_file = os.path.join(output_file_path, f"proposal_{json_data['Version']}.html")

    convert_md_to_html(md_file, html_file)

    try:
        shutil.copy(f"{json_data['Year']}_{json_data['Semester']}_{json_data['Version']}.png", output_file_path)
    except FileNotFoundError:
        print('No Figure is needed.')
    print(f"proposal_{json_data['Version']}.md generated successfully.")
