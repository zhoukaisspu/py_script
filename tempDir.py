import sys
import os.path as p
import os
TEMPLATE_DIR = ("bin",
                "doc",
                "example",
                "inc",
                "lib",
                "src",
                "test",
                "script",
                "external")

DIR_OF_SCRIPT = p.dirname(p.abspath(__file__))

def make_template_dir(rootdir,temp_dir,force=False):
    root_dir = p.join(DIR_OF_SCRIPT,rootdir)
    if(force == False):
        if(p.isdir(root_dir)):
            sys.exit("[INFO]: Because of " + DIR_OF_SCRIPT+ " is exit,"
                    "\nTemplate directory creation will be stoped")
    for dir in TEMPLATE_DIR:
        dir = p.join(root_dir,dir)
        os.makedirs(dir)

    


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit("Please input root directory,\n"
                "Template directory creation failed")
    root_dir = sys.argv[1]
    make_template_dir(root_dir,TEMPLATE_DIR)
