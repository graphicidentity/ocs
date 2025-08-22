import os
import re

# The new "All modules" section to insert
new_section = '''
<section class="list-group menu list-unstyled">
    <h3 class="wb-navcurr">All modules</h3>
    <ul class="list-group menu list-unstyled">
        <li><a class="list-group-item" href="../module2/info-pane.html">The Info Pane</a></li>
        <li><a class="list-group-item" href="../module2/document-title.html">Document Title</a></li>
        <li><a class="list-group-item" href="../module2/writing-for-accessibility.html">Writing for Accessibility</a></li>
        <li><a class="list-group-item" href="../module2/descriptive-hyperlinks.html">Descriptive Hyperlinks</a></li>
        <li><a class="list-group-item" href="../module2/images-and-visual-content.html">Images and Visual Content</a></li>
        <li><a class="list-group-item" href="../module2/tables-and-data.html">Tables and Data</a></li>
        <li><a class="list-group-item" href="../module2/multimedia-accessibility.html">Multimedia Accessibility</a></li>
        <li><a class="list-group-item" href="../module2/final-accessibility-review.html">Final Accessibility Review</a></li>
    </ul>
</section>
'''

# Regex to match the "All modules" section
pattern = re.compile(
    r'<section class="list-group menu list-unstyled">\s*<h3 class="wb-navcurr">\s*All modules\s*</h3>.*?</section>',
    re.DOTALL
)

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content, count = pattern.subn(new_section, content)
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated: {filepath}')
    else:
        print(f'No change: {filepath}')

def main():
    module2_dir = './learning/document-accessibility-course/module2'
    for filename in os.listdir(module2_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(module2_dir, filename)
            update_file(filepath)

if __name__ == '__main__':
    main()