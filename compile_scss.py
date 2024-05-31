import sass
import os


print("Compiling SCSS...")
base_dir = os.path.abspath(os.path.dirname(__file__))
sass.compile(dirname=(os.path.join(base_dir, 'static/scss'), os.path.join(base_dir, 'static/css')), output_style='compressed')
print("SCSS compiled successfully.")